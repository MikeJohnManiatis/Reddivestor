from .Processor import Processor
from bs4 import BeautifulSoup


class CryptoProcessor(Processor):
    
    def __init__(self):
        super(CryptoProcessor, self).__init__()
        self.test_coin_list = ["btc", "bitcoin", "eth", "ethereum", "bch", "bitcoin cash", "bitcoincash", "satoshi", "xrp", "cardano", "ada", "binancecoin", "binance coin", "bnb", "litecoin", "ltc", "chainlink", "link"]
        self.seen_post_titles = []

    def handle(self, message: BeautifulSoup):
        for message_item in message.findAll(['h3', 'p']):
            post = message_item.text.lower()
            if(post not in self.seen_post_titles):
                # words_in_post_count = 0 #add this as a unit test TODO
                for word in post.split(" "):
                    if (word in self.test_coin_list):
                        # print(word)
                        # words_in_post_count += 1
                        # print(words_in_post_count)
                        if(word not in self.processor_dict.keys()):
                            self.processor_dict[word] = 1
                        else:
                            self.processor_dict[word] = self.processor_dict[word] + 1
                        break
            self.seen_post_titles.append(post)

        