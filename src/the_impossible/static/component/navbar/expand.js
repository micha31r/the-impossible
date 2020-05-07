function navbar_expand() {
	$('.navbar-collapse').css('animation-name','appear');
	if ($(window).height() >= 320 && $(window).width() >= 300 && aspect_diff() < 400) {
		$('.navbar-collapse').css('animation-delay','0.8s');
		$('#mask').css('animation-name','enlarge');
		$('#mask').css('display','block');
		$('#mask').css('position','fixed');
	} else {
		$('#mask').css('display','none');
	}
}

function navbar_contract() {
	$('.navbar-collapse').css('animation-name','reverse-appear');
	$('.navbar-collapse').css('animation-delay','0s');
	if ($(window).height() >= 320 && $(window).width() >= 300 && aspect_diff() < 400) {
		$('#mask').css('animation-name','reverse-enlarge');
	} else {
		$('#mask').css('display','none');
	}
}