import socketio
import eel

import settings

class SocketManager:
	def __init__(self):
		self.url = self.makeURL()
		self.namespace = settings.namespace
		self.socket = socketio.Client()
		self.socket.connect(self.url, namespaces = f"/{self.namespace}")


	# Собираем URL адрес
	def makeURL(self) -> str:
		if settings.port == 0:
			resp_url = f"{settings.protocol}://{settings.server_url}"
		else:
			resp_url = f"{settings.protocol}://{settings.server_url}:{settings.port}"

		return resp_url


	# Изменить пространство имён
	def changeNameSpace(self, new_namespace):
		self.socket.disconnect()
		self.socket.connect(self.url, namespaces = f"/{new_namespace}")


	# Отключение от сервера
	def disconnect(self):
		self.socket.disconnect()


	# Создание события на сервере
	def emit(self, event: str, data=None):
		self.socket.emit(event, data)


	# Отслеживание событий на клиенте
	def on(self, event: str):
		def wrapper(func):
			print(event)
			@self.socket.on(event)
			def upper(data):
				func(data)

		return wrapper

	# Отслеживание событий на клиенте (для JS)
	def js_on(self, event: str):
		print(2)
		@self.socket.on(event)
		def upper(data):
			print(3)
			eel.getResponse(event, data)
