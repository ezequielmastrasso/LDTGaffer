import functools

import IECore
import Gaffer
import GafferUI


print ("LDTGAFFER:startup:gui:customVariables")

def __scriptAdded( container, script ) :

	variables = script["variables"]

	if "LDTGafferResources" not in variables :
		LDTResources = variables.addMember(
			"LDTGaffer:resources",
			IECore.StringData( "${LDTGaffer}/resources/" ),
			"LDTGafferResources"
		)

	Gaffer.MetadataAlgo.setReadOnly( variables["LDTGafferResources"]["name"], True )

application.root()["scripts"].childAddedSignal().connect( __scriptAdded, scoped = False )


