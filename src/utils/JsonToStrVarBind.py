from tkinter import StringVar


# json_object - это json с возможными данными
# dict_path - путь до значения
# Например:
# json_obj =
# {
#   "company": {
#       "name" : "Фёдор"
#   }
# }
# dict_path = company.name
# Ожидаемый результат:
# Фёдор
def _get_value(json_obj, dict_path: str):
    res = json_obj
    for it in dict_path.split("."):
        if it not in res:
            return ""
        res = res[it]
    return res


# json_object - это json
# dict_path - путь до значения
# value - новое значение
# Например:
# json_obj =
# {
#   "company": {
#       "name" : "Фёдор"
#   }
# }
# dict_path = company.name
# value = "Новое что-то"
# Ожидаемый результат:
# json_obj =
# {
#   "company": {
#       "name" : "Новое что-то"
#   }
# }
def _update_json(json_obj, dict_path: str, value: str):
    obj_it = json_obj
    dict_paths = dict_path.split(".")
    for it in dict_paths[:-1]:
        if it in obj_it:
            obj_it = obj_it[it]
        else:
            new_dict = {}
            obj_it[it] = new_dict
            obj_it = new_dict
    obj_it[dict_paths[-1]] = value


class JsonToStrVarBind:
    def __init__(self, json_obj, dict_path):
        self._json_obj = json_obj
        self._dict_path = dict_path
        self._str_var = StringVar(
            master=None,
            value=_get_value(json_obj, dict_path),
            name=dict_path
        )

    def get_str_var(self):
        return self._str_var

    def update_json(self):
        _update_json(self._json_obj, self._dict_path, self._str_var.get())
