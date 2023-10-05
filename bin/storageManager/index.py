from .storage import LocalStorage, Cookie
import eel

localStorage = LocalStorage()

# Выводим функции localStorage в JS
@eel.expose
def localStorage__setItem(key: str, value):
	localStorage.setItem(key, value)

@eel.expose
def localStorage__getItem(key: str):
	print(localStorage.getItem(key))
	return localStorage.getItem(key)

@eel.expose
def localStorage__deleteItem(key: str):
	localStorage.deleteItem(key)

@eel.expose
def localStorage__clear(key: str):
	localStorage.clear(key)