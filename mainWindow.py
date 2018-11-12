# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\adi\PycharmProjects\scraping\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
import re
import logging
import constants as c
from datetime import datetime, timedelta

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        baseFont = c.baseFont

        fontBigger = QtGui.QFont(baseFont)
        fontBigger.setPointSize(c.BASE_FONT_SIZE + 2)

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(301, 363)
        MainWindow.setMinimumSize(QtCore.QSize(301, 363))
        MainWindow.setMaximumSize(QtCore.QSize(301, 363))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(170, 50, 121, 31))
        self.searchButton.setFont(fontBigger)
        self.searchButton.setObjectName("button")

        self.stockName = QtWidgets.QLineEdit(self.centralwidget)
        self.stockName.setGeometry(QtCore.QRect(10, 50, 151, 31))
        self.stockName.setFont(fontBigger)
        self.stockName.setObjectName("stockName")

        self.buttonPlus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPlus.setGeometry(QtCore.QRect(260, 10, 31, 31))
        self.buttonPlus.setFont(baseFont)
        self.buttonPlus.setObjectName("buttonPlus")

        self.buttonMinus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMinus.setGeometry(QtCore.QRect(230, 10, 31, 31))
        self.buttonMinus.setFont(baseFont)
        self.buttonMinus.setObjectName("buttonMinus")

        self.buttonBold = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBold.setGeometry(QtCore.QRect(200, 10, 31, 31))
        self.buttonBold.setFont(baseFont)
        self.buttonBold.setObjectName("buttonBold")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 19, 90, 21))
        self.label.setFont(fontBigger)
        self.label.setObjectName("label")

        self.buttonReset = QtWidgets.QPushButton(self.centralwidget)
        self.buttonReset.setGeometry(QtCore.QRect(170, 10, 31, 31))
        self.buttonReset.setFont(baseFont)
        self.buttonReset.setObjectName("buttonReset")

        self.infoBox = QtWidgets.QListWidget(self.centralwidget)
        self.infoBox.setGeometry(QtCore.QRect(10, 90, 281, 221))
        self.infoBox.setObjectName("infoBox")
        self.infoBox.setFont(baseFont)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 301, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Define buttons functions
        self.searchButton.clicked.connect(self.yahooInfo)
        self.buttonPlus.clicked.connect(self.fontXL)
        self.buttonMinus.clicked.connect(self.fontBig)
        self.buttonBold.clicked.connect(self.fontMedium)
        self.buttonReset.clicked.connect(self.fontSmall)


        self.stockName.returnPressed.connect(self.yahooInfo)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #sets default size
        self.fontMedium()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock Info"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.buttonPlus.setText(_translate("MainWindow", "XL"))
        self.buttonMinus.setText(_translate("MainWindow", "L"))
        self.buttonBold.setText(_translate("MainWindow", "M"))
        self.label.setText(_translate("MainWindow", "Symbol"))
        self.buttonReset.setText(_translate("MainWindow", "S"))

    def getStockInfo(self, url, stock, urlEnd):
        try:
            req = requests.get(url + stock + urlEnd, timeout=5)
            if req.status_code != 200:
                req = 0
        except:
            req = 1
        return req

    def fontSmall(self):
        self.fontResize(0)

    def fontMedium(self):
        self.fontResize(1)

    def fontBig(self):
        self.fontResize(2)

    def fontXL(self):
        self.fontResize(3)

    def fontResize(self, font_size):
        c.sizeFlag = font_size
        width = c.BASE_WIDTH + 60 * font_size
        height = c.BASE_HEIGHT + 20 * font_size
        font_size = c.BASE_FONT_SIZE + font_size * 2
        MainWindow.setMinimumSize(width, height)
        MainWindow.setMaximumSize(width, height)
        self.infoBox.setMinimumSize(width - 20, height - 120)
        self.infoBox.setMaximumSize(width - 20, height - 120)
        font = c.baseFont
        font.setPointSize(font_size)
        self.infoBox.setFont(font)

    def yahooInfo(self):
        baseUrl = 'https://finance.yahoo.com/quote/'
        stock = self.stockName.text()
        # get all yahoo data
        self.infoBox.clear()
        yahooMain = self.getStockInfo(baseUrl, stock, '')
        yahooStatistics = self.getStockInfo(baseUrl, stock, '/key-statistics')
        yahooProfile = self.getStockInfo(baseUrl, stock, '/profile')

        # Soup all yahoo data +
        # Get relevant data from souped objects +
        # Set the info in the listBox
        if yahooMain != 0 and yahooMain != 1:
            yahooSoupMain = BeautifulSoup(yahooMain.text, 'html.parser')
            if yahooSoupMain.find('span', string=re.compile("Symbols similar to")) and yahooSoupMain.find('tbody'):
                self.infoBox.clear()
                suggestionsTable = yahooSoupMain.find('tbody').findAll('tr')
                self.infoBox.addItem('Symbol is wrong, try one of the following:')
                for tr in suggestionsTable:
                    self.infoBox.addItem(tr.next_element.text + ' | ' + tr.next_element.next_sibling.text)
            elif yahooSoupMain.find('span', string=re.compile("Symbols similar to")) or yahooSoupMain.find('span', string=re.compile("Previous Close")).parent.next_sibling.text == 'N/A':
                self.infoBox.clear()
                self.infoBox.addItem('You entered an invalid')
                self.infoBox.addItem('symbol and there are')
                self.infoBox.addItem('no suggestions')
            else:
                widgetItem = QtWidgets.QListWidgetItem()
                self.fontResize(c.sizeFlag)
                widgetItem.setText('Information for symbol: ' + stock.upper())
                self.infoBox.addItem(widgetItem)

                widgetItem = QtWidgets.QListWidgetItem()
                yahooEarningDate = yahooSoupMain.find('td', {"data-test": "EARNINGS_DATE-value"}).text
                widgetItem.setText('Earnings: ' + yahooEarningDate)
                yahooEarningDateSplit = yahooEarningDate.split(' - ')
                yahooEarningDateFirst = yahooEarningDateSplit[0]
                today = datetime.now()
                if today + timedelta(days=21) >= datetime.strptime(yahooEarningDateFirst, '%b %d, %Y') > today:
                    if yahooEarningDateSplit.length() > 1 and datetime.strptime(yahooEarningDateSplit[1], '%b %d, %Y') > today:
                        widgetItem.setForeground(QtCore.Qt.red)
                self.infoBox.addItem(widgetItem)

                yahooPE = yahooSoupMain.find('td', {"data-test": "PE_RATIO-value"}).text
                self.infoBox.addItem('PE Ratio (TTM): ' + yahooPE)

                if yahooStatistics != 0:
                    yahooSoupStat = BeautifulSoup(yahooStatistics.text, 'html.parser')
                    yahooShortRatioDate = yahooSoupStat.find('span', string=re.compile("Short Ratio")).text
                    yahooShortRatio = yahooSoupStat.find('span', string=re.compile("Short Ratio")).parent.next_sibling.text
                    widgetItem = QtWidgets.QListWidgetItem()
                    widgetItem.setText(yahooShortRatioDate + ': ' + yahooShortRatio)
                    if yahooShortRatio != 'N/A' and float(yahooShortRatio) > 5.0:
                        widgetItem.setForeground(QtCore.Qt.red)
                    self.infoBox.addItem(widgetItem)

                if yahooProfile != 0:
                    yahooSoupProfile = BeautifulSoup(yahooProfile.text, 'html.parser')
                    yahooSector = yahooSoupProfile.find('span', string='Sector').find_next_sibling('strong').text
                    yahooIndustry = yahooSoupProfile.find('span', string='Industry').find_next_sibling('strong').text
                    self.infoBox.addItem('Sector: ' + yahooSector)
                    self.infoBox.addItem('Industry: ' + yahooIndustry)
        elif yahooMain != 0:
            self.infoBox.clear()
            self.infoBox.addItem('Error Occured')
        else:
            self.infoBox.clear()
            self.infoBox.addItem('Timed out, Try again')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

