##########################################################################################
#	GPL LICENSE:
#-------------------------
# This file is part of ExtraGroups.
#
#    ExtraGroups is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    ExtraGroups is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with ExtraGroups.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################################
#
#	Copyright 2016 Julien Duroure (contact@julienduroure.com)
#
##########################################################################################
import bpy
import bpy_extras
import json

class POSE_OT_jueg_export_to_file(bpy.types.Operator, bpy_extras.io_utils.ExportHelper):
    """Export to file"""
    bl_idname = "jueg.export_to_file"
    bl_label = "Export To File"

    filename_ext = ".txt"

    filter_glob = bpy.props.StringProperty(default="*.txt", options={'HIDDEN'}, maxlen=255,)


    def execute(self, context):
        armature = context.object
        data = {}
        data['Extragroups'] = []
        for grouptype in armature.jueg_grouptypelist:
            grouptype_ = {}
            grouptype_["name"] = grouptype.name
            grouptype_["groups"] = []
            for group in [group_it for group_it in grouptype.group_ids if group_it.current_selection == False]:
                group_ = {}
                group_["name"] = group.name
                group_["bones"] = []
                for bone in group.bone_ids:
                    group_["bones"].append(bone.name)
                grouptype_["groups"].append(group_)
            data['Extragroups'].append(grouptype_)

        f = open(self.filepath, 'w', encoding='utf-8')
        f.write(json.dumps(data))
        f.close()

        return {'FINISHED'}

def register():
	bpy.utils.register_class(POSE_OT_jueg_export_to_file)

def unregister():
	bpy.utils.unregister_class(POSE_OT_jueg_export_to_file)