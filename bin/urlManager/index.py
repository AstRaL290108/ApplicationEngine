import eel
from .manage import URLManager

# Создаём объект класса
url = URLManager()

# Восстановление URL
@eel.expose
def resetURL():
	url.setURL(url.now_page)


# Выноси нужные функции в JS
@eel.expose
def setURL(new_url: str):
	url.setURL(new_url)