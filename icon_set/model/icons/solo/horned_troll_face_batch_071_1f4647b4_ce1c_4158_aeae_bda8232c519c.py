"""01-horned-troll-face--1f4647b4-ce1c-4158-aeae-bda8232c519c
Plan: One mirrored horn/ear/face silhouette generated around x=24, with curved horn flanks, a circular nose and horizontal mouth. Centerline extremes (6,6)-(42,42).
Construction: No useful Lucide match found.
Reduction: Broad ears merge into the horn/cheek silhouette; brow strokes share the bulbous nose.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f4647b4-ce1c-4158-aeae-bda8232c519c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/troll_1f4647b4-ce1c-4158-aeae-bda8232c519c.svg'
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



class Batch071Icon01(Solo48):
    icon_id = 'horned-troll-face-batch-071'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('horned', 'troll', 'face')

    def build(self):
        _symmetric(self,'outline',(24,12),[((14,12),),((8,6),),((6,18),2,12,False),((10,26),4,8,False),((10,34),),((18,42),8,8,False),((24,42),)])
        axis, nose_radius, brow_half, mouth_half = 24, 3, 5, 4
        _path(self,'nose',(axis-brow_half,21),[((axis-nose_radius,21),),((axis+nose_radius,21),nose_radius,nose_radius,False),((axis+brow_half,21),)])
        self.add_line('mouth',(axis-mouth_half,33),(axis+mouth_half,33))
