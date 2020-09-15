---
layout: article
title: 制作多系统安装U盘并安装windows+ubuntu
tags: 系统安装 ubuntu
aside:
  toc: true
article_header:
  type: cover
  image:
    src: assets/images/background/pic/sky.jpg
mathjax: true
mathjax_autoNumber: true
---
# 摘要
本文介绍如何安装双系统windows+ubuntu，并且制作安装U盘。
单个的系统安装很简单，Windows直接去官网下载就行，ubuntu官网也有教程，写本文的目的是想制作
一个U盘可以放多个系统，可以选择性安装不同系统。也可以双系统共存。
<!--more-->
## 下载系统文件
### windows系统下载
进入微软官网下载系统

[https://www.microsoft.com/zh-cn/software-download/windows10ISO](https://www.microsoft.com/zh-cn/software-download/windows10ISO)
### ubuntu下载
ubuntu官网下载系统

[https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)

### U盘启动软件下载
这里我的选择是使用 winsetupfromusb

官网下载[http://www.winsetupfromusb.com/downloads/](http://www.winsetupfromusb.com/downloads/)

## 制作启动U盘
作者有说如何安装,我就不再重复，记得选择高级选项那里一定要点上。

[http://www.winsetupfromusb.com/add-multiple-windows-nt6-vista-7-8-sources-ubuntu-usb-disk/](http://www.winsetupfromusb.com/add-multiple-windows-nt6-vista-7-8-sources-ubuntu-usb-disk/)
## 开始安装系统
PS:双系统安装需要先安装windows再安装ubuntu，否则windows的引导会覆盖grub2,导致不能选择ubuntu就直接进入windows系统。
- 开机按F12选择boot模式，选择legacy模式，这样才能看到所有内容。

![](https://socofels.github.io/assets/images/install_system/bootmode.jpg){:width="512px"}

- 选择你的U盘

![](https://socofels.github.io/assets/images/install_system/chooseUpan.jpg){:width="512px"}

- 选择系统，0是win10,2是ubuntu，依次选择win10和ubuntu进行安装。
![](https://socofels.github.io/assets/images/install_system/choose_system.jpg){:width="512px"}
### 安装win10
- win10安装一般不会有什么问题，按照提示选择自定义安装。
![win10](https://socofels.github.io/assets/images/install_system/win10.jpg){:width="512px"}
- 分区的时候记得分一块地留给ubuntu。
### 安装ubuntu
- win装好后重启，选择ubuntu

![](https://socofels.github.io/assets/images/install_system/choose_system.jpg){:width="512px"}

![](https://socofels.github.io/assets/images/install_system/ubuntu_pre.jpg){:width="512px"}
![](https://socofels.github.io/assets/images/install_system/ubuntu1.jpg){:width="512px"}
- 如果安装卡到了这个画面不动了，然后提示你没有找到文件什么的那么请重启电脑，当再次看到这个画面时拔掉U盘立即重新插上。
- 此时一步一步按提示装ubuntu

![](https://socofels.github.io/assets/images/install_system/ubuntu_1.jpg){:width="512px"}
- 这里记得不要选择安装ubuntu时下载更新，有可能网络原因导致安装很久。
![](https://socofels.github.io/assets/images/install_system/ubuntu_2.jpg){:width="512px"}
- 选择共存，弹出提示分区留意下没有错就行了。
- 然后就大工高成，开机时会出现grub2选择菜单,选择想要的系统就行。

---
