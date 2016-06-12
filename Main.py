from helpers.NeatLights import NeatLights
from helpers.AmbientLightSensor import AmbientLightSensor
from helpers.RedisHelper import RedisHelper
import json
from config.config import *
from threading import Thread


class Main:
    completed = 0
    redis = None

    def __init__(self):
        self.redis = RedisHelper()

    def light_sense(self):
        func = AmbientLightSensor(AMBIENT_LIGHT_CHANNEL, PIN_ID).start
        func(1)
        # Thread(target=func, args=(1))

    def listen(self):
        self.redis.subscribe(PUBSUB_NAME)
        for message in self.redis.PubSub.listen():
            try:
                data = message["data"]
                print(data)
                if data == 1:
                    continue
                datastr = data.decode('utf8').replace("'", '"')
                datadict = json.loads(datastr)
                controller = None
                controller = NeatLights()
                method = None

                # methods are used for different types of light patterns
                if datadict['method_name'] == 'party':
                    method = controller.party
                elif datadict['method_name'] == 'demo':
                    method = controller.demo
                elif datadict['method_name'] == 'fade':
                    method = controller.fade
                elif datadict['method_name'] == 'comet':
                    method = controller.comet
                elif datadict['method_name'] == 'fuse':
                    method = controller.fuse
                elif datadict['method_name'] == 'gradient':
                    method = controller.gradient
                elif datadict['method_name'] == 'typewriter':
                    method = controller.typewriter
                elif datadict['method_name'] == 'room_lighting':
                    method = controller.room_lighting
                    datadict['cleanup'] = 0
                else:
                    method = print

                if datadict['senselight'] == 1:
                    # modify brightness based on ambient light if true
                    br = int(RedisHelper().Connection.get(
                        AMBIENT_LIGHT_CHANNEL))
                    if br is None or br == 0:
                        br = -1
                    if br <= -255:
                        br = -254
                    datadict['brightness'] = 255 + br

                controller.start(method, datadict)
                self.completed += 1
                print('Completed runs: ' + str(self.completed))

            except Exception as e:
                print(e)


if __name__ == '__main__':
    print("Starting LED listener for PUBSUB: %s." % PUBSUB_NAME)
    # Main().light_sense()
    Main().listen()
