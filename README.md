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


### Hardware
ws2812(B) Addressable LED lights:
https://www.amazon.com/s/ref=nb_sb_ss_xo_1_6/155-1522052-4634337?url=search-alias%3Daps&field-keywords=ws2812b&sprefix=ws2812%2Clawngarden%2C220

Power Supply for LED strip (Optional)
https://www.amazon.com/Led-World-Supply-Adapter-WS2812B/dp/B01D4P6VC8/ref=sr_1_33?ie=UTF8&qid=1472402743&sr=8-33&keywords=5v+8a+dc+power+supply

Raspberry Pi 1 Model B(+) (This stuff won't work with anything newer than a Raspberry Pi 1 Model B(+) - bummer)
https://www.amazon.com/Raspberry-Pi-756-8308-Motherboard-RASPBRRYPCBA512/dp/B009SQQF9C/ref=sr_1_3?ie=UTF8&qid=1472402399&sr=8-3&keywords=raspberry+pi+1+model+b

Breakout adapter for Raspberry Pi 1 Model B
https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=pi+1+breakout+26+pin&rh=i%3Aaps%2Ck%3Api+1+breakout+26+pin

Also:
Jumper Wires
Breadboard


### Pictures of the Breadboard
Sorry, I this is kinda lazy.  I'll try to make a proper diagram later.

![alt tag](https://raw.githubusercontent.com/vacoj/neatlights/master/images/pi1.jpg)

![alt tag](https://raw.githubusercontent.com/vacoj/neatlights/master/images/pi2.jpg)

![alt tag](https://raw.githubusercontent.com/vacoj/neatlights/master/images/pi3.jpg)

![alt tag](https://raw.githubusercontent.com/vacoj/neatlights/master/images/pi4.jpg)
