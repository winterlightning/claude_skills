"""Scissors Cutting Dotted Path.

Plan: Retained both finger loops, crossed blades and cutting path. Narrow blade outlines become strokes and the path becomes three broad dashes.
Construction reference: Lucide scissors: circular loops and crossing stroke blades; source cutting line retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7fd3346-6754-4a1f-960f-4b3c7be0b3f0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/coupon cut_a7fd3346-6754-4a1f-960f-4b3c7be0b3f0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-scissors-above-dashed-cut-line'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('open', 'scissors', 'above', 'dashed', 'cut', 'line')

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

        circle('upper',12,12,6);circle('lower',12,28,5)
        poly('blade-a',(18,12),(24,21),(42,32));poly('blade-b',(17,28),(24,21),(42,6))
        join('upper','blade-a');join('lower','blade-b');join('blade-a','blade-b')
        for x in (6,22,38):line('dash-'+str(x),(x,42),(x+4,42))
