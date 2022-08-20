$(document).ready(function(){
	$('#content').load('EldelyCare/eldely/templates/index.html');

	$('ul#nav li a').click(function(){
		var page = $(this).attr('href');
		$('#content').load('EldelyCare/eldely/templates/' + page + '.html');
		return false;
	})
})