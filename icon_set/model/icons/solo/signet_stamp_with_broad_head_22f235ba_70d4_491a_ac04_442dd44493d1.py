"""Handheld Rubber Stamp Tool.

Plan: VRECT_L, centerline extremes (8, 4, 40, 44); 48 x 48, stroke 4.
The broad blank stamp head sits above a narrowed neck and rounded handle.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: stamp.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22f235ba-70d4-491a-ac04-442dd44493d1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/signet_22f235ba-70d4-491a-ac04-442dd44493d1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'signet-stamp-with-broad-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('signet', 'stamp', 'with', 'broad', 'head')

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

        rect('face',8,4,32,16,4)
        path('grip',(20,20),[('L',(20,28)),('C',(16,36),(20,32),(16,32)),('A',(24,44),8,8,False),('A',(32,36),8,8,False),('C',(28,28),(32,32),(28,32)),('L',(28,20))]);join('grip','face')
