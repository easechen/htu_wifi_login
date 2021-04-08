# 河南师范大学寝室校园网自动登录脚本
本脚本仅供学习使用，目前只在东16实验过。

目前不支持教学楼校园网的登录。

## 效果

### 登录

![login](.\img\login.gif)

### 登出

![loginout](.\img\loginout.gif)

## 功能完成

- [x] 宿舍网络的登录
- [x] 宿舍网络的登出

## 所需的库
- requests

## 使用方法
首先安装`requests`库，
下载[Release中的文件](https://github.com/easechen/htu_wifi_login/releases/)，修改`src/login.py`代码中的用户名、密码和网络类型，之后直接运行即可。

~~~python
python login.py
~~~
