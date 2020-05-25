print ("LDTGAFFER:extensions:startup:gui:Loading nodes")

import IECore
import GafferUI
import GafferArnold
import GafferSceneUI

from LDTGafferArnold import LDTArnoldShaderBall
from LDTGafferScene import LDTShaderBall

print ("LDTGAFFER:extensions:startup:gui:Loading nodes")

nodeMenu = GafferUI.NodeMenu.acquire(application)
nodeMenu.append(
    path="/LDT/LDTArnoldShaderBall",
    nodeCreator=LDTArnoldShaderBall.LDTArnoldShaderBall,
    searchText="LDTArnoldShaderBall",
)


with IECore.IgnoredExceptions(ImportError):

    import GafferArnold

    GafferSceneUI.ShaderView.registerRenderer(
        "ai", GafferArnold.InteractiveArnoldRender
    )

    def __LDTArnoldShaderBall():

        result = LDTArnoldShaderBall.LDTArnoldShaderBall()

        # Reserve some cores for the rest of the UI
        result["threads"]["enabled"].setValue(True)
        result["threads"]["value"].setValue(-3)

        return result

    GafferSceneUI.ShaderView.registerScene(
        "ai", "Default", LDTArnoldShaderBall.LDTArnoldShaderBall
    )
    print "LDTArnoldShaderBall: GafferSceneUI.ShaderView.registerScene"

