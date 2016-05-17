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

from bpy.props import (
	BoolProperty,
	StringProperty,
	IntProperty,
)

from bpy.types import (
	Operator,
)

class POSE_OT_jueg_changevisibility(Operator):
	"""Change visibility"""
	bl_idname = "pose.jueg_change_visibility"
	bl_label = "Change visibility"
	
	
	ops_id		 = StringProperty()
	index			= IntProperty()
	
	@classmethod
	def poll(self, context):
		return (context.object and
				context.object.type == 'ARMATURE' and
				context.mode == 'POSE')
				
	def execute(self, context):
		armature = context.object
		
		#retrieve on_off
		on_off = False
		found = False
		for ops in armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].on_off:
			if ops.id == self.ops_id:
				on_off = ops.on_off
				found = True
				

		if found == False:
			print("error")
		
		current_selection = armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].current_selection
		if current_selection == False:
			bones = armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].bone_ids
		else:
			bones = []
			for bone in armature.pose.bones:
				if bone.bone.select == True:
					bones.append(bone)
		
		to_deleted = []
		idx = -1
		for bone in bones:
			idx = idx + 1
			if bone.name not in armature.data.bones:
				to_deleted.append(idx)
				continue
################################## Insert your code here ##########################
			if on_off == True:
				armature.data.bones[bone.name].hide = True
			else:
				armature.data.bones[bone.name].hide = False
###################################################################################	
		if len(to_deleted) > 0:
			for i in to_deleted:
				armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].bone_ids.remove(i)

		
		for ops in armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].on_off:
			if ops.id == self.ops_id:
				ops.on_off = not ops.on_off
		
		return {'FINISHED'}
	
class POSE_OT_jueg_addtoselection(Operator):
	"""Add to selection"""
	bl_idname = "pose.jueg_addtoselection"
	bl_label = "Add to selection"
	
	
	ops_id		 = StringProperty()
	index			= IntProperty()
	
	@classmethod
	def poll(self, context):
		return (context.object and
				context.object.type == 'ARMATURE' and
				context.mode == 'POSE')
				
	def execute(self, context):
		armature = context.object

		
		#retrieve on_off
		on_off = False
		found = False
		for ops in armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].on_off:
			if ops.id == self.ops_id:
				on_off = ops.on_off
				found = True
		
		if found == False:
			print("error")
		
		current_selection = armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].current_selection
		if current_selection == False:
			bones = armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].bone_ids
		else:
			bones = []
			for bone in armature.pose.bones:
				if bone.bone.select == True:
					bones.append(bone)		
		
		to_deleted = []
		idx = -1
		for bone in bones:
			idx = idx + 1
			if bone.name not in armature.data.bones:
				to_deleted.append(idx)
				continue
################################## Insert your code here ##########################
			if on_off == True:
				armature.data.bones[bone.name].select = True
			else:
				armature.data.bones[bone.name].select = True
###################################################################################			
		if len(to_deleted) > 0:
			for i in to_deleted:
				armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].bone_ids.remove(i)

		for ops in armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].on_off:
			if ops.id == self.ops_id:
				ops.on_off = not ops.on_off
		
		return {'FINISHED'}
	
	
class POSE_OT_jueg_selectonly(Operator):
	"""Toggle selected bones"""
	bl_idname = "pose.jueg_selectonly"
	bl_label = "Toggle selection"
	
	
	ops_id		 = StringProperty()
	index			= IntProperty()
	
	@classmethod
	def poll(self, context):
		return (context.object and
				context.object.type == 'ARMATURE' and
				context.mode == 'POSE')
				
	def execute(self, context):
		armature = context.object

		
		#retrieve on_off
		on_off = False
		found = False
		for ops in armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].on_off:
			if ops.id == self.ops_id:
				on_off = ops.on_off
				found = True
		
		if found == False:
			print("error")
		
		current_selection = armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].current_selection
		if current_selection == False:
			bones = armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].bone_ids
		else:
			bones = []
			for bone in armature.pose.bones:
				if bone.bone.select == True:
					bones.append(bone)		
		
#############
		for bone in armature.pose.bones:
			bone.bone.select = False
#############		
		to_deleted = []
		idx = -1
		for bone in bones:
			idx = idx + 1
			if bone.name not in armature.data.bones:
				to_deleted.append(idx)
				continue
################################## Insert your code here ##########################
			if on_off == True:
				armature.data.bones[bone.name].select = True
			else:
				armature.data.bones[bone.name].select = True
###################################################################################		
		if len(to_deleted) > 0:
			for i in to_deleted:
				armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].bone_ids.remove(i)
	
		for ops in armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].on_off:
			if ops.id == self.ops_id:
				ops.on_off = not ops.on_off
		
		return {'FINISHED'}
	
		
	
	
class POSE_OT_jueg_bonemute(Operator):
	"""Mute action of bones"""
	bl_idname = "pose.jueg_bonemute"
	bl_label = "Mute bones"
	
	
	ops_id		 = StringProperty()
	index			= IntProperty()
	
	@classmethod
	def poll(self, context):
		return (context.object and
				context.object.type == 'ARMATURE' and
				context.mode == 'POSE')
				
	def execute(self, context):
		armature = context.object
		
		#retrieve on_off
		on_off = False
		found = False
		for ops in armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].on_off:
			if ops.id == self.ops_id:
				on_off = ops.on_off
				found = True
		
		if found == False:
			print("error")
		
		current_selection = armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].current_selection
		if current_selection == False:
			bones = armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].bone_ids
		else:
			bones = []
			for bone in armature.pose.bones:
				if bone.bone.select == True:
					bones.append(bone)
					
		to_deleted = []
		idx = -1
		for bone in bones:
			idx = idx + 1
			if bone.name not in armature.data.bones:
				to_deleted.append(idx)
				continue
################################## Insert your code here ##########################
			if on_off == True:
				if armature.animation_data and bone.name in armature.animation_data.action.groups:
					for channel in armature.animation_data.action.groups[bone.name].channels:
						channel.mute = True
				if armature.animation_data:		
					for fc in armature.animation_data.action.fcurves:
						if not fc.group:
							if fc.data_path.startswith("pose.bones"):
								tmp = fc.data_path.split("[", maxsplit=1)[1].split("]", maxsplit=1)
								bone_name = tmp[0][1:-1]
								if bone.name == bone_name:
									fc.mute = True
			else:
				if armature.animation_data and bone.name in armature.animation_data.action.groups:
					for channel in armature.animation_data.action.groups[bone.name].channels:
						channel.mute = False
				if armature.animation_data:
					for fc in armature.animation_data.action.fcurves:
						if not fc.group:
							if fc.data_path.startswith("pose.bones"):
								tmp = fc.data_path.split("[", maxsplit=1)[1].split("]", maxsplit=1)
								bone_name = tmp[0][1:-1]
								if bone.name == bone_name:
									fc.mute = False
###################################################################################		
		if len(to_deleted) > 0:
			for i in to_deleted:
				armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].bone_ids.remove(i)
	
		for ops in armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].on_off:
			if ops.id == self.ops_id:
				ops.on_off = not ops.on_off
		
		return {'FINISHED'}

class POSE_OT_jueg_restrict_select(Operator):
	"""Restrict/Allow selection"""
	bl_idname = "pose.jueg_restrict_select"
	bl_label = "Restrict Select"
	
	
	ops_id		 = StringProperty()
	index			= IntProperty()
	
	@classmethod
	def poll(self, context):
		return (context.object and
				context.object.type == 'ARMATURE' and
				context.mode == 'POSE')
				
	def execute(self, context):
		armature = context.object
		
		#retrieve on_off
		on_off = False
		found = False
		for ops in armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].on_off:
			if ops.id == self.ops_id:
				on_off = ops.on_off
				found = True
		
		if found == False:
			print("error")
		
		#check if this is a classic group or current selection
		current_selection = armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].current_selection
		if current_selection == False:
			#retrieve bones from group
			bones = armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].bone_ids
		else:
			#retrieve bones from current selection
			bones = []
			for bone in armature.pose.bones:
				if bone.bone.select == True:
					bones.append(bone)		
		
		
		to_delete = []
		idx = -1
		for bone in bones:
			idx = idx + 1
			if bone.name not in armature.data.bones: #If bone no more exists
				to_delete.append(idx)
				continue
			armature.pose.bones[bone.name].bone.hide_select = on_off
			
			
		
		#delete bones if any
		if len(to_delete) > 0:
			for i in to_delete:
				armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].bone_ids.remove(i)
		 
		 #switch on/off
		for ops in armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].on_off:
			if ops.id == self.ops_id:
				ops.on_off = not ops.on_off
		
		return {'FINISHED'}
	
def register():
	bpy.utils.register_class(POSE_OT_jueg_changevisibility)
	bpy.utils.register_class(POSE_OT_jueg_addtoselection)
	bpy.utils.register_class(POSE_OT_jueg_selectonly)
	bpy.utils.register_class(POSE_OT_jueg_bonemute)
	bpy.utils.register_class(POSE_OT_jueg_restrict_select)
	
	
def unregister():
	bpy.utils.unregister_class(POSE_OT_jueg_changevisibility)
	bpy.utils.unregister_class(POSE_OT_jueg_addtoselection)
	bpy.utils.unregister_class(POSE_OT_jueg_selectonly)
	bpy.utils.unregister_class(POSE_OT_jueg_bonemute)
	bpy.utils.unregister_class(POSE_OT_jueg_restrict_select)
	
	
	
if __name__ == "__main__":
	register()
