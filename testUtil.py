import time
import hashlib
import requests
session = requests.session()

# hashlibts = int(round(time.time() * 1000))
# param = "ts=1650790879273&verify=2323232&phone=15727023402&key=NiPcywkZs2eWmTIYZWHj1oTLNOggog95"
# h1 = hashlib.md5()
# h1.update(param.encode(encoding='utf-8'))
# sign = h1.hexdigest()
# decodeURL = "9099BE74481792CBC95B7664C8295569"
# print(sign.upper())


headers = {
'Accept': 'application/json, text/plain, */*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Authorization': 'Bearer null',
'Connection': 'keep-alive',
'Content-Length': '119',
'Content-Type': 'application/json',
'Host': 'api.nftqin.com',
'Origin': 'https://www.nftqin.com',
'Referer': 'https://www.nftqin.com/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-site',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

ts = int(round(time.time() * 1000))
signParam = "id=61454&pay_type=sand_h5&ts={0}&key=NiPcywkZs2eWmTIYZWHj1oTLNOggog95".format(ts)
h1 = hashlib.md5()
h1.update(signParam.encode(encoding='utf-8'))
sign = h1.hexdigest().upper()
purchaseUrl = "https://api.nftqin.com/api/payment/purchase"
accessToken = "'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLm5mdHFpbi5jb21cL2FwaVwvYXBwXC9sb2dpbiIsImlhdCI6MTY1MDg3MjA5OSwiZXhwIjoxNjUzNDY0MDk5LCJuYmYiOjE2NTA4NzIwOTksImp0aSI6InhQcnB5aTFBNXJBY3RLTUwiLCJzdWIiOjMxNDQyOCwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.c2zMl3rQXjP6Y6T-7I8t5CLp_Ne4FWZcC0iZLxb59R0'"
form_data = {'id': '61454',
             'pay_type': 'sand_h5',
             'ts': ts,
             'sign': sign
             }
headers = {'Authorization': accessToken}

res = session.post(url=purchaseUrl, data=form_data, headers=headers, verify=False)
print(res.status_code)
print(res.json())




