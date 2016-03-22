bl_info = {
    "name": "Cursor Array",
    "category": "Object",
}

import bpy
from bpy import *


class ObjectCursorArray(bpy.types.Operator):
    """Object Cursor Array"""
    bl_idname = "object.cursor_array"
    bl_label = "Cursor Array"
    bl_options = {'REGISTER', 'UNDO'}
    
    scn = context.window_manager
    #total = bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)
    total = bpy.context.window_manager.num

    def execute(self, context):
        scene = context.scene
        cursor = scene.cursor_location
        obj = scene.objects.active

        for i in range(self.total):
            obj_new = obj.copy()
            scene.objects.link(obj_new)

            factor = i / self.total
            obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))

        return {'FINISHED'}
    
    
class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        scn = context.window_manager
        
        layout = self.layout

        obj = context.object
        
        row = layout.row()
        row.prop(scn, "num")

        row = layout.row()
        row.operator("object.cursor_array")



def menu_func(self, context):
    self.layout.operator(ObjectCursorArray.bl_idname)




def register():
    bpy.utils.register_class(ObjectCursorArray)
    bpy.utils.register_class(HelloWorldPanel)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
    
        
        

   

def unregister():
  

    bpy.utils.unregister_class(ObjectCursorArray)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    bpy.utils.unregister_class(HelloWorldPanel)

if __name__ == "__main__":
    #Some Integer property
    bpy.types.WindowManager.num = bpy.props.IntProperty(
    name="I Am An Input Button",
    description = "Enter Some Value here you'd like to be stored",
    default = 512, 
    min = 1,
    )

    register()