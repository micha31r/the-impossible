function expand(element_id, button_id) {
	var element = document.getElementById(element_id);
	var button = document.getElementById("collapse-link-trigger");
	if (button.name === "open") {
		button.name = "close";
		var style = `display: block !important;
			position: absolute;
			animation-name: popuplink;
			animation-duration: 0.5s;
			animation-fill-mode: forwards;
			z-index: 1 !important;`;
		element.style = style;
	} else {
		button.name = "open";
		// Retract menu
		element.style = `
			display: block !important;
			position: absolute;
			animation-name: reverse-popuplink;
			animation-duration: 0.5s;
			animation-fill-mode: forwards;`;
	}
}

function reset_expand(element_id, button_id) {
	var element = document.getElementById(element_id);
	var button = document.getElementById(button_id);
	button.name = "open";
	// Reset element css to default
	element.style = "";
}
