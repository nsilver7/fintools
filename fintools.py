#!/usr/bin/env python

import requests
import yfinance as yf

def options_expirations(ticker):
    expirations = ticker.options
    print(expirations)
    print(ticker.option_chain('2021-04-23'))


def main():
    print('hello self')
    fangs = yf.Tickers("FB AMZN AAPL NFLX GOOG")
    print(fangs.tickers['FB'].info['regularMarketPrice'])
    options_expirations(fangs.tickers['FB'])


if __name__ == '__main__':
    main()