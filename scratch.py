from collections import deque
import time
from helpers.GRB_Parser import GRB_Parser

size = 10
display = [i for i in range(size)]

head = ['y', 'o', 'r']
tail = ['w']

comet = ['y', 'o', 'r', 'w', 'w', 'w', 'w',
         'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']

counter = 0
start_location = 0
tracker = 0


colors = ['red', 'white', 'blue']
trail_colors = ['silver']
LED_COUNT = 10

comet = colors + (trail_colors * (LED_COUNT - len(colors)))
# print(comet)
# while True:
#     comet = deque(comet)
#     comet.rotate(1)
#     print(comet)
# sleep(0.2)

l1 = ['joe']

#print(l1 * 7)


c1 = GRB_Parser().convert(['pink'])
c2 = GRB_Parser().convert(['orange'])

c3 = c1 + c1

# print(c3)

gradient_data = {
    'length': 50,
    'color_range': ['orange', 'blue'],
    'speed': 0.1
}


def gradient(style):
    chain = []
    length = style['length']
    crange = style['color_range']  # ['blue', 'yellow']
    speed = style['speed']
    crange = GRB_Parser().convert(crange)
    div = crange[1] - crange[0]
    cnt = 0

    for n in range(length):
        time.sleep(speed)
        cnt += 1
        chain.append(div * cnt)
        if n % length == 0:
            if n < 0:
                n = n * -1
    print(chain)

#gradient(gradient_data)






