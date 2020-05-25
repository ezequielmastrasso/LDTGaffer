import Gaffer
import GafferUI
import os

print ("LDTGAFFER:startup:gui:nodes")

def __LDTShaderBallScene() :

	return Gaffer.Reference( "LDTShaderBallScene" )

def __LDTShaderBallScenePostCreator( node, menu ) :

	node.load(
		os.path.expandvars( "LDTShaderBallScene.grf" )
	)

nodeMenu = GafferUI.NodeMenu.acquire( application )
nodeMenu.append(
	path = "/LDT/primitives/LDTShaderBallScene",
	nodeCreator = __LDTShaderBallScene,
	postCreator = __LDTShaderBallScenePostCreator,
	searchText = "LDTShaderBallScene"
)
