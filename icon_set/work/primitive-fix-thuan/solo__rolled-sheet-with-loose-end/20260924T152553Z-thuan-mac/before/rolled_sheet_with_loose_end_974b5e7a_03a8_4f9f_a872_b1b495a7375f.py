"""Rolled Fabric Material.

Plan: Horizontal rolled sheet with spiral mouth and loose flap; bounds4,8,44,40.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '974b5e7a-03a8-4f9f-a872-b1b495a7375f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/roll_974b5e7a-03a8-4f9f-a872-b1b495a7375f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rolled-sheet-with-loose-end'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('rolled', 'sheet', 'with', 'loose', 'end')

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

        circle('front',18,18,12)
        path('body',(18,6),[('L',(30,6)),('A',(30,30),12,12,True),('L',(18,30))]);join('body','front')
        path('core',(15,18),[('A',(18,15),3,3,True),('A',(21,18),3,3,True),('A',(18,21),3,3,True)])
        poly('flap',(18,30),(26,42),(42,42),(30,30));join('flap','body');join('flap','front')
