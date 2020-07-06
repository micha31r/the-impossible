// Center body 
function center_body() {
	var diff = $(window).width() - $(".main-container").width();
	if (diff > 0) {
		$(".main-container").css("margin-left",`${diff/2}px`);
	} else {
		$(".main-container").css("margin-left","0");
	}
}

function body_margin() {
	var height = $("nav").outerHeight() + 20;
	$(".main-container").css("margin-top",`${height}px`);
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