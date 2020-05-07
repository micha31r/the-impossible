function expand() {
	$('.navbar-collapse').css('animation-name','appear');
	if ($(window).height() >= 320 && $(window).width() >= 300) {
		$('.navbar-collapse').css('animation-delay','0.8s');
		$('#mask').css('animation-name','enlarge');
		$('#mask').css('display','block');
		$('#mask').css('position','fixed');
	}
}

function contract() {
	$('.navbar-collapse').css('animation-name','reverse-appear');
	if ($(window).height() >= 320 && $(window).width() >= 300) {
		$('.navbar-collapse').css('animation-delay','0s');
		$('#mask').css('animation-name','reverse-enlarge');
		$('.navbar-collapse').css('animation-delay','0.5s');
	}
}