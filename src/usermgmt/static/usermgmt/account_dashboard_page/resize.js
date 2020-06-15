function notification_resize() {
	var padding_top = parseInt($(".notification-container").css("padding-top").replace("px",""));
	var new_height = $(".user-info").height() - padding_top;
	$(".notification-container").height(new_height);
}

auto_run.queue( 
	function() {
		notification_resize();
		window.addEventListener(
			"resize", 
			notification_resize
		);
	}
);