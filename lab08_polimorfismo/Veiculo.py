class Veiculo:
	def __init__(self, placaVeiculo, fabricanteVeiculo, numeroRodas, tipoVeiculo):
		self._placaVeiculo = placaVeiculo
		self._fabricanteVeiculo = fabricanteVeiculo
		self._numeroRodas = numeroRodas
		self._tipoVeiculo = tipoVeiculo

	def imprime(self):
		return f"Placa do veiculo: {self._placaVeiculo}\nFabricante do veiculo: {self._fabricanteVeiculo}\nNumero de rodas: {str(self._numeroRodas)}\nTipo de veiculo: {self._tipoVeiculo}"
    
	def getFabricanteVeiculo(self):
		return self._fabricanteVeiculo

	def setFabricanteVeiculo(self, fabricanteVeiculo):
		if len(fabricanteVeiculo) == 0:
			print ("Fabricante de veiculo nao infomado")
		else:
			self._fabricanteVeiculo = fabricanteVeiculo

	def getPlacaVeiculo(self):
		return self._placaVeiculo

	def setPlacaVeiculo(self, placaVeiculo):
		if len(placaVeiculo) == 0:
			print ("Placa de veiculo nao infomado")
		else:
			self._placaVeiculo = placaVeiculo

	def getNumeroRodas(self):
		return self._numeroRodas

	def setNumeroRodas(self, numeroRodas):
		if numeroRodas > 0:
			self._numeroRodas = numeroRodas
		else:
			print ("Numero de rodas invalido")

	def getTipoVeiculo(self):
		return self._tipoVeiculo

	def setTipoVeiculo(self, tipoVeiculo):
		if len(tipoVeiculo) == 0:
			print ("Tipo de veiculo nao infomado")
		else:
			self._tipoVeiculo = tipoVeiculo
