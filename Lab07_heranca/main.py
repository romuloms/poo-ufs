from catalogoHeranca import Catalogo
from cdHeranca import CD
from dvdHeranca import DVD


catalogo1 = Catalogo()
cd1 = CD("Ganso Rosa: GH", 90, "Ganso Rosa", 13, True, "Top")
dvd1 = DVD("Pulp fiction", 90, "Tarantino", True, "Top")

catalogo1.inserirItem(cd1)
catalogo1.inserirItem(dvd1)
catalogo1.listarItens()

