$.fn.toModal = function (options) {
    var settings = $.extend({
        id: "form_" + new Date().getTime().toString(),
        title: "Title Here",
        width: 580,
        withSubmit: false

    }, options);
    body = $('<div>').append($(this).clone()).html();
    modal_html = '<div id="' + settings.id + '" class="modal fade custom-modal"  tabindex="-1" role="modal" aria-labelledby="custom-modal-label" aria-hidden="true">' +
        '<div class="modal-dialog" style="width:' + settings.width + 'px;">' +
        '<div class="modal-content">' +
        '<div class="modal-header">' +
        '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>' +
        '<h4 class="modal-title">' + settings.title + '</h4>' +
        '</div>' +
        '<div class="modal-body">' + body + '</div>' +
        '<div class="modal-footer">' +
        '<button id="" type="button" data-dismiss="modal" class="btn btn-default">Close</button>' +
        (settings.withSubmit == true ? '<button rel="' + settings.id + '" type="submit"  class="btn btn-primary customFormSubmit">Submit</button>' : "") +
        '</div>' +
        '</div>' +
        '</div>' +
        '</div>';

    $("body").append(modal_html);
    $('#' + settings.id).modal({
        show: true,
        keyboard: false,
        backdrop: "static"
    });

}

// get form on modal widget
// to use this you must provide this tag
// <button class="btn btn-sm btn-primary pull-right modalFormBtn" data-href="<%= new_front_office_guest_path %>" data-action="Add New Guest" data-modal-id="GuestForm" data-modal-width="1000" data-form="#guest-form">
  // <i class="glyphicon glyphicon-plus"></i>
// </button>
function initiateBtn(){
		btn = $(".modalFormBtn");
		getModal(btn);
	}
function setFormToModal(object, modalTitle, modalWidth, modalID){
	$(object).toModal({
		width: modalWidth,
		title: modalTitle,
		id: modalID,
		withSubmit: true
	});
}
function getModal(btn){
	btn.on('click',function(event){
		event.preventDefault();
		$("#processing-modal").modal("show");
		url = $(this).attr("data-href");
		form = $(this).attr("data-form");
		modalTitle = $(this).attr("data-action");
		modalWidth = parseInt($(this).attr("data-modal-width"));
		modalID = $(this).attr("data-modal-id");
		$.get(url).done(function(data){
			res = $('<div/>').html(data).find(form);
		}).error(function(){
			res = $('<div/>').html("<p>Unexpected error has occured!</p>");
		});
		setTimeout(function(){
			$("#processing-modal").modal("hide");
			setFormToModal(res, modalTitle, modalWidth, modalID);
			initiateBtn();
		}, 1000);
	});
}

// this widget is for adding ajax support on modal form submit
// how to use?
// you must call this function modalFormAjaxSubmission(modalID, func)
// modalID is the ID of your modal form
// func is your callback, it returns the responseText enables you to manipulate
// func callback should have "resp" as first argument
// example:
// $(document).ready(function(){
	// modalFormAjaxSubmission("IdTypeForm", alertResp);
// });
// function alertResp(resp) {
	// console.log(resp)
// }
function modalFormAjaxSubmission(modalID, func){
	// pass your custom function that will
	// process the responseText to the argument func
	preload = $("<p>processing...</p>");
	$("#"+modalID).find("button[rel='"+ modalID +"']").unbind().click(function(event){
		event.preventDefault();
		modal = $("#"+modalID);
		modalBody = modal.find(".modal-body");
		form = modalBody.find("form");
		form.slideUp(300);
		modalBody.append(preload);
		modalFormSubmit(modal, form, preload, func);
	});
}


function modalFormSubmit(modal, form, preload, func){
	// pass your custom function that will
	// process the responseText to the argument func
	var options = {
		success: function(responseText, statusText, xhr, $form){
			setTimeout(function(){
				modal.modal("hide");
			}, 1000);
			res = JSON.parse(xhr.responseText);
			func(res);
		},
		error: function(responseText, statusText, xhr, $form){
			console.log(responseText.responseText);
			res = JSON.parse(responseText.responseText);
			// console.log(res.errors[0]);
			len=res.errors.length;
			err = "<ul>";
			for(i=0; len > i; i++){
				// err.append($("</li>").text(res.errors[i]));
				err += "<li>"+res.errors[i]+"</li>";
			}
			err += "</ul>";
			preload.show();
			setTimeout(function(){
				$("p.errNote").remove();
				form.prepend($("<p></p>").attr("class", "errNote alert alert-danger").html(err));
				preload.remove();
				form.slideDown(300);
			}, 2000);
		},
		asynchronous: false
	};
	form.submit(function(event){
		event.preventDefault();
		$(this).ajaxSubmit(options);
	});
}