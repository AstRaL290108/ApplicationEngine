window.onload = () => {
	eel.resetURL();
}


function addHeaderFiles(head) {
	let head_div = document.querySelector("head");

	let scripts = head_div.querySelectorAll(".loaded");
	for (let i = 0; i < scripts.length; i++) {
		item = scripts[i];
		head_div.removeChild(item);
	}

	for (let i = 0; i < head.length; i++) {
		item = head[i];

		var file = document.createElement(item[0]);
        file.src = `../../../static/${item[1]}`;
        file.href = `../../../static/${item[1]}`;
        if (item[0] == "link")
        	file.rel = item[2];
        file.classList.add("loaded");
        document.getElementsByTagName('head')[0].appendChild(file);
	}
}


function loadPage(title, head, body) {
	document.querySelector("title").textContent = title;
	let body_div = document.querySelector("body");
	body_div.innerHTML = body;
	addHeaderFiles(head);

	app.onunload = () => {}
}

eel.expose(loadPage);