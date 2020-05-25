import Gaffer

print ("LDTGAFFER:startup:gui:NameSwitchUI")
Gaffer.Metadata.registerValue( Gaffer.NameSwitch, "selector", "preset:Sequence and Shot", "${sequence}/${shot}" )
Gaffer.Metadata.registerValue( Gaffer.NameSwitch, "selector", "preset:Sequence", "${sequence}" )
Gaffer.Metadata.registerValue( Gaffer.NameSwitch, "selector", "preset:Shot", "${shot}" )
Gaffer.Metadata.registerValue( Gaffer.NameSwitch, "selector", "preset:Layer", "${layer}" )
Gaffer.Metadata.registerValue( Gaffer.NameSwitch, "selector", "plugValueWidget:type", "GafferUI.PresetsPlugValueWidget" )
Gaffer.Metadata.registerValue( Gaffer.NameSwitch, "selector", "presetsPlugValueWidget:allowCustom", True )