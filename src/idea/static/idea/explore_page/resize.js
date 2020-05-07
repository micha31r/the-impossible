function auto_height(recursion) {
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
		auto_height(true);
	} 
}

auto_run.queue(
	function() {
		auto_height();
		window.addEventListener(
			"resize", 
			function(){ auto_height(); }
		);
	}
);
