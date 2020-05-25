import os

import GafferUI
import Gaffer

def export_extension( menu ) :
	scriptWindow = menu.ancestor( GafferUI.ScriptWindow )
	script = scriptWindow.scriptNode()
	path, bookmarks = GafferUI.FileMenu.__pathAndBookmarks( scriptWindow )

	dialogue = GafferUI.PathChooserDialogue( path, title="Save script", confirmLabel="Save", leaf=True, bookmarks=bookmarks )
	path = dialogue.waitForPath( parentWindow = scriptWindow )

	if not path :
		return

	path = str( path )

	script["fileName"].setValue( path )
	with GafferUI.ErrorDialogue.ErrorHandler( title = "Error Saving File", parentWindow = scriptWindow ) :

		scriptWindow = menu.ancestor( GafferUI.ScriptWindow )
		Gaffer.ExtensionAlgo.exportExtension(
			os.path.splitext(os.path.basename(path))[0],	#PackageName
			script.selection(),							   	#Nodelist
			path
		)