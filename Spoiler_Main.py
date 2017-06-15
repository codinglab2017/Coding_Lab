# -*- coding: utf-8 -*-

import Spoiler_Crawler
#import Utils
import os

class Main():
    """
    This class provides the basic functionalities to run the programm.
    """
    
    def __init__(self, **kwargs):
        # first, looks if there is a file that contains a portfolio
        if os.path.exists(os.path.join(os.getcwd(),"Portfolio.db")):
            pass # Enter DB-Access here, if ready
        else:
            self.portfolio = {}
            self.money = 10000 
            self.portfolio_value = self.money
        # Initialize the crawler and the list of all prices
        if "Stocks" in kwargs:
            self.crawler = Spoiler_Crawler.Crawler(kwargs["Stocks"])
            self.prices = self.crawler.get_prices()
        else: 
            self.crawler = Spoiler_Crawler.Crawler([])
            self.prices = {}  
        
    def __repr__(self):
        return "\n".join("{} : {}".format(x, y) for x, y in self.portfolio.items())
    
    def buy_stock(self, symbol, money):
        """ allows to add a stock to your portfolio, reducing your money """
        if money <= self.money: # No credit
            price = self.crawler.get_stock_price(symbol)
            amount = money // price
            self.portfolio[symbol] = amount
            self.money -= price
            self.portfolio_value += amount
        
    def sell_stock(self, symbol, amount):
        """ allows to sell a stock to your portfolio, increasing your money """
        if amount <= self.portfolio[symbol]: # No shortselling
            money = amount * self.crawler.get_stock_price(symbol)
            self.money += money
            self.portfolio_value -= money
            self.portfolio[symbol] -= amount
            if self.portfolio[symbol] == 0: del self.portfolio[symbol]
    
    def add_stock_to_watchlist(self, symbol):
        """ adds a stock to the stocklist if it is not already there """
        if symbol not in self.prices: 
            self.crawler.stocks.append(symbol)
            self.prices[symbol] = self.crawler.get_stock_price(symbol)
        
    def delete_stock_from_watchlist(self, symbol):
        """ removes a stock if this stock was in the list """
        if symbol in self.prices: 
            self.crawler.stocks.remove(symbol)
            del self.prices[symbol]

    def update_watchlist(self):
        """ refreshes the prices of all stocks """
        self.prices = self.crawler.get_prices()







if __name__ == "__main__":
    # Test cases:
    main = Main(Stocks=["AAPL", "GOOG"])
    assert main.crawler, \
                 "Your was not imported propery"
    print("crawler imported correctly")
    main.add_stock_to_watchlist("ALV")
    assert len(main.prices) == 3, \
                 "Your programm failed at adding a stock to the watchlist"
    print("passed watchlisttest")
    main.delete_stock_from_watchlist("AAPL")
    assert "AAPL" not in main.prices, \
                "Your programm failed at removing a stock from the watchlist"
    print("passed watchlisttest2")
    main.buy_stock("AAPL", 500)
    assert len(main.portfolio) == 1 and main.portfolio_value != 0, \
                "Your programm failed at buying a stock"
    print("buying seems to work propery")   
    before = main.portfolio["AAPL"]
    main.sell_stock("AAPL", 1)
    assert main.portfolio["AAPL"] == before - 1, \
                "Your programm failed at selling a stock"
    print("selling seems to work propery")  
    main.update_watchlist()
    assert len(main.portfolio) ==  1, \
                "You´ve got too much stocks in your portfolio"
    print("updating works properly")
    print(main)
    print("Congrats! Everything seems to be fine!")