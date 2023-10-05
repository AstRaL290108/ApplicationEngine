from tools import url, localStorage, ajax


@url.listen("/")
def index(req):
	req.render("index.html", {"hello": 3})