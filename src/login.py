import requests
from lxml import etree
# 这里修改成自己的帐号密码和网络类型
# ------------------------------------
userName = '192842***' # 用户名
passwd = 'abc***' # 密码
net = '移动' # 类型，移动，联通，电信

passwd_1 = ''#教学楼校园网密码（身份证后七位的前六位）
# ------------------------------------

# return start urls
def getStartUrl():
    return "http://www.baidu.com"
    # return "http://210.42.255.130/portalReceiveAction.do?wlanuserip=10.37.131.137&wlanacname=HNSFDX_H3C-S8808-X"

# 构造数据
def createInfo(location,userName, passwd, net, r):
    
    # 网络类型字典
    network = {'移动':'@yd','联通':'@lt','电信':'@dx'}

    # body 参数
    userid = userName+network[net]
    useridtemp = userid
    operator = network[net]
    #获取登录url
    login_url = r.url
    cookie = r.headers['Set-Cookie']
    cookie = cookie[:-18]
    # 获取 wlanuserip
    userip_p1 = login_url.index('wlanuserip=')+11
    userip_p2 = login_url.index('&')
    wlanuserip = login_url[userip_p1:userip_p2]
    # 获取 wlanacname
    acname_p1=login_url.index('wlanacname=')+11
    wlanacname = login_url[acname_p1:]
    # 获取网关地址
    gateway_end = login_url.find("portal")-1
    gateway_host_ip = login_url[7:gateway_end]
    gateway_host = login_url[:gateway_end]
    # 获取交换机 wlanacIp
    html = etree.HTML(r.text)
    wlanacIp = html.xpath('//input[@id="wlanacIp"]/@value')[0]
    # 宿舍
    if (location == '宿舍'):
        head={'Host': gateway_host_ip,'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','Content-Length': '668','Origin': gateway_host,'Connection': 'close','Referer': login_url,'Cookie': cookie,'Upgrade-Insecure-Requests': '1'}
        body = 'wlanuserip=%s&wlanacname=%s&chal_id=&chal_vector=&auth_type=PAP&seq_id=&req_id=&wlanacIp=%s&ssid=&vlan=&mac=&message=&bank_acct=&isCookies=&version=0&authkey=88----89&url=&usertime=0&listpasscode=0&listgetpass=0&getpasstype=0&randstr=4430&domain=&isRadiusProxy=true&usertype=0&isHaveNotice=0&times=12&weizhi=0&smsid=1&freeuser=&freepasswd=&listwxauth=0&templatetype=1&tname=shida_pc_portal_mubiao_V2.1&logintype=0&act=&is189=false&terminalType=&checkterminal=true&portalpageid=261&listfreeauth=0&viewlogin=1&userid=%s&authGroupId=&userName=%s&passwd=%s&useridtemp=%s&operator=%s' % (wlanuserip, wlanacname, wlanacIp, userid, userName, passwd, useridtemp, operator)
    # 东综
    elif (location == '教学楼'):
        head = {'Host': gateway_host_ip,'Proxy-Connection': 'keep-alive','Content-Length': '600','Cache-Control': 'max-age=0','Upgrade-Insecure-Requests': '1','Origin': gateway_host,'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Referer': login_url,'Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-CN,zh;q=0.9','Cookie': cookie}
        body = {'wlanuserip': wlanuserip,'wlanacname': wlanacname,'chal_id':'' ,'chal_vector':'' ,'auth_type': 'PAP','seq_id':'' ,'req_id': '','wlanacIp': wlanacIp,'ssid': '','vlan':'' ,'mac': '','message':'' ,'bank_acct': '','isCookies':'' ,'version': '0','authkey': '88----89','url': '','usertime': '0','listpasscode': '0','listgetpass': '0','getpasstype': '0','randstr': '8587','domain': '','isRadiusProxy': 'false','usertype': '0','isHaveNotice': '0','times': '12','weizhi': '0','smsid': '','freeuser':'' ,'freepasswd': '','listwxauth': '0','templatetype': '1','tname': 'shida_pc_portal','logintype': '0','act':'' ,'is189': 'false','terminalType':'' ,'checkterminal': 'true','portalpageid': '101','listfreeauth': '0','viewlogin': '1','userid': '1928424171', 'authGroupId':'' , 'useridtemp': userName, 'passwd': passwd_1 } 
        #raw_body = "wlanuserip=%s&wlanacname=%s&chal_id=&chal_vector=&auth_type=PAP&seq_id=&req_id=&wlanacIp=210.42.255.60&ssid=&vlan=&mac=&message=&bank_acct=&isCookies=&version=0&authkey=88----89&url=&usertime=0&listpasscode=0&listgetpass=0&getpasstype=0&randstr=2934&domain=&isRadiusProxy=false&usertype=0&isHaveNotice=0&times=12&weizhi=0&smsid=&freeuser=&freepasswd=&listwxauth=0&templatetype=1&tname=shida_pc_portal&logintype=0&act=&is189=false&terminalType=&checkterminal=true&portalpageid=101&listfreeauth=0&viewlogin=1&userid=601nb&authGroupId=&useridtemp=%s&passwd=%s" % (wlanuserip, wlanacname, userName, passwd)
    return head, body

#登录
def login(head, body, r):
    login_url = r.url
    # 获取网关地址
    gateway_end = login_url.find("portal")-1
    gateway_host = login_url[:gateway_end]

    login_api = gateway_host+"/portalAuthAction.do"
    # post
    r = requests.post(login_api,headers=head,data=body)
    # r = requests.post(login_api,data=body)
    # print(r.text)
    # 判断是否登录成功
    if r.url in ["http://autewifi.net", "http://www.htu.cn/"]:
        return True
    else:
        return False

# 登出
def login_out():
    loginOutUrl = "http://autewifi.net/loginOut"
    head={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0','Cookie': 'JSESSIONID=29256E22762FCB9073F8492E5EBB6001',
    }
    r = requests.post(url=loginOutUrl,headers=head)
    if "下线成功" in r.text:
        return True
    else:
        return False

# 测试是否已连接至网络
def isConnected(start_url):
    # get请求
    try:
        requests.get(start_url)
    # 未连接至网络，出错
    except:
        return False
    # 已连接至网络
    else:
        return True
    
# 是否已经登录
def isLogin(r):
    if "河南师范大学" in r.text or "location.href" in r.text:
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

# 返回所处环境名称
def returnLocation(r):
    location = ''
    if "location.href" in r.text or "河南省新乡市建设东路46号" in r.text:
        location = '教学楼'
    elif '河南师范大学校园网登录' in r.text:
        location = '宿舍'
    
    return location


if __name__=='__main__':
    print("已运行")
    print("正在检测运行环境......") 
    
    start_url = getStartUrl()

    # 测试是否连接至网络
    if isConnected(start_url):
        r = requests.get(start_url)
    else:
        print("错误！您尚未连接至网络！请检查网络设置后再试！")
        input()
        exit(1)

    #  如果未登录
    if not isLogin(r):
        # 获取地点名称
        location = returnLocation(r)
        print("当前处于 "+location+" ！")
        # 如果位于宿舍
        if (location == '宿舍'):
            while (True):
                
                # 输入功能
                # -----------------------------------
                #userName = input("请输入用户名：")
                #passwd = input("请输入密码：")
                #net = getNet()
                # -----------------------------------
                Info = createInfo(location,userName, passwd, net, r)
                isLoginSuccess = login(Info[0], Info[1], r)
                print("正在尝试登录......")
                # 登录成功
                if isLoginSuccess:
                    print("登录成功！")
                    break
                # 登录失败
                else:
                    print("认证错误或其他设备已登录，是否要重新登录？(yes or no):")
                    isRelogin = input()
                    if isRelogin in ['yes', 'y','\n']:
                        continue
                    else:
                        print("登录失败！")
                        input()
                        exit(1)
        # 如果位于东综
        elif (location == '教学楼'):
            html = etree.HTML(r.text)
            new_url = html.xpath('//a/@href')[0]
            r = requests.get(new_url)
            Info = createInfo(location,'1928424171','207211','移动',r)
            isLoginSuccess = login(Info[0], Info[1], r)
            if isLoginSuccess:
                print("登录成功！")
    else :
        print("您已登录!\n是否要退出登录？(yes or no):")
        isloginOut=input()
        if isloginOut in ['yes','y', '\n']:
            if login_out():
                print("已退出！")
            else:
                print("退出失败！")
    print("运行结束！") 
    input()
    exit(0)
