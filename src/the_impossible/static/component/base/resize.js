// Center body 
function center_body() {
	var diff = $(window).width() - $(".main-container").width();
	if (diff > 0) {
		$(".main-container").css("margin-left",`${diff/2}px`);
	} else {
		$(".main-container").css("margin-left","0");
	}
}

auto_run.queue( 
	function() {
		center_body();
		window.addEventListener(
			"resize", 
			center_body
		);
	}
);	