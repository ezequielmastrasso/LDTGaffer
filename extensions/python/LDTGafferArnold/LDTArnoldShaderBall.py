import IECore

import Gaffer
import GafferScene
import GafferArnold
from LDTGafferScene import LDTShaderBall


class LDTArnoldShaderBall(LDTShaderBall.LDTShaderBall):
    def __init__(self, name="ArnoldLDTShaderBall"):

        LDTShaderBall.LDTShaderBall.__init__(self, name)
        self["__envMapFilename"] = Gaffer.StringPlug(
            defaultValue="${GAFFER_ROOT}/resources/hdri/studio.exr"
        )

        self["__envMap"] = GafferArnold.ArnoldShader()
        self["__envMap"].loadShader("image")
        self["__envMap"]["parameters"]["filename"].setInput(self["__envMapFilename"])

        self["__skyDome"] = GafferArnold.ArnoldLight()
        self["__skyDome"].loadShader("skydome_light")
        self["__skyDome"]["parameters"]["color"].setInput(self["__envMap"]["out"])
        self["__skyDome"]["parameters"]["format"].setValue("latlong")
        # self.addChild(
        #    self["__skyDome"]["parameters"]["exposure"].createCounterpart(
        #        "exposure", Gaffer.Plug.Direction.In
        #    )
        # )
        # self["__skyDome"]["parameters"]["exposure"].setInput(self["exposure"])

        self["__parentLights"] = GafferScene.Parent()
        self["__parentLights"]["in"].setInput(self._outPlug().getInput())
        self["__parentLights"]["child"].setInput(self["__skyDome"]["out"])
        self["__parentLights"]["parent"].setValue("/")
        self["__arnoldOptions"] = GafferArnold.ArnoldOptions()
        self["__arnoldOptions"]["in"].setInput(self["__parentLights"]["out"])
        self["__arnoldOptions"]["options"]["aaSamples"]["enabled"].setValue(True)
        self["__arnoldOptions"]["options"]["aaSamples"]["value"].setValue(3)

        self.addChild(
            self["__arnoldOptions"]["options"]["threads"].createCounterpart(
                "threads", Gaffer.Plug.Direction.In
            )
        )
        self["__arnoldOptions"]["options"]["threads"].setInput(self["threads"])

        self._outPlug().setInput(self["__arnoldOptions"]["out"])


IECore.registerRunTimeTyped(
    LDTArnoldShaderBall, typeName="GafferArnold::ArnoldLDTShaderBall",
)
