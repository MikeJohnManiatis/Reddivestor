from com.src.Spider import Spider
from com.src.CryptoProcessor import CryptoProcessor
from com.src.network.ApiRequester import ApiRequester
import threading
import time


processor = CryptoProcessor()

def engine_start():
    interval = 5
    print("!!!! Spider Engine starting, initializing processors and spiders !!!!")
    spider_cryptoCurrency = Spider(interval, 'https://www.reddit.com/r/CryptoCurrencies/new/', processor)
    spider_cryptoCurrency.setUpDriver()
    spider_cryptoCurrencyTrading = Spider(interval, 'https://www.reddit.com/r/CryptoCurrencyTrading/new/', processor)
    spider_cryptoCurrencyTrading.setUpDriver()
    spider_cryptoCryptoMarkets = Spider(interval, 'https://www.reddit.com/r/CryptoMarkets/new/', processor)
    spider_cryptoCryptoMarkets.setUpDriver()

    thread = threading.Thread(target=spider_cryptoCurrency.crawlAndRefresh, args=())
    thread.daemon = True    

    thread2 = threading.Thread(target=spider_cryptoCurrencyTrading.crawlAndRefresh, args=())
    thread2.daemon = True

    thread3 = threading.Thread(target=spider_cryptoCryptoMarkets.crawlAndRefresh, args=())
    thread3.daemon = True


    thread.start()
    thread2.start()
    thread3.start()
       

    

def main():
    api_requester = ApiRequester(None, None, None)
    print(api_requester.get())
    # engine_start()
    # while(True):
    #     print("Engine is up and running...")
    #     print("Displaying contents of processor: ") 
    #     print(" ")
    #     time.sleep(20)
    #     processor.display()

if __name__ == "__main__":
    main()
