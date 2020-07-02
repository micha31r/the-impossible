function image_resize() {
	if ($(window).width() < 750) {
		$(".right-container").children().each(
			function() {
				$(this).appendTo("#append-target1");
			}
		);
		$(".right-container").css("display","none");
		$(".left-container").css("width","100%");
	} else {
		$("#append-target1").children().each(
			function() {
				$(this).appendTo(".right-container");
			}
		);
		$(".left-container").css("width","");
		$(".right-container").css("display","");

		var new_width = $(".wrapper").width() - $(".left-container").outerWidth() - 30;
		$(".right-container").width(new_width);
	}
}

auto_run.queue( 
	function() {
		image_resize();
		window.addEventListener(
			"resize", 
			image_resize
		);
	}
);