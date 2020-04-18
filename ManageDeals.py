from PyQt5 import Qt
import json

class Widget(Qt.QWidget):

    def __init__(self):
        super().__init__()
        layout = Qt.QVBoxLayout(self)
        iconCreate = Qt.QIcon("create.png")
        iconEdit = Qt.QIcon("edit.png")
        iconDelete = Qt.QIcon("delete.png")

        toolbutton = Qt.QPushButton("Создать ДАП")
        toolbutton.setFixedWidth(110)
        toolbutton.setFixedHeight(30)
        toolbutton.setIcon(iconCreate)
        layout.addWidget(toolbutton)

        with open('numbers.json', 'r', encoding='utf-8') as f:
            d = json.load(f)
        labels = [""] + [""] + [""] + ["№ дела об АП"] + ["КоАП РФ"] + ["юридическое лицо"] + ["юридический адрес"]

        w = Qt.QTableWidget(0, len(labels))
        w.setColumnHidden(7, True)
        w.setHorizontalHeaderLabels(labels)

        for i, (key, value) in enumerate(d.items()):
            rows = [""] + [""] + [""] + ["10418000-"+ key + "/2020"] + \
                   [d[key]["stkoap"] + " ч." + d[key]["chkoap"]] + [d[key]["company"]["ul"]] + \
                   [d[key]["company"]["address"]["naspunkt"] + ", " + d[key]["company"]["address"]["ulitsadom"]]
            w.insertRow(w.rowCount())

            for j, v in enumerate(rows):
                buttonCreate = Qt.QPushButton("Сформировать")
                w.setCellWidget(j, 0, buttonCreate)
                buttonEdit = Qt.QPushButton()
                buttonEdit.setIcon(iconEdit)
                w.setCellWidget(j, 1, buttonEdit)
                buttonDelete = Qt.QPushButton()
                buttonDelete.setIcon(iconDelete)
                w.setCellWidget(j, 2, buttonDelete)
                it = Qt.QTableWidgetItem(v)
                w.setItem(i, j, it)
                w.resizeColumnsToContents()
        w.resize(1000, 500)
        w.show()

        layout.addWidget(w)

if __name__ == '__main__':
    app = Qt.QApplication([])
    workWin = Widget()
    workWin.show()
    workWin.resize(850, 500)
    app.exec()