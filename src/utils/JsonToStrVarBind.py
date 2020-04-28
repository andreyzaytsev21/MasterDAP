from tkinter import StringVar


def _get_name(fst_lvl_key, scd_lvl_key):
    return fst_lvl_key + ("." + scd_lvl_key or "")


def _get_value(json_obj, dict_path: str):
    res = json_obj
    for it in dict_path.split("."):
        if it not in res:
            return ""
        res = res[it]
    return res


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
