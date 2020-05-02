import json

from PyQt5 import Qt
from PyQt5.QtGui import QPalette, QColor

from CreateDocs import runCreateDocs
from ResourcesProvider import ResourcesProvider
from SaveDeal import save_deal


def run_manage_deals(resourcesProvider: ResourcesProvider, chosenEmployeeOar: str):
    class ManageDealsWidget(Qt.QWidget):

        def __init__(self):
            super().__init__()

            def create_button_callback():
                save_deal(resourcesProvider)
                update_table_content()

            def edit_button_callback(deal_number, deal_json):
                save_deal(resourcesProvider, deal_number, deal_json)
                update_table_content()

            # def delete_button_callback()

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
            createCaseButton.clicked.connect(create_button_callback)
            modeButton = Qt.QPushButton()
            modeButton.setFixedHeight(30)
            modeButton.setFixedWidth(30)
            modeButton.setIcon(iconMode)
            # modeButton.pressed.connect(self.poverhMode)
            layoutVertical.addWidget(createCaseButton)

            labels = [""] + [""] + [""] + ["№ дела об АП"] + ["КоАП РФ"] + ["юридическое лицо"] + ["ИНН"] + [
                "юридический адрес"]

            table = Qt.QTableWidget(0, len(labels))
            table.setColumnHidden(10, False)
            table.setHorizontalHeaderLabels(labels)

            def update_table_content():
                table.setRowCount(0)

                with open(resourcesProvider.get_deals_path(), 'r', encoding='utf-8') as f:
                    d = json.load(f)
                allItems = d.items()
                allItemsReversed = sorted(allItems, reverse=True)

                for i, (key, value) in enumerate(allItemsReversed):
                    rows = [""] + [""] + [""] + ["10418000-" + key + "/2020"] + \
                           [d[key]["articleCode"]] + [d[key]["company"]["name"]] + [d[key]["company"]["inn"]] + \
                           [d[key]["company"]["address"]["index"] + ", " + d[key]["company"]["address"]["city"] + ", " + \
                            d[key]["company"]["address"]["street"]]
                    table.insertRow(table.rowCount())
                    buttonCreate = Qt.QPushButton()
                    buttonCreate.setIcon(iconForm)
                    buttonCreate.pressed.connect(
                        lambda chosen_deal=key:
                        runCreateDocs(resourcesProvider, chosen_deal, chosenEmployeeOar)
                    )
                    table.setCellWidget(i, 0, buttonCreate)
                    buttonEdit = Qt.QPushButton()
                    buttonEdit.setIcon(iconEdit)
                    buttonEdit.pressed.connect(
                        lambda chosen_deal_number=key, chosen_deal_json=value:
                        edit_button_callback(chosen_deal_number, chosen_deal_json)
                    )
                    table.setCellWidget(i, 1, buttonEdit)
                    buttonDelete = Qt.QPushButton()
                    # buttonDelete.pressed.connect(lambda chosenDeal=key: self.goToDeleteDeal(chosenDeal))
                    buttonDelete.setIcon(iconDelete)
                    table.setCellWidget(i, 2, buttonDelete)

                    for j, val in enumerate(rows):
                        it = Qt.QTableWidgetItem(val)
                        table.setItem(i, j, it)
                        table.resizeColumnsToContents()

            update_table_content()
            table.show()

            layoutVertical.addWidget(table)
            layoutVertical.addWidget(modeButton)

        # def poverhMode(app):
        #   workWin.wm_attributes('-topmost',1)
        # def goToDeleteDeal(self, chosenDeal):

        # runDeleteDeal(resourcesProvider, chosen Deal)

    # if __name__ == '__main__':
    app = Qt.QApplication([])
    manage_deals_widget = ManageDealsWidget()
    manage_deals_widget.setWindowTitle("МастерДАП / Приволжская электронная таможня - ОАР - " + chosenEmployeeOar)

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor('#bdf0d4'))
    manage_deals_widget.setPalette(palette)
    manage_deals_widget.resize(800, 600)
    manage_deals_widget.show()

    app.exec()
