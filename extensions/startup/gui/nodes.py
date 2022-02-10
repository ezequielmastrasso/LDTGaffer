import IECore
import GafferUI
import GafferArnold
import GafferSceneUI

from LDTGafferScene import LDTShaderBall
from LDTGafferScene import LDTShaderBallScene
from LDTGafferScene import LDTGetBoundingBox

print ("LDTGAFFER:extensions:startup:gui:Loading nodes")

nodeMenu = GafferUI.NodeMenu.acquire(application)
nodeMenu.append(
    path="/LDT/ShaderBall/LDTShaderBallScene",
    nodeCreator=LDTShaderBallScene.LDTShaderBallScene,
    searchText="LDTShaderBallScene",
)
nodeMenu.append(
    path="/LDT/ShaderBall/LDTShaderBall",
    nodeCreator=LDTShaderBall.LDTShaderBall,
    searchText="LDTShaderBall",
)

"""
nodeMenu.append(
    path="/LDT/LGTGetBoundingBox",
    nodeCreator=LDTGetBoundingBox.LDTGetBoundingBox,
    searchText="LDTGetBoundingBox",
)
"""

with IECore.IgnoredExceptions(ImportError):
    
    GafferSceneUI.ShaderView.registerRenderer(
        "ai", GafferArnold.InteractiveArnoldRender
    )

    def __LDTShaderBall():

        result = LDTShaderBall.LDTShaderBall()

        # Reserve some cores for the rest of the UI
        result["threads"]["enabled"].setValue(True)
        result["threads"]["value"].setValue(-3)

        return result

    GafferSceneUI.ShaderView.registerScene(
        "ai", "LDTShaderBall", LDTShaderBall.LDTShaderBall
    )
    print ("LDTShaderBall: GafferSceneUI.ShaderView.registerScene")

with IECore.IgnoredExceptions(ImportError):
    GafferSceneUI.ShaderView.registerRenderer(
        "ai", GafferArnold.InteractiveArnoldRender
    )

    def __LDTShaderTeapot():

        result = LDTShaderBall.LDTShaderTeapot()

        # Reserve some cores for the rest of the UI
        result["threads"]["enabled"].setValue(True)
        result["threads"]["value"].setValue(-3)

        return result

    GafferSceneUI.ShaderView.registerScene(
        "ai", "LDTShaderTeapot", LDTShaderBall.LDTShaderTeapot
    )
    print ("LDTShaderTeapot: GafferSceneUI.ShaderView.registerScene")

