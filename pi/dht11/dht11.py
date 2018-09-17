import RPi.GPIO as GPIO
import MySQLdb
import time

# BCM编号方式的20对应树莓派的pin38
channel = 20
data = []
j = 0
# I/O口使用BCM编号方式
GPIO.setmode(GPIO.BCM)
time.sleep(1)

# 设置数据线为输出
GPIO.setup(channel, GPIO.OUT)
GPIO.output(channel, GPIO.LOW)
time.sleep(0.02)
GPIO.output(channel, GPIO.HIGH)
# 设置数据线为输入
GPIO.setup(channel, GPIO.IN)
while GPIO.input(channel) == GPIO.LOW:
    continue
while GPIO.input(channel) == GPIO.HIGH:
    continue
while j < 40:
    k = 0
    while GPIO.input(channel) == GPIO.LOW:
        continue
    while GPIO.input(channel) == GPIO.HIGH:
        k += 1
        if k > 100:
            break
    if k < 8:
        data.append(0)
    else:
        data.append(1)
    j += 1

# 读取数值
humidity_bit = data[0:8]
humidity_point_bit = data[8:16]
temperature_bit = data[16:24]
temperature_point_bit = data[24:32]
check_bit = data[32:40]
humidity = 0
humidity_point = 0
temperature = 0
temperature_point = 0
check = 0

# 转换数值
for i in range(8):
    humidity += humidity_bit[i] * 2 ** (7 - i)
    humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
    temperature += temperature_bit[i] * 2 ** (7 - i)
    temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
    check += check_bit[i] * 2 ** (7 - i)
tmp = humidity + humidity_point + temperature + temperature_point
nowtime = int(time.time())


# 时间格式转换
def change_time(t):
    local_time = time.localtime(t)
    return time.strftime("%Y-%m-%d %H:%M:%S", local_time)


# 数据校验
t = change_time(int(time.time()))
if check == tmp:

    # 储存数据到数据库
    conn = MySQLdb.connect(host="host", user="user", passwd="passwd", db="db", charset='utf8')
    curosr = conn.cursor()
    curosr.execute("insert into info(nowtime, temperature, humidity) values(%s,%s,%s)",
                   (nowtime, temperature, humidity))
    conn.commit()
    curosr.close()
    conn.close()
    print("time:", t, "info:", "success\n")
else:
    print("wrong")
    print("time:", t, "temperature : ", temperature, ", humidity : ", humidity, " check : ", check, " tmp : ", tmp, "/")
GPIO.cleanup()
