import requests
## author:Olvk 
## input:model you wanna search,download PDF or not
## output:the description of search model from semiee,and download PDF from semiee.
## date:230921

keyword='TPS63020'
download_pdf=False

def download_pdf(id):
    url = f"https://www.semiee.com/bdxx-api/chip/detail/{id}"
    response = requests.get(url, headers=headers, cookies=cookies)
    company = response.json()
    url=company['result']['dsFile']['path']
    return url


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


def get_model_description(model_name:str):
    params = {
    "pageIndex": 0,
    "pageSize": "10",
    "model": model_name
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    data=response.json()
    return data

if __name__=="__main__":
    print(get_model_description("741"))