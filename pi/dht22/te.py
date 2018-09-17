import Adafruit_DHT
import time
import MySQLdb

hum, temp = Adafruit_DHT.read_retry(22, 21)
temperature, humidity = int(temp), int(hum)
nowtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
if humidity is not None and temperature is not None:
    conn = MySQLdb.connect(host="dbhost", user="user", passwd="oassword", db="dbname", charset='utf8')
    curosr = conn.cursor()
    curosr.execute("insert into info(nowtime, temperature, humidity) values(%s,%s,%s)",
                   (nowtime, temperature, humidity))
    conn.commit()
    curosr.close()
    conn.close()
    print("time:", nowtime, "info:", "success\n")
else:
   print('Failed to get reading. Try again!')
