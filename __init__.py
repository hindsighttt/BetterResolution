import bpy

bl_info ={
    "name": "Better Resolution",
    "description": "Allows the user to set the resolution in millimeters",
    "author": "Hindsight",
    "version": (1,0,0),
    "blender": (3, 0, 0),
    "location": "Output Properties -> Better Resolution",
    "category": "User Interface"
}

default_x = 297
default_y = 210
default_dpi = 300

def slider_update_width(self, context):
    print("DEBUG: " +"Width in mm value changed to:", self['width_in_mm'])

    dpi_value = bpy.context.scene.dpi

    px_width = convert_mm_px(self['width_in_mm'], dpi_value)
    bpy.context.scene.render.resolution_x = px_width

def slider_update_height(self, context):
    print("DEBUG: " + "Height in mm value changed to:", self['height_in_mm'])

    dpi_value = bpy.context.scene.dpi

    px_height = convert_mm_px(self['height_in_mm'], dpi_value)
    bpy.context.scene.render.resolution_y = px_height

def slider_update_dpi(self, context):
    print("DEBUG: " +"DPI value changed to:", self['dpi'])
    slider_update_height(self,context)
    slider_update_width(self, context)

bpy.types.Scene.width_in_mm = bpy.props.FloatProperty(
    name = "Width in mm",
    description = "Width in millimeters",
    default = default_x,
    min = 0.0,
    step = 1,
    update = slider_update_width
)

bpy.types.Scene.height_in_mm = bpy.props.FloatProperty(
    name = "Height in mm",
    description = "Height in millimeters",
    default = default_y,
    min = 0.0,
    step = 1,
    update = slider_update_height
)

bpy.types.Scene.dpi = bpy.props.FloatProperty(
    name = "DPI",
    description = "Dots Per Inch",
    default = 300.0,
    min = 1.0,
    step = 1,
    update = slider_update_dpi
)

class BetterResolutionPanel(bpy.types.Panel):
    bl_label = "Better Resolution"
    bl_idname = "OUTPUT_PT_better_resolution"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.prop(context.scene, "width_in_mm")
        layout.prop(context.scene, "height_in_mm")
        layout.prop(context.scene, "dpi")

def convert_mm_px(mm, dpi):
    return int((mm * dpi) / 25.4)

def register():
    bpy.utils.register_class(BetterResolutionPanel)

def unregister():
    bpy.utils.unregister_class(BetterResolutionPanel)
    del bpy.types.Scene.width_in_mm
    del bpy.types.Scene.height_in_mm
    del bpy.types.Scene.dpi

if __name__ == "__main__":
    register()
