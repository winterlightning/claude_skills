"""Grilled Shish Kebab Meat Skewer.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
Three equal food blocks share a diagonal skewer axis. Rounded source pieces are reduced to compact square blocks and the projecting end stubs are omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: No useful local Lucide match was found..
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '268d30c3-e280-4e9e-b635-a834bc354118'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/kebab_268d30c3-e280-4e9e-b635-a834bc354118.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-piece-kebab-skewer-268d30c3'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('three', 'piece', 'kebab', 'skewer', '268d30c3')

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

        for j,(x,y) in enumerate([(6,34),(20,20),(34,6)]):poly(f'food-{j}',(x,y),(x+8,y),(x+8,y+8),(x,y+8),closed=True)
        line('skewer-a',(14,34),(20,28));line('skewer-b',(28,20),(34,14))
        join('skewer-a','food-0');join('skewer-a','food-1');join('skewer-b','food-1');join('skewer-b','food-2')
