from PyQt5 import Qt
from PyQt5.QtGui import QPalette, QColor

from CreateDocs import create_docs
from SaveDeal import save_deal
from utils.qt.ButtonUtils import create_qt_button
from utils.storage.Icons import *
from utils.storage.ResourcesManager import ResourcesProvider
from utils.tkinter.DialogUtils import create_withdraw_dialog, destroy_dialog
from utils.tkinter.MessageBoxUtils import show_confirm, show_info


def run_manage_deals(resources_provider: ResourcesProvider, chosen_employee: str):
    class ManageDealsWidget(Qt.QWidget):

        def __init__(self):
            super().__init__()

            def create_button_callback():
                save_deal(resources_provider)
                update_table_content()

            def edit_button_callback(deal_number, deal_json):
                save_deal(resources_provider, deal_number, deal_json)
                update_table_content()

            def delete_button_callback(chosen_deal_number):
                wdd = create_withdraw_dialog()
                answer = show_confirm(message="Удалить дело об АП\n\n10418000-" + chosen_deal_number + "/2020?")
                if answer:
                    resources_provider.remove_deal(chosen_deal_number)
                    update_table_content()
                    show_info("Удалено", "Удалено дело об АП\n\n10418000-" + chosen_deal_number + "/2020")
                destroy_dialog(wdd)


            layout = Qt.QVBoxLayout(self)
            icon_create = Qt.QIcon(CREATE)
            icon_form = Qt.QIcon(FORM)
            icon_edit = Qt.QIcon(EDIT)
            icon_delete = Qt.QIcon(DELETE)

            create_case_button = create_qt_button(
                icon_create,
                create_button_callback,
                "Создать ДАП"
            )
            create_case_button.setFixedWidth(110)
            create_case_button.setFixedHeight(30)
            layout.addWidget(create_case_button)

            labels = [""] + [""] + [""] + ["№ дела об АП"] + ["КоАП РФ"] + ["дата возбуждения"] + ["юридическое лицо"] + \
                     ["юридический адрес"] + ["ИНН"] + ["КПП"] + ["ОГРН"] + ["законный представитель"] + ["эл.почта"] + ["№ ДТ"]

            table = Qt.QTableWidget(0, len(labels))
            table.setColumnHidden(16, False)
            table.setHorizontalHeaderLabels(labels)

            def update_table_content():
                table.setRowCount(0)

                deals = resources_provider.load_deals()
                all_items = sorted(deals.items(), reverse=True)

                for row_number, (key, value) in enumerate(all_items):
                    if deals[key]["code_part"] == '-':
                        code_full_sh = deals[key]["code_art"]
                    else:
                        code_full_sh = deals[key]["code_art"] + " ч." + deals[key]["code_part"]
                    rows = [""] + [""] + [""] + ["10418000-" + key + "/2020"] + [code_full_sh] + \
                           [deals[key]["day_init"] + " " + deals[key]["month_init"] + " 2020"] + [deals[key]["company"]["name"]] + \
                           [deals[key]["company"]["address"]["index"] + ", " + deals[key]["company"]["address"]["city"] + ", " + \
                            deals[key]["company"]["address"]["street"]] + \
                           [deals[key]["company"]["inn"]] + [deals[key]["company"]["kpp"]] + [deals[key]["company"]["ogrn"]] + \
                           [deals[key]["company"]["representative"]["position"] + ", " + deals[key]["company"]["representative"]["name"]] + \
                           [deals[key]["company"]["email"]] + [deals[key]["number_dt"]]
                    table.insertRow(table.rowCount())

                    create_deal_button = create_qt_button(
                        icon_form,
                        lambda chosen_deal=key:
                        create_docs(resources_provider, chosen_deal, chosen_employee)
                    )
                    table.setCellWidget(row_number, 0, create_deal_button)

                    edit_deal_button = create_qt_button(
                        icon_edit,
                        lambda chosen_deal_number=key, chosen_deal_json=value:
                        edit_button_callback(chosen_deal_number, chosen_deal_json)
                    )
                    table.setCellWidget(row_number, 1, edit_deal_button)

                    delete_deal_button = create_qt_button(
                        icon_delete,
                        lambda chosen_deal_number = key:
                        delete_button_callback(chosen_deal_number)
                    )
                    table.setCellWidget(row_number, 2, delete_deal_button)

                    for j, val in enumerate(rows):
                        it = Qt.QTableWidgetItem(val)
                        table.setItem(row_number, j, it)
                        table.resizeColumnsToContents()

            update_table_content()
            table.show()

            layout.addWidget(table)

    app = Qt.QApplication([])
    manage_deals_widget = ManageDealsWidget()
    config = resources_provider.load_config()
    duty = config['employeesOar'][chosen_employee]['doloar_ip_sh']
    manage_deals_widget.setWindowTitle(
        "МастерДАП / Приволжская электронная таможня - ОАР - " + chosen_employee + " (" + duty + ")"
    )

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor('#bdf0d4'))
    manage_deals_widget.setPalette(palette)
    manage_deals_widget.resize(800, 600)
    manage_deals_widget.show()

    app.exec()