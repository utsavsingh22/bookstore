import sys

from PyQt5.QtWidgets import QDialog, QApplication

from book import *



class MyForm(QDialog):
      def __init__(self):

            super().__init__()

            self.ui = Ui_Dialog()

            self.ui.setupUi(self)

            self.ui.button1.clicked.connect(self.price)
            self.ui.button2.clicked.connect(self.total)

            sel.show()
            



      def price(self):
        import sqlite3

        db=sqlite3.connect("m5assignment.db")
        cur=db.cursor()
        ttl=self.lineedit1.text()

        sql="SELECT * FROM books WHERE title='"+ttl+"'"
        cur=db.cursor()
        cur.execute(sql)
        rec=cur.fetchone()
        if rec!=None:
            print (rec)
            self.pr=rec[3]
            self.lineedit2.setText(str(self.pr))
        else:
            print ("Title Not Found")
      def total(self):
        self.qty=float(self.lineedit3.text())
        ttl=self.pr*self.qty
        self.lineedit4.setText(str(ttl))

 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

