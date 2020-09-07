import imath

import Gaffer
import GafferArnold

print ("LDTGAFFER:startup:Gaffer:defaults")

# Nodes Defaults Values
Gaffer.Metadata.registerValue(
    "gl:surface:Phong:Cs", "userDefault", imath.Color3f( 1.0, 1.0, 1.0 ))
# Nodes Defaults Values
Gaffer.Metadata.registerValue(
    "gl:surface:Phong:transparency", "userDefault", 1.0)