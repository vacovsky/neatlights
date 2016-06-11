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
        Thread(target=AmbientLightSensor, args=(
            AMBIENT_LIGHT_CHANNEL, PIN_ID)).start()

    def listen(self):
        self.redis.subscribe(PUBSUB_NAME)
        for message in self.redis.PubSub.listen():
            try:
                data = message["data"]
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
                else:
                    method = print

                controller.start(method, datadict)
                self.completed += 1
                print('Completed runs: ' + str(self.completed))

            except Exception as e:
                print(e)


if __name__ == '__main__':
    # print("Starting LED listener for PUBSUB: %s." % PUBSUB_NAME)
    # Main().listen()
    Main().light_sense()
