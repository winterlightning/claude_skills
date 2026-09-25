"""09-open-storage-trunk--278f1b86-a035-4a00-8662-1e6773fedd33
Plan: Raised back lid and perspective front/right faces with common hinge nodes. Extremes (4,8)-(44,40).
Construction: Lucide box: perspective edges meeting at shared nodes.
Reduction: Right interior wall removed; perspective front edge lowered to preserve 8-unit parallel spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '278f1b86-a035-4a00-8662-1e6773fedd33'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/trunk_278f1b86-a035-4a00-8662-1e6773fedd33.svg'
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


class Batch071Icon09(Solo48):
    icon_id = 'open-storage-trunk-batch-071'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('open', 'storage', 'trunk')

    def build(self):

        self.add_polyline('lid',(4,22),(12,8),(44,8),(36,22),(4,22))
        self.add_polyline('box',(4,22),(4,36),(14,40),(44,40),(44,30),(36,22))
        self.add_polyline('front',(4,22),(14,30),(44,30))
        self.add_line('corner',(14,30),(14,40))
        self.relate('connect','lid','box'); self.relate('connect','lid','front')
        self.relate('connect','box','front'); self.relate('connect','box','corner'); self.relate('connect','front','corner')
