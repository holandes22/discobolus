def selected_server_pk(request):
    # This context helps to show the warning when no selection
    # has been made for server and to show it alias in the toolbar
    if 'server_pk' in request.session:
        # TODO:  Find a way to just return the same context
        return {
                'server_pk': request.session['server_pk']
                }
    return {
            'server_not_selected': True,
            }
