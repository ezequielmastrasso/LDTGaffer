import IECore

import Gaffer
import GafferScene
import GafferArnold
from LDTGafferScene import LDTShaderBallScene


class LDTShaderBall(LDTShaderBallScene.LDTShaderBallScene):
    def __init__(self, name="LDTShaderBall"):

        LDTShaderBallScene.LDTShaderBallScene.__init__(self, name)
        # ShaderBall reference node
        s = Gaffer.ScriptNode()
        __shaderBallReference = s["__shaderBallReference"] = Gaffer.Reference()
        __shaderBallReference.load("LDTShaderBallScene.grf")

        self.addChild(__shaderBallReference)

        self._inPlug().setInput(self["__shaderBallReference"]["out"])


IECore.registerRunTimeTyped(
    LDTShaderBall, typeName="GafferArnold::LDTShaderBall",
)

class LDTShaderTeapot(LDTShaderBallScene.LDTShaderBallScene):
    def __init__(self, name="LDTShaderTeapot"):

        LDTShaderBallScene.LDTShaderBallScene.__init__(self, name)
        # ShaderBall reference node
        s = Gaffer.ScriptNode()
        __shaderBallReference = s["__shaderBallReference"] = Gaffer.Reference()
        __shaderBallReference.load("LDTShaderBallTeapot.grf")

        self.addChild(__shaderBallReference)

        self._inPlug().setInput(self["__shaderBallReference"]["out"])


IECore.registerRunTimeTyped(
    LDTShaderBall, typeName="GafferArnold::LDTShaderTeapot",
)