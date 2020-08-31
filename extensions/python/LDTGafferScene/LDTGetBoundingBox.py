"""

import imath
import IECore
import Gaffer
import GafferScene
import GafferUI

class LDTGetBoundingBox( Gaffer.ComputeNode ) :

    def __init__( self, name="LDTGetBoundingBox" ) :

        Gaffer.ComputeNode.__init__( self, name )

        scene_in = GafferScene.ScenePlug( "scene_in", Gaffer.Plug.Direction.In )
        path = Gaffer.StringPlug( "path", Gaffer.Plug.Direction.In, defaultValue="/")
        bound = Gaffer.StringPlug( "bound", Gaffer.Plug.Direction.Out )
        scene_out = GafferScene.ScenePlug( "scene_out", Gaffer.Plug.Direction.Out )
        
        self.addChild( path )
        self.addChild( scene_in )
        self.addChild( scene_out )
        self.addChild( bound )
        self.addChild( Gaffer.BoolPlug( "enabled", defaultValue = True ) )

        scene_out.setInput(scene_in)

        self.numHashCalls = 0
        self.numComputeCalls = 0

    def enabledPlug( self ) :

		return self["enabled"]

    def correspondingInput( self, output ) :

		if output.isSame( self["scene_out"] ) :

			return self["scene_in"]

		return Gaffer.ComputeNode.correspondingInput( self, output )

    def affects( self, input ) :

        outputs = Gaffer.ComputeNode.affects( self, input )
        if input.getName() in ("scene_in","enabled","path" ) :
            outputs.append( self.getChild("bound") )

        return outputs

    def hash( self, output, context, h ) :
        
        #self.getChild("scene_in").hash( h )
        self.getChild("path").hash( h )
        self.getChild("enabled").hash( h )
        self.numHashCalls += 1

    def compute( self, plug, context ) :
        with Gaffer.Context(context) as context:
            context["scene:path"] = GafferScene.ScenePlug.stringToPath( self["path"].getValue() )
            scene_path_bound = self["scene_out"].bound(self["path"].getValue())
            self["bound"].setValue(str(scene_path_bound))
        self.numComputeCalls += 1

IECore.registerRunTimeTyped( LDTGetBoundingBox, typeName = "GafferScene::LDTGetBoundingBox" )

"""