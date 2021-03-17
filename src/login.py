import requests

# 构造数据
def createInfo(start_url, userName, passwd, net, r):
    
    # 网络类型字典
    network = {'移动':'@yd','联通':'@lt','电信':'@dx'}

    # body 参数
    userid = userName+network[net]
    useridtemp = userid
    operator = network[net]
    #获取登录url
    login_url = r.url
    cookie = r.headers['Set-Cookie']
    # 获取 wlanuserip
    userip_p1 = login_url.index('wlanuserip=')+11
    userip_p2 = login_url.index('&')
    wlanuserip = login_url[userip_p1:userip_p2]
    # 获取 wlanacname
    acname_p1=login_url.index('wlanacname=')+11
    wlanacname = login_url[acname_p1:]

    head={
        'Host': '10.101.2.199',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '668',
        'Origin': 'http://10.101.2.199',
        'Connection': 'close',
        'Referer': login_url,
        'Cookie': cookie,
        'Upgrade-Insecure-Requests': '1'
    }
    body={
        'wlanuserip' : wlanuserip,
        'wlanacname' : wlanacname,
        'auth_type' : 'PAP',
        'wlanacIp' : '10.101.2.35',
        'version' : '0',
        'authkey' : '88----89',
        'usertime' : '0',
        'listpasscode' : '0',
        'listgetpass' : '0',
        'getpasstype' : '0',
        'randstr' : '4929',
        'isRadiusProxy' : 'true',
        'usertype' : '0',
        'isHaveNotice' : '0',
        'times' : '12',
        'weizhi' : '0',
        'smsid' : '1',
        'listwxauth' : '0',
        'templatetype' : '1',
        'tname' : 'shida_pc_portal_mubiao_V2.1',
        'logintype' : '0',
        'is189' : 'false',
        'checkterminal' : 'true',
        'portalpageid' : '261',
        'listfreeauth' : '0',
        'viewlogin' : '1',
        'userid' : userid,
        'userName' : userName,
        'passwd' : passwd,
        'useridtemp' : useridtemp,
        'operator' : operator
    }

    return head, body

#登录
def login(head, body, login_url):
    login_api = "http://10.101.2.199/portalAuthAction.do"
    # post
    r = requests.post(login_api,headers=head,data=body)
    # 判断是否登录成功
    if r.url == "http://autewifi.net":
        return True
    else:
        return False

# 登出
def login_out():
    loginOutUrl = "http://autewifi.net/loginOut"
    head={
        'Host': 'autewifi.net',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http://autewifi.net',
        'Connection': 'close',
        'Referer': 'http://autewifi.net/',
        'Cookie': 'JSESSIONID=29256E22762FCB9073F8492E5EBB6001',
        'Content-Length': '0'
    }
    r = requests.post(url=loginOutUrl,headers=head)
    if "下线成功" in r.text:
        return True
    else:
        return False

# 是否已经登录
def isLogin(r):
    if "河南师范大学" in r.text:
        return False
    else:
        return True

# 返回网络类型        
def getNet():
    netDict={'1':'移动', '2':'电信', '3':'联通'}
    print("1、移动\n2、电信\n3、联通\n")
    while(True):
        num = input("请输入网络类型：")
        try:
            net = netDict[num] 
        except:
            print("非法，请重新输入:")
            continue
        # 如果没有发生异常，返回值
        else:
            return net
            break

if __name__=='__main__':
    print("已运行")
    start_url = 'http://119.29.29.29/'
    # 帐号密码和网络类型
    userName = '' # 用户名
    passwd = '' # 密码
    net = '' # 类型，移动，联通，电信
    # get请求
    try:
        r = requests.get(start_url)
    except:
        print("错误！未连接至校园网，请检查网络设置！\n")
        print("任意键退出！")
        exit(1)
    # login_url
    login_url = r.url
    #  如果未登录
    if not isLogin(r):
        userName = input("请输入用户名：")
        passwd = input("请输入密码：")
        net = getNet()
        Info = createInfo(start_url, userName, passwd, net, r)
        r = login(Info[0], Info[1], login_url)
        if r:
            print("您已登录")
    else:
        print("您已登录!\n是否要退出登录？(yes or no):")
        isloginOut=input()
        if isloginOut in ['yes','y']:
            if login_out():
                print("已退出！")
            else:
                print("退出失败！")
    print("运行结束！按任意键推出。") 
    input()
