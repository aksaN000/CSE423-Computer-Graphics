'''OpenGL extension NV.shading_rate_image

This module customises the behaviour of the 
OpenGL.raw.GLES2.NV.shading_rate_image to provide a more 
Python-friendly API

Overview (from the spec)
	
	By default, OpenGL runs a fragment shader once for each pixel covered by a
	primitive being rasterized.  When using multisampling, the outputs of that
	fragment shader are broadcast to each covered sample of the fragment's
	pixel.  When using multisampling, applications can also request that the
	fragment shader be run once per color sample (when using the "sample"
	qualifier on one or more active fragment shader inputs), or run a fixed
	number of times per pixel using SAMPLE_SHADING enable and the
	MinSampleShading frequency value.  In all of these approaches, the number
	of fragment shader invocations per pixel is fixed, based on API state.
	
	This extension allows applications to bind and enable a shading rate image
	that can be used to vary the number of fragment shader invocations across
	the framebuffer.  This can be useful for applications like eye tracking
	for virtual reality, where the portion of the framebuffer that the user is
	looking at directly can be processed at high frequency, while distant
	corners of the image can be processed at lower frequency.  The shading
	rate image is an immutable-format two-dimensional or two-dimensional array
	texture that uses a format of R8UI.  Each texel represents a fixed-size
	rectangle in the framebuffer, covering 16x16 pixels in the initial
	implementation of this extension.  When rasterizing a primitive covering
	one of these rectangles, the OpenGL implementation reads the texel in the
	bound shading rate image and looks up the fetched value in a palette of
	shading rates.  The shading rate used can vary from (finest) 16 fragment
	shader invocations per pixel to (coarsest) one fragment shader invocation
	for each 4x4 block of pixels.
	
	When this extension is advertised by an OpenGL implementation, the
	implementation must also support the GLSL extension
	"GL_NV_shading_rate_image" (documented separately), which provides new
	built-in variables that allow fragment shaders to determine the effective
	shading rate used for each fragment.  Additionally, the GLSL extension also
	provides new layout qualifiers allowing the interlock functionality provided
	by ARB_fragment_shader_interlock to guarantee mutual exclusion across an
	entire fragment when the shading rate specifies multiple pixels per fragment
	shader invocation.
	
	Note that this extension requires the use of a framebuffer object; the
	shading rate image and related state are ignored when rendering to the
	default framebuffer.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/shading_rate_image.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.NV.shading_rate_image import *
from OpenGL.raw.GLES2.NV.shading_rate_image import _EXTENSION_NAME

def glInitShadingRateImageNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

glGetShadingRateImagePaletteNV=wrapper.wrapper(glGetShadingRateImagePaletteNV).setInputArraySize(
    'rate', 1
)
glGetShadingRateSampleLocationivNV=wrapper.wrapper(glGetShadingRateSampleLocationivNV).setInputArraySize(
    'location', 3
)
# INPUT glShadingRateImagePaletteNV.rates size not checked against count
glShadingRateImagePaletteNV=wrapper.wrapper(glShadingRateImagePaletteNV).setInputArraySize(
    'rates', None
)
# INPUT glShadingRateSampleOrderCustomNV.locations size not checked against 'rate,samples'
glShadingRateSampleOrderCustomNV=wrapper.wrapper(glShadingRateSampleOrderCustomNV).setInputArraySize(
    'locations', None
)
### END AUTOGENERATED SECTION