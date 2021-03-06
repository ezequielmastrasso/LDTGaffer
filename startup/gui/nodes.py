import Gaffer
import GafferScene
import GafferUI
import os

print ("LDTGAFFER:startup:gui:nodes")

def __LDTShaderBallScene() :

	return Gaffer.Reference( "LDTShaderBallScene" )

def __LDTShaderBallScenePostCreator( node, menu ) :

	node.load(
		os.path.expandvars( "LDTShaderBallScene.grf" )
	)

def __Phong ():
	shader_node = GafferScene.OpenGLShader( "Phong" )
	shader_node.loadShader( "Phong" )
	return shader_node

nodeMenu = GafferUI.NodeMenu.acquire( application )

nodeMenu.append(
	path = "/LDT/primitives/LDTShaderBallScene",
	nodeCreator = __LDTShaderBallScene,
	postCreator = __LDTShaderBallScenePostCreator,
	searchText = "LDTShaderBallScene"
)

nodeMenu.append(
	path = "/LDT/OpenGL/Phong",
	nodeCreator = __Phong,
	searchText = "Phong"
)
