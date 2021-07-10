# 河南师范大学校园网自动登录脚本
> 本脚本仅供学习使用，请勿用于非法用途，否则一切责任均与本人无关。
>
> 如果您下载并使用本程序，即视为同意上述条款。

此脚本可用于登录河南师范大学寝室或者教学楼的校园网络，无需打开浏览器。

目前已支持寝室（仅在东区宿舍进行过测试）和东综教学楼的校园网登录。

## 效果

### 登录

![login.gif](https://pic.chens.life/images/2021/04/08/login.gif)

### 登出

![loginout.gif](https://pic.chens.life/images/2021/04/08/loginout.gif)

## 功能完成

- [x] 宿舍网络的登录
- [x] 宿舍网络的登出
- [x] 教学楼（东综）

## 所需的库
- requests
- lxml

## 使用方法
首先安装`requests`和`lxml`库，

~~~bash
pip install requests lxml
~~~

下载代码，修改`src/login.py`代码中的用户名、密码和网络类型，之后直接运行即可。

~~~python
python login.py
~~~

## 自动登录

使用脚本实现开机自动启动脚本进行登录。

### windows

使用@CykaOWO提供的方法：

新建bat代码如下
~~~bash
 @echo off
 choice /t T /d y /n >nul
 start "" "路径\login.py"
~~~
 第二行T改为时间，单位为秒。将他们添加到开机启动项即可。详见 https://answers.microsoft.com/zh-hans/windows/forum/windows_10-other_settings/windows/a81e83eb-a079-4b3c-9d8f-facc9ed03871?tm=1442997086548

### Linux

新建`wifi`，填入

~~~bash
#!/bin/bash
python3 PATH/login.py
~~~

赋予权限

~~~bash
sudo chmod +x wifi
~~~

将其复制到`bin`目录，这样即可在终端直接输入`wifi`直接启动。

~~~bash
sudo cp wifi /usr/bin/
~~~



## 更新日志

### 2021-4-9

1. 增强了通用性，目前西区宿舍应该可以正常登录。
2. 东区综合教学楼已可以进行登录。

### 2021-3-17

1. 增加了异常处理，使其在未连接至路由器时，不至于闪退。
2. 修改了一些代码，使得程序更具有通用性。
3. 增加了，如果账户已在其他设备登录，选择进行重新登录的机制。
4. 提高了代码质量。

### 2021-3-12

1. 增加了输入功能
