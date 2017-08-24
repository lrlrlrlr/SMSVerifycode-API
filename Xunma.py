import requests
import time
import re


def Xunma_login(userName='akii', psw='psw'):
    url = 'http://xapi.xunma.net/Login?uName={}&pWord={}&VER=2'.format(userName, psw)
    # Developer='beerGyZRfCtQABhVf9XP9g%3d%3d'
    # url='http://xapi.xunma.net/Login?uName={}&pWord={}&Developer={}'.format(userName,psw,Developer)
    r = requests.get(url)
    if r.status_code == 200:

        token, balance, _, _, _, _, _ = r.text.split('&')
        print('登录成功!账户余额:', balance)
        return token
    else:
        print('登录错误!status_code:{},\n详细:{}'.format(r.status_code, r.text))


def Xunma_getphone(token):
    url = 'http://xapi.xunma.net/getPhone?token={}&ItemId=9317&Count=1&Area=%E4%B8%8D%E9%99%90&PhoneType=0&Phone='.format(
        token)
    r = requests.get(url)

    print('申请号码:{}'.format(r.text))
    return re.search(r'\d+', r.text).group()


def Xunma_getQueue(token):
    url = 'http://xapi.xunma.net/getQueue?token={}'.format(token)
    r = requests.get(url)
    return r.text


def Xunma_getMessage(token, phone):
    url = 'http://xapi.xunma.net/getMessage?token={}&itemId=9317&phone={}'.format(token, phone)
    r = requests.get(url)
    if r.status_code == 200:
        # token, balance, _, _, _, _, _ = r.text.split('&')

        return r.text
        # return token
    else:
        print('获取错误!status_code:{},\n详细:{}'.format(r.status_code, r.text))


def Xunma_releasePhone(token, phone, itemId='9317'):
    url = 'http://xapi.xunma.net/releasePhone?token={}&phoneList={}-{};'.format(token, phone, itemId)
    r = requests.get(url)
    if r.status_code == 200:
        print('释放号码:', phone, r.text)
    else:
        print('释放错误!status_code:{},\n详细:{}'.format(r.status_code, r.text))


if __name__ == '__main__':
    token = Xunma_login()
    phone = str(Xunma_getphone(token))

    result = Xunma_getMessage(token, phone)
    timeout = 0

    while result == 'Null' or result == 'NOTION&单笔充值满 50元送 5%单笔充值满100元送10%自动赠送！上不封顶！[End]':
        time.sleep(8)
        result = Xunma_getMessage(token, phone)
        timeout += 1
        if timeout >= 20:
            print('timeout!release!')
            Xunma_releasePhone(token, phone)
            break
        else:
            print('check..', timeout)

    try:
        verifycode = re.search(r'(?<=\?)\d{4}(?=\?)', result).group()
    except:
        print('正则提出验证码的时候好像出错了!请检查!', result)
