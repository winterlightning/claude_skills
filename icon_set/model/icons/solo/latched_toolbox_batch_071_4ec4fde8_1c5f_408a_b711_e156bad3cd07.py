"""14-portable-toolbox-with-handle--4ec4fde8-1c5f-408a-b711-e156bad3cd07
Plan: Toolbox rounded box, integral raised handle, lid seam and central latch. Extremes (4,8)-(44,40).
Construction: Lucide briefcase-business: raised handle and rounded enclosure.
Reduction: Latch reduced to a single stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ec4fde8-1c5f-408a-b711-e156bad3cd07'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tool chest_4ec4fde8-1c5f-408a-b711-e156bad3cd07.svg'
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


class Batch071Icon14(Solo48):
    icon_id = 'latched-toolbox-batch-071'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('latched', 'toolbox')

    def build(self):

        _path(self,'box',(8,16),[((16,16),),((32,16),),((40,16),),((44,20),4,4,True),((44,26),),((44,36),),((40,40),4,4,True),((8,40),),((4,36),4,4,True),((4,26),),((4,20),),((8,16),4,4,True)],True)
        _path(self,'handle',(16,16),[((16,12),),((20,8),4,4,True),((28,8),),((32,12),4,4,True),((32,16),)])
        self.relate('connect','box','handle')
        self.add_polyline('seam',(4,26),(24,26),(44,26)); self.relate('connect','box','seam')
        self.add_line('latch',(24,26),(24,32)); self.relate('connect','seam','latch')
