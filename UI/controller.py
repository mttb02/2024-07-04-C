import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_graph(self, e):
        self._view.txt_result1.controls.clear()
        self._model.crea_graph(self._anno_selected, self._shape_selected)
        print(self._anno_selected, self._shape_selected)
        self._view.txt_result1.controls.append(ft.Text(f"Numero di vertici: {self._model.get_num_of_nodes()}"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero di archi: {self._model.get_num_of_edges()}"))

        temp_edges = self._model.get_cinque_preso_maggiore()
        for i in range(0, 5):
            e = temp_edges[i]
            self._view.txt_result1.controls.append(ft.Text(f"Numero di vertici: {e[0].id} -> {e[1].id} | weight = {e[2]["weight"]}"))

        self._view.update_page()

    def load_dd(self):
        self._listYear = self._model.get_years()
        for a in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(key=a, text=a, on_click=self.read_anno))
        self._view.update_page()

    def read_anno(self, e):
        self._anno_selected = e.control.key
        self.load_dd_shape()

    def load_dd_shape(self):
        self._list_shapes = self._model.get_shapes(self._anno_selected)
        for s in self._list_shapes:
            self._view.ddshape.options.append(ft.dropdown.Option(key=s, text=s, on_click=self.read_shape))
        self._view.update_page()

    def read_shape(self, e):
        self._shape_selected = e.control.key



    def handle_path(self, e):
        pass


