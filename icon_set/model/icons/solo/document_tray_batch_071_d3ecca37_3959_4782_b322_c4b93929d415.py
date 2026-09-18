"""03-inbox-document-tray--d3ecca37-3959-4782-b322-c4b93929d415
Plan: Symmetric perspective tray with scooped front. Extremes (4,8)-(44,40).
Construction: Lucide inbox: sloping back and continuous scooped front wall.
Reduction: No identifying features omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3ecca37-3959-4782-b322-c4b93929d415'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tray_d3ecca37-3959-4782-b322-c4b93929d415.svg'
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


class Batch071Icon03(Solo48):
    icon_id = 'document-tray-batch-071'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('document', 'tray')

    def build(self):

        self.add_polyline('back',(4,24),(12,8),(36,8),(44,24))
        _path(self,'front',(4,24),[((12,24),),((16,28),4,4,False),((32,28),),((36,24),4,4,False),((44,24),),((44,36),),((40,40),4,4,True),((8,40),),((4,36),4,4,True),((4,24),)],True)
        self.relate('connect','back','front')
