auto_run.queue(
	function() {
		$(".tab-switcher *").click(
			function() {
				$('h3[name="current"]').attr("name","");
				$(this).attr("name","current");

				// Show corresponding element
				$(".following-container").show();
				$(".follower-container").hide();
				if ($(".follower-tab").attr("name") == "current") {
					$(".follower-container").show();
					$(".following-container").hide();
				}
			}
		);
		$(".follower-container").show();
		$(".following-container").hide();
	}
);