import GafferSceneUI

print ("LDTGAFFER:startup:gui:sceneViewInspector")

for p in ["density", "scatter_anisotropy", "transparent_depth"] :
	GafferSceneUI._SceneViewInspector.registerShaderParameter( "ai:surface", p )

for p in [ "camera", "transmission", "diffuse", "specular", "sss", "indirect", "volume"] :
	GafferSceneUI._SceneViewInspector.registerShaderParameter( "ai:light", p )