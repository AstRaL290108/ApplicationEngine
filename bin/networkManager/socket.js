class SocketIO {
	waitList = {};

	on(event, func) {
		eel.js_on(event);
		this.waitList[event] = func;
	}
	emit(event, data) {eel.js_emit(event, data);}
	disconnect() {eel.js_disconnect();}
	changeNameSpace(newNaneSpace) {eel.js_changeNameSpace(newNaneSpace);}
}
const socket = new SocketIO();

function getResponse(event, data) {
	socket.waitList[event](data);
}
eel.expose(getResponse);