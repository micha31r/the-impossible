function resize() {
	if ($(window).width() < 690) {
		$("#idea-setting").appendTo("#append-target");
	} else {
		$("#idea-setting").appendTo("#append-origin");
	}
}

window.onload = function() {
	resize();
	window.addEventListener(
		"resize", 
		resize
	);
}