vertex_shader = """
#version 330
layout (location = 0) in vec4 position;
layout (location = 1) in vec4 normal;
layout (location = 2) in vec2 texcoords;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

uniform vec4 color;
uniform vec4 light;

out vec4 vertexColor;
out vec2 vertexTexcoords;
out vec4 fnormal;
out float fintensity;
out vec4 v3Position;

void main()
{
    float intensity = dot(model * normal, normalize(light - position));
    fintensity = intensity;
    fnormal=normal;
    v3Position = position;
    gl_Position = projection * view * model * position;
    vertexColor = color * intensity;
    vertexTexcoords = texcoords;
}
"""
fragment_shader = """
#version 330
layout (location = 0) out vec4 newColor;
in vec4 vertexColor;
in vec2 vertexTexcoords;
uniform sampler2D tex;

void main()
{
    newColor =  vertexColor * texture(tex, vertexTexcoords);
}
"""

termic_vision = """
#version 330
layout (location = 0) out vec4 newColor;
precision highp float;
in vec4 fnormal;
uniform float timer;

void main()
{
  float theta = timer/50;
  
  vec4 first_directional = vec4(cos(theta),0,0, 0.0); 
  vec4 second_directional = vec4(0,cos(theta),0, 0.0);
  
  float diffuse_1 = pow(dot(fnormal,first_directional),1.0);
  float diffuse_2 = pow(dot(fnormal,second_directional),1.0);
  
  vec4 color_1 = diffuse_1 * vec4(1,0,0,0.0);
  vec4 color_2 = diffuse_2 * vec4(0,1,0, 0.0);
  
  newColor = vec4(color_1 + color_2);
}
"""

all_colors_shader = """
#version 330
layout (location = 0) out vec4 newColor;
precision highp float;

in float intensity;
in vec4 fnormal;

void main()
{
	newColor = vec4(fnormal);
}
"""

expand_shader = """
#version 330
layout (location = 0) in vec4 position;
layout (location = 1) in vec4 normal;
layout (location = 2) in vec2 texcoords;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

uniform vec4 color;
uniform vec4 light;
uniform float ratio;

out vec4 vertexColor;
out vec2 vertexTexcoords;
out vec4 fnormal;

void main()
{
    vec4 newPos= (position + (model * normal) * ratio/50);
    newPos = newPos/100;
    float intensity = dot(model * normal, normalize(light - position));
    fnormal=normal;
    gl_Position = projection * view * model * newPos;
    vertexColor = color * intensity;
    vertexTexcoords = texcoords;
}
"""