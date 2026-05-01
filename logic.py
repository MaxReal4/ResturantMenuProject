from PyQt6.QtWidgets import *


from menu import *
import csv

# DO I NEED DOCK STRINGS!@!!!
class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFixedSize(500, 425)




        self.SendButton.clicked.connect(lambda: self.submit())

    def submit(self):
        tablenumber = self.TableBox.text().strip()
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

        #I used AI here until csv file
        for catagory, items in whole_menu.items():
            for name, amount in items.items():
                value = amount.text().strip()

                if value.isdigit():
                    quantity = int(value)

                    rows.append([
                        f"Table {tablenumber}",
                        catagory,
                        name,
                        quantity

                    ])


        with open('ResturantTickets.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for row in rows:
                writer.writerow(row)

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




