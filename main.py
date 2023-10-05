import eel
import os
import settings as cfg
import application



if __name__ == "__main__":
	eel.init("./")
	eel.start('bin/urlManager/front/template.html', mode="chrome", size=(cfg.width, cfg.height))