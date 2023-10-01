class LocalStorage {
	async setItem(key, value) {await eel.localStorage__setItem(key, value);}
	async getItem(key, func) {
		let data = await eel.localStorage__getItem(key)();
		func(data);
	}
	async deleteItem(key, value) {await eel.localStorage__deleteItem(key);}
	async clear(key, value) {await eel.localStorage__clear();}
}


class Application {
	setURL(url) {
		eel.setURL(url);
		this.onunload();
	}

	localStorage = new LocalStorage;
	
}

const app = new Application();