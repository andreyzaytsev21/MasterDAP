import json

from PyQt5 import Qt
from PyQt5.QtGui import QPalette, QColor
from tkinter import messagebox
from tkinter import *
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

            def delete_button_callback(chosenDeal):
                delWin = Tk()
                delWin.withdraw()
                answer = messagebox.askyesno(message="Удалить дело об АП\n\n10418000-" + chosenDeal + "/2020?")
                delWin.destroy()
                if answer == True:
                    fileToDel = open(resourcesProvider.get_deals_path(), 'r', encoding='utf-8')
                    fileChosenToDel = json.load(fileToDel)
                    fileToDel.close()
                    del fileChosenToDel[chosenDeal]
                    fileToDel1 = open(resourcesProvider.get_deals_path(), 'w', encoding='utf-8')
                    fileToDel1.write(str(json.dumps(fileChosenToDel, ensure_ascii=False, sort_keys=True, indent=4)))
                    fileToDel1.close()
                    update_table_content()
                    delWin1 = Tk()
                    delWin1.withdraw()
                    messagebox.showinfo("Удалено", "Удалено дело об АП\n\n10418000-" + chosenDeal + "/2020")
                    delWin1.destroy()


            layoutVertical = Qt.QVBoxLayout(self)
            iconCreate = Qt.QIcon("../icons/create.png")
            iconForm = Qt.QIcon("../icons/form.png")
            iconEdit = Qt.QIcon("../icons/edit.png")
            iconDelete = Qt.QIcon("../icons/delete.png")

            createCaseButton = Qt.QPushButton("Создать ДАП")
            createCaseButton.setFixedWidth(110)
            createCaseButton.setFixedHeight(30)
            createCaseButton.setIcon(iconCreate)
            createCaseButton.clicked.connect(create_button_callback)
            layoutVertical.addWidget(createCaseButton)

            labels = [""] + [""] + [""] + ["№ дела об АП"] + ["КоАП РФ"] + ["дата возбуждения"] + ["юридическое лицо"] + \
                     ["юридический адрес"] + ["ИНН"] + ["КПП"] + ["ОГРН"] + ["законный представитель"] + ["эл.почта"] + ["№ ДТ"]

            table = Qt.QTableWidget(0, len(labels))
            table.setColumnHidden(16, False)
            table.setHorizontalHeaderLabels(labels)

            def update_table_content():
                table.setRowCount(0)

                with open(resourcesProvider.get_deals_path(), 'r', encoding='utf-8') as f:
                    d = json.load(f)
                allItems = d.items()
                allItemsReversed = sorted(allItems, reverse=True)

                for i, (key, value) in enumerate(allItemsReversed):
                    if d[key]["code_part"] == '-':
                        code_full_sh = d[key]["code_art"]
                    else:
                        code_full_sh = d[key]["code_art"] + " ч." + d[key]["code_part"]
                    rows = [""] + [""] + [""] + ["10418000-" + key + "/2020"] + [code_full_sh] + \
                           [d[key]["day_init"] + " " + d[key]["month_init"] + " 2020"] + [d[key]["company"]["name"]] + \
                           [d[key]["company"]["address"]["index"] + ", " + d[key]["company"]["address"]["city"] + ", " + \
                            d[key]["company"]["address"]["street"]] + \
                           [d[key]["company"]["inn"]] + [d[key]["company"]["kpp"]] + [d[key]["company"]["ogrn"]] + \
                           [d[key]["company"]["representative"]["position"] + ", " + d[key]["company"]["representative"]["name"]] + \
                           [d[key]["company"]["email"]] + [d[key]["number_dt"]]
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
                    buttonDelete.pressed.connect(lambda chosenDeal = key: delete_button_callback(chosenDeal))
                    buttonDelete.setIcon(iconDelete)
                    table.setCellWidget(i, 2, buttonDelete)

                    for j, val in enumerate(rows):
                        it = Qt.QTableWidgetItem(val)
                        table.setItem(i, j, it)
                        table.resizeColumnsToContents()

            update_table_content()
            table.show()

            layoutVertical.addWidget(table)

    app = Qt.QApplication([])
    manage_deals_widget = ManageDealsWidget()
    with open(resourcesProvider._get_config_path(), 'r', encoding='utf-8') as f:
        dapJson = json.load(f)
    dolzhnost = dapJson['employeesOar'][chosenEmployeeOar]['doloar_ip_sh']
    manage_deals_widget.setWindowTitle("МастерДАП / Приволжская электронная таможня - ОАР - " + chosenEmployeeOar + " (" + dolzhnost + ")")

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor('#bdf0d4'))
    manage_deals_widget.setPalette(palette)
    manage_deals_widget.resize(800, 600)
    manage_deals_widget.show()

    app.exec()