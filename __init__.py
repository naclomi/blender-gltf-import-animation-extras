bl_info = {
        "name": "glTF custom animation property importer",
        "description": "Add support for importing custom properties from glTF animation extras",
        "author": "NL Alterman",
        "version": (1, 0),
        "blender": (3, 1, 0),
        "location": "",
        "warning": "", # used for warning icon and text in add-ons panel
        "wiki_url": "",
        "tracker_url": "https://github.com/naclomi/blender-gltf-import-animation-extras/issues",
        "support": "COMMUNITY",
        "category": "Import-Export"
        }

import bpy

from io_scene_gltf2.blender.com.gltf2_blender_extras import set_extras

if locals().get('loaded'):
    loaded = False
    from importlib import reload
    from sys import modules

    modules[__name__] = reload(modules[__name__])
    for name, module in modules.items():
        if name.startswith(f"{__package__}."):
            globals()[name] = reload(module)
    del reload, modules

class glTF2ImportUserExtension:
    def __init__(self):
        pass

    def gather_import_animation_after_hook(self, anim_idx, track_name, gltf):
        extras = gltf.data.animations[anim_idx].extras
        for action in gltf.action_cache.values():
            set_extras(action, extras)

def register():
    pass

def unregister():
    pass

if __name__ == '__main__':
    register()

