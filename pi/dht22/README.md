# dht22 温湿度传感器

## 介绍

DHT22数字温湿度传感器是一款含有已校准数字信号输出的温湿度复合传感器。它应用专用的数字模块采集技术和温湿度传感技术，确保产品具有极高的可靠性与卓越的长期稳定性。

通过crontab每十分钟使dht22读取一次数据，并储存到mysql（mariadb）数据库中。

后端使用Go database/sql读取mysql中的数据，并将数据输出为web json。

使用supervisord后台运行Go web。

## 目录结构

```shell
dht22/
├── README.md 介绍文件
├── db
│   ├── dump.sh 备份脚本
│   └── osdb.go 上传程序
├── main.go web主文件
├── supervisord_conf supervisord配置文件
├── te.py dht22温湿度传感器
└── web
    ├── index.html 网站页面首页
    └── lib
        ├── axios.min.js
        ├── index.css
        ├── index.js
        └── vue.js
```

## python版本

python 3.5.5

## Go版本

Go 1.10.3

## 快速开始

+ crontab

```shell
*/10 * * * * /home/pi/.pyenv/versions/te/bin/python /home/pi/te/test.py >/dev/null
*/60 * * * * /bin/bash /home/pi/te/db/dump.sh > /dev/null
```

## 效果

![web](https://blogst.b0.upaiyun.com/img/2018/09/17/5f595a7e.jpg)
