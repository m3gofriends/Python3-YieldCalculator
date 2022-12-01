"""                                      
      First publication date : 2022 / 12 / 1
      Author : 張哲銘(Che-Ming Chang)
"""

from bs4 import BeautifulSoup
from lxml import etree
import requests

def now_yield(stock_code, language='en'):
    response = requests.get("https://tw.stock.yahoo.com/quote/" + stock_code + "/dividend")
    soup = BeautifulSoup(response.content, "html.parser")
    dom = etree.HTML(str(soup))
    share_price = float(dom.xpath('//*[@id="main-0-QuoteHeader-Proxy"]/div/div[2]/div[1]/div/span[1]')[0].text)
    cash_dividend = float(dom.xpath('//*[@id="main-2-QuoteDividend-Proxy"]/div/section[2]/div[2]/div/div/div[2]/ul/li[1]/div/div[2]/span')[0].text)
    stock_dividend = float(dom.xpath('//*[@id="main-2-QuoteDividend-Proxy"]/div/section[2]/div[2]/div/div/div[2]/ul/li[1]/div/div[3]/span')[0].text)
    if language == 'zh-TW':
        print(stock_code + "  當前股價:" + str(share_price) + ",  現金殖利率:" + str(round(cash_dividend * 100 / share_price, 1)) + "%,  股票殖利率:" + str(round(stock_dividend * 100 / share_price, 1)) + "%\n")
    elif language == 'zh-CN':
        print(stock_code + "  当前股价:" + str(share_price) + ",  现金殖利率:" + str(round(cash_dividend * 100 / share_price, 1)) + "%,  股票殖利率:" + str(round(stock_dividend * 100 / share_price, 1)) + "%\n")
    elif language == 'jp':
        print(stock_code + "  現在の株価:" + str(share_price) + ",  配当利回り:" + str(round(cash_dividend * 100 / share_price, 1)) + "%,  株式利回り:" + str(round(stock_dividend * 100 / share_price, 1)) + "%\n")
    elif language == 'kr':
        print(stock_code + "  현재 주가:" + str(share_price) + ",  현금수익률:" + str(round(cash_dividend * 100 / share_price, 1)) + "%,  주식 수익률:" + str(round(stock_dividend * 100 / share_price, 1)) + "%\n")
    else:
        print(stock_code + "  Current share price:" + str(share_price) + ",  Cash yield:" + str(round(cash_dividend * 100 / share_price, 1)) + "%,  Stock yield:" + str(round(stock_dividend * 100 / share_price, 1)) + "%\n")
        
now_yield('2330.TW', 'zh-TW')
now_yield('2882.TW', 'zh-TW')
now_yield('2885.TW', 'zh-TW')
now_yield('2881.TW', 'zh-TW')
now_yield('2891.TW', 'zh-TW')
now_yield('2889.TW', 'zh-TW')
now_yield('2888.TW', 'zh-TW')
now_yield('2890.TW', 'zh-TW')
now_yield('2886.TW', 'zh-TW')
now_yield('2887.TW', 'zh-TW')
now_yield('2892.TW', 'zh-TW')
now_yield('5880.TW', 'zh-TW')
now_yield('5876.TW', 'zh-TW')
now_yield('2880.TW', 'zh-TW')
now_yield('2884.TW', 'zh-TW')
