// Center body 
function center_body() {
	var diff = $(window).width() - $(".main-container").width();
	if (diff > 0) {
		$(".main-container").css("margin-left",`${diff/2}px`);
	} else {
		$(".main-container").css("margin-left","0");
	}
}

// Set margin top to give way for navbar
function body_margin() {
	if ($("nav").css("display") != "none") {
		var height = $("nav").outerHeight();
		$(".main-container").css("margin-top",`${height}px`);
	}
}

auto_run.queue( 
	function() {
		center_body();
		body_margin();
		window.addEventListener(
			"resize", 
			function() {
				center_body();
				body_margin();
			}
		);
	}
);	