"""Diagonal jet with speed trail. Lucide plane informs swept wing geometry and round nose. Directional asymmetry retained; one clear speed stroke replaces three tiny trails.
Keyshape SQUARE: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0e875ede-b8a7-4a7d-9958-1135f0fdc76d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jet_0e875ede-b8a7-4a7d-9958-1135f0fdc76d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='jet-with-speed-trails'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('jet', 'with', 'speed', 'trails')

    def build(self):
        self.path('jet',(6,14),[('L',(10,6)),('L',(28,14)),('L',(36,6)),('A',(42,12),6,6,True),('L',(36,24)),('L',(42,36)),('L',(34,42)),('L',(26,28)),('L',(22,32)),('L',(20,38)),('L',(14,34)),('L',(10,28)),('L',(16,26)),('L',(20,22)),('L',(6,14))],True)
        self.add_line('speed',(6,42),(8,40))

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
