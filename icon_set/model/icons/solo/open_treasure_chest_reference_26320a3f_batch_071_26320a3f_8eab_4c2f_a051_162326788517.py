"""10-open-treasure-chest-with-sparkling-diamond--26320a3f-8eab-4c2f-a051-162326788517
Plan: Raised rounded lid on the left, a wide rectangular chest front, an outlined diamond at its rim and a small sparkle at upper right. Centerline extremes (6,6)-(42,42).
Construction: Lucide box: connected chest edges.
Reduction: Diamond facets and the second sparkle omitted; widened lid interior preserves an open region.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26320a3f-8eab-4c2f-a051-162326788517'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/treasure_26320a3f-8eab-4c2f-a051-162326788517.svg'
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


class Batch071Icon10(Solo48):
    icon_id = 'open-treasure-chest-reference-26320a3f-batch-071'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('open', 'treasure', 'chest', 'reference', '26320a3f')

    def build(self):
        _path(self,'lid',(6,30),[((6,18),),((18,6),12,12,True),((26,6),),((6,30),)],True)
        self.add_polyline('chest',(6,30),(6,42),(42,42),(42,30),(32,30),(6,30))
        self.add_polyline('diamond',(32,30),(24,22),(32,14),(40,22),(32,30))
        self.relate('connect','lid','chest'); self.relate('connect','diamond','chest')
        self.add_polyline('sparkle-h',(38,8),(40,8),(42,8))
        self.add_polyline('sparkle-v',(40,6),(40,8),(40,10))
        self.relate('connect','sparkle-h','sparkle-v')
