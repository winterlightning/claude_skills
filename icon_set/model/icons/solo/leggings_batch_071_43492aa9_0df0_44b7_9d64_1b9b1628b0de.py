"""13-pair-of-slim-leggings--43492aa9-0df0-44b7-9d64-1b9b1628b0de
Plan: Shared x=24 reflection constructs a straight waistband and two fitted legs around a widened central opening. Centerline extremes (10,4)-(38,44).
Construction: No useful Lucide match found.
Reduction: No stitching; crotch opening widened to preserve leg separation.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43492aa9-0df0-44b7-9d64-1b9b1628b0de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tights_43492aa9-0df0-44b7-9d64-1b9b1628b0de.svg'
AUTHOR = 'gpt-6'

def _path(icon, name, start, steps, closed=False):
    members=[]
    for i, step in enumerate(steps):
        end=step[0]; member=f'{name}-{i}'
        if len(step)==1: icon.add_line(member,start,end)
        else: icon.add_arc(member,start,end,radius_x=step[1],radius_y=step[2],sweep=step[3])
        members.append(member); start=end
    icon.add_contour(name,*members,closed=closed)


def _circle(icon,name,x,y,r):
    _path(icon,name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)

def _symmetric(icon, name, start, left_steps):
    # The left half owns every dimension. Reverse its reflection around x=24.
    axis_x = 24
    starts = [start] + [step[0] for step in left_steps[:-1]]
    right_steps = []
    for old_start, step in reversed(list(zip(starts, left_steps))):
        mirrored = (2*axis_x-old_start[0], old_start[1])
        right_steps.append((mirrored,) + step[1:])
    _path(icon,name,start,left_steps+right_steps,True)



class Batch071Icon13(Solo48):
    icon_id = 'leggings-batch-071'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('leggings',)

    def build(self):
        _symmetric(self,'outline',(24,4),[((10,4),),((10,12),),((12,44),),((20,44),),((20,23),),((24,23),)])
        self.add_line('waist',(10,12),(38,12))
        self.relate('connect','waist','outline')
