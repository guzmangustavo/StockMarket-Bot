# StockMarket-Bot

A Telegram chatbot that informs the last stock price in Argentinean stock markets.

## Table of contents

* [Introduction](#introduction)
* [Supported stocks](#supportedstocks)
* [Disclaimer](#disclaimer)

### Introduction

StockMarketAR is a Telegram chatbot that returns the last price in Argentinean market of the stock that you indicate. 

In order to get this information, you must enter the stock's ticker.

If you have a Telegram account, it is available at: [t.me/StockMarketARbot](https://telegram.me/StockMarketARbot).

### Supported stocks

The main Python library used in the development of StockMarketAR is [python-telegram-bot](https://python-telegram-bot.org/).

As long as you provide the ticker, the bot can return the last price of the corresponding stock.

The tickers supported by the chatbot are:

 - AGRO, ALUA, AUSO.
 - BBAR, BHIP, BMA, BOLT, BPAT, BRIO, BYMA.
 - CADO, CAPU, CAPX, CARC, CECO2, CELU, CEPU, CGPA2, COME, CRES, CTIO, CVH.
 - DGCU2, DOME, DYCA.
 - EDN, ESME.
 - FERR, FIPL.
 - GAMI, GARO, GBAN, GCLA, GGAL, GRIM.
 - MIRG.
 - HARG, HAVA.
 - INAG, INDU, INTR, INVJ, IRCP, IRSA.
 - LEDE, LOMA, LONG.
 - MERA, METR, MIRG, MOLA, MOLI, MORI.
 - OEST.
 - PAMP, PATA, PATY, PGR, POLL.
 - RICH, RIGO, ROSE.
 - SAMI, SEMI, SUPV.
 - TECO2, TGLT, TGNO4, TGSU2, TRAN, TXAR.
 - VALO.
 - YPFD.

The price is obtained by the use of [yfinance](https://pypi.org/project/yfinance/) library.

### Disclaimer

StockMarketAr is a software developed with a educational purpose. It wasn't designed to support real financial desicion making. So it shouldn't be used this way.

Official stock markets are the main source about stock prices.

In Argentina, the enforcement authority in stock markets is the [National Value Comission](https://www.cnv.gov.ar/sitioweb/). You can check its site in order to get more information.