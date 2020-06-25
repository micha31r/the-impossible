function notification_resize() {
	// Width 
	var container_width = $(".user-info").innerWidth() - 80;
	var user_info_container = $(".user-info-container").outerWidth();
	var padding = 40;
	var new_width = container_width - user_info_container - padding - 20; // 20px spacing
	$(".notification-container").width(new_width);
	// Height
	var padding_top = parseInt($(".notification-container").css("padding-top").replace("px",""));
	var new_height = $(".user-info").height() - padding_top;
	$(".notification-container").height(new_height);
}

function follower_profile_resize() {
	// 150 is the profile image width, 40 is the text wrapper padding (L & R)
	var width = $(".follower-profile-wrapper").width() - 150 - 40; 
	$(".profile-info-wrapper").css("width",`${width}px`);
}

auto_run.queue( 
	function() {
		notification_resize();
		follower_profile_resize();
		window.addEventListener(
			"resize", 
			function() {
				notification_resize();
				follower_profile_resize();
			}
		);
	}
);