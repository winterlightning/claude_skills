"""Scissor Car Jack.

Plan: Retained the diamond lifting frame, top saddle, base, horizontal screw and circular handle. The screw stops at the handle rim to preserve its opening.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '995738af-e22c-4f32-af97-1632d28f1f3e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car jack_995738af-e22c-4f32-af97-1632d28f1f3e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diamond-scissor-jack'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('diamond', 'scissor', 'jack')

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

        poly('frame',(6,24),(22,8),(34,24),(22,38),(6,24),closed=True)
        line('saddle',(16,6),(28,6));line('top',(22,6),(22,8));join('top','saddle');join('top','frame')
        line('base',(10,42),(32,42));line('pedestal',(22,38),(22,42));join('base','pedestal');join('pedestal','frame');join('base','frame')
        line('screw',(6,24),(34,24));circle('handle',38,24,4);join('screw','frame');join('screw','handle')
