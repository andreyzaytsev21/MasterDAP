from PyQt5 import Qt
from PyQt5.QtGui import QPalette, QColor
import json
from SaveDeal import runSaveDeal
from ResourcesProvider import ResourcesProvider
from CreateDocs import runCreateDocs

def runManageDeals(resourcesProvider: ResourcesProvider, employee: str):
    class Widget(Qt.QWidget):

        def __init__(self):
            super().__init__()
            layout = Qt.QVBoxLayout(self)
            iconCreate = Qt.QIcon("../icons/create.png")
            iconEdit = Qt.QIcon("../icons/edit.png")
            iconDelete = Qt.QIcon("../icons/delete.png")

            toolbutton = Qt.QPushButton("Создать ДАП")
            toolbutton.setFixedWidth(110)
            toolbutton.setFixedHeight(30)
            toolbutton.setIcon(iconCreate)
            toolbutton.clicked.connect(self.goToRunSaveDeal)
            layout.addWidget(toolbutton)

            with open(resourcesProvider.getDealsPath(), 'r', encoding='utf-8') as f:
                d = json.load(f)
            labels = [""] + [""] + [""] + ["№ дела об АП"] + ["КоАП РФ"] + ["юридическое лицо"] + ["юридический адрес"]

            win = Qt.QTableWidget(0, len(labels))
            win.setColumnHidden(10, False)
            win.setHorizontalHeaderLabels(labels)

            allItems = d.items()
            allItemsReversed = sorted(allItems, reverse=True)

            for i, (key, value) in enumerate(allItemsReversed):
                rows = [""] + [""] + [""] + ["10418000-"+ key + "/2020"] + \
                       [d[key]["stkoap"] + " ч." + d[key]["chkoap"]] + [d[key]["company"]["ul"]] + \
                       [d[key]["company"]["address"]["naspunkt"] + ", " + d[key]["company"]["address"]["ulitsadom"]]
                win.insertRow(win.rowCount())
                buttonCreate = Qt.QPushButton("Сформировать")
                buttonCreate.pressed.connect(lambda chosenDeal=key: self.goToFormDocs(chosenDeal))
                win.setCellWidget(i, 0, buttonCreate)
                buttonEdit = Qt.QPushButton()
                buttonEdit.setIcon(iconEdit)
                win.setCellWidget(i, 1, buttonEdit)
                buttonDelete = Qt.QPushButton()
                buttonDelete.setIcon(iconDelete)
                win.setCellWidget(i, 2, buttonDelete)

                for j, val in enumerate(rows):
                    it = Qt.QTableWidgetItem(val)
                    win.setItem(i, j, it)
                    win.resizeColumnsToContents()
            win.show()

            layout.addWidget(win)
        def goToRunSaveDeal(self):
            runSaveDeal(resourcesProvider)

        def goToFormDocs(self, chosenDeal):
            runCreateDocs(resourcesProvider, chosenDeal)

        def goToEditDeal(self):
            #runEditDeal(resourcesProvider, chosenDeal)

        def goToDeleteDeal(self):
            #runDeleteDeal(resourcesProvider, chosen Deal)

    #if __name__ == '__main__':
    app = Qt.QApplication([])
    workWin = Widget()
    workWin.setWindowTitle("МастерДАП / Приволжская электронная таможня - ОАР - " + employee)

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor('#bdf0d4'))
    workWin.setPalette(palette)
    workWin.resize(800, 400)
    workWin.show()

    app.exec()