# HACKxFDU

本仓库是[HACKxFDU](http://hackx.org/)的项目源代码仓库。

[最终项目演示视频](https://youtu.be/7C0NfFHb5Rw)

## 项目背景

在城市的交通高峰期，交通常常出现程度不等的拥塞状况，需要交警进行人工调控。

而交警在需要疏导车流(交通手势)的同时，常常还需要人工控制信号灯，多线操作非常不方便，警力资源也很紧张。

## 项目场景

我们通过将智能硬件接入语音输入和语义理解，实现用语音的方式去进行硬件操控，以更智能的方式协助交警进行交通疏导。

例如交警说：

- 『红色信号灯亮』或『禁止通行』时，信号灯变为红色；
- 『绿色信号灯亮』或『请快速通过』时，信号灯变为绿色；
- 『黄色信号灯亮』或『减速慢行』时，信号灯变为黄色；
- 『点亮所有信号灯』，信号灯全部点亮；
- 『关闭所有信号灯』，信号灯全部关闭；
- 『请不要打手机』或『请系上安全带』等无关语句时，不会影响信号灯控制。
- （以上语句均支持语义理解，具有鲁棒性）

## 项目架构

语音为输入，翻译成文本后，进行语义理解，绑定到相应的函数，树莓派为硬件中心，根据对应的函数调用相应的硬件模块进行操作。

目前采用的架构：

![img](http://hackx.org/uploads/photo/image/48/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7_2016-10-16_%E4%B8%8A%E5%8D%8810.53.25.png)

理想架构：

![img](http://hackx.org/uploads/photo/image/49/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7_2016-10-16_%E4%B8%8A%E5%8D%8810.53.20.png)

![img](http://hackx.org/uploads/photo/image/50/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7_2016-10-16_%E4%B8%8A%E5%8D%8810.53.15.png)

## 相关技术

- 流语音处理
- [语音识别(Bing API)](https://www.microsoft.com/cognitive-services/en-us/speech-api)
- [语义理解(LUIS)](https://www.microsoft.com/cognitive-services/en-us/language-understanding-intelligent-service-luis)
- [树莓派](https://www.raspberrypi.org/)
- [Ruff](https://ruff.io/zh-cn/)
- 采用了三色LED灯(模拟交通信号灯)，红外发送和接受模块
- 测试了光源传感器，蜂鸣器等其它辅助模块
- 采用Socket进行主机和树莓派之间的通信

