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
				$("#navbar-notification-close-svg").css("stroke","#000");
				$("#navbar-notification-close-svg").css("background-color","#FFF");
			},
			// Un-hover
			function() {
				$("#navbar-notification-close-svg").css("stroke","#FFF");
				$("#navbar-notification-close-svg").css("background-color","#000");
			}
		)
	}
);