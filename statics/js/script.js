$(document).ready(function(){
	$("#login").click(function(){
		var user = $("#username").val();
		var pwd = $("#password").val();
		var pd = {"username":user,"password":pwd};
		$.post("/",pd,function(data,status){
			window.location.href='/matlab';
		});
	});
});
