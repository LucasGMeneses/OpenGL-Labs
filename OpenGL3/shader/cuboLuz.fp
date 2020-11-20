#version 130
uniform vec3 objectColor;
uniform vec3 lightColor;
uniform vec3 lightPos;
uniform vec3 viewPos;

in vec3 normal;
in vec3 fPos;

out vec4 fcolor;

void main(){
  // luz ambiente
  float ambientStrength = 0.1;
  vec3 ambient = ambientStrength * lightColor;
  
  
  // luz difusa
  float difuseStregth = 0.2;
  vec3 norm = normalize(normal);
  vec3 lightDir = normalize(lightPos-fPos);
  float diff = max(dot(norm,lightDir),0.0);
  vec3 difuse = diff * lightColor * difuseStregth;
  
  // luz especular
  float specularStregth = 0.4;
  vec3 viewDir = (viewPos - fPos);
  vec3 reflectDir = reflect(-lightDir, norm);
  float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
  vec3 specular = specularStregth * spec * lightColor;

  vec3 result = (ambient + difuse + specular) * objectColor;
  fcolor = vec4(result, 1.0);
}
