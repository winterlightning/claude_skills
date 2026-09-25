"""Hand Holding Pride Flag.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
The blank flag waves above a pole held by the left-entering hand. Small finger grooves are omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: flag hand-fist.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b50450df-a0b2-4543-acfe-30ea5158a73f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/romance pride lesbian lgbt flag hand_b50450df-a0b2-4543-acfe-30ea5158a73f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-gripping-a-waving-flag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('hand', 'gripping', 'a', 'waving', 'flag')

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

        poly('pole',(24,6),(24,22));line('pole-low',(24,42),(24,42))
        path('flag',(24,6),[('C',(42,10),(32,6),(32,14)),('L',(42,22)),('C',(24,18),(32,24),(32,18)),('L',(24,6))],True);join('flag','pole')
        path('hand',(6,28),[('L',(14,28)),('L',(18,22)),('L',(24,22)),('L',(24,32)),('L',(32,32)),('A',(36,34),4,4,True),('L',(36,38)),('A',(32,42),4,4,True),('L',(6,42))]);join('hand','pole');join('hand','pole-low')
