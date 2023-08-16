from Frota import Frota
from Moto import Moto
from Carro import Carro
from Bicicleta import Bicicleta



frota = Frota()
moto = Moto("abc123", "Honda", 2, "", 150)
carro = Carro("def456", "toyota", 4, "", 2)
bike = Bicicleta("ghi789", "bike", 2, "", 6)
moto2 = Moto("jkl101", "Suzuki", 2, "", 400)

frota.inserirVeiculo(moto)
frota.inserirVeiculo(carro)
frota.inserirVeiculo(bike)
frota.inserirVeiculo(moto2)

frota.removerVeiculo(bike)
frota.localizarVeiculo("jkl101")