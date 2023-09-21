import requests
# import pandas as pd
#
# df=pd.DataFrame(columns=['model','description','company'])

keyword='TPS63020'
download_pdf=True

def download_pdf_1_4(id):
    url = f"https://www.semiee.com/bdxx-api/chip/detail/{id}"
    response = requests.get(url, headers=headers, cookies=cookies)
    company = response.json()
    # print(response.text)
    # print(response)


    # r = requests.get(company['result']['dsFile']['path'], headers=headers,
    #                         cookies=cookies)
    # response_header=r.headers['content-disposition']
    # name = name.replace('*','')
    # name = urllib.parse.unquote(response_header)#.replace('"attachment;filename*=UTF-8''','').replace('"','')
    # name=name.replace('attachment;filename*=UTF-8''','').replace("''",'')
    # name=f'{name}'
    name=company['result']['dsFile']['name']
    url=company['result']['dsFile']['path']
    print(f"pdf链接为{url}")
    # if not os.path.exists(name):
    #     with open(f"{name}", "wb") as code:
    #         code.write(r.content)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "deviceId": "ca339206",
    "token": "",
    "source": "1",
    "os": "2",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "https://www.semiee.com/search?searchModel=LM358",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
cookies = {
    "JSESSIONID": "C955A2FDACD71937FDF493C925827727",
    "UM_distinctid": "18ab58b778c54-071d3c42767be18-d525429-110400-18ab58b779038",
    "CNZZDATA1272851447": "1181596866-1695262931-%7C1695262950"
}
# for page in range(4,6):
url = "https://www.semiee.com/bdxx-api/chip/v3/rich/search"
params = {
    "pageIndex": 0,
    "pageSize": "10",
    "model": keyword
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
data=response.json()
if len(data['result'])>10:
    for line in data['result'][:10]:
        print({'model':keyword,'description':line['descri'],'company':line['brand_name']})
        if download_pdf:
            download_pdf_1_4(line['id'])

else:
    for line in data['result']:
        print({'model':keyword,'description':line['descri'],'company':line['brand_name']})
        if download_pdf:
            download_pdf_1_4(line['id'])
    # df=df._append({'model':keyword,'description':line['descri'],'company':line['brand_name']},ignore_index=True)
    # print()
# print(response.text)
# print(response)