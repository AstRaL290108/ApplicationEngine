import requests
import settings


class Response:
	def __init__(self, resp, method, url, other=None):
		self.status_code = resp.status_code
		self.method = method
		self.url = url
		self.content = resp.content

		if other['response_type'] == "text":
			self.resp = resp.text	
		elif other['response_type'] == "json":
			self.resp = resp.json()	


		if self.method == "POST":
			self.data = other["data"]
			self.json = other["json"]
			self.params = other["params"]
			self.files = other["files"]


	# Сохранение файла
	def saveFile(self, dir, filename):
		with open(f"{dir}/{filename}", 'wb+') as file:
			file.write(self.content)


class AjaxManager:
	response_type = "text"

	def __init__(self):
		self.server = settings.server_url
		self.protocol = settings.protocol
		self.port = settings.port


	# Собираем URL адрес
	def makeURL(self, url) -> str:
		if self.port == 0:
			resp_url = f"{self.protocol}://{self.server}/{url}"
		else:
			resp_url = f"{self.protocol}://{self.server}:{self.port}/{url}"

		return resp_url


	# Отпрвляем GET запрос на сервер
	def get(self, url, params=None) -> Response:
		url = self.makeURL(url)
		resp = requests.get(url, params=params)

		response = Response(resp, "GET", url, {'response_type': self.response_type})

		self.response_type = "text"

		return response


	# Отпрвляем POST запрос на сервер
	def post(self, url: str, json=None, data=None, params=None, file=None, files=None) -> Response:
		url = self.makeURL(url)
		all_files = {}

		if not(file is None):
			f = open(file, 'rb')
			all_files = {'file': f}
		elif not(files is None):
			for i in range(len(files)):
				f = open(files[i], 'rb')
				all_files[str(i)] = f


		resp = requests.post(url, data=data, json=json, params=params, files=all_files)
		response = Response(resp, "POST", url, {"response_type": self.response_type, "data":data, "json":json, "params":params, "files":files})

		self.response_type = "text"

		return response