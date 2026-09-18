"""15-professional-chef-hat--7fe48e3b-7cda-4409-89b9-f168cc621d06
Plan: Shared x=24 reflection constructs three circular crown lobes and a straight cuff. Centerline extremes (6,6)-(42,42).
Construction: Lucide chef-hat: lobed crown and straight cuff.
Reduction: No extra pleats.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fe48e3b-7cda-4409-89b9-f168cc621d06'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/toque_7fe48e3b-7cda-4409-89b9-f168cc621d06.svg'
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



class Batch071Icon15(Solo48):
    icon_id = 'chef-hat-batch-071'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('chef', 'hat')

    def build(self):
        _symmetric(self,'outline',(24,6),[((16,14),8,8,False),((14,14),),((6,22),8,8,False),((14,30),8,8,False),((14,34),),((14,42),),((24,42),)])
        self.add_line('cuff',(14,34),(34,34));self.relate('connect','cuff','outline')
