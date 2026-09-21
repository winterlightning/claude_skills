"""Hand Touching Smartphone Screen.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
A pointing finger overlaps the phone at a visible contact point. Hidden side-wall sections and small curled fingers are omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: hand.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3730401c-4d35-4b72-a477-2313ba8f23f7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bendable phone touch_3730401c-4d35-4b72-a477-2313ba8f23f7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'index-finger-touching-a-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('index', 'finger', 'touching', 'a', 'phone')

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

        path('phone',(18,42),[('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(18,6)),('A',(22,10),4,4,True),('L',(22,18))])
        path('hand',(28,42),[('L',(18,32)),('A',(24,26),4,4,True),('L',(28,30)),('L',(22,18)),('A',(30,10),8,8,True),('L',(36,28)),('L',(42,28)),('L',(42,36)),('C',(36,42),(42,40),(40,42)),('L',(28,42))],True)
        join('phone','hand')
