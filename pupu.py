from time import strftime
import requests
import json


## url地址
url = "https://j1.pupuapi.com/client/product/storeproduct/detail/6660fb8b-9a97-417c-ab47-1ef9c102e64a/ed60af11-25b0-48b8-bc5b-f9136d9f89ad"
## 同学的模拟安卓的head
hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'}
## 百度的处理http连接或者访问速度过快
s = requests.session()
s.keep_alive = False

requests = requests.get(url, headers=hd)
dict = json.loads(requests.text)

## 获取商品信息
def p():
    name = dict["data"]["name"]  # 商品名字
    price = str(int(dict["data"]["price"]) / 100)  # 折扣价
    y_price = str(int(dict["data"]["market_price"]) / 100)  # 原价
    spec = dict["data"]["spec"]  # 规格
    content = dict["data"]["sub_title"]  # 描述
    origin = dict["data"]["origin"]  # 产地
    store = dict["data"]["storage_condition"]  # 储存方式
    print("-------------商品：" + name + "-------------")
    print("价格：" + price)
    print("规格：" + spec)
    print("原价/折扣价：" + y_price + "/" + price)
    print("详细内容：" + content)
    print("产地：" + origin)
    print("储存方式：" + store)

#实时价格监控
def time():
    price = str(int(dict["data"]["price"]) / 100)
    print("当前时间为"+strftime("%Y-%m-%d %H:%M")+",价格为"+price)
#主函数
if __name__ == '__main__':
    p()
    time()