import sys
from PyQt5.QtWidgets import *


# initialize the number of items
global num_of_item
num_of_item=0

def create_btn_item(name,btn_id):
    bt_name = name + str(btn_id)
    bt = QPushButton(bt_name)
    return bt

def add_btn_item():
    global boxlay      # global layout --> to be definded only onec in the main 
    global num_of_item # global counter for the items
    
    num_of_item +=1
    tmp_btn=create_btn_item("bt",num_of_item)
    boxlay.addWidget(tmp_btn)
    


if __name__ == "__main__":
    global boxlay
    
    app = QApplication([])
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle("add item demo")
    boxlay=QHBoxLayout(w) 


    #add item button
    btn = QPushButton(w)
    btn.setText('add item')
    btn.move(10,10)
    btn.show()
    btn.clicked.connect(add_btn_item)

    w.show()
    app.exec_()
    #sys.exit(app.exec_())
