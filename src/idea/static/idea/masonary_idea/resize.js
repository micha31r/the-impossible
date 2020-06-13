function explore_height(recursion) {
	var element = document.getElementsByClassName("flex-container")[0];
	// Reset element height
	if (!recursion) { 
		element.style.height = "400px";
	}
	if (element.scrollWidth > element.clientWidth) {
		// Adjust to the new height
		var new_height = element.clientHeight += 100;
		element.style.height = `${new_height}px`;
		// Repeat process
		explore_height(true);
	} 
}

function announcement_padding() {
	var extra = $(".announcement-wrapper").outerWidth() - $(".announcement-wrapper div").outerWidth();
	if (extra > 0) {
		$(".announcement-wrapper").css("padding-left",`${extra/2}px`);
	} else {
		$(".announcement-wrapper").css("padding-left",`40px`);
	}
}

auto_run.queue(
	function() {
		explore_height();
		announcement_padding();
		window.addEventListener(
			"resize", 
			function() {
				explore_height(); 
				announcement_padding();
			}
		);
	}
);
