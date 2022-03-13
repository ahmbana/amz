from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
#############################################
## class to identfy an item ##
#############################################
class Item():
    ##item attributs
    def __init__(self,name,price,icon="./Icons/logo.jpg"):
        self.name=name
        self.price=price
        ##logo is a pic. of item// optional otherwise submits general logo
        ##related to icon path
        self.logo=icon 
        ##origenal item status is available("True")
        self.available="True"
        self.amount=0
    def add_amount(self,x):##add amount of items
        self.amount+=x 
#############################################
## class for all items in a shop ##
#############################################
class Shop():
    def __init__(self,name="My Shop"):
        self.name=name
        ##nu. of all items
        self.nu_items=0
        ## button(items) positions on grid(i,j) 
        self.pos_i=0 
        self.pos_j=0
        ##list to contain all availble items
        self.items_list=[]
        ##list of amount price for each item
        self.items_price=[]
        self.end_price=0
    def add_item(self,item:Item):##add item to item"s list
        (self.items_list).append(item)
        self.nu_items+=1
    def remov_item(self,item:Item):##remove item from shop
        (self.items_list).remove(item)
        self.nu_items-=1
    def item_buy(self,x,y):##calc. amount"s price of singel item
        ## x=item nu. in items_list[]
        ## y=amount desired to buy
        price=(self.items_list[x].price)*y
        (self.items_price).append(price)
        ## remove y from item"s ammount
        self.items_list[x].amount-=y ##????????????????????????????????????
    def final_sum(self):##calc. end price of all items
        ##add al nu. in list as final price
        i=sum(self.items_price)
        self.end_price+=i
    def discount(self,x):##calc. price discount if wanted
        ## x=discount amount in percentag(%)
        a=self.end_price*(x/100)
        self.end_price-=a
#######################################################################
############################# GUI #####################################
#######################################################################
MFont=QFont() ## set font  ##
MFont.setBold(True)
MFont.setPointSize(9)
MFont.setFamily("Optima")
#**********************************************************
class Shop_GUI(QMainWindow): ##main window
    def __init__(self):
        super().__init__()
        self.shop=Shop()
        ##window geometry,titel and logo
        self.setGeometry(180,80,1000,600)
        self.setMinimumSize(1000,600)
        self.setWindowTitle(self.shop.name)
        self.setWindowIcon(QIcon("./Icons/logo.png"))
        ##main window method
        self.mainwindow()
        self.show()
    def updat_added_item(self,flag):
        return 0
        ##*****************************************************
        ##BUTOONS ACTIONS ON CLICK
        ##*****************************************************
    def additem(self):##method of adding item BUTTON-1
        ##popup a child window
        self.dia_win=Add_Win(self.shop,self.gbox)##pass var.
        ##*****************************************************
    def removeit(self):
        ask,a=QInputDialog.getInt(self,"Remove Item","Please Enter Item's Number.",1,1,1000,1,Qt.CustomizeWindowHint)
    def deacit(self):
        ask1,a1=QInputDialog.getInt(self,"Item ON|OFF","Please Enter Item's Number.",1,1,1000,1,Qt.CustomizeWindowHint)
    def mainwindow(self):##main window method
        ##window grid
        self.layout=QGridLayout(self)
        ##add center self.widget to set grid##
        self.widget=QWidget(self)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        #**********************************
        ##logo pic. in a label TOP-RIGHT##
        logo=QLabel(self)
        pic=QPixmap("./Icons/logo.png")
        logo.setPixmap(pic)
        logo.setMaximumWidth(90) 
        logo.setMaximumHeight(90)
        logo.setScaledContents(True)
        self.layout.addWidget(logo,0,5,1,1)
        #**********************************
        ##despself.lay screen RIGHT-UNDER LOGO##
        self.desplay=QLabel(self)
        self.desplay.setStyleSheet("QLabel""{""border:2px solid black;""background:white;""}")
        self.layout.addWidget(self.desplay,2,4,2,2)
        #**********************************
        ##Tool Box as groupbox TOP-LEFT##
        tools=QGroupBox(self)
        tools.setStyleSheet("QGroupBox:title {"
                 "subcontrol-origin:margin;"   ##?????????????
                 "subcontrol-position:top center;"
                 "padding-left:5px;"
                 "padding-right:5px;""}")
        self.layout.addWidget(tools,0,0,1,3)
        ####set Tool Box buttons
        tb_layout=QHBoxLayout(self)# tool box self.layout
        tools.setLayout(tb_layout)
        add_item=QPushButton("  Add Item")## button 1
        add_item.setFont(MFont)
        add_item.setStyleSheet("QPushButton{background-color:lightgreen;" ##customize button
                            "padding:18px;"
                            "border-width:2px;"
                            "border-radius:15px;}"
                            "QPushButton::hover{background-color:lightblue;}"
                            "QPushButton::pressed{background-color:lightgreen;}")
        add_item.setIcon(QIcon("./Icons/logoadd.png"))##add logo to button
        add_item.clicked.connect(self.additem)
        tb_layout.addWidget(add_item)
        remove_item=QPushButton("  Remove Item",self)## button 2
        remove_item.setFont(MFont)
        remove_item.setStyleSheet("QPushButton{background-color:pink;" ##customize button
                            "padding:18px;"
                            "border-width:2px;"
                            "border-radius:15px;}"
                            "QPushButton::hover{background-color:lightblue;}"
                            "QPushButton::pressed{background-color:pink;}")
        remove_item.setIcon(QIcon("./Icons/logodel.png"))##add logo to button
        tb_layout.addWidget(remove_item)
        remove_item.clicked.connect(self.removeit)
        deactiv_activ=QPushButton("  Item ON|OFF")## button 3
        deactiv_activ.setFont(MFont)
        deactiv_activ.setStyleSheet("QPushButton{background-color:lightgray;" ##customize button
                            "padding:18px;"
                            "border-width:2px;"
                            "border-radius:15px;}"
                            "QPushButton::hover{background-color:lightblue;}"
                            "QPushButton::pressed{background-color:lightgray;}")
        deactiv_activ.setIcon(QIcon("./Icons/logodiac.png"))##add logo to button
        tb_layout.addWidget(deactiv_activ)
        deactiv_activ.clicked.connect(self.deacit)
        #***********************************
        ##items window as groub box LEFT-BOTTOM##
        self.gbox=QGroupBox(self)
        self.gbox.setUpdatesEnabled(True)
        # self.btlay=QGridLayout(self)
        # self.gbox.setLayout(self.btlay)
        scroll=QScrollArea(self)##adding scroll bar
        scroll.setWidget(self.gbox)
        scroll.setWidgetResizable(True)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)##vertical scroll bar on
        self.layout.addWidget(scroll,2,0,2,3)
    ##############################################  
    def closeEvent(self,event): ##close child window when manin is closed
        try:
            self.dia_win.close()
        except Exception as e:
            pass
        self.close()
    ##############################################
    #***************************************
class Add_Win(QMainWindow): ##child window of adding items
    def __init__(self,myshop,butbox:QGroupBox):
        super().__init__()
        self.butbox=butbox
        ##window geometry,titel and logo
        self.myshop=myshop
        self.setGeometry(330,150,0,0)
        self.setFixedSize(350,300)
        self.setWindowTitle("Add Item")
        self.setWindowIcon(QIcon("./Icons/logoadd.png"))
        ##first flag to remove max- and minimize window options
        ##secound flag to stay window on top
        self.setWindowFlags(Qt.WindowCloseButtonHint|Qt.WindowStaysOnTopHint|Qt.WindowTitleHint)
        ##child window main method
        self.dial_win()
        self.show()
        #**************************************
    def dial_win(self):
        ##window self.layout
        lay=QFormLayout(self)
        lay.setVerticalSpacing(15)
        ##add center self.widget to set self.layout##
        wid=QWidget(self)
        wid.setLayout(lay)
        self.setCentralWidget(wid)
        #***********************************
        ##text entry boxes  
        self.e1=QLineEdit(self) ##name entry
        self.e1.setPlaceholderText("Enter Name")
        self.e1.setValidator(QRegExpValidator()) ##set entry type
        self.e1.setMaxLength(30)
        self.e1.setFont(MFont)
        self.e1.setMinimumSize(250,25)
        lay.addRow("Item Name:",self.e1)
        self.e2=QLineEdit(self) ##price entry
        self.e2.setValidator(QDoubleValidator(0.99,99.99,2)) ##set entry type
        self.e2.setPlaceholderText("Enter Price ex. 999.99")
        self.e2.setFont(MFont)
        self.e2.setMinimumSize(250,25)
        lay.addRow("Item Price:",self.e2)
        self.e3=QLineEdit(self) ##amount entry
        self.e3.setValidator(QDoubleValidator(0.0,99.0,1)) ##set entry type
        self.e3.setPlaceholderText("Enter Amount")
        self.e3.setFont(MFont)
        self.e3.setMinimumSize(250,25)
        lay.addRow("Item Amount:",self.e3)
        #**************************************
        ##upload image and save buttons
        b1=QPushButton("  Upload Item Image") ##upload image
        b1.setStyleSheet("QPushButton{background-color:gray;" ##customize button
                           "padding:15px;"
                            "border-width:2px;"
                            "border-radius:15px;}"
                            "QPushButton::hover{background-color:lightblue;}"
                            "QPushButton::pressed{background-color:lightgray;}")
        b1.setIcon(QIcon("./Icons/logoup.png"))##add logo to button
        b1.setMaximumSize(250,50)
        b1.setFont(MFont)
        lay.addRow(b1)
        b2=QPushButton("  Save") ##save button
        b2.setFont(MFont)
        b2.setStyleSheet("QPushButton{background-color:lightgreen;" ##customize button
                            "padding:15px;"
                            "border-width:2px;"
                            "border-radius:15px;}"
                            "QPushButton::hover{background-color:lightblue;}"
                            "QPushButton::pressed{background-color:lightgreen;}")
        b2.setIcon(QIcon("./Icons/logosave.png"))##add logo to button
        b2.setMaximumSize(150,50)
        b2.clicked.connect(self.save_item)
        lay.addRow(b2)
        #************************************
    def create_but_item(self,item:Item):
        a=str(item.amount)
        print(a)
        ib=QPushButton(item.name +"\n" +item.price+"Euro\n" +a,self)
        #ib.setFont(MFont)
        ib.setStyleSheet("QPushButton{background-color:lightblue;" 
                           "padding:15px;"
                            "border-width:2px;"
                            "border-radius:15px;}"
                            "QPushButton::hover{background-color:gray;}"
                            "QPushButton::pressed{background-color:lightgray;}")
        return ib
             
    def save_item(self):

        temp_item=Item(self.e1.text(),self.e2.text())
        temp_item.amount=self.e3.text()
        ib=self.create_but_item(temp_item)
        #ib1=self.create_but_item(temp_item)

        self.myshop.add_item(temp_item)
        if self.myshop.pos_j<5:
            self.myshop.pos_j+=1
        if self.myshop.pos_j==5:
            self.myshop.pos_i+=1
            self.myshop.pos_j=0
        
        if self.myshop.pos_i==0 and self.myshop.pos_i==0:
            self.btlay=QGridLayout(self)
            self.butbox.setLayout(self.btlay)

        
        self.btlay.addWidget(ib,self.myshop.pos_i,self.myshop.pos_j)
        self.btlay.addWidget(ib,self.myshop.pos_i + 1,self.myshop.pos_j)
        #btlay.update()
        #self.butbox.update()
        
        self.close()

app=QApplication(sys.argv)
window=Shop_GUI()
sys.exit(app.exec_())