import Gaffer


print ("LDTGAFFER:startup:gui:SpreadsheetUI")
Gaffer.Metadata.registerValue( Gaffer.Spreadsheet, "selector", "preset:Sequence and Shot and Layer", "${sequence}/${shot}/${layer}" )
Gaffer.Metadata.registerValue( Gaffer.Spreadsheet, "selector", "preset:Sequence and Shot", "${sequence}/${shot}" )
Gaffer.Metadata.registerValue( Gaffer.Spreadsheet, "selector", "preset:Sequence", "${sequence}" )
Gaffer.Metadata.registerValue( Gaffer.Spreadsheet, "selector", "preset:Shot And Layer", "${shot}/${layer}" )
Gaffer.Metadata.registerValue( Gaffer.Spreadsheet, "selector", "preset:Shot", "${shot}" )
Gaffer.Metadata.registerValue( Gaffer.Spreadsheet, "selector", "preset:Layer", "${layer}" )
Gaffer.Metadata.registerValue( Gaffer.Spreadsheet, "selector", "preset:Quality", "${scene:quality}" )
Gaffer.Metadata.registerValue( Gaffer.Spreadsheet, "selector", "plugValueWidget:type", "GafferUI.PresetsPlugValueWidget" )
Gaffer.Metadata.registerValue( Gaffer.Spreadsheet, "selector", "presetsPlugValueWidget:allowCustom", True )