function resize() {
	var p_height = $("#navbar-notification").outerHeight();
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

auto_run.queue(
	function() {
		$("#navbar-notification-close").hover(
			// Hover
			function() {
				$("#navbar-notification-close").css("background-color","#FFF");
				$("#navbar-notification-close-svg").css("stroke","#000");
			},
			// Un-hover
			function() {
				$("#navbar-notification-close").css("background-color","#000");
				$("#navbar-notification-close-svg").css("stroke","#FFF");
			}
		)
	}
);