# LDTGaffer
My gaffer toolset, presets, and configs.

```Requires Gaffer 0.58.1.0```

### Folders and Variables
* Custom Variables LDT resources
* Bookmarks LDT folders

### LDT Menu
* Export Extension
* Node Annotations
* register includeInNavigationMenu 

### Node Defaults nodeGadget:color
Same as Gaffer Defaults, but paler colours easier on the eye.
Except lights (yellow color), and filters (similar color to the Filter plugs colors).   

<img width="30%" src="docs/nodeGadget_color.png" alt="EZSurfacing Tools" style="" />

### Viewer:
##### SceneView:Phong, graph Editor Phong, and Diagnostics 2k/4k textures

<img width="31%" src="docs/sceneViewPhong.png" alt="EZSurfacing Tools" style="" /><img width="31%" src="docs/sceneViewPhong_2.png" alt="EZSurfacing Tools" style="" /><img width="32%" src="docs/gafferDiagnosticPatterns.png" alt="EZSurfacing Tools" style="" />

Phong courtesy of [Irene Hernández](https://www.linkedin.com/in/ireneher/).  
Cs and transparency plugs.

### ShaderView:Shader Balls and 
<img width="40%" src="docs/gafferShaderView2.png" alt="EZSurfacing Tools" style="" /><img width="50.5%" src="docs/gafferShaderTeapot.png" alt="EZSurfacing Tools" style="" />

### Arnold Outputs
* Lightgroup_[a-g]
* Lightgroups_denoise[a-g] with optix filter.

### NameSwitch and Spreadsheet Presets
```
${sequence}/${shot}/${layer}
${sequence}/${shot}
${sequence}
${shot}/${layer}
${shot}
${layer}
```

### Node Defaults EditScopes
* IncludeInNavigationMenu:
  * GafferArnold.ArnoldLight
  * GafferScene.ShaderTweaks
  * GafferScene.StandardOptions
  * GafferArnold.ArnoldOptions
  * GafferScene.StandardAttributes
  * GafferArnold.ArnoldAttributes
  * And some LDTNodes

<img src="docs/editscopes.png" alt="EZSurfacing Tools" style="" />

### Scene Inspector registerShaderParameter
* aiStandardVolume: density, scatter_anisotropy, transparent_depth 
* aiLights: all contributions
<img width="11.7%" src="docs/editscopes_2.png" alt="EZSurfacing Tools" style="" />

### Boxes 3d

##### LightCreator
<img width="50%" src="docs/LightCreator.png" alt="EZSurfacing Tools" style="" />

##### Attribute Sets
Give it an attribute name and a scene:path, and will create a Set per unique attribute value containing the geometry.   

<img width="50%" src="docs/gafferSets.png" alt="EZSurfacing Tools" style="" />

##### LDTRenderLayer
<img src="docs/LDTRenderLayer.png" alt="EZSurfacing Tools" style="" />

##### contextEnabled Editscope and Box
Contents will only be enabled when in the given context. Both Editscope and Box based.
The EditScope based contains Edit TweaksNodes ready to use.

<img width="50%" src="docs/contextEnabled.png" alt="EZSurfacing Tools" style="" />

##### LightsMuteSolo
Mutes/Solo lights, using intensity or prune.

<img width="50%" src="docs/LightsMuteSolo.png" alt="EZSurfacing Tools" style="" />

##### Center To Origin
Centers the given objects to the origin.

<img width="50%" src="docs/CenterToOrigin.png" alt="EZSurfacing Tools" style="" />

##### UvSizeMultipler
Scales the objects UVs. Useful for the ShaderBall scene, where you want to scale the uvs
for visualization instead of modifying the material tiling.

##### Inspection Camera
Inspection camera drop in.

<img width="50%" src="docs/InpectionCamera.png" alt="EZSurfacing Tools" style="" />

### Boxes 2d
##### ShowMetadata
Search metadata keys with partial matching, and overlays on the image. For ie: /stats/geo will display all /arnold/stats/geo..., samples will display all keys that contain the word samples. Leave a blank field, and it will display all available keywords   
<img src="docs/gafferLDTShowMetadataKeys.png" alt="EZSurfacing Tools" style="" />
<img width="100%" src="docs/gafferLDTShowMetadata.png" alt="EZSurfacing Tools" style="" />

### Misc
* Gaffer Cache MemoryLimit