# LDTGaffer
My gaffer toolset, presets, and configs.

## UI

### Miscelaneous
* Custom Variables LDT resources
* Bookmarks LDT folders
* LDT Menu: Export Extension
* LDT Menu: Node Annotations
* LDT Menu: register Editscope preprocessor metadata
* Gaffer Cache MemoryLimit
* Arnold Outputs: Custom lightgroup_[a-g], and lightgroup_denoise[a-g] using optix filter.

### NameSwitch and Spreadsheet Presets
```
${sequence}/${shot}/${layer}
${sequence}/${shot}
${sequence}
${shot}/${layer}
${shot}
${layer}
```

### nodeGadget:color
Same as Gaffer Defaults, but paler colours easier on the eye.
Except lights (yellow color), and filters (similar color to the Filter plugs colors).   

<img src="docs/nodeGadget_color.png" alt="EZSurfacing Tools" style="" />

## Python

### LDT Menu
##### Export Extension
Default Gaffer export extension example. Might not work with Spreadsheets, etc.

##### Annotation
Set selected nodes Metadata `annotation:greeting:text`   

<img src="docs/annotations.png" alt="EZSurfacing Tools" style="" />

##### Editscopes register nodes
Set selected nodes and add register Editscope preprocessor metadata to make nodes accesible from the editscope menu. Default LDT.   

<img src="docs/editscopes_1.png" alt="EZSurfacing Tools" style="" /> <img src="docs/editscopes_2.png" alt="EZSurfacing Tools" style="" />


### SceneView:Phong and graph editor OpenGL phong Shader
Tired of the facing ratio look?
You can thank [Irene Hernández](https://www.linkedin.com/in/ireneher/) for this.

<img width="100%" src="docs/sceneViewPhong.png" alt="EZSurfacing Tools" style="" />

### ShaderView:Shader Ball
Based on an editable Box inside the resources folder.
<img width="100%" src="docs/gafferShaderView2.png" alt="EZSurfacing Tools" style="" />

### ShaderView:Shader Teapot
<img width="100%" src="docs/gafferShaderTeapot.png" alt="EZSurfacing Tools" style="" />

### Viewport Diagnostic Patterns
<img width="100%" src="docs/gafferDiagnosticPatterns.png" alt="EZSurfacing Tools" style="" />

## Boxes 3d

#### LightCreator
<img width="50%" src="docs/LightCreator.png" alt="EZSurfacing Tools" style="" />

#### Attribute Sets
<img width="50%" src="docs/gafferSets.png" alt="EZSurfacing Tools" style="" />

### LDTRenderLayer
<img width="100%" src="docs/LDTRenderLayer.png" alt="EZSurfacing Tools" style="" />
<img width="100%" src="docs/LDTRenderLayer2.png" alt="EZSurfacing Tools" style="" />

### contextEnabled Editscope and Box
Contents will only be enabled when in the given context. Both Editscope and Box based.
The EditScope based contains Edit TweaksNodes ready to use.

<img width="50%" src="docs/contextEnabled.png" alt="EZSurfacing Tools" style="" />

### LightsMuteSolo
Mutes/Solo lights, using intensity or prune.

<img width="50%" src="docs/LightsMuteSolo.png" alt="EZSurfacing Tools" style="" />

### Center To Origin
Centers the given objects to the origin.

<img width="50%" src="docs/CenterToOrigin.png" alt="EZSurfacing Tools" style="" />

### UvSizeMultipler
Scales the objects UVs. Useful for the ShaderBall scene, where you want to scale the uvs
for visualization instead of modifying the material tiling.

### Inspection Camera
Inspection camera drop in.

<img width="50%" src="docs/InpectionCamera.png" alt="EZSurfacing Tools" style="" />

## Boxes 2d
### ShowMetadata
Search metadata keys with partial matching, and overlays on the image. For ie: /stats/geo will display all /arnold/stats/geo..., samples will display all keys that contain the word samples. Leave a blank field, and it will display all available keywords   
<img width="70%" src="docs/gafferLDTShowMetadataKeys.png" alt="EZSurfacing Tools" style="" />
<img width="100%" src="docs/gafferLDTShowMetadata.png" alt="EZSurfacing Tools" style="" />