"""
This script to convert form material to another based on cfg dictionary inside clarisse
"""
import os

import ix

disney_autodesk_standard = {
    "base_multiply": "base_weight",
    "base_color": "base_color",
    "metallic": "metalness",
    "normal_input": "normal_input",
    "specular": "specular_weight",
    "roughness": "specular_roughness",
    "transmission": "transmission_weight",
    "specular_color": "specular_color",
    "transmission_color": "transmission_color",
    "subsurface": "subsurface_weight",
    "subsurface_color": "subsurface_color",
    "subsurface_radius": "subsurface_radius",
    "clear_coat": "coat_weight",
    "sheen": "sheen_weight",
    "sheen_color": "sheen_color",
    "emission": "emission_weight",
    "emission_color": "emission_color",
    "opacity": "opacity",
}


def switch_mtls_connections(mtl_old, mtl_new, **kwargs):
    """
    TO switch the connection between two given materials
    """
    for attr_name in kwargs:
        tex_attr_old = mtl_old.get_attribute(attr_name)

        if not tex_attr_old:
            continue
        if not tex_attr_old.is_textured():
            continue

        connected_tex = tex_attr_old.get_texture()

        tex_attr_new = mtl_new.get_attribute(kwargs[attr_name])
        if not tex_attr_new:
            continue
        tex_attr_new.set_texture(connected_tex)


def replace_mtls():
    items = ix.selection
    for item in items:
        cntx = ix.cmds.CreateContext("ss_materials", "Global", os.path.dirname(str(item)))

        mtls_old_attr = item.attrs.materials

        for i in range(len(mtls_old_attr)):
            mtl_old = mtls_old_attr[i]
            mtl_name = os.path.basename(str(mtl_old))

            mtl_new = ix.cmds.CreateObject(mtl_name + "_ads", "MaterialPhysicalAutodeskStandardSurface", "Global", cntx)

            mtl_new.attrs.sidedness = "1"

            item.attrs.materials[i] = mtl_new

            switch_mtls_connections(mtl_old, mtl_new, **disney_autodesk_standard)


ix.begin_command_batch("Convert to Autodesk Standard Material")
replace_mtls()
ix.end_command_batch()
