"""Protective Gas Mask.

Plan: Gas mask bounds8,4,40,44 with two circular lenses and round lower filter. Simplify divided filter to one hole.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a3783e0-41d2-4d15-a1e5-75484922e780'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/mask 1_0a3783e0-41d2-4d15-a1e5-75484922e780.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'gas-mask-with-two-round-eye-lenses'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ()
    keywords = ('gas', 'mask', 'with', 'two', 'round', 'eye', 'lenses')

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

        path('mask',(16,34),[('C',(6,18),(6,30),(6,26)),('C',(18,6),(6,10),(10,6)),('L',(30,6)),('C',(42,18),(38,6),(42,10)),('C',(32,34),(42,26),(42,30))])
        circle('lens-left',17,17,2);circle('lens-right',31,17,2)
        circle('filter',24,34,8);join('filter','mask')
