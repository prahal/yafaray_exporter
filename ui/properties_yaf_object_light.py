import bpy
from bpy.props import *

bpy.types.Object.ml_enable = bpy.props.BoolProperty(attr="ml_enable")
bpy.types.Object.ml_color = bpy.props.FloatVectorProperty(attr="ml_color",description = "Color Settings", subtype = "COLOR", step = 1, precision = 2, min = 0.0, max = 1.0, soft_min = 0.0, soft_max = 1.0)
bpy.types.Object.ml_power = bpy.props.FloatProperty(attr="ml_power")
bpy.types.Object.ml_samples = bpy.props.IntProperty(attr="ml_samples")
bpy.types.Object.ml_double_sided = bpy.props.BoolProperty(attr="ml_double_sided")
bpy.types.Object.bgp_enable = bpy.props.BoolProperty(attr="bgp_enable")
bpy.types.Object.bgp_power = bpy.props.FloatProperty(attr="bgp_power")
bpy.types.Object.bgp_samples = bpy.props.IntProperty(attr="bgp_samples")
bpy.types.Object.bgp_with_caustic = bpy.props.BoolProperty(attr="bgp_with_caustic")
bpy.types.Object.bgp_with_diffuse = bpy.props.BoolProperty(attr="bgp_with_diffuse")
bpy.types.Object.bgp_photon_only = bpy.props.BoolProperty(attr="bgp_photon_only")
bpy.types.Object.vol_enable = bpy.props.BoolProperty(attr="vol_enable")
bpy.types.Object.vol_region = bpy.props.EnumProperty(attr="vol_region",
	items = (
		("Volume Region","Volume Region",""),
		("ExpDensity Volume","ExpDensity Volume",""),
		("Noise Volume","Noise Volume",""),
		("Uniform Volume","Uniform Volume",""),
		#("Grid Volume","Grid Volume",""),
		("Sky Volume","Sky Volume",""),
),default="Uniform Volume")
bpy.types.Object.vol_height = bpy.props.FloatProperty(attr="vol_height")
bpy.types.Object.vol_steepness = bpy.props.FloatProperty(attr="vol_steepness")
bpy.types.Object.vol_sharpness = bpy.props.FloatProperty(attr="vol_sharpness")
bpy.types.Object.vol_cover = bpy.props.FloatProperty(attr="vol_cover")
bpy.types.Object.vol_density = bpy.props.FloatProperty(attr="vol_density")
bpy.types.Object.vol_absorp = bpy.props.FloatProperty(attr="vol_absorp")
bpy.types.Object.vol_scatter = bpy.props.FloatProperty(attr="vol_scatter")
bpy.types.Object.vol_l_e = bpy.props.FloatProperty(attr="vol_l_e", default = 0.0, min = -1.0, max = 1.0, soft_min = -1.0, soft_max = 1.0)
bpy.types.Object.vol_g = bpy.props.FloatProperty(attr="vol_g", default = 0.0, min = 0.0, max = 1.0, soft_min = 0.0, soft_max = 1.0)

#volume Integrator
#EnumProperty(attr="v_int_type",
#	items = (
#		("Volume Integrator","Volume Integrator",""),
#		("None","None",""),
#		("Single Scatter","Single Scatter",""),
#		("Sky","Sky",""),
#),default="Sky")
#FloatProperty(attr="v_int_step_size")
#BoolProperty(attr="v_int_adaptive")
#BoolProperty(attr="v_int_optimize")
#IntProperty(attr="v_int_attgridres")
#FloatProperty(attr="v_int_scale")
#FloatProperty(attr="v_int_alpha")


class YAF_PT_object_light(bpy.types.Panel):

	bl_label = 'Object Light'
	bl_space_type = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context = 'object'
	COMPAT_ENGINES =['YAFA_RENDER']

	@classmethod
	def poll(self, context):

		engine = context.scene.render.engine

		import properties_object

		if (True  and  (engine in self.COMPAT_ENGINES) ) :
			try :
				properties_object.unregister()
			except: 
				pass
		else:
			try:
				properties_object.register()
			except: 
				pass
		return (context.object.type == 'MESH'  and  (engine in self.COMPAT_ENGINES) ) 


	def draw(self, context):

		layout = self.layout
		split = layout.split()
		col = split.column()

		col.prop(context.object,"ml_enable", text= "Enable Meshlight", toggle = True)

		if context.object.ml_enable:
			col.prop(context.object,"ml_color", text= "Meshlight Color")
			col.prop(context.object,"ml_power", text= "Power")
			col.prop(context.object,"ml_samples", text= "Samples")
			col.prop(context.object,"ml_double_sided", text= "Double Sided")


		col.prop(context.object,"bgp_enable", text= "Enable Bgportallight", toggle = True)

		if context.object.bgp_enable:
			col.prop(context.object,"bgp_power", text= "Power")
			col.prop(context.object,"bgp_samples", text= "Samples")
			col.prop(context.object,"bgp_with_caustic", text= "With Caustic")

			col.prop(context.object,"bgp_with_diffuse", text= "With Diffuse")

			col.prop(context.object,"bgp_photon_only", text= "Photons Only")


		col.prop(context.object,"vol_enable", text= "Enable Volume", toggle = True)

		if context.object.vol_enable:
			col.prop(context.object,"vol_region", text= "Volume Region")

			if context.object.vol_region == 'ExpDensity Volume':
				col.prop(context.object,"vol_height", text= "Height")
				col.prop(context.object,"vol_steepness", text= "Steepness")

			if context.object.vol_region == 'Noise Volume':
				col.prop(context.object,"vol_sharpness", text= "Sharpness")
				col.prop(context.object,"vol_cover", text= "Cover")
				col.prop(context.object,"vol_density", text= "Density")

			col.prop(context.object,"vol_absorp", text= "Absroption")
			col.prop(context.object,"vol_scatter", text= "Scatter")
			col.prop(context.object,"vol_g", text= "Phase Coefficient")
			col.prop(context.object,"vol_l_e", text= "Emitted Light")
		
		
		
		#col.prop(context.object,"v_int_type", text= "Volume Integrator")
		#
		#if context.object.v_int_type == 'None':
		#	col.prop(context.object,"v_int_step_size", text= "Step Size")
		#
		#if context.object.v_int_type == 'Single Scatter':
		#	col.prop(context.object,"v_int_adaptive", text= "Adaptive")
		#
		#	col.prop(context.object,"v_int_optimize", text= "Optimize")
		#
		#	col.prop(context.object,"v_int_attgridres", text= "Att. grid resolution")
		#
		#if context.object.v_int_type == 'Sky':
		#	col.prop(context.object,"v_int_scale", text= "Scale")
		#	col.prop(context.object,"v_int_alpha", text= "Alpha")




classes = [
	YAF_PT_object_light,
]

def register():
	pass

def unregister():
	pass

if __name__ == "__main__":
	register()
