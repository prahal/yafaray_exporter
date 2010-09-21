import bpy
from bpy.props import *

bpy.types.Scene.AA_min_samples = bpy.props.IntProperty(attr="AA_min_samples",
		default = 1)
bpy.types.Scene.AA_inc_samples = bpy.props.IntProperty(attr="AA_inc_samples",
		default = 1)
bpy.types.Scene.AA_passes = bpy.props.IntProperty(attr="AA_passes",
		default = 1)
bpy.types.Scene.AA_threshold = bpy.props.FloatProperty(attr="AA_threshold",
		default = 0.05, precision = 4)
bpy.types.Scene.AA_pixelwidth = bpy.props.FloatProperty(attr="AA_pixelwidth",
		default = 1.5)
bpy.types.Scene.AA_filter_type = bpy.props.EnumProperty(attr="AA_filter_type",
	items = (
		("AA Filter Type","AA Filter Type",""),
		("Box","Box",""),
		("Mitchell","Mitchell",""),
		("Gauss","Gauss",""),
),default="Gauss")


class YAF_PT_AA_settings(bpy.types.Panel):

	bl_label = 'AA Settings'
	bl_space_type = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context = 'render'
	COMPAT_ENGINES =['YAFA_RENDER']

	@classmethod
	def poll(self, context):

		engine = context.scene.render.engine
		return (True  and  (engine in self.COMPAT_ENGINES) ) 


	def draw(self, context):
		
		self.list = [1,2,4,5]
		layout = self.layout
		split = layout.split()
		col = split.column()

		col.prop(context.scene,"AA_min_samples", text= "AA Samples")

		col.prop(context.scene,"AA_passes", text= "AA Passes")
		if context.scene.AA_passes > 1:
			col.prop(context.scene,"AA_inc_samples", text= "AA Inc. Samples")
		
		col = split.column()
		col.prop(context.scene,"AA_threshold", text= "AA Threshold")
		col.prop(context.scene,"AA_pixelwidth", text= "AA Pixelwidth")
		col.prop(context.scene,"AA_filter_type", text= "AA Filter Type")




classes = [
	YAF_PT_AA_settings,
]

def register():
	pass

def unregister():
	pass

if __name__ == "__main__":
	register()
