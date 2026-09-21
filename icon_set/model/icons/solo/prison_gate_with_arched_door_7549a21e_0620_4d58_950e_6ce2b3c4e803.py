"""Prison Cell Gate.

Plan: Prison gate bounds6,6,42,42, two outer bars and center arched door. Single top/bottom rails replace thick bands.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7549a21e-0620-4d58-950e-6ce2b3c4e803'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/prison_7549a21e-0620-4d58-950e-6ce2b3c4e803.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'prison-gate-with-arched-door'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('prison', 'gate', 'with', 'arched', 'door')

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

        poly('frame',(6,6),(16,6),(32,6),(42,6),(42,42),(32,42),(16,42),(6,42),closed=True)
        line('bar-left',(16,6),(16,26));line('bar-right',(32,6),(32,26));join('bar-left','frame');join('bar-right','frame')
        path('door',(16,42),[('L',(16,26)),('A',(32,26),8,8,True),('L',(32,42))]);join('door','frame');join('door','bar-left');join('door','bar-right')
