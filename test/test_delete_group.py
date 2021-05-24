def test_del_group(app):
    #otworzyc edytor
    app.group.open_group_editor()
    #spr czy sa jakies grupy
    # jesli nie ma to stworzyc
    old_groups = app.group.get_group_list()
    if len(old_groups) == 0:
        app.group.add_new_group("New Group")
    #usunac grupe
    app.group.delete_group(1)
    #pobrac liste grup
    #porownac grupy