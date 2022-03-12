import sys
from PyQt5.QtWidgets import *



class mygui():

    def __init__(self) :
        self.app = QApplication([])
        self.w = QWidget()
        self.w.resize(300,300)
        self.w.setWindowTitle("add item demo")
        self.boxlay=QHBoxLayout(self.w) 
        self.num_of_item=0
    
    def show_mygui(self):

        btn = QPushButton(self.w)
        btn.setText('add item')
        btn.move(10,10)
        btn.show()
        btn.clicked.connect(self.add_btn_item)

        self.w.show()
        self.app.exec_()

    def create_btn_item(self,name,btn_id):
        bt_name = name + str(btn_id)
        bt = QPushButton(bt_name)
        return bt

    def add_btn_item(self):

        self.num_of_item +=1
        tmp_btn=self.create_btn_item("bt",self.num_of_item)
        self.boxlay.addWidget(tmp_btn)
        


if __name__ == "__main__":
    testGUI=mygui()
    testGUI.show_mygui()
