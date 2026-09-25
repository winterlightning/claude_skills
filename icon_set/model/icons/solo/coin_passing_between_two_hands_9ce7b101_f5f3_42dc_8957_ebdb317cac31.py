"""Hand Giving Coin to Receiving Hand.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
Opposed giving and receiving hands frame a small coin. Fine finger anatomy is reduced to the hand silhouettes.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: hand-coins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ce7b101-f5f3-42dc-8957-ebdb317cac31'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/begging hands give coin_9ce7b101-f5f3-42dc-8957-ebdb317cac31.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'coin-passing-between-two-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('coin', 'passing', 'between', 'two', 'hands')

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

        path('upper',(42,6),[('L',(30,6)),('L',(18,12)),('A',(22,20),5,5,False),('L',(32,14)),('L',(42,14))])
        circle('coin',8,22,2)
        path('lower',(6,34),[('L',(18,34)),('L',(28,30)),('L',(36,30)),('A',(36,38),4,4,True),('L',(20,42)),('L',(6,42))])
