import Gaffer
import GafferScene
import GafferArnold

print ("LDTGAFFER:startup:gui:defaults")

# Nodes Default editScope:includeInNavigationMenu
Gaffer.Metadata.registerValue(
    GafferArnold.ArnoldLight,
    'editScope:includeInNavigationMenu', 'LDTLight' 
)
Gaffer.Metadata.registerValue(
    GafferScene.ShaderTweaks,
    'editScope:includeInNavigationMenu', 'LDTShaderTweaks' 
)

Gaffer.Metadata.registerValue(
    GafferScene.StandardOptions,
    'editScope:includeInNavigationMenu', 'LDTOptions' 
)

Gaffer.Metadata.registerValue(
    GafferArnold.ArnoldOptions,
    'editScope:includeInNavigationMenu', 'LDTOptions' 
)

Gaffer.Metadata.registerValue(
    GafferScene.StandardAttributes,
    'editScope:includeInNavigationMenu', 'LDTAttributes' 
)

Gaffer.Metadata.registerValue(
    GafferArnold.ArnoldAttributes,
    'editScope:includeInNavigationMenu', 'LDTAttributes' 
)