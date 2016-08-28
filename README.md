# NEATLIGHTS
##### PubSub-based controller for controlling strands of addressable LED lights connected to a Raspberry Pi. 


### The Gist of It

In the ```config/config.py``` file, set up appropriate info for the redis pubsub instance you want to listen on.  Posting a json blob/python dictionary on the specified channel will result in the listening thread parsing the message, and configuring the LED strand as specified.  Examples can be found in ```config/blink_patterns.py```.  

* When passing colors into the message, use the CSS3 color names: ['black', 'red', 'cornflowerblue', 'paleturquoise'].  

* The max brightness value is 255, and the min (lights off) is 0.

* To make the strands to fancy things, you will need to write your own methods.  Plenty of examples of can be found in ```helpers/NeatLights.py```, and in order to have the method executed, you will need to modify Main.py with the name of the method.

### Example Message

```
{
    'style_name': 'Diamonds',
    'method_name': 'party',
    'css3_colors': [
        'red', 'yellow', 'blue',
        'orange', 'purple', 'green',
        'teal', 'fuchsia', 'white'
    ],
    'brightness': 100,  # 255 max - SEE NOTE BELOW
    'led_count': 480,  # total number of LEDs being operated
    'speed': 0.01,  # speed at which lights change
    'offset': 1,  # number of LEDs to jump per tick
    'reverse_after': 500,
    'iterations': 1,
    'direction': 2,
    'cleanup': 1,
    'senselight': False  # can make use of an ambient light sensor to adjust bightness of lights based on the brightness of the room
}

```
NOTE:  The Pi alone can power about 50 at max brightness, but any more will cause it to lock up due to lack of available energy.  I added a 5v, 8Amp power supply to my lights to be able to power about 700 lights at 100 brightness.

### Pictures of the Breadboard
Sorry, I this is kinda lazy.  I'll try to make a proper diagram later.

