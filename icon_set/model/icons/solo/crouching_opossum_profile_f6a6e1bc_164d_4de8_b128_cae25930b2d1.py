"""Crouching opossum profile with long tail, round ear, curved haunch and pointed muzzle. No useful exact local Lucide match. Smooth coherent curves replace angular forepaw and lumpy back. Omit tiny eye.
Keyshape HRECT_L: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f6a6e1bc-164d-4de8-b128-cae25930b2d1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/opossum_f6a6e1bc-164d-4de8-b128-cae25930b2d1.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='crouching-opossum-profile'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('crouching', 'opossum', 'profile')

    def build(self):
        self.path('back',(4,22),[('L',(16,12)),('A',(24,12),4,4,True),('C',(28,14),(24,14),(26,14)),('C',(44,28),(38,14),(44,18)),('C',(34,40),(44,36),(40,40)),('L',(18,40))])
        self.path('front',(4,22),[('C',(14,24),(8,24),(12,24)),('C',(14,32),(18,24),(18,30)),('L',(10,32))]);self.relate('connect','back','front')
        self.path('haunch',(34,24),[('A',(26,32),8,8,False),('A',(34,40),8,8,False)]);self.relate('connect','haunch','back')

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
