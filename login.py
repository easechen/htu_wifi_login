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

if __name__=='__main__':
    print("已运行")
    start_url = 'http://1.1.1.1'
    # 帐号密码
    userName = ''  # 账户名
    passwd = '' # 密码
    net = '移动' # 移动、电信、联通
    # get请求
    r = requests.get(start_url)
    # login_url
    login_url = r.url
    # 未登录
    if '河南师范大学' in r.text:
        Info = createInfo(start_url, userName, passwd, net, r)
        r = login(Info[0], Info[1], login_url)
        if r:
            print("您已登录")
    else:
        print("您已登录")
        #login_out()
