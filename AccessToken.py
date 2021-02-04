from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json
def get_AccessToken():
# 创建AcsClient实例
    client = AcsClient(
    "<您的AccessKey Id>", 
    "<您的AccessKey Secret>",
    "cn-shanghai"
    )
    #AccessKey Id,AccessKey Secret 获取连接https://ram.console.aliyun.com/manage/ak

    # 创建request，并设置参数。
    request = CommonRequest()
    request.set_method('POST')
    request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
    request.set_version('2019-02-28')
    request.set_action_name('CreateToken')
    response = client.do_action_with_exception(request)
    AccessToken = json.loads(response)
    # print(token['Token']['Id'])
    Token = AccessToken['Token']['Id']
    print(Token)
    return Token

if __name__ == "__main__":
    get_AccessToken()


    # a = {"ErrMsg":"","Token":{"UserId":"1871151503227322","Id":"1c6645087c7c4b3185d5f637dc165282","ExpireTime":1606048513}}
    # print(a)