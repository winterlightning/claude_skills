"""Hand Drill Fire Starting.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
A hand grips the vertical fire drill above a horizontal log. Sparks and fine finger creases are omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: hand-fist.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e94edbaf-c94d-4cdc-a976-817dfd2498ef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/outdoors camp fire make_e94edbaf-c94d-4cdc-a976-817dfd2498ef.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-drill-fire-log'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('hand', 'drill', 'fire', 'log')

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

        rect('log',6,32,36,10,5)
        line('stick',(20,6),(20,32));join('stick','log')
        path('hand',(42,10),[('L',(30,10)),('L',(24,6)),('L',(16,6)),('A',(12,10),4,4,False),('L',(12,20)),('A',(16,24),4,4,False),('L',(42,24))]);join('stick','hand')
        line('finger',(12,16),(24,16));join('finger','hand');join('finger','stick')
