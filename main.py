#Exemplo de programa para interface com OLED SSD1306
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
 
WIDTH  = 128  #largura da tela
HEIGHT = 64   #altura da tela
 
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)       #Inicia i2c GPIO8 e GPIO9
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) #mostra endereco do dispositivo na rede
print("I2C Configuration: "+str(i2c))                   #mostra config i2C
  
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  #incializa o display OLED

cont = 0

while True:
  oled.fill(0)  
  oled.text("PUC GOIAS",0,0)
  oled.text("POLITECNICA",0,10)
  oled.text("ENG1107",0,20)
  oled.text("PROJ. INTEGRADOR",0,30)
  cont = cont + 1
  oled.text(str(round(cont)),0,50)
  oled.show()
  time.sleep_ms(1000)
