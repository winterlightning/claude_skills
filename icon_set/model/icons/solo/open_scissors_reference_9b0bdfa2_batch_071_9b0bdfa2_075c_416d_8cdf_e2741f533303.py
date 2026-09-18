"""12-pair-of-open-scissors--9b0bdfa2-075c-416d-8cdf-e2741f533303
Plan: Mirrored circular grips and two straight blades at a central pivot. Extremes (6,6)-(42,42).
Construction: Lucide scissors: circular grips joined to crossed blade strokes.
Reduction: Blade double outlines and pivot hole removed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b0bdfa2-075c-416d-8cdf-e2741f533303'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/trim_9b0bdfa2-075c-416d-8cdf-e2741f533303.svg'
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
    _path(icon,name,(x-r,y),[((x,y-r),r,r,True),((x+r,y),r,r,True),((x,y+r),r,r,True),((x-r,y),r,r,True)],True)


class Batch071Icon12(Solo48):
    icon_id = 'open-scissors-reference-9b0bdfa2-batch-071'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('open', 'scissors', 'reference', '9b0bdfa2')

    def build(self):

        for i,x in enumerate((13,35)):
            _circle(self,f'grip-{i}',x,35,7)
        self.add_polyline('blade-left',(10,6),(24,24),(35,28))
        self.add_polyline('blade-right',(38,6),(24,24),(13,28))
        self.relate('connect','blade-left','blade-right')
        self.relate('connect','blade-left','grip-1'); self.relate('connect','blade-right','grip-0')
