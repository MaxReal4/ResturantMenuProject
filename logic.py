from PyQt6.QtWidgets import *


from menu import *
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #sets a fixed size of the menu
        self.setFixedSize(500, 425)




        self.SendButton.clicked.connect(lambda: self.submit())

    def submit(self):
        tablenumber: str = self.TableBox.text().strip()

        if tablenumber == '':
            self.ThanksLabel.setText('You need a table number!')
            return

        rows = []

        whole_menu = {
            "Raw": {
                "Tuna": self.TunaBox,
                "Mahi": self.MahiBox,
                "Salmon": self.SalmonBox
            },
            "Cooked": {
                "Steak": self.SteakBox,
                "Volcano": self.VolcanoBox,
                "Dragon": self.DragonBox
            },
            "Special": {
                "Cali": self.CaliBox,
                "TunaWrap": self.TunaWrapBox,
                "Rainbow": self.RainbowRollBox
            },
            "Drinks": {
                "Coke": self.CokeBox,
                "Sprite": self.SpriteBox,
                "MapleBoba": self.MapleBobaBox
            }
        }
        '''
        nested for loop taking each catagory raw,cooked... then taking the items in those
        catagorys like cali roll then grabing the amount listed in that dictionary. What it 
        then does is strip the value then sees if it is a digit because if not it wont print
        it and moves on. If it is a digit then it adds it into the list of rows in the order
        table number, catagory, name, quantity.
        '''
        #I used AI here until csv file writer
        for catagory, items in whole_menu.items():
            for name, amount in items.items():
                value = amount.text().strip()

                digits = ''.join(char for char in value if char.isdigit())

                if digits != '':
                    quantity = int(digits)

                    rows.append([
                        f"Table {tablenumber}",
                        catagory,
                        name,
                        quantity

                    ])

        """
        opening of the csv file and writes each row in the list rows which should be
        Table number, catagory/type of food, name of food/drink, quantity.
        """
        with open('ResturantTickets.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for row in rows:
                writer.writerow(row) #writes each row in the list rows


        '''
        clears all the boxes on the menu
        '''



        self.TunaBox.clear()
        self.MahiBox.clear()
        self.SalmonBox.clear()
        self.SpriteBox.clear()
        self.CokeBox.clear()
        self.MapleBobaBox.clear()
        self.TunaWrapBox.clear()
        self.CaliBox.clear()
        self.RainbowRollBox.clear()
        self.SteakBox.clear()
        self.VolcanoBox.clear()
        self.DragonBox.clear()
        self.TableBox.clear()




