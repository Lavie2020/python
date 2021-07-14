import requests
if __name__ == '__main__':
    url = 'https://www.sogou.com/web?s?'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }

    kw = input('请输入要查找的关键词：')
    param = {
        'query': kw
    }

    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text

    Filename = kw + '.html'
    with open(Filename,'w',encoding='utf-8') as f:
        f.write(page_text)
    print(Filename,'保存成功')
