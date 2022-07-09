# Main Window
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

# Search engine change here:
url_home = 'google' # You can use your fav search engine my is google.

# Main Class For GUI Application


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()

        self.browser.setUrl(QUrl(f"http://%s.com" % url_home))
        self.setCentralWidget(self.browser)
        self.setWindowTitle("My Browser")
        self.setWindowIcon(QIcon(os.path.join('icons', 'browser.png')))
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # navbar widgets
        back_btn = QAction(
            QIcon(os.path.join('icons', 'back.png')), "Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction(
            QIcon(os.path.join('icons', 'forward.png')), 'Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(
            QIcon(os.path.join('icons', 'reload.png')), 'Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction(
            QIcon(os.path.join('icons', 'home.png')), 'Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Adding Separtor between navbar push button and LineEdit
        navbar.addSeparator()

        # Adding URL Box
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

        # Functions

    def navigate_home(self):
        self.browser.setUrl(QUrl(f"http://%s.com" % url_home))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName('My Browser')
    window = MainWindow()
    app.exec_()
