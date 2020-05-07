function resize() {
	$("#hidden").css("display", "block"); 
	var parent_height = $("#hidden").height();
	var parent_width = $("#hidden").width();
	if (parent_height <= 5) {
		parent_height = 350;
	}
    $("#file-wrapper").css("height", `${parent_height}`); 
    $("#blur").css("height", `${parent_height}`); 
    $("#blur").css("width", `${parent_width}`); 
    $("#hidden").css("display", "none"); 
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