from .ajax import AjaxManager
from .socket import SocketManager
import eel
import settings

ajax = AjaxManager()
if settings.socket_connect:
	socket = SocketManager()


# Выносим методы класс AjaxManager
@eel.expose
def getLink(url):
	return ajax.makeURL(url)


# Выносим методы из SocketManager
if settings.socket_connect:
	@eel.expose
	def js_changeNameSpace(newNameSpace):
		socket.changeNameSpace(newNameSpace)

	@eel.expose
	def js_disconnect():
		socket.disconnect()

	@eel.expose
	def js_emit(event: str, data=None):
		socket.emit(event, data)

	@eel.expose
	def js_on(event):
		print(1)
		socket.js_on(event)