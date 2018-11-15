# Reference: https://www.linuxvoice.com/build-a-web-browser-with-20-lines-of-python/

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QFileDialog, QDialog, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sys
import logging, logging.config

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

# logging.config.dictConfig({
#     'disable_existing_loggers': True
# })

class MainWindow(QDialog):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__()

        layout = QtWidgets.QVBoxLayout()

        self.pushButton = QtWidgets.QPushButton(self)
        self.lineEdit = QtWidgets.QLineEdit(self)
        # self.list = QtWidgets.QListWidget(self)
        self.tableView = QtWidgets.QTableView(self)
        # self.textBrowser = QtWidgets.QTextBrowser(self)
        # self.tableWidget = QTableWidget(self)
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tab1 = QWidget(self)
        self.tab2 = QWidget(self)
        self.tab1.setObjectName("viewRecord")
        self.tab2.setObjectName("editRecord")
        self.tabWidget.addTab(self.tab1,"")
        self.tabWidget.addTab(self.tab2,"")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1),"View Record")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2),"Edit Record")

        self.model = QStandardItemModel(self.tableView)

        self.pushButton.setText("Select File")

        layout.addWidget(self.lineEdit)
        layout.addWidget(self.pushButton)
        # layout.addWidget(self.list)
        layout.addWidget(self.tableView)
        # layout.addWidget(self.textBrowser)
        # layout.addWidget(self.tableWidget)
        layout.addWidget(self.tabWidget)

        self.setLayout(layout)

        self.setWindowTitle("PyBibClean")

        self.pushButton.clicked.connect(self.openFile)

        # self.tableView.edit

        # self.tableView.click

    def openFile(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', filter = '*.bib')
        logging.debug("File selected: {}".format(file_name[0]))
        self.lineEdit.setText(file_name[0])

        with open(file_name[0]) as bibtex_file:
            parser = bibtexparser.bparser.BibTexParser(common_strings=True)
        #    parser = BibTexParser()
        #    parser.customization = customizations
            parser.customization = homogenize_latex_encoding
            bib_database = bibtexparser.load(bibtex_file, parser=parser)

            self.numBibItems = len(bib_database.entries)

            logging.debug("File Opened: {}".format(bibtex_file))
            logging.debug("Found entries: {}".format(self.numBibItems))

            self.bibKeyList = sorted(self.extractKeys(bib_database))
            self.bibKeyIndices = {}
            i = 0
            for key in self.bibKeyList:
                self.bibKeyIndices[key] = i
                i = i+1

            logging.debug("Found bibliography keys: {}".format(self.bibKeyIndices))

            self.numBibKeys = len(self.bibKeyList)

            logging.debug("Number of bibliography keys: {}".format(self.numBibKeys))

            self.model.setRowCount(self.numBibItems)
            self.model.setColumnCount(self.numBibKeys)

            for key in self.bibKeyIndices.keys():
                self.model.setHorizontalHeaderItem(self.bibKeyIndices[key],QStandardItem(key))

            count = 0
            for entry in bib_database.entries:
                # self.list.addItem(entry['title'])
                # self.listView.addItem(QStandardItem(entry['title']))
                for key in self.bibKeyList:
                    if key in entry.keys():
                        print(count," ", self.bibKeyIndices[key], " ", entry[key])
                        item = QStandardItem(entry[key])
                        self.model.setItem(count,self.bibKeyIndices[key],item)
                    else:
                        item = QStandardItem("")
                        self.model.setItem(count,self.bibKeyIndices[key],item)
                count += 1

                # item = QStandardItem(entry['title'])
                # self.model.appendRow(item)

            self.tableView.setModel(self.model)
            self.tableView.show()

            # self.listView.setModel(self.model)
            # self.listView.show()

            # self.listView.addItems(bib_database.entries)
            # print(bib_database.entries)
            # self.textBrowser.setText(bib_database.entries)
            # self.listView.addI

    def extractKeys(self,bib_database):
        '''
        bib_database is a list of dictionaries, with each dictionary corresponding to a single
        bibtex entry
        '''
        keySet = ()
        for entry in bib_database.entries:
            tempSet = set(entry.keys())
            keySet = tempSet.union(keySet)
        logging.debug("Found bibtex keys: {}".format(keySet))
        return list(keySet)

    def addBibItem(model,entry):
        '''
        Adds a single row to the QStandardItemModel object, with values taken from entry[key], and key being elements of self.bibKeyList
        '''
        model.insertRow(0)
        for i in self.numBibKeys:
            self.mo


logging.debug(">>>App Execution Initiated")
app = QApplication(sys.argv)
view = MainWindow()
view.show()
# view.setUrl(QUrl("http://linuxvoice.com"))

app.exec_()
logging.debug(">>>App Execution Terminated")
