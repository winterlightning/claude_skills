"""Flying Kite and Cloud.

Plan: Kite in outdoor cloud scene, no reusable action badge. Bounds6,6,42,42. Blank diamond plus long tail and small cloud.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'beeba30d-8d4a-48a4-85a6-836e8a238bd0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/outdoors kite flying cloud_beeba30d-8d4a-48a4-85a6-836e8a238bd0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kite-beside-small-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('kite', 'beside', 'small', 'cloud')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        poly('kite',(30,18),(42,24),(36,36),(24,30),closed=True)
        path('tail',(36,36),[('C',(24,42),(36,42),(30,36)),('L',(20,42))]);join('tail','kite')
        path('cloud',(6,12),[('C',(10,10),(6,10),(8,10)),('C',(14,6),(10,8),(12,6)),('C',(18,10),(16,6),(18,8)),('C',(20,13),(20,10),(20,11)),('C',(18,16),(20,15),(20,16)),('L',(8,16)),('C',(6,12),(6,16),(6,14))],True)
