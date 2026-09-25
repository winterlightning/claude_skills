"""Open laptop with blank screen and flared base. Lucide laptop: matching rounded upper screen corners, straight hinge and symmetric base. Shared axis24, no omitted identifying parts.
Keyshape HRECT_L: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7b74abd1-6530-4972-a359-b5ebb36734a5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/netbook_7b74abd1-6530-4972-a359-b5ebb36734a5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='blank-open-laptop'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('blank', 'open', 'laptop')

    def build(self):
        self.path('screen',(8,28),[('L',(8,12)),('A',(12,8),4,4,True),('L',(36,8)),('A',(40,12),4,4,True),('L',(40,28))])
        self.add_polyline('base',(8,28),(4,40),(44,40),(40,28),(8,28),closed=True)
        self.relate('connect','screen','base')

    def path(self,name,start,commands,closed=False):
        members=[];here=start
        for j,(kind,end,*args) in enumerate(commands):
            eid=f'{name}-{j}'
            if kind=='L':self.add_line(eid,here,end)
            elif kind=='A':self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C':self.add_bezier(eid,here,(args[0],args[1],end))
            members.append(eid);here=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
