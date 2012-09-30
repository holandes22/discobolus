def selected_server_alias(request):
    # This context helps to show the warning when no selection
    # has been made for server and to show it alias in the toolbar
    if 'selected_server_alias' in request.session:
        # TODO:  Find a way to just return the same context
        return {'selected_server_alias': request.session['selected_server_alias']}
    return {
            'selected_server_alias': 'No Selection',
            'server_not_selected': True,
            }
