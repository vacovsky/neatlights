import time
from collections import deque
from helpers.GRB_Parser import GRB_Parser

#head = [2, 1]
#empty = [0]
#slime = [3, 4, 5, 6, 7, 8, 9]
#length = 10


slub = {
    'style_name': 'Slub',
    'method_name': 'typewriter',
    'brightness': 25,
    'head': ['H1', 'H2'],
    'base': ['_', '-', '='],
    'empty': [' '],
    'led_count': 10,  # number of LEDs being operated
    'speed': 0.2,  # speed at which lights change
    'offset': 1,  # number of LEDs to jump per tick
    'iterations': 1,
    'direction': -1,  # forward or back, and how many pixels to move.
    'cleanup': 1
}


def simulate(style):
    head = style['head']
    empty = style['empty']
    base = style['base']
    length = style['led_count']
    speed = style['speed']

    chain = head + (empty * (length - len(head)))
    head_pos = len(head)
    base_color = 0
    direction = style['direction']

    for i in range(50):
        base_trail = [base[base_color]] * \
            (length - len(list(chain)[0:head_pos]))

        chain = empty * \
            (length - (len(head) + len(base_trail) - 2)) + head + base_trail

        time.sleep(speed)
        print('  Head: ', head_pos, '  ', chain, end="\r", flush=True)

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


style2 = {
    'style_name': 'style2',
    'method_name': 'style2',
    'brightness': 25,
    # starting color, ending color - can be numbers or colors
    'color_gradient': ['blue', 'white'],
    'led_count': 15,  # number of LEDs being operated
    'speed': 1,  # speed at which lights change
    'offset': 1,  # number of LEDs to jump per tick
    'iterations': 1,
    'direction': -1,  # forward or back, and how many pixels to move.
    'cleanup': 1
}


def simulate_2(style):
    length = style['led_count']
    speed = style['speed']
    direction = style['direction']

    chain = []
    crange = ['blue', 'yellow']
    crange = GRB_Parser().convert(crange)

    div = crange[1] - crange[0]
    cnt = 0

    for n in range(length):
        cnt += 1
        chain.append(div * cnt)
        if n % length == 0:
            if n < 0:
                n = n * -1

    while True:
        chain = deque(chain)
        chain.rotate(direction)
        print(list(chain), end="\r", flush=True)
        time.sleep(speed)


style3 = {'led_count': 10,
          'speed': .2,
          'iterations': 1

          }


def simulate_3(style):
    length = style['led_count']
    speed = style['speed']
    iterations = style['iterations'] or 1

    fade_out_brightness, fade_in_brightness = 0, 255
    in_color, out_color = GRB_Parser().convert(
        ['red']), GRB_Parser().convert(['blue'])

    chain = []
    div = (out_color[0] - in_color[0]) / length

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
        brightness += brightness_direction * 10
        if (brightness >= fade_in_brightness - 1 and brightness_direction == 1) or (brightness <= fade_out_brightness + 1 and brightness_direction == -1):
            brightness_direction *= -1
            returns += 1
            print(returns, iterations)

        print("Brightness: {0}".format(brightness),
              list(chain), end="\r", flush=True)
        time.sleep(speed)

        if returns == 1:
            iterations -= 1
            returns = 0


if __name__ == '__main__':
    c = 3
    while c > 0:
        # simulate(slub)
        simulate_3(style3)
        c -= 1
