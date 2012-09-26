def selected_server_alias(request):
    if 'selected_server_alias' in request.session:
        selected_server_alias = request.session['selected_server_alias']
    else:
        selected_server_alias = 'No Selection'
    return {'selected_server_alias': selected_server_alias}
