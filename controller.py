from datetime import datetime

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choiceAeroportoP = None
        self._choiceAeroportoA = None

    def handleAnalizza(self, e):
        nMinStr = self._view._txtInNumC.value

        try:
            nMin = int(nMinStr)

        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Il valore inserito nel campo nMin non è un intero"))
            self._view.update_page()
            return

        self._model.buildGraph(nMin)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Num nodi: {self._model.getNumNodi()}"))
        self._view.txt_result.controls.append(ft.Text(f"Num archi: {self._model.getNumArchi()}"))

        self._view._ddAeroportoP.disabled = False
        self._view._ddAeroportoA.disabled = False
        self._view._btnItinerario.disabled = False
        self._view._btnConnessi.disabled = False
        self._view._txtInNumTratte.disabled = False

        self.fillDD()




        self._view.update_page()


    def handleConnessi(self, e):
        if self._choiceAeroportoP is None:
            self._view.txt_result.controls.append(ft.Text("Selezionare un aereoporto di partenza"))
            self._view.update_page()
            return

        v0 = self._choiceAeroportoP
        vicini = self._model.getSortedVicini(v0)

        self._view.txt_result.controls.append(ft.Text(f"Ecco i vicini di {v0}"))
        for v in vicini:
            self._view.txt_result.controls.append(ft.Text(f"{v[1]} - {v[0]}"))

        print("handleConnessi called")

        self._view.update_page()


    def hanldeCercaItinerario(self, e):
        v0 = self._choiceAeroportoP
        v1 = self._choiceAeroportoA
        t = self._view._txtInNumTratte.value

        try:
            tInt = int(t)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Il valore inserito non è un numero"))
            self._view.update_page()
            return


        tic = datetime.now()
        path, nTot = self._model.getCamminoOttimo(v0, v1, tInt)
        self._view.txt_result.controls.append(ft.Text(f"Il percorso ottimo fra {v0} e {v1} è:"))

        for p in path:
            self._view.txt_result.controls.append(ft.Text(p))

        self._view.txt_result.controls.append(ft.Text(f"Numero totale di voli: {nTot}"))
        self._view.txt_result.controls.append(ft.Text(f"Tempo impiegato per la ricerca: {datetime.now() - tic} secondi"))

        self._view.update_page()



    def fillDD(self):
        allNodes = self._model.getAllNodes()
        for n in allNodes:
            self._view._ddAeroportoP.options.append(ft.dropdown.Option(data=n, on_click=self.readDDAereoportoP, text=n.AIRPORT))
            self._view._ddAeroportoA.options.append(
                ft.dropdown.Option(data=n, on_click=self.readDDAereoportoA, text=n.AIRPORT))


    def readDDAereoportoP(self, e):

        if e.control.data is None:
            self._choiceAeroportoP = None
        else:
            self._choiceAeroportoP = e.control.data

        print(f"readDDAeroportoP called -- {self._choiceAeroportoP}")


    def readDDAereoportoA(self, e):

        if e.control.data is None:
            self._choiceAeroportoA = None
        else:
            self._choiceAeroportoA = e.control.data

        print(f"readDDAeroportoA called -- {self._choiceAeroportoA}")


    def handleTestConnessione(self, e):
        v0 = self._choiceAeroportoP
        v1 = self._choiceAeroportoA

        # verificare che ci sia un percorso
        if (not self._model.esistePercorso(v0, v1)):
            self._view.txt_result.controls.append(ft.Text(f"Non esiste un percorso tra {v0} e {v1}"))

        else:
            self._view.txt_result.controls.append(ft.Text(f"Percorso tra {v0} e {v1} trovato"))

        # trovare un possibile percorso

        path = self._model.trovaCamminoBFS(v0, v1)
        for p in path:
            self._view.txt_result.controls.append(ft.Text(f"{p}"))

        self._view._txtInNumTratte.disabled = False
        self._view._btnItinerario.disabled = False

        self._view.update_page()


