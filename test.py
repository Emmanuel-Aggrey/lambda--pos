import requests

cookies = {
    'csrftoken': 'Zxq3FStFYro1AeWRLggNYvcB2ENFMcA00UKMGRcyBkicYTnGIvAjRIIROhEepBmm',
    'sessionid': '95p1cs94gg79aafn9dqh8273al912jy4',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'http://127.0.0.1:8000/',
    'Accept-Language': 'en-US,en;q=0.9,la;q=0.8',
}

response = requests.get('http://127.0.0.1:8000/business/supliers/', headers=headers, cookies=cookies)

print("response",response)