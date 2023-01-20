def get_current_node():
    # to get the context node 
    editors = [pane for pane in hou.ui.paneTabs() if isinstance(pane, hou.NetworkEditor) and pane.isCurrentTab()]
    if not editors:
        return None
        
    network_editor = editors[-1]
    network_path = network_editor.pwd()
    display_node= hou.node(network_path.displayNode().path())
    
    return display_node.parent()
