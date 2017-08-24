import requests

'''
草码API功能:

1.用户登陆
2.获取个人信息
3.获取手机号码
4.释放已获取号码
5.获取短信并不再使用本号
6.获取短信并继续使用本号(还没做)
7.加黑无用号码
8.已获取号码列表(还没做)
9.发短信详细说明(还没做)
10.获取短信发送状态(还没做)
接口地址： http://api.vvvce.org/http.aspx?action=
备用接口地址1：http://api64.tel8.net/http.aspx?action=
备用接口地址2： http://api68.tel8.net/http.aspx?action=
备用接口地址3： http://api75.tel8.net/http.aspx?action=

'''
Caoma_id = 'q209209a'
Caoma_psw = 'psw'


class Caoma(object):
    # url = 'http://xapi.tguma.com:9999/Method?'
    url = 'http://api64.tel8.net/http.aspx?action='

    def login(self, Caoma_id='q209209a', Caoma_psw='psw'):
        self.url = Caoma.url + 'loginIn&uid={}&pwd={}'.format(Caoma_id, Caoma_psw)
        self.r = requests.get(self.url)
        print('登录情况:', self.r.text)
        return self.r.text

    def getUserInfos(self, uid, token):
        self.url = Caoma.url + 'getUserInfos&uid={}&token={}'.format(uid, token)
        self.r = requests.get(self.url)
        print('账号情况:', self.r.text)

    def getMobilenum(self, pid, uid, token):
        self.url = Caoma.url + 'getMobilenum&pid={}ID&uid={}&token={}&size=1'.format(pid, uid, token)
        self.r = requests.get(self.url)
        print('获取账号情况:', self.r.text)
        return self.r.text

    def getVcodeAndReleaseMobile(self, pid, uid, token, mobile, author='q209209a'):
        self.url = Caoma.url + 'getVcodeAndReleaseMobile&uid={}&token={}&pid={}&mobile={}&author_uid={}'.format(uid,
                                                                                                                token,
                                                                                                                pid,
                                                                                                                mobile,
                                                                                                                author)
        self.r = requests.get(self.url)
        print('获取验证码:', self.r.text)
        return self.r.text
        pass

    def addIgnoreList(self, pid, uid, token, mobile):  # 这里可以批量加黑,用','分隔开即可! 因暂不需要 没做这个功能!
        self.url = Caoma.url + 'addIgnoreList&uid={}&token={}&mobiles={}&pid={}'.format(uid, token, mobile, pid)
        self.r = requests.get(self.url)
        print('加黑账号:', self.r.text)
        return self.r.text
        pass


if __name__ == '__main__':
    t = Caoma()
    uid, token = t.login().split('|')



    pid = '2171'

    t.getUserInfos(uid, token)
    t.getMobilenum(pid, uid, token).split('|')

    pass
