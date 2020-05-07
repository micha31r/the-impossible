function navbar_resize() {
    if ($(window).width() < 575) {
    	navbar_append_element(".nav-item","#navbar-append-target1");
    	navbar_append_element(".nav-auth","#navbar-append-target2");
    } else {
    	navbar_append_element(".nav-item","#navbar-append-origin1");
    }
}

function navbar_append_element(element,target,order=1) {
	if (order == 0) {
		return $(element).prepend(target);
	}
	$(element).appendTo(target);
}

auto_run.queue(
	function() {
		navbar_resize();
		window.addEventListener(
			"resize", 
			function() {
				navbar_resize();
			}
		);
	}
);