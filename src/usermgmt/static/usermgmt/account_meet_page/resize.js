function profile_resize() {
	// Width 
	var container_width = $(".search-user-content").innerWidth();
	var sibling_width = $(".recent-idea-container").outerWidth();
	// Minus extra 10px just in case
	$(".search-profile-container").width(container_width-sibling_width-30);

	if ($(window).width() < 1020) {
		$(".search-user-content").prepend($(".search-profile-container"));
		$(".search-profile-container").width(container_width - 42); // 2 is border width (L & R)
		$(".recent-idea-container").width(container_width);
	}
	
}

auto_run.queue( 
	function() {
		profile_resize();
		window.addEventListener(
			"resize", 
			function() {
				profile_resize();
			}
		);
	}
);