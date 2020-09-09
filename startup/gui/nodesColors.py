import Gaffer
import GafferScene
import GafferDispatch
import GafferArnold

import imath

print ("LDTGAFFER:startup:gui:nodesColors")

# Nodes Default Colors
# Same colors from Gaffer's Default, only paler easier on the eyes.

Gaffer.Metadata.registerValue(
    Gaffer.Node,
    'nodeGadget:color', imath.Color3f( 0.200000003, 0.200000003, 0.200000003 ) )
Gaffer.Metadata.registerValue(
    GafferScene.SceneProcessor,
    "nodeGadget:color", imath.Color3f( 0.38, 0.209, 0.2757 ) )
Gaffer.Metadata.registerValue(
    GafferScene.GlobalsProcessor,
    "nodeGadget:color", imath.Color3f( 0.325, 0.505, 0.343 ) )
Gaffer.Metadata.registerValue(
    GafferScene.SetFilter,
    "nodeGadget:color", imath.Color3f( 0.55, 0.4114, 0.1754 ) )
Gaffer.Metadata.registerValue(
    GafferScene.PathFilter,
    "nodeGadget:color", imath.Color3f( 0.55, 0.4114, 0.1754 ) )
Gaffer.Metadata.registerValue(
    Gaffer.EditScope,
    "nodeGadget:color", imath.Color3f( 0.273, 0.434, 0.6 ) )
Gaffer.Metadata.registerValue(
    GafferDispatch.TaskNode,
    "nodeGadget:color", imath.Color3f( 0.5, 0.17, 0.17 ) )

# Nodes Default Colors GafferArnold
Gaffer.Metadata.registerValue(
    GafferArnold.ArnoldLight,
    "nodeGadget:color", imath.Color3f( 0.75, 0.56, 0 )
)
