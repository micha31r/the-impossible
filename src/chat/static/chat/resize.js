// Set margin top to give way for navbar
function body_margin() {
	if ($("nav").css("display") != "none") {
		var height = $("nav").outerHeight();
		$(".main-container").css("padding-top",`${height}px`);
		$(".main-container").outerHeight(`${$(window).height() - height}px`);
	}
}

auto_run.queue( 
	function() {
		setTimeout(body_margin, 50);
		window.addEventListener(
			"resize", 
			body_margin
		);
	}
);	