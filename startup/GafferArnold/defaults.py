import imath

import Gaffer
import GafferArnold

print ("LDTGAFFER:startup:GafferArnold:defaults")

# Nodes Defaults Values
Gaffer.Metadata.registerValue(
    "ai:surface:standard_surface:transmit_aovs", "userDefault", 1
)

Gaffer.Metadata.registerValue(
    "ai:surface:standard_surface:aov_id1", "userDefault", "id_1"
)
Gaffer.Metadata.registerValue(
    "ai:surface:standard_surface:aov_id2", "userDefault", "id_2"
)
Gaffer.Metadata.registerValue(
    "ai:surface:standard_surface:aov_id3", "userDefault", "id_3"
)
Gaffer.Metadata.registerValue(
    "ai:surface:standard_surface:aov_id4", "userDefault", "id_4"
)
Gaffer.Metadata.registerValue(
    "ai:surface:standard_surface:aov_id5", "userDefault", "id_5"
)
Gaffer.Metadata.registerValue(
    "ai:surface:standard_surface:aov_id6", "userDefault", "id_6"
)
Gaffer.Metadata.registerValue(
    "ai:surface:standard_surface:aov_id7", "userDefault", "id_7"
)
Gaffer.Metadata.registerValue(
    "ai:surface:standard_surface:aov_id8", "userDefault", "id_8"
)

# Nodes Default Colors
Gaffer.Metadata.registerValue(
    GafferArnold.ArnoldLight,
    "nodeGadget:color", imath.Color3f( 0.69, 0.60, 0.2255 )
)
