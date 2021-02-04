---

---

### Ai语音合成软件

1、 语音合成服务，通过先进的深度学习技术，将文本转换成自然流畅的语音。目前有多种音色可供选择，并提供调节语速、语调、音量等功能。适用于智能客服、语音交互、文学有声阅读和无障碍播报等场景。 

2、 本软件发音接近人声，比同类的本地语音合成软件声音要好很多！视频配字幕等！本接口采用阿里云免费接口有使用限制！此软件开源免费，代码已上传[GitHub](https://github.com/lyjxhxn)，可以下载下来配置阿里云密钥即可使用，源码支持更多人物声音。

3、每次提交请求不能超过300个汉字。

#### **一、使用方法及运行环境**

**1、推荐使用python3.6以上版本编译器！**

**2、[语音合成必要sdk获取链接及使用方法](https://www.alibabacloud.com/help/zh/doc-detail/120699.htm)**

![](https://img.zsykjm.com/2021/02/04/01.png)

**3、[阿里云SDK核心库使用方法](https://help.aliyun.com/document_detail/72153.html)**

![](https://img.zsykjm.com/2021/02/04/02.png)

> 此方法是实时获取阿里云sdk，阿里云后台管理首页有临时sdk

**4、需要在cmd命令下安装以下依赖包！**

```python
pip install PyQt5 #Gui界面模块
```

**5、配置密钥**

①语音合成appkey密钥，[获取连接](https://nls-portal.console.aliyun.com/applist)

![](https://img.zsykjm.com/2021/02/04/03.png)

```python
appkey = '<您的Appkey>' #获取链接：https://nls-portal.console.aliyun.com/applist
```

②实时sdk密钥，[获取连接](https://ram.console.aliyun.com/manage/ak)

![](https://img.zsykjm.com/2021/02/04/04.png)

```python
  client = AcsClient(
    "<您的AccessKey Id>", 
    "<您的AccessKey Secret>",
    "cn-shanghai"
    )
    #AccessKey Id,AccessKey Secret 获取连接https://ram.console.aliyun.com/manage/ak

```

**6、运行yuyin1.1 .py主程序**

### 二、发行版本

- 若安装环境或运行报错，可直接下载打包好的exe使用！
### 三、程序界面

### 四、感谢

阿里云提供接口支持！https://ai.aliyun.com/nls/tts?

注意，此版本是免费版有使用时间限制！



![](https://img.zsykjm.com/2021/02/04/05.png)

  