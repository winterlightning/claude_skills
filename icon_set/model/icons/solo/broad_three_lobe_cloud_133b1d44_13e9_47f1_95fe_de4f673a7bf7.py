"""Simple Cloud Icon.

Plan: Three rounded cloud lobes and a flat lower edge retained. Keyshape HRECT_M uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: Lucide cloud: coherent round lobes sharing a flat lower contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '133b1d44-13e9-47f1-95fe-de4f673a7bf7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cloud gamimg service 2_133b1d44-13e9-47f1-95fe-de4f673a7bf7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broad-three-lobe-cloud'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('broad', 'three', 'lobe', 'cloud')

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
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('cloud',(14,38),[('A',(4,28),10,10,True),('A',(14,18),10,10,True),('C',(26,10),(16,12),(20,10)),('C',(37,20),(32,10),(36,14)),('C',(44,29),(42,20),(44,24)),('A',(35,38),9,9,True),('L',(14,38))],True)
