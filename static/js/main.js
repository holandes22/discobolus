var LAST_SELECTED_LOADABLE_LINK

function addActiveClass(element){
    $(".loadable-link").parent().removeClass('active')
    $(element).parent().addClass('active')
}
function hideFormFieldTooltips(){
	// Need to be separated and not boud to hide event of modal dialog, since 
	// datepicker hide event would also trigger it and we don't want that.
	$('.form-field').tooltip('hide');
}
function loadDialog(){
	dialog_selector = "#editor-dialog"
	form_selector = "#editor-form"
	$.ajax({
		url: $(form_selector).attr('action'),
		type: 'POST',
		data:  $(form_selector).serialize(),
		success: function(data, textStatus, jqXHR){
			hideFormFieldTooltips();
			if(data.match("invalid_form")){
				// We got errors in form
				$(dialog_selector).html(data).modal('show');
				options = {trigger: 'manual', placement: 'in right'}
				$('.form-field').tooltip(options).tooltip('show');
				return false;
			}
			$(dialog_selector).modal('hide');
			$(LAST_SELECTED_LOADABLE_LINK).click()
		},
	})
}

function loadDeleteConfirmDialog(){
	dialog_selector = "#warning-dialog"
	form_selector = "#warning-form"
	$.ajax({
		url: $(form_selector).attr('action'),
		type: 'POST',
		data:  $(form_selector).serialize(),
		success: function(data, textStatus, jqXHR){
			$(dialog_selector).modal('hide');
			$(LAST_SELECTED_LOADABLE_LINK).click()
		},
	    error: function(jqXHR, textStatus, errorThrown){
	    	$(dialog_selector).modal('hide');
    		$('#body-content').html(jqXHR.responseText);
    	}
	})	
}

$(document).ready(function () {
    $('.loadable-link').live('click', function(e) {
    	LAST_SELECTED_LOADABLE_LINK = this
        addActiveClass(this);

        // Load left panel
        target = $(this).attr('data-target')
        
        $.ajax({
        	url: $(this).attr('url'),
        	success: function(data, textStatus, jqXHR){
        		$(target).html(data);
        	},
        	error: function(jqXHR, textStatus, errorThrown){
        		$(target).html(jqXHR.responseText);
        	}
        })
    })
})