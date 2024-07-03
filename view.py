import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._txtInNumC = None
        self._btnAnalizza = None
        self._btnConnessi = None
        self._ddAeroportoP = None
        self._ddAeroportoA = None
        self._txtInNumTratte = None
        self._btnItinerario = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("TdP Flights Manager 2024", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self._txtInNumC = ft.TextField(
            label="Num compagnie",
            width=250
        )

        # button for the "hello" reply
        self._btnAnalizza = ft.ElevatedButton(text="Analizza Aeroporti", on_click=self._controller.handleAnalizza)
        self._btnConnessi = ft.ElevatedButton(text="Aeroporti Connessi", on_click=self._controller.handleConnessi, disabled=True)
        row1 = ft.Row([self._txtInNumC, self._btnAnalizza, self._btnConnessi],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row1)

        self._ddAeroportoP = ft.Dropdown(label="Partenza", disabled=True)
        self._ddAeroportoA = ft.Dropdown(label="Arrivo", disabled=True)

        row2 = ft.Row([self._ddAeroportoP, self._ddAeroportoA],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row2)

        self._txtInNumTratte = ft.TextField(
            label="Num Tratte Max",
            width=250,
            disabled=True
        )

        self._btnItinerario = ft.ElevatedButton(text="Cerca Itinerario", on_click=self._controller.hanldeCercaItinerario, disabled=True)

        row3 = ft.Row([self._txtInNumTratte, self._btnItinerario],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
