import imath

import Gaffer
import GafferArnold

print ("LDTGAFFER:startup:GafferArnold:defaults")

# Nodes Defaults Values
Gaffer.Metadata.registerValue(
    "ai:surface:standard_surface:transmit_aovs", "userDefault", 1
)

# Nodes Default Colors
Gaffer.Metadata.registerValue(
    GafferArnold.ArnoldLight,
    "nodeGadget:color", imath.Color3f( 0.69, 0.60, 0.2255 )
)
