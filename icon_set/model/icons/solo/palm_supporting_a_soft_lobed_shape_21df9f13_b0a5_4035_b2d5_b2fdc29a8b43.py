"""Hand Holding Soft Play Dough.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
A three-lobed soft shape sits above a flat supporting palm. Auxiliary motion marks are omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: hand-platter.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21df9f13-b0a5-4035-b2d5-b2fdc29a8b43'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baby family slime play dough 1_21df9f13-b0a5-4035-b2d5-b2fdc29a8b43.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'palm-supporting-a-soft-lobed-shape'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('palm', 'supporting', 'a', 'soft', 'lobed', 'shape')

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

        path('hand',(6,32),[('L',(20,32)),('L',(26,34)),('L',(34,34)),('A',(42,42),8,8,True),('L',(6,42))])
        path('dough',(16,22),[('A',(8,14),8,8,True),('C',(20,12),(8,6),(16,6)),('C',(30,6),(20,6),(26,6)),('C',(36,14),(36,6),(36,10)),('C',(32,24),(44,18),(38,24)),('L',(16,22))],True)
