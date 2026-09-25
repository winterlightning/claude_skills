"""Canister vacuum with wheel, curved hose, straight wand and floor nozzle. No useful exact local Lucide match. Quarter arcs and smooth hose curves replace lumps; nozzle and wheel remain clear. Small housing details omitted.
Keyshape SQUARE: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4ec2ee75-a22d-55f3-9911-352714be5d1e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/cleaning vacuum_4ec2ee75-a22d-55f3-9911-352714be5d1e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='canister-vacuum-curved-hose'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="furnitures"
    aliases=()
    keywords=('canister', 'vacuum', 'curved', 'hose')

    def build(self):
        self.circle('wheel',10,37,3)
        self.path('canister',(10,34),[('L',(10,24)),('A',(22,36),12,12,True),('L',(22,40)),('L',(10,40))]);self.relate('connect','wheel','canister')
        self.path('hose',(10,24),[('C',(12,16),(18,24),(18,20)),('C',(6,12),(8,14),(6,14)),('A',(12,6),6,6,True),('L',(20,6)),('L',(36,34))]);self.relate('connect','hose','canister')
        self.path('nozzle',(32,42),[('L',(32,36)),('A',(34,34),2,2,True),('L',(36,34)),('L',(40,34)),('A',(42,36),2,2,True),('L',(42,42)),('L',(32,42))],True);self.relate('connect','nozzle','hose')

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
