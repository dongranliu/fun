# dht11 温湿度传感器

## 介绍

DHT11数字温湿度传感器是一款含有已校准数字信号输出的温湿度复合传感器。产品为4针单排引脚封装。

通过crontab每十分钟用dht11读取一次数据，并储存到mysql（mariadb）数据库中。

使用flask读取数据，并将数据输出到网页。

使用gunicorn后台运行flask。

## 目录结构

* info.sql 数据表结构
* dht11.py 读取数据并存到数据库
* server 读取数据并输出到网页
* index.html 主页
* layui.css layui css文件
* layui.js layui.js文件
* requirements.txt 项目依赖

## python版本

python 3.5.5

## 快速开始


## 效果

![web](https://blogst.b0.upaiyun.com/img/2018/07/10/f43cc5e4!hysg)
