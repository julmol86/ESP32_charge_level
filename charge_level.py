from machine import Pin, SoftI2C 
from ssd1306 import SSD1306_I2C
import machine

i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128, 64, i2c)

#white frame
oled.fill_rect(5, 5, 30, 50, 1)
#black filling
oled.fill_rect(7, 7, 26, 46, 0)

def charge_level(k):
    oled.fill_rect(9, 9, 22, 42, 0)
    #full charge
    oled.fill_rect(9, 9, 22, 42, 1)
    #charge level
    oled.fill_rect(9, 9, 22, k, 0)
    
    oled.text("Charge level:",60,15)
    oled.text(str(level),60,30)
    oled.text("%",67,30)
    oled.show()

while True:
    level = int(input("Enter charge level: "))
    b = 100 - level
    k = int(b*42/100)
    charge_level(k)
