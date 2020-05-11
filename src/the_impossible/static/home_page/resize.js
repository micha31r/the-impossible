function resize() {
	var p_height = $("#navbar-notification").height();
	$("#navbar-notification-close").height(p_height);
}

auto_run.queue(
	function() {
		resize();
		window.addEventListener(
			"resize", 
			resize
		);
	}
);