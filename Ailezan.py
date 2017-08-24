import requests,time


class Ailezan(object):
	url='http://api.hellotrue.com/api/do.php?'

	def login(self,uid='api-c777w00r',psw='psw'):
		self.url=Ailezan.url+'action=loginIn&name={}&password={}'.format(uid,psw)
		print(self.url)
		self.r=requests.get(self.url)
		print('登录情况:',self.r.text)
		return self.r.text

	def getUserInfos(self,uid,token):
		pass

	def getMobilenum(self,pid,token):
		self.url=Ailezan.url+'action=getPhone&sid={}&token={}'.format(pid,token)
		self.r=requests.get(self.url)
		print('获取账号情况:',self.r.text)
		return self.r.text

	def getVcode(self,pid,token,mobile):
		self.url=Ailezan.url+'action=getMessage&sid={}&phone={}&token={}'.format(pid,mobile,token)
		self.r=requests.get(self.url)
		print('获取验证码:',self.r.text)
		return self.r.text
		pass

	def addIgnoreList(self, pid,token,mobile):  # 这里可以批量加黑,用','分隔开即可! 因暂不需要 没做这个功能!
		self.url=Ailezan.url+'action=addBlacklist&sid={}&phone={}&token={}'.format(pid,mobile,token)
		self.r=requests.get(self.url)
		print('加黑账号:',self.r.text)
		return self.r.text
		pass

	def getSummary(self,token):
		self.url=Ailezan.url+'action=getSummary&token={}'.format(token)
		self.r=requests.get(self.url)
		status,balance,level,批量取号数,usrtype,_ = self.r.text.split('|')
		print('获取账号信息:balance={},level={},批量取号数={}'.format(balance,level,批量取号数))


	def cancelAllRecv(self,token):
		self.url=Ailezan.url+'action=cancelAllRecv&token={}'.format(token)
		self.r=requests.get(self.url)
		print('释放所有账号:',self.r.text)

if __name__=='__main__':


	pid='5062'
	t=Ailezan()
	login_status,token=t.login().split('|')

	if login_status =='1':

		getmobilenum_status,mobile=t.getMobilenum(pid,token).split('|')


		if getmobilenum_status == '1':
			time.sleep(2)

			Vcode_status,Vcode=t.getVcode(pid,token,mobile).split('|')

			checktimes=0
			while Vcode_status != '1':
				time.sleep(3)
				checktimes+=1
				Vcode_status,Vcode=t.getVcode(pid,token,mobile).split('|')
				if checktimes > 20:
					print('timeout!realease...')
					t.addIgnoreList(pid,token,mobile)
					break
			if Vcode_status == '1':
				print(Vcode)
				t.addIgnoreList(pid,token,mobile)
		else:
			print('获取号码出错了!')
	else:
		print('登录出错了!')


