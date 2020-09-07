in vec3 fragmentN;
in vec3 geometryP;
in vec3 geometryCs;
uniform float transparency;

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
    if (geometryCs != vec3(0.0, 0.0, 0.0)){
        colour = colour * geometryCs;
        }
    gl_FragColor = vec4(colour, transparency);
}
