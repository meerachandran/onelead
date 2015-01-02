$(document).ready(function() {
	$(function() {
		$("#attndialog").dialog({
			autoOpen: false
		});
		$("#attnbutton").on("click", function() {
			$("#attndialog").dialog("open");
		});
	});

	$("#submit").click(function(e) {
		alert("done")
	});
});