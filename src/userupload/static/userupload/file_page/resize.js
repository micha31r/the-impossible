function resize() {
	$("#hidden").css("display","block"); 
	var parent_height = $("#hidden").height();
	var parent_width = $("#hidden").width();
	if (parent_height <= 5) {
		parent_height = 350;
	}
    $("#file-wrapper").css("height", `${parent_height}`); 
    $("#blur").css("height", `${parent_height}`); 
    $("#blur").css("width", `${parent_width}`); 
    $("#hidden").css("display","none"); 
}

function show_spinner() {
	if ($("#id_file").val() && $("#id_description").val()) {
		$('.spinner-border').css('display','inline-block');
		$('.delete-btn').hide();
	}
}

// https://stackoverflow.com/questions/4459379/preview-an-image-before-it-is-uploaded
function preview_image() {
    var oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("id_file").files[0]);
    oFReader.onload = function (oFREvent) {
        document.getElementById("file-wrapper").style.backgroundImage = `url("${oFREvent.target.result}")`;
        document.getElementById("hidden").src = oFREvent.target.result;
    };
};

auto_run.queue(
	function() {
		resize();
		// Set trigger
		$("#id_file").change(
			function() {
				preview_image();
				// Wait 1s for image to load then resize
				setTimeout(resize, 1000);
			}
		);
		window.addEventListener(
			"resize", 
			resize
		);
	}
);