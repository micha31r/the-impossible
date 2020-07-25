// Set button label's position to mouse position
function element_label_position(event) {
	var label = $(".element-label:visible");
	if (label.height()) { // Check if element is valid (not an empty jquery obj)
		label.css("left", event.pageX - $(window).scrollLeft() + 10);
		label.css("top", event.pageY - $(window).scrollTop() + 10);
		element_label_overflow(label);
	}
}

// Prevent button label from going off-screen
function element_label_overflow(label) {
	var screen = $(window).width();
	var label = label
	// Right overflow
	if (((label.offset().left - $(window).scrollLeft()) + label.outerWidth()) > ($(window).width() - 10)) {
		label.css("left", $(window).width() - 10 - label.outerWidth());
	} 
	// Left overflow
	if (label.offset().left < 10) {
		label.css("left", 10);
	}
	// Top overflow
	if (label.offset().top < 10) {
		label.css("top", 10);
	}
	// Bottom overflow
	if (((label.offset().top - $(window).scrollTop()) + label.outerHeight()) > ($(window).height() - 10)) {
		label.css("top", $(window).height() - 10 - label.outerHeight());
	}
}

auto_run.queue( 
	function() {
		// Show label when hovered
		$(".has-label").each(
			function() {
				$(this).hover(
					function() {
						$(this).find(".element-label").show();
					},
					function() {
						$(this).find(".element-label").hide();
					}
				);
			}
		);
	}
);

$(document).on(
	"mousemove", 
	function(event) {
		element_label_position(event);
	}
);