from random import randint, random
LED_COUNT = 480
BRIGHTNESS = 10
SENSELIGHT = 0

css3colors = [
    'aliceblue',
    'antiquewhite',
    'aqua',
    'aquamarine',
    'azure',
    'beige',
    'bisque',
    'black',
    'blanchedalmond',
    'blue',
    'blueviolet',
    'brown',
    'burlywood',
    'cadetblue',
    'chartreuse',
    'chocolate',
    'coral',
    'cornflowerblue',
    'cornsilk',
    'crimson',
    'cyan',
    'darkblue',
    'darkcyan',
    'darkgoldenrod',
    'darkgray',
    'darkgreen',
    'darkgrey',
    'darkkhaki',
    'darkmagenta',
    'darkolivegreen',
    'darkorange',
    'darkorchid',
    'darkred',
    'darksalmon',
    'darkseagreen',
    'darkslateblue',
    'darkslategray',
    'darkslategrey',
    'darkturquoise',
    'darkviolet',
    'deeppink',
    'deepskyblue',
    'dimgray',
    'dimgrey',
    'dodgerblue',
    'firebrick',
    'floralwhite',
    'forestgreen',
    'fuchsia',
    'gainsboro',
    'ghostwhite',
    'gold',
    'goldenrod',
    'gray',
    'green',
    'greenyellow',
    'grey',
    'honeydew',
    'hotpink',
    'indianred',
    'indigo',
    'ivory',
    'khaki',
    'lavender',
    'lavenderblush',
    'lawngreen',
    'lemonchiffon',
    'lightblue',
    'lightcoral',
    'lightcyan',
    'lightgoldenrodyellow',
    'lightgray',
    'lightgreen',
    'lightgrey',
    'lightpink',
    'lightsalmon',
    'lightseagreen',
    'lightskyblue',
    'lightslategray',
    'lightslategrey',
    'lightsteelblue',
    'lightyellow',
    'lime',
    'limegreen',
    'linen',
    'magenta',
    'maroon',
    'mediumaquamarine',
    'mediumblue',
    'mediumorchid',
    'mediumpurple',
    'mediumseagreen',
    'mediumslateblue',
    'mediumspringgreen',
    'mediumturquoise',
    'mediumvioletred',
    'midnightblue',
    'mintcream',
    'mistyrose',
    'moccasin',
    'navajowhite',
    'navy',
    'oldlace',
    'olive',
    'olivedrab',
    'orange',
    'orangered',
    'orchid',
    'palegoldenrod',
    'palegreen',
    'paleturquoise',
    'palevioletred',
    'papayawhip',
    'peachpuff',
    'peru',
    'pink',
    'plum',
    'powderblue',
    'purple',
    'red',
    'rosybrown',
    'royalblue',
    'saddlebrown',
    'salmon',
    'sandybrown',
    'seagreen',
    'seashell',
    'sienna',
    'silver',
    'skyblue',
    'slateblue',
    'slategray',
    'slategrey',
    'snow',
    'springgreen',
    'steelblue',
    'tan',
    'teal',
    'thistle',
    'tomato',
    'turquoise',
    'violet',
    'wheat',
    'white',
    'whitesmoke',
    'yellow',
    'yellowgreen'
]


def rand_color(length=1):
    result = []
    for i in range(length):
        result.append(css3colors[randint(0, len(css3colors) - 1)])
    return result


def rand_brightness(minbright=0, maxbright=128):
    return randint(minbright, maxbright)


def rand_speed():
    return random() / randint(1, 20)


def room_lighting():
    return {
        'style_name': 'Room Lighting',
        'method_name': 'room_lighting',
        'color': rand_color(),
        'brightness': BRIGHTNESS,
        'led_count': LED_COUNT,
        'senselight': SENSELIGHT
    }


def room_lighting_on():
    return {
        'style_name': 'Room Lighting',
        'method_name': 'room_lighting',
        'color': rand_color(),
        'brightness': BRIGHTNESS,
        'led_count': LED_COUNT,
        'senselight': SENSELIGHT
    }


def room_lighting_off():
    return {
        'style_name': 'Room Lighting Off',
        'method_name': 'room_lighting_off',
        'color': ['black'],
        'brightness': 0,
        'led_count': LED_COUNT,
        'senselight': SENSELIGHT
    }

diamonds = {
    'style_name': 'Diamonds',
    'method_name': 'party',
    'css3_colors': [
        'red', 'yellow', 'blue',
        'orange', 'purple', 'green',
        'teal', 'fuchsia', 'white'
    ],
    'brightness': BRIGHTNESS,  # 255 max
    'led_count': LED_COUNT,  # number of LEDs being operated
    'speed': 0.01,  # speed at which lights change
    'offset': 1,  # number of LEDs to jump per tick
    'reverse_after': 500,
    'iterations': 1,
    'direction': 2,
    'cleanup': 1,
    'senselight': SENSELIGHT
}

strobe = {
    'style_name': 'Strobe',
    'method_name': 'comet',
    'comet_head': ['white'],
    'comet_tail': ['black'],
    'brightness': BRIGHTNESS,
    'led_count': LED_COUNT,  # number of LEDs being operated
    'speed': 0.02,  # speed at which lights change
    'offset': 1,  # number of LEDs to jump per tick
    'iterations': 2,
    'direction': -18,  # forward or back, and how many pixels to move.
    'cleanup': 1,
    'senselight': SENSELIGHT
}

comet = {
    'style_name': 'Comet',
    'method_name': 'comet',
    'comet_head': ['white', 'red', 'orange', 'yellow'],
    'comet_tail': ['black'],
    'brightness': BRIGHTNESS,
    'led_count': LED_COUNT,  # number of LEDs being operated
    'speed': 0.02,  # speed at which lights change
    'offset': 1,  # number of LEDs to jump per tick
    'iterations': 1,
    'direction': -1,  # forward or back, and how many pixels to move.
    'cleanup': 1,
    'senselight': SENSELIGHT
}

fuse = {
    'style_name': 'Kaboom',
    'method_name': 'fuse',
    'fuse_fire': ['orange', 'yellow'],
    'fuse_unlit': ['black'],
    'explosion': ['red', 'orange'],
    'explosion_speed': .2,
    'explosion_brightness': 100,
    'explode_time': 50,
    'brightness': BRIGHTNESS,
    'led_count': LED_COUNT,  # number of LEDs being operated
    'speed': 0.02,  # speed at which lights change
    'offset': 1,  # number of LEDs to jump per tick
    'iterations': 1,
    'direction': 1,  # forward or back, and how many pixels to move.
    'cleanup': 1,
    'senselight': SENSELIGHT
}


slub = {
    'style_name': 'Slub',
    'method_name': 'typewriter',
    'brightness': BRIGHTNESS,
    'head': ['blue', 'teal', 'purple'],
    'base': ['red', 'orange', 'yellow', 'blue', 'green', 'teal'],
    'empty': ['black'],
    'led_count': LED_COUNT,  # number of LEDs being operated
    'speed': 0.02,  # speed at which lights change
    'offset': 1,  # number of LEDs to jump per tick
    'iterations': 1,
    'direction': 1,  # forward or back, and how many pixels to move.
    'cleanup': 1,
    'senselight': SENSELIGHT
}

gradient = {
    'style_name': 'Gradient',
    'method_name': 'gradient',
    'brightness': BRIGHTNESS,
    'color_range': ['blue', 'yellow'],
    'led_count': LED_COUNT,  # number of LEDs being operated
    'speed': 0.02,  # speed at which lights change
    'offset': 0,  # number of LEDs to jump per tick
    'iterations': 1,
    'direction': -1,  # forward or back, and how many pixels to move.
    'cleanup': 0,
    'senselight': SENSELIGHT
}


########### RANDOMS #############


def get_strobe_rand():
    return {
        'style_name': 'Random Strobe',
        'method_name': 'comet',
        'comet_head': rand_color(randint(1, 1)),
        'comet_tail': ['black'],  # rand_color(randint(0, 1)),
        'brightness': rand_brightness(),
        'led_count': LED_COUNT,  # number of LEDs being operated
        'speed': rand_speed(),  # speed at which lights change
        'offset': 1,  # number of LEDs to jump per tick
        'iterations': 1,
        # forward or back, and how many pixels to move.
        'direction': randint(1, 20),
        'cleanup': 1,
        'senselight': SENSELIGHT
    }


def get_fade_rand():
    return {
        'style_name': 'Random Fade',
        'method_name': 'fade',
        'fade_in': rand_color(randint(1, 10)),
        'fade_out': rand_color(randint(1, 10)),  # rand_color(randint(0, 1)),
        'fade_dim': 0,
        'fade_bright': 255,
        'led_count': LED_COUNT,  # number of LEDs being operated
        'speed': rand_speed(),  # speed at which lights change
        'offset': 1,  # number of LEDs to jump per tick
        'iterations': 1,
        'offset': 1,
        'brightness': rand_brightness(),
        # forward or back, and how many pixels to move.
        'cleanup': 1,
        'senselight': SENSELIGHT
    }


def get_comet_rand():
    return {
        'style_name': 'Random Comet',
        'method_name': 'comet',
        'comet_head': rand_color(randint(0, 10)),
        'comet_tail': rand_color(randint(1, 1)),
        'brightness': rand_brightness(),
        'led_count': LED_COUNT,  # number of LEDs being operated
        'speed': rand_speed(),  # speed at which lights change
        'offset': 1,  # number of LEDs to jump per tick
        'iterations': 1,
        'direction': -1,  # forward or back, and how many pixels to move.
        'cleanup': 1,
        'senselight': SENSELIGHT
    }


def get_kaboom_rand():
    return {
        'style_name': 'Random Kaboom',
        'method_name': 'fuse',
        'fuse_fire': rand_color(randint(0, 10)),
        'fuse_unlit': rand_color(randint(1, 1)),
        'explosion': rand_color(randint(0, 10)),
        'explosion_speed': rand_speed(),
        'explosion_brightness': rand_brightness(),
        'explode_time': 10,
        'brightness': rand_brightness(),
        'led_count': LED_COUNT,  # number of LEDs being operated
        'speed': rand_speed(),  # speed at which lights change
        'offset': 1,  # number of LEDs to jump per tick
        'iterations': 1,
        'direction': 1,  # forward or back, and how many pixels to move.
        'cleanup': 1,
        'senselight': SENSELIGHT
    }


def get_slub_rand():
    return {
        'style_name': 'Random Slub',
        'method_name': 'typewriter',
        'brightness': rand_brightness(),
        'head': rand_color(randint(0, 10)),
        'base': rand_color(randint(0, 10)),
        'empty': rand_color(randint(0, 10)),
        'led_count': LED_COUNT,  # number of LEDs being operated
        'speed': rand_speed(),  # speed at which lights change
        'offset': 1,  # number of LEDs to jump per tick
        'iterations': 1,
        'direction': -1,  # forward or back, and how many pixels to move.
        'cleanup': 1,
        'senselight': SENSELIGHT
    }


def get_gradient_rand():
    return {
        'style_name': 'Random Gradient',
        'method_name': 'gradient',
        'brightness': rand_brightness(),
        'color_range': rand_color(randint(0, 2)),
        'led_count': LED_COUNT,  # number of LEDs being operated
        'speed': rand_speed(),  # speed at which lights change
        'offset': 1,  # number of LEDs to jump per tick
        'iterations': 1,
        'direction': -1,  # forward or back, and how many pixels to move.
        'cleanup': 1,
        'senselight': SENSELIGHT
    }


def get_diamonds_rand():
    return {
        'style_name': 'Random Party',
        'method_name': 'party',
        'css3_colors': rand_color(randint(0, 10)),
        'brightness': rand_brightness(),  # 255 max
        'led_count': LED_COUNT,  # number of LEDs being operated
        'speed': rand_speed(),  # speed at which lights change
        'offset': 1,  # number of LEDs to jump per tick
        'reverse_after': 500,
        'iterations': 1,
        'direction': 2,
        'cleanup': 1,
        'senselight': SENSELIGHT
    }
