// Resize notification
function resize() {
	var p_height = $("#navbar-notification").outerHeight();
	$("#navbar-notification-close").height(p_height);
}

auto_run.queue(
	function() {
		resize();
		window.addEventListener(
			"resize", 
			resize
		);
	}
);

auto_run.queue(
	function() {
		$("#navbar-notification-close").hover(
			// Hover
			function() {
				$("#navbar-notification-close-svg").css("stroke","#000");
				$("#navbar-notification-close-svg").css("background-color","#FFF");
			},
			// Un-hover
			function() {
				$("#navbar-notification-close-svg").css("stroke","#FFF");
				$("#navbar-notification-close-svg").css("background-color","#000");
			}
		)
	}
);

function navbar_css() {
	if ($(window).width() < 770) {
		var height = $("#navbar-notification").outerHeight() + $(".navbar").outerHeight() + 50;
		$(".earth").css("top",`${height}px`);
		$(".intro").css("margin-bottom",`${$(".card:eq(1)").height() + 50}px`);
	} else {
		$(".earth").removeAttr("style");
		$(".intro").css("margin-bottom","");
	}

	// Set and reset navbar css
	if ($(window).width() > 575) {
		$(".navbar").css(
			{
	    		"border": "0",
				"background-color": "rgba(0,0,0,0) !important",
				"position": "relative !important",
				"transform": "translateY(100%)",
				"margin-top": "-100px",
			}
		);
		/* 	Intro's margin top need to account for navbar's height because 
			in desktop resolution navbar is positioned absolute. */
		$(".intro").css("margin-top",`${$(".navbar").outerHeight() + 40}px`);
	} else {
		$(".navbar").removeAttr("style");
		$(".intro").css("margin-top","40px");
	}
}

auto_run.queue(
	function() {
		navbar_css();
		window.addEventListener(
			"resize", 
			navbar_css
		);
	}
);
