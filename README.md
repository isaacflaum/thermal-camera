# thermal-camera
Homemade Circuitpython Thermal Camera with MLX90640 32x24 radiometric sensor with TFT display powered by RP2040/ESP32 devices. I am using a KB2040 to power this right now.



Things you will need:
* Circuit Python + adafruit MLX90640 drivers
* 1 x RP2040 or ESP32 like device (Eg Rasperry Pi Pico, KB2040, Adafruit feather, ...)
* 1 x SPI TFT DISPLAY (I used a 240x135 TFT display from adafruit as it already has SPI connections ready to go. It can be found found here https://www.mouser.com/ProductDetail/Adafruit/4383?qs=wnTfsH77Xs5%252BKXRBrl3nUg%3D%3D)
* 1 x MLX90640 Thermal sensor (I went with adafruit breakout due to I2c connection ready to go but can easily just buy the sensor from Mouser/Digikey)
* 1 x Breadboard + wires (3M is expensive but IMO the highest quality breadboard they will last years with constant usage and you make up for the $$$ by not running into connection issues with wires not being grabbed/making contact)




How to run:
* Setup/Install Circuitpython on your device (Recommend using Thonny if this is your first time. Thonny makes it super easy to insatll libraries, upload/run code and view serial output of running code)
* Install the adafruit MLX90640 driver
* Install adafruit_st7789 (if using different display not powered by st7789 controller you will need a different display driver here)
* Install terminalio, displayio
* Copy code.py to Circuitpython device and run it!