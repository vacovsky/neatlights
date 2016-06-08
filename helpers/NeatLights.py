import time
import _rpi_ws281x as ws
from helpers.GRB_Parser import GRB_Parser
from random import random
from collections import deque


class NeatLights:
    LED_CHANNEL = 0
    LED_COUNT = 630
    LED_FREQ_HZ = 800000
    LED_DMA_NUM = 5
    LED_GPIO = 18
    LED_BRIGHTNESS = 255
    LED_INVERT = 0
    CYCLES = 1
    channel = None
    speed = .05
    led_design = {}

    def __init__(self,
                 led_channel=0,
                 led_freq_hz=800000,
                 led_dma_num=5,
                 led_gpio=18,
                 led_invert=0,
                 ):
        print("Initializing...")
        self.LED_CHANNEL = led_channel
        self.LED_FREQ_HZ = led_freq_hz
        self.LED_DMA_NUM = led_dma_num
        self.LED_GPIO = led_gpio
        self.LED_INVERT = led_invert

    def start(self, delegate, style):
        print("Setting up LED environment...")
        self.LED_BRIGHTNESS = style['brightness'] or 64
        self.LED_COUNT = style['led_count'] or 630
        self.leds = ws.new_ws2811_t()
        cleanup = style['cleanup'] == 1 or True

        # Initialize all channels to off
        for channum in range(2):
            self.channel = ws.ws2811_channel_get(self.leds, channum)
            ws.ws2811_channel_t_count_set(self.channel, 0)
            ws.ws2811_channel_t_gpionum_set(self.channel, 0)
            ws.ws2811_channel_t_invert_set(self.channel, 0)
            ws.ws2811_channel_t_brightness_set(self.channel, 0)

        self.channel = ws.ws2811_channel_get(self.leds, self.LED_CHANNEL)

        ws.ws2811_channel_t_count_set(self.channel, self.LED_COUNT)
        ws.ws2811_channel_t_gpionum_set(self.channel, self.LED_GPIO)
        ws.ws2811_channel_t_invert_set(self.channel, self.LED_INVERT)
        ws.ws2811_channel_t_brightness_set(self.channel, self.LED_BRIGHTNESS)

        ws.ws2811_t_freq_set(self.leds, self.LED_FREQ_HZ)
        ws.ws2811_t_dmanum_set(self.leds, self.LED_DMA_NUM)

        # Initialize library with LED configuration.
        resp = ws.ws2811_init(self.leds)
        if resp != 0:
            raise RuntimeError('ws2811_init failed with code {0}'.format(resp))

        try:
            print(
                "Starting {0} via {1}...".format(
                    style['style_name'] or 'unknown', style['method_name'] or 'unkown')
            )
            delegate(style)

            if cleanup:
                self.cleanup()

        except Exception as e:
            print(e)

        finally:
            ws.ws2811_fini(self.leds)
            ws.delete_ws2811_t(self.leds)

    def cleanup(self):
        self.LED_BRIGHTNESS = 0
        print('Cleaning up...')
        for i in range(self.LED_COUNT):
            ws.ws2811_led_set(self.channel, i, 0x000000)
        ws.ws2811_render(self.leds)

    def party(self, style, internal=False):
        temp_led_count = 150
        if internal:
            temp_led_count = int(self.LED_COUNT / 15)
        cycle_counter = 0
        colors = GRB_Parser().convert(style['css3_colors'])
        speed = style['speed'] or random()
        offset = style['offset'] or 1
        reverse_after = style['reverse_after'] or 0
        iterations = style['iterations'] or 1
        direction = style['direction'] or 1

        while iterations > 0:
            # Update each LED color in the buffer.
            for i in range(self.LED_COUNT):
                # Pick a color based on LED position and an offset for
                # animation.
                color = colors[
                    (i + offset) % len(colors)]

                # Set the LED color buffer value.
                ws.ws2811_led_set(self.channel, i, color)

            # Send the LED color data to the hardware.
            resp = ws.ws2811_render(self.leds)
            if resp != 0:
                raise RuntimeError(
                    'ws2811_render failed with code {0}'.format(resp))

            # Delay for a small period of time.
            time.sleep(speed)

            # Increase offset to animate colors moving.  Will eventually overflow, which
            # is fine.
            if offset > reverse_after or offset < (reverse_after * -1):
                direction *= -1
            offset += direction

            # used to determine end of a task
            cycle_counter += 1
            if not internal:
                if cycle_counter % self.LED_COUNT == 0:
                    iterations -= 1
            else:
                if cycle_counter % temp_led_count == 0:
                    iterations -= 1

    def comet(self, style):
        print('COMET')
        cycle_counter = 0
        colors = GRB_Parser().convert(style['comet_head'])
        speed = style['speed'] or random()
        offset = style['offset'] or 1
        iterations = style['iterations'] or 1
        direction = style['direction'] or 1
        trail_colors = GRB_Parser().convert(
            style['comet_tail'] * (self.LED_COUNT - len(colors)))

        comet = colors + trail_colors

        while iterations > 0:
            for i in range(self.LED_COUNT):
                color = comet[
                    (i + offset) % len(comet)
                ]
                # Set the LED color buffer value.
                ws.ws2811_led_set(self.channel, i, color)
            # Send the LED color data to the hardware.
            resp = ws.ws2811_render(self.leds)
            # shift things
            comet = deque(comet)
            comet.rotate(direction)
            if resp != 0:
                raise RuntimeError(
                    'ws2811_render failed with code {0}'.format(resp))
            # Delay for a small period of time.
            time.sleep(speed)
            cycle_counter += 1
            if cycle_counter % self.LED_COUNT == 0:
                iterations -= 1

    def fuse(self, style):
        """
        Perform a fuse burn, then explode!
        """
        explode = False
        cycle_counter = 1
        colors = GRB_Parser().convert(style['fuse_fire'])
        explode_colors = style['explosion'] or ['red', 'orange']
        speed = style['speed'] or .002
        offset = style['offset'] or 1
        iterations = style['iterations'] or 1
        direction = style['direction'] or 1
        # * (style['led_count'] - len(style['comet_head']))
        trail_colors = GRB_Parser().convert(
            style['fuse_unlit'] * (self.LED_COUNT - len(colors)))

        afuse = colors + trail_colors

        while iterations > 0:
            if cycle_counter % self.LED_COUNT != 0:
                cycle_counter += 1
                # Set the LED color buffer value.
                for i in range(self.LED_COUNT):
                    color = afuse[
                        (i + offset) % len(afuse)
                    ]
                    ws.ws2811_led_set(self.channel, i, color)

                # Send the LED color data to the hardware.
                resp = ws.ws2811_render(self.leds)
                time.sleep(speed)

                afuse = deque(afuse)
                afuse.rotate(direction)
                if resp != 0:
                    raise RuntimeError(
                        'ws2811_render failed with code {0}'.format(resp))
            else:
                explode = True
                cycle_counter += 1

            if explode:
                print('Exploding!')
                explode = False
                self.LED_BRIGHTNESS = style['explosion_brightness'] or 100
                explosion = {
                    'style_name': style['style_name'],
                    'method_name': style['method_name'],
                    'css3_colors': explode_colors,
                    # speed at which lights change
                    'speed': style['explosion_speed'] or .25,
                    'offset': 1,  # number of LEDs to jump per tick
                    'reverse_after': 500,
                    'iterations': 1,
                    'direction': 1,
                    'cleanup': 1,
                }
                self.LED_BRIGHTNESS = style['explosion_brightness']

                self.party(explosion, True)
                cycle_counter += 1
                iterations -= 1

    def typewriter(self, style):
        head = GRB_Parser().convert(style['head'] or ['red'])
        empty = GRB_Parser().convert(style['empty'] or ['black'])
        base = GRB_Parser().convert(style['base'] or ['blue'])
        length = style['led_count'] or 630
        speed = style['speed'] or 0.05
        iterations = style['iterations'] or 1
        chain = head + (empty * (length - len(head)))
        head_pos = len(head)
        base_color = 0
        direction = style['direction'] or 1
        offset = style['offset'] or 1
        cycle_counter = 1

        while iterations > 0:
            for i in range(self.LED_COUNT):
                color = chain[
                    (i + offset) % len(list(chain))
                ]
                ws.ws2811_led_set(self.channel, i, color)
            base_trail = [base[base_color]] * \
                (length - len(list(chain)[0:head_pos]))
            chain = empty * \
                (length - (len(head) + len(base_trail) - 2)) + \
                head + base_trail
            time.sleep(speed)
            # print(list(chain))
            resp = ws.ws2811_render(self.leds)
            if resp != 0:
                raise RuntimeError(
                    'ws2811_render failed with code {0}'.format(resp))
            # print('  Head: ', head_pos, '  ', chain, end="\r", flush=True)
            chain = deque(chain)
            chain.rotate(direction)
            if head_pos == length - 1:
                head_pos = 0
                head.reverse()
                direction *= -1
                if base_color == len(base) - 1:
                    base_color = 0
                else:
                    base_color += 1
            else:
                head_pos += 1
            if cycle_counter % length == 0:
                iterations -= 1

    def gradient(self, style):
        cycle_counter = 1
        iterations = style['iterations'] or 1
        length = style['led_count']
        speed = style['speed']
        direction = style['direction']
        crange = style['color_range']
        crange = GRB_Parser().convert(crange)
        div = (crange[1] - crange[0]) / self.LED_COUNT
        offset = 0

        cnt = 0
        chain = []

        for n in range(length):
            cnt += 1
            chain.append(div * cnt)
            if n % length == 0:
                if n < 0:
                    n = n * -1

        while iterations > 0:
            cycle_counter += 1
            chain = deque(chain)
            for i in range(self.LED_COUNT):
                color = chain[
                    (i + offset) % len(list(chain))
                ]
                ws.ws2811_led_set(self.channel, i, color)

            resp = ws.ws2811_render(self.leds)
            if resp != 0:
                raise RuntimeError(
                    'ws2811_render failed with code {0}'.format(resp))
            chain.rotate(direction)
            # print(list(chain), end="\r", flush=True)
            time.sleep(speed)
            if cycle_counter % length == 0:
                iterations -= 1

    def fade(self, style):
        length = style['led_count']
        speed = style['speed']
        iterations = style['iterations'] or 1
        fade_out_brightness, fade_in_brightness = style[
            'fade_dim'], style['fade_bright']
        in_color, out_color = GRB_Parser().convert(
            style['fade_in']), GRB_Parser().convert(style['fade_out'])

        chain = []
        div = int((out_color[0] - in_color[0]) / length)

        if div < 0:
            div *= -1

        cnt = 0
        for n in range(length):
            cnt += 1
            chain.append(div * cnt)
            if n % length == 0:
                if n < 0:
                    n = n * -1

        brightness_direction = 1
        brightness = 0
        returns = 0

        while iterations > 0:
            brightness += brightness_direction
            if (brightness >= fade_in_brightness - 1 and brightness_direction == 1) or (
                    brightness <= fade_out_brightness + 1 and brightness_direction == -1):
                brightness_direction *= -1
                returns += 1

            for i in range(self.LED_COUNT):
                ws.ws2811_led_set(self.channel, i, chain[i])
            ws.ws2811_channel_t_brightness_set(self.channel, brightness)
            # print(brightness)
            resp = ws.ws2811_render(self.leds)
            if resp != 0:
                raise RuntimeError(
                    'ws2811_render failed with code {0}'.format(resp))

            time.sleep(speed)

            if returns == 1:
                iterations -= 1
                returns = 0
