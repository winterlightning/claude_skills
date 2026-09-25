"""Rolled Yoga Exercise Mat.

Plan: Diagonal rolled mat beside broad unfolded sheet; bounds6,6,42,42. Open curl replaces dense spiral.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '726942f2-2e5c-4550-a984-cf244808ef79'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/carpet_726942f2-2e5c-4550-a984-cf244808ef79.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'partly-rolled-exercise-mat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('partly', 'rolled', 'exercise', 'mat')

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

        circle('front',16,32,10)
        path('roll',(6,32),[('L',(6,16)),('A',(16,6),10,10,True),('A',(26,16),10,10,True),('L',(26,32))]);join('roll','front')
        self.add_dot('core',(16,32))
        poly('mat',(26,16),(42,16),(38,42),(16,42));join('mat','roll');join('mat','front')
