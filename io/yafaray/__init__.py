import bpy
from yafaray import yaf_export
#from yafaray import yaf_properties
from yafaray import yaf_object

# register engine and panels
classes = [
    yaf_export.YafaRayRenderEngine,
    #yaf_export.YafaRayCameraPoll,
    #yaf_export.YafaRayCameraButtonsPanel
    ]

def register():
    pass

def unregister():    
    pass

#yaf_properties.yaf_register_camera_types()
