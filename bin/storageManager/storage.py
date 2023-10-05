import eel
import json
import os

class LocalStorage:
	def setItem(self, key: str, value):
		with open("bin/storageManager/storage.json", "r") as file:
			key   = str(key)

			template = json.load(file)
			template[key] = value

		with open("bin/storageManager/storage.json", "w") as file:
			json.dump(template, file)


	def getItem(self, key: str) -> str:

		with open("bin/storageManager/storage.json") as file:
			try:
				template = json.load(file)

				key = str(key)
				return str(template[key])

			except KeyError:
				return None


	def deleteItem(self, key: str):
		try:
			with open("bin/storageManager/storage.json", "r") as file:
				key   = str(key)
				template = json.load(file)
				del template[key]

			with open("bin/storageManager/storage.json", "w") as file:
				json.dump(template, file)

		except KeyError:
			pass

	def clear(self):
		with open("bin/storageManager/storage.json", "w") as file:
			json.dump({}, file)


class Cookie:
	def set(self, name, value, options = None):
		if options is None:
			eel.setCookie(name, value)
		else:
			eel.setCookie(name, value, options)


	def delete(self, name):
		eel.deleteCookie(name)


	def get(self, name):
		return eel.getCookie(name)()