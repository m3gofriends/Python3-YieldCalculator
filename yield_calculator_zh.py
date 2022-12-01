from bs4 import BeautifulSoup
from lxml import etree
import requests

def now_yield(stock_code):
    response = requests.get("https://tw.stock.yahoo.com/quote/" + stock_code + "/dividend")
    soup = BeautifulSoup(response.content, "html.parser")
    dom = etree.HTML(str(soup))
    stock_name = dom.xpath('//*[@id="main-0-QuoteHeader-Proxy"]/div/div[1]/h1')[0].text
    share_price = float(dom.xpath('//*[@id="main-0-QuoteHeader-Proxy"]/div/div[2]/div[1]/div/span[1]')[0].text)
    cash_dividend = float(dom.xpath('//*[@id="main-2-QuoteDividend-Proxy"]/div/section[2]/div[2]/div/div/div[2]/ul/li[1]/div/div[2]/span')[0].text)
    stock_dividend = float(dom.xpath('//*[@id="main-2-QuoteDividend-Proxy"]/div/section[2]/div[2]/div/div/div[2]/ul/li[1]/div/div[3]/span')[0].text)
    print(stock_name + stock_code + "  當前股價:" + str(share_price) + ",  現金殖利率:" + str(round(cash_dividend *100 /share_price, 1)) + "%,  股票殖利率:" + str(round(stock_dividend *100 /share_price, 1)) + "%\n")
    

now_yield('2330.TW')
now_yield('2882.TW')
now_yield('2885.TW')
now_yield('2881.TW')
now_yield('2891.TW')
now_yield('2889.TW')
now_yield('2888.TW')
now_yield('2890.TW')
now_yield('2886.TW')
now_yield('2887.TW')
now_yield('2892.TW')
now_yield('5880.TW')
now_yield('5876.TW')
now_yield('2880.TW')
now_yield('2884.TW')
