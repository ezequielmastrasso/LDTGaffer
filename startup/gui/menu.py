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

GafferUI.ScriptWindow.menuDefinition(application).append(
	"/LDT/tools/" + "registerAnnotation",
	{
		"command" : functools.partial( LDTGafferUtils.registerAnnotation), #stream data during loop
		"label" : "registerAnnotation"
	}
)

GafferUI.ScriptWindow.menuDefinition(application).append(
	"/LDT/tools/" + "registerEditScopeProcessorType",
	{
		"command" : functools.partial( LDTGafferUtils.registerEditScopeProcessorType), #stream data during loop
		"label" : "registerEditScopeProcessorType"
	}
)

