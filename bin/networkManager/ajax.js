class Response {
	constructor(resp) {
		this.resp = resp;

		try {
			this.json = JSON.parse(resp);
		}catch {
			console.log(321);
		}
	}
}

class Ajax {
	async get(url, responce_func) {
		let resp_url = await eel.getLink(url)();
		this.sendGet(resp_url, responce_func);
	}
	async post(url, data, responce_func) {
		let resp_url = await eel.getLink(url)();
		this.sendPost(resp_url, data, responce_func);
	}

	sendGet(url, responce_func) {
		const req = new XMLHttpRequest();
		req.open("GET", url);
		req.onload = () => {
			responce_func(new Response(req.response));
		}
		req.send();
	}
	sendPost(url, data, responce_func) {
		const req = new XMLHttpRequest();
		const formData = new FormData();

		req.open("POST", url);
		for(let i=0; i < Object.keys(data).length; i++) {
			let item = Object.keys(data)[i];
			formData.append(item, data[item]);
		}

		req.onload = () => {
			responce_func(new Response(req.response));
		}

		req.send(formData);
	}
}

const ajax = new Ajax();