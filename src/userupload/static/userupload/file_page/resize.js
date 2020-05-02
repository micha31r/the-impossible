function resize() {
	$("#hidden").css("display", "block"); 
	var parent_height = $("#hidden").height();
	var parent_width = $("#hidden").width();
    $("#file-wrapper").css("height", `${parent_height}`); 
    $("#blur").css("height", `${parent_height}`); 
    $("#blur").css("width", `${parent_width}`); 
    $("#hidden").css("display", "none"); 
}

window.onload = function() {
	resize();
	window.addEventListener(
		"resize", 
		resize
	);
}