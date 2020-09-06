import imath
import Gaffer
import GafferImage
import GafferScene
import GafferSceneUI
import functools
import inspect

print ("LDTGAFFER:startup:gui:viewer")

def __createLDTPatternShader2k() :
    pattern = GafferScene.SceneProcessor( "pattern" )

    pattern["shaderAssignment"] = GafferScene.ShaderAssignment( "TextureShaderAssignment" )
    pattern["texture"] = GafferScene.OpenGLShader( "Texture" )
    pattern["texture"].loadShader( "Texture" )
    pattern["texture"]["parameters"]["tint"].setValue( imath.Color4f( 1, 1, 1, 1 ) )
    pattern["texture"]["parameters"]["mult"].setValue( 1.0 )
    pattern["image"] = GafferImage.ImageReader( "ImageReader" )
    pattern["image"]["fileName"].setValue( '${LDTGAFFER}/resources/patterns/2048x2048_Texel_Density_Texture_1.png' )
    pattern["image"]["colorSpace"].setValue( 'ACES - ACEScg' )

    pattern["texture"]["parameters"]["texture"].setInput(pattern["image"]["out"])
    pattern["shaderAssignment"]["shader"].setInput(pattern["texture"]["out"])
    pattern["shaderAssignment"]["in"].setInput(pattern["in"])
    pattern["out"].setInput(pattern["shaderAssignment"]["out"])

    return pattern

GafferSceneUI.SceneView.registerShadingMode( "LDTGafferPattern2k", functools.partial( __createLDTPatternShader2k ) )

def __createLDTPatternShader4k() :
    pattern = GafferScene.SceneProcessor( "pattern" )

    pattern["shaderAssignment"] = GafferScene.ShaderAssignment( "TextureShaderAssignment" )
    pattern["texture"] = GafferScene.OpenGLShader( "Texture" )
    pattern["texture"].loadShader( "Texture" )
    pattern["texture"]["parameters"]["tint"].setValue( imath.Color4f( 1, 1, 1, 1 ) )
    pattern["texture"]["parameters"]["mult"].setValue( 1.0 )
    pattern["image"] = GafferImage.ImageReader( "ImageReader" )
    pattern["image"]["fileName"].setValue( '${LDTGAFFER}/resources/patterns/4096x4096_Texel_Density_Texture_1.png' )
    pattern["image"]["colorSpace"].setValue( 'ACES - ACEScg' )

    pattern["texture"]["parameters"]["texture"].setInput(pattern["image"]["out"])
    pattern["shaderAssignment"]["shader"].setInput(pattern["texture"]["out"])
    pattern["shaderAssignment"]["in"].setInput(pattern["in"])
    pattern["out"].setInput(pattern["shaderAssignment"]["out"])

    return pattern

GafferSceneUI.SceneView.registerShadingMode( "LDTGafferPattern4k", functools.partial( __createLDTPatternShader4k ) )


def __createPhongShader() :
    phong = GafferScene.SceneProcessor( "Phong" )
    phong["attributes"] = GafferScene.CustomAttributes()
    phong["attributes"]["in"].setInput( phong["in"] )
    phong["assignment"] = GafferScene.ShaderAssignment()
    phong["assignment"]["in"].setInput( phong["attributes"]["out"] )
    phong["shader"] = GafferScene.OpenGLShader( "phong" )
    phong["shader"]["name"].setValue( "phong" )
    phong["shader"]["type"].setValue( "gl:surface" )
    phong["shader"]["parameters"].addChild( Gaffer.StringPlug( "glFragmentSource", defaultValue = inspect.cleandoc(
        '''
        in vec3 fragmentN;
        in vec3 geometryP;
        vec3 ADSLightModel(in vec3 normal, in vec3 pos){
            vec3 lightPos = vec3(1.0, 0.5, 0.0);
            vec3 lightAmbient = vec3(0.3, 0.3, 0.3);
            vec3 lightDiffuse = vec3(1.0, 1.0, 1.0);
            vec3 lightSpecular = vec3(1.0, 1.0, 1.0);
            vec3 materialAmbient = vec3(0.9, 0.9, 0.9);
            vec3 materialDiffuse = vec3(0.5, 0.5, 0.6);
            vec3 materialSpecular = vec3(0.6, 0.6, 0.6);
            float materialShininess = 100.0;
            vec3 norm = normalize(normal);
            vec3 lightv = normalize(lightPos - pos);
            vec3 viewv = normalize(vec3(0.0) - pos);
            vec3 refl = reflect(vec3(0.0) - lightv, norm);
            vec3 ambient = materialAmbient * lightAmbient;
            vec3 diffuse = max(0.0, dot(lightv, norm)) * materialDiffuse * lightDiffuse;
            vec3 specular = vec3(0.0);
            if(dot(lightv, viewv) > 0.0)
            {
                specular = pow(max(0.0, dot(viewv, refl)), materialShininess)*materialSpecular*lightSpecular;
            }
            return clamp(ambient + diffuse + specular, 0.0, 1.0);
        }
        void main(){
            vec3 colour = ADSLightModel(fragmentN, geometryP);
            gl_FragColor = vec4(colour, 1.0);
        }
    '''
    ) ) )
    phong["shader"]["out"] = Gaffer.Plug()
    phong["assignment"]["shader"].setInput( phong["shader"]["out"] )
    phong["out"].setInput( phong["assignment"]["out"] )

    return phong

GafferSceneUI.SceneView.registerShadingMode( "Phong", functools.partial( __createPhongShader ) )