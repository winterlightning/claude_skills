"""Turban wearer: rounded wrapped turban, circular lower face and broad detached shoulders. Shared user.svg proportions, face radius8 at24,20, jaw bottom28, shoulder top36: exact4 visible gap. No useful exact Lucide match. Omit secondary wrap seams.
Keyshape VRECT_L: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6750efc1-07cd-4c25-a6ba-c62334e6c61e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/sultan_6750efc1-07cd-4c25-a6ba-c62334e6c61e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='turban-wearer'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="avatars"
    aliases=()
    keywords=('turban', 'wearer')

    def build(self):
        self.path('turban',(12,16),[('A',(24,4),12,12,True),('A',(36,16),12,12,True),('L',(32,20)),('L',(24,14)),('L',(16,20)),('L',(12,16))],True)
        self.add_arc('jaw',(32,20),(16,20),radius_x=8,sweep=True)
        self.relate('connect','turban','jaw')
        self.path('shoulders',(8,44),[('A',(16,36),8,8,True),('L',(32,36)),('A',(40,44),8,8,True)])

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
