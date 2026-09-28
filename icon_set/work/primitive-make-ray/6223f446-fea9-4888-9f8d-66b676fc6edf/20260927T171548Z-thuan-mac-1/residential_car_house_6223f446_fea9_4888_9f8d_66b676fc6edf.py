"""Residential Car Parking.

Plan: Natural car-and-house scene, not badge; bounds4,8,44,40. One door and car windshield with short legs.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6223f446-fea9-4888-9f8d-66b676fc6edf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__residential-car-house/20260927T171300Z-thuan-mac-1/reference/parking resident_6223f446-fea9-4888-9f8d-66b676fc6edf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'residential-car-house'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('residential', 'car', 'house')

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

        path('house',(20,16),[('L',(32,8)),('L',(44,16)),('L',(44,32)),('L',(36,32)),('L',(36,26)),('A',(28,26),4,4,False),('L',(28,32))])
        path('car',(4,32),[('L',(8,24)),('L',(16,24)),('L',(19,32)),('L',(19,40)),('L',(4,40)),('L',(4,32))],True)
        line('windshield',(4,32),(19,32));join('windshield','car')
