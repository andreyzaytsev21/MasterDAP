from PyQt5 import Qt
from PyQt5.QtGui import QPalette, QColor
import json
from SaveDeal import runSaveDeal
from ResourcesProvider import ResourcesProvider
from CreateDocs import runCreateDocs

def runManageDeals(resourcesProvider: ResourcesProvider, chosenEmployeeOar: str):
    class Widget(Qt.QWidget):


        def __init__(self):
            super().__init__()
            layoutVertical = Qt.QVBoxLayout(self)
            iconCreate = Qt.QIcon("../icons/create.png")
            iconForm = Qt.QIcon("../icons/form.png")
            iconEdit = Qt.QIcon("../icons/edit.png")
            iconDelete = Qt.QIcon("../icons/delete.png")
            iconMode = Qt.QIcon("../icons/mode.png")

            createCaseButton = Qt.QPushButton("Создать ДАП")
            createCaseButton.setFixedWidth(110)
            createCaseButton.setFixedHeight(30)
            createCaseButton.setIcon(iconCreate)
            createCaseButton.clicked.connect(self.goToRunSaveDeal)
            modeButton = Qt.QPushButton()
            modeButton.setFixedHeight(30)
            modeButton.setFixedWidth(30)
            modeButton.setIcon(iconMode)
            #modeButton.pressed.connect(self.poverhMode)
            layoutVertical.addWidget(createCaseButton)


            with open(resourcesProvider.getDealsPath(), 'r', encoding='utf-8') as f:
                d = json.load(f)
            labels = [""] + [""] + [""] + ["№ дела об АП"] + ["КоАП РФ"] + ["юридическое лицо"] + ["ИНН"] + ["юридический адрес"]

            win = Qt.QTableWidget(0, len(labels))
            win.setColumnHidden(10, False)
            win.setHorizontalHeaderLabels(labels)

            allItems = d.items()
            allItemsReversed = sorted(allItems, reverse=True)

            for i, (key, value) in enumerate(allItemsReversed):
                rows = [""] + [""] + [""] + ["10418000-"+ key + "/2020"] + \
                       [d[key]["artCode"] + " ч." + d[key]["partCode"]] + [d[key]["company"]["ul"]] + [d[key]["company"]["inn"]] +\
                       [d[key]["company"]["address"]["ulIndex"] + ", " + d[key]["company"]["address"]["ulCity"] + ", " + d[key]["company"]["address"]["ulStreetOffice"]]
                win.insertRow(win.rowCount())
                buttonCreate = Qt.QPushButton()
                buttonCreate.setIcon(iconForm)
                buttonCreate.pressed.connect(lambda chosenDeal=key: self.goToFormDocs(chosenDeal, chosenEmployeeOar))
                win.setCellWidget(i, 0, buttonCreate)
                buttonEdit = Qt.QPushButton()
                buttonEdit.setIcon(iconEdit)
                win.setCellWidget(i, 1, buttonEdit)
                buttonDelete = Qt.QPushButton()
                #buttonDelete.pressed.connect(lambda chosenDeal=key: self.goToDeleteDeal(chosenDeal))
                buttonDelete.setIcon(iconDelete)
                win.setCellWidget(i, 2, buttonDelete)

                for j, val in enumerate(rows):
                    it = Qt.QTableWidgetItem(val)
                    win.setItem(i, j, it)
                    win.resizeColumnsToContents()
            win.show()

            layoutVertical.addWidget(win)
            layoutVertical.addWidget(modeButton)

        #def poverhMode(app):
         #   workWin.wm_attributes('-topmost',1)

        def goToRunSaveDeal(self):
            runSaveDeal(resourcesProvider)

        def goToFormDocs(self, chosenDeal, chosenEmployeeOar):
            runCreateDocs(resourcesProvider, chosenDeal, chosenEmployeeOar)


        #def goToEditDeal(self):
            #runEditDeal(resourcesProvider, chosenDeal)

        #def goToDeleteDeal(self, chosenDeal):

            #runDeleteDeal(resourcesProvider, chosen Deal)


    #if __name__ == '__main__':
    app = Qt.QApplication([])
    workWin = Widget()
    workWin.setWindowTitle("МастерДАП / Приволжская электронная таможня - ОАР - " + chosenEmployeeOar)

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor('#bdf0d4'))
    workWin.setPalette(palette)
    workWin.resize(800, 950)
    workWin.show()

    app.exec()