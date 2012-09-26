var LAST_SELECTED_LOADABLE_LINK
var LAST_SELECTED_SERVER_ALIAS = ""
var LAST_SELECTED_SERVER_ID = null

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


function loadWizardStep(){
	target = $(this).attr('data-target')
	$.ajax({
		url: $(form_selector).attr('action'),
		type: 'POST',
		data:  $(form_selector).serialize(),
    	success: function(data, textStatus, jqXHR){
    		$(target).html(data);
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

function setCookie(c_name,value,exdays)
{
	var c_value;
	var exdate = new Date();
	exdate.setDate(exdate.getDate() + exdays);
	c_value = escape(value) + ((exdays == null) ? "" : "; expires=" + exdate.toUTCString());
	document.cookie = c_name + "=" + c_value;
}

function getCookie(c_name){
	var i, x, y, ARRcookies = document.cookie.split(";");
	for (i = 0; i < ARRcookies.length; i++)
	{
		x = ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
		y = ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
		x = x.replace(/^\s+|\s+$/g,"");
		if (x == c_name)
		{
	    	return unescape(y);
	    }
	}
}

$(document).ready(function () {
	$('#last-selected-server-alias').html(getCookie('last-selected-server-alias'))
	
	$('.server-selection').live('click', function(e){
		addActiveClass(this);	
		var last_selected_server_alias = $(this).attr('server-alias')
		$('#last-selected-server-alias').html(last_selected_server_alias)
		setCookie('last-selected-server-alias', last_selected_server_alias, 7)
		setCookie('last-selected-server-id', $(this).attr('server-id'), 7)
	})


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