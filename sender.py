from helpers.RedisHelper import RedisHelper
from config import config
from config import blink_patterns
import time


def send_patterns(count):
    r = RedisHelper()
    inc = 0
    while inc < count:

        # r.publish(config.PUBSUB_NAME, blink_patterns.fuse)
        # r.publish(config.PUBSUB_NAME, blink_patterns.diamonds)
        # r.publish(config.PUBSUB_NAME, blink_patterns.comet)
        # r.publish(config.PUBSUB_NAME, blink_patterns.strobe)
        # r.publish(config.PUBSUB_NAME, blink_patterns.slub)
        # r.publish(config.PUBSUB_NAME, blink_patterns.gradient)
        r.publish(config.PUBSUB_NAME, blink_patterns.room_lighting())

        # r.publish(config.PUBSUB_NAME, blink_patterns.get_kaboom_rand())
        # r.publish(config.PUBSUB_NAME, blink_patterns.get_diamonds_rand())
        # r.publish(conWfig.PUBSUB_NAME, blink_patterns.get_comet_rand())
        # r.publish(config.PUBSUB_NAME, blink_patterns.get_strobe_rand())
        # r.publish(config.PUBSUB_NAME, blink_patterns.get_slub_rand())
        # r.publish(config.PUBSUB_NAME, blink_patterns.get_gradient_rand())
        # r.publish(config.PUBSUB_NAME, blink_patterns.get_fade_rand())
        inc += 1
        time.sleep(.3)

send_patterns(100)
