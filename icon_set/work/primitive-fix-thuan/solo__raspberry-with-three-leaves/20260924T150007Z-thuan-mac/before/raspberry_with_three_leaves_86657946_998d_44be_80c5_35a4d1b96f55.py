"""Raspberry with a three-leaf crown and tapered drupelet cluster.
VRECT_L reaches (8,4)-(40,44). Shared crown and berry contour with an
attachment seam; paired leaves mirror x=24. Three broad fruit cells replace
the seven source lobes. Reference sets count of leaves and fruit taper;
Lucide grape supplies the repeated round-cell construction principle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86657946-998d-44be-80c5-35a4d1b96f55'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/boysenberry_86657946-998d-44be-80c5-35a4d1b96f55.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'raspberry-with-three-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Fresh Raspberry Berry Fruit',)
    keywords = ('raspberry','berry','fruit','leaves','food','plant','produce')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            if name not in ('berry','crown'): self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('berry',(32,20),[('C',(40,28),(38,20),(40,23)),('C',(34,36),(40,32),(38,36)),('C',(24,44),(34,42),(28,44)),('C',(14,36),(20,44),(14,42)),('C',(8,28),(10,36),(8,32)),('C',(16,20),(8,23),(10,20))])
        path('crown',(16,20),[('C',(8,8),(10,18),(8,12)),('C',(20,14),(14,8),(18,10)),('C',(24,4),(20,10),(22,6)),('C',(28,14),(26,6),(28,10)),('C',(40,8),(30,10),(34,8)),('C',(32,20),(40,12),(38,18))])
        self.add_contour('outline',*[f'berry-{i}' for i in range(6)],*[f'crown-{i}' for i in range(6)],closed=True)
        path('attachment',(16,20),[('L',(24,20)),('L',(32,20))]);join('attachment','outline')
        path('lobes',(8,28),[('C',(24,30),(12,36),(20,36)),('C',(40,28),(28,36),(36,36))]);join('lobes','outline')
        path('middle',(24,20),[('C',(24,30),(19,22),(19,27)),('L',(24,36))]);join('middle','attachment');join('middle','lobes')
