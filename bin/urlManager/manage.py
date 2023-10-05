import eel
from bs4 import BeautifulSoup
from pathlib import Path

import settings
from bin.storageManager import Cookie


class Request:
	def __init__(self, params: dict):
		self.params = params
		self.code = 200
		
		self.cookie = Cookie()


	# Поиск и захват html документа
	def getFile(self, html: str) -> BeautifulSoup:
		html_doc = ""
		way = Path(__file__).resolve().parent.parent.parent
		f = open(f"{way}\\views\\{html}" , 'rb')
		for line in f:
			html_doc += line.decode("utf-8")
		f.close()
		soup = BeautifulSoup(html_doc, 'lxml')

		return soup


	# Основное разделение документа
	def documentSplit(self, soup: BeautifulSoup, data = None) -> dict:
		head = []

		links = soup.find_all("link")
		for i in links:
			if str(type(i.get("rel"))) == "<class 'list'>":
				head.append(["link", i.get("href"), f'{i.get("rel")[0]} {i.get("rel")[1]}'])
			else:
				head.append(["link", i.get("href"), i.get("rel")])

		scripts = soup.find_all("script")
		for i in scripts:
			head.append(["script", i.get("src")])

		body = str(soup.select_one("body"))
		if not(data is None):
			keys = data.keys()
			for i in keys:
				body = body.replace("{"+ f" {i} " + "}", str(data[f'{i}']))

		body = body.replace("{ static_dir }", "../../../static/") 

		return {"head": head, 'body': body}


	# Отрисовка страницы
	def render(self, html: str, data = None):
		soup = self.getFile(html)
		splited_document = self.documentSplit(soup, data)
			
		eel.loadPage(soup.select_one("title").text, splited_document["head"], splited_document["body"])
		


class URLManager:
	now_page = "/"
	all_urls = []

	last_params = {}


	# Функция обработки 404
	def notFound(self):
		if settings.not_found_file:
			r = Request({})
			r.render(html = "404.html")
		else:
			eel.loadPage("Страница не найдена", [], "Перезапустите приложение!")


	# Собираем параметры из ссылки
	def selectParams(self, listener: dict) -> int:
		if listener['url'] == "":
			return 0

		split_url = listener['url'].split("/")
		split_now_url = self.now_page.split("/")

		for i in range(len(split_url)):
			if split_url[i] != "":
				if (split_url[i][0] == ":"):
					self.last_params[split_url[i].replace(":", "")] = split_now_url[i]


	# Ищим подходящий URL
	def searchURL(self, url: str) -> dict:
		for item in self.all_urls:
			split_i = item['url'].split("/")
			split_e = url.split("/")
			return_ = 0

			if len(split_e) != len(split_e):
				continue


			for i in range(len(split_e)):
				if (split_i[i] == split_e[i]):
					return_ += 1
				try:
					if (split_i[i][0] == ":"):
						return_ += 1
				except IndexError:
					continue


			if return_ == len(split_e):
				self.selectParams(item)
				return item


	# Добавление функции на обработку
	def listen(self, url: str):
		def wrapper(func):
			self.all_urls.append({
				'url': url,
				'func': func
			})
		return wrapper


	# Изменение URL адреса
	def setURL(self, url: str):
		self.now_page = url
		new_url_func = self.searchURL(url)
		if new_url_func is None:
			self.notFound()
			return 0

		request = Request(self.last_params)
		new_url_func['func'](request)