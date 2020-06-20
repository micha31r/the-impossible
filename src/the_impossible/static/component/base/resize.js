// Center body 
function center_body() {
	var diff = $(window).width() - $("body").width();
	if (diff > 0) {
		$("body").css("margin-left",`${diff/2}px`);
	} else {
		$("body").css("margin-left","0");
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