"""04-isometric-cube-shape--bb826ef1-d970-4a85-b905-bccf35abde80
Plan: Hexagonal cube outline split at its three visible edge junctions. Extremes (8,4)-(40,44).
Construction: Lucide box: three edge branches at a common front corner.
Reduction: No identifying features omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb826ef1-d970-4a85-b905-bccf35abde80'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tofu_bb826ef1-d970-4a85-b905-bccf35abde80.svg'
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


class Batch071Icon04(Solo48):
    icon_id = 'isometric-cube-batch-071'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('isometric', 'cube')

    def build(self):

        self.add_polyline('silhouette',(24,4),(40,14),(40,34),(24,44),(8,34),(8,14),closed=True)
        for name,end in [('left',(8,14)),('right',(40,14)),('bottom',(24,44))]:
            self.add_line(name,(24,24),end)
            self.relate('connect',name,'silhouette')
        self.relate('connect','left','right','bottom')
