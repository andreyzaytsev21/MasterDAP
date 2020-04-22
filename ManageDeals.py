from PyQt5 import Qt
import json
from files.SaveDeal import runSaveDeal


def runManageDeals():
    class Widget(Qt.QWidget):

        def __init__(self):
            super().__init__()
            layout = Qt.QVBoxLayout(self)
            iconCreate = Qt.QIcon("icons/create.png")
            iconEdit = Qt.QIcon("icons/edit.png")
            iconDelete = Qt.QIcon("icons/delete.png")

            toolbutton = Qt.QPushButton("Создать ДАП")
            toolbutton.setFixedWidth(110)
            toolbutton.setFixedHeight(30)
            toolbutton.setIcon(iconCreate)
            toolbutton.clicked.connect(self.goToRunSaveDeal)
            layout.addWidget(toolbutton)

            with open('numbers.json', 'r', encoding='utf-8') as f:
                d = json.load(f)
            labels = [""] + [""] + [""] + ["№ дела об АП"] + ["КоАП РФ"] + ["юридическое лицо"] + ["юридический адрес"]

            win = Qt.QTableWidget(0, len(labels))
            win.setColumnHidden(7, True)
            win.setHorizontalHeaderLabels(labels)

            allItems = d.items()
            allItemsReversed = sorted(allItems, reverse=True)

            for i, (key, value) in enumerate(allItemsReversed):
                rows = [""] + [""] + [""] + ["10418000-"+ key + "/2020"] + \
                       [d[key]["stkoap"] + " ч." + d[key]["chkoap"]] + [d[key]["company"]["ul"]] + \
                       [d[key]["company"]["address"]["naspunkt"] + ", " + d[key]["company"]["address"]["ulitsadom"]]
                win.insertRow(win.rowCount())
                for j, val in enumerate(rows):
                    #buttonCreate = Qt.QPushButton("Сформировать")
                    #buttonCreate.clicked.connect(self.goToFormDocs)
                    #win.setCellWidget(j, 0, buttonCreate)
                    #buttonEdit = Qt.QPushButton()
                    #buttonEdit.setIcon(iconEdit)
                    #win.setCellWidget(j, 1, buttonEdit)
                    #buttonDelete = Qt.QPushButton()
                    #buttonDelete.setIcon(iconDelete)
                    #win.setCellWidget(j, 2, buttonDelete)

                    it = Qt.QTableWidgetItem(val)
                    win.setItem(i, j, it)
                    win.resizeColumnsToContents()

            win.resize(1000, 500)
            win.show()


            layout.addWidget(win)
        def goToRunSaveDeal(self):
            runSaveDeal()
        def goToFormDocs(self):
            print(key[j])

    #if __name__ == '__main__':
    app = Qt.QApplication([])
    workWin = Widget()
    workWin.show()
    workWin.resize(850, 500)
    app.exec()