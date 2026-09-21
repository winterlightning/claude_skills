"""Hand Holding a Growing Sprout.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
A two-leaf sprout grows above a supporting palm. The stem meets the hand at the support point.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: hand-helping sprout.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6d7e2d5-6eab-4182-9a4c-2d666181696c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/aquascaping plant_e6d7e2d5-6eab-4182-9a4c-2d666181696c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-hand-supporting-a-sprout'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('open', 'hand', 'supporting', 'a', 'sprout')

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

        path('thumb',(6,30),[('L',(14,24)),('L',(20,24)),('L',(24,24)),('A',(24,32),4,4,True),('L',(18,32))])
        path('palm',(6,42),[('L',(26,42)),('L',(36,34)),('A',(36,22),6,6,False),('L',(24,32))]);join('thumb','palm')

        path('leaves',(26,16),[('C',(12,6),(14,16),(12,10)),('C',(26,16),(20,6),(26,10)),('C',(40,6),(26,10),(32,6)),('C',(26,16),(40,10),(38,16))]);line('stem',(26,16),(26,24));join('leaves','stem');join('stem','thumb')
