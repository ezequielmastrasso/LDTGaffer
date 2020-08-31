import LDTGafferUtils

import functools

import GafferUI

print ("LDTGAFFER:startup:gui:menu")

GafferUI.ScriptWindow.menuDefinition(application).append(
	"/LDT/tools/" + "Export extension",
	{
		"command" : functools.partial( LDTGafferUtils.export_extension), #stream data during loop
		"label" : "Export Extension"
	}
)
