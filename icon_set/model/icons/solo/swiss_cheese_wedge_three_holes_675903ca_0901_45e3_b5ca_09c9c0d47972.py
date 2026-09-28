"""Wedge of Swiss Cheese.

Cheese wedge with triangular top above deep side and circular holes. Centerline extremes (4,8)-(44,40). Preserve asymmetric perspective; simplify left bite and use two complete circular holes; drop the third to preserve readable openings. Lucide cookie informs sparse circular food detail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '675903ca-0901-45e3-b5ca-09c9c0d47972'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/cheese_675903ca-0901-45e3-b5ca-09c9c0d47972.svg'
AUTHOR = 'gpt-6'

class SwissCheeseWedgeThreeHoles(Solo48):
    icon_id = 'swiss-cheese-wedge-three-holes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('wedge', 'of', 'swiss', 'cheese')

    def build(self):
        # Symbol plan: Cheese wedge with triangular top above deep side and circular holes. Centerline extremes (4,8)-(44,40). Preserve asymmetric perspective; simplify left bite and use two complete circular holes; drop the third to preserve readable openings. Lucide cookie informs sparse circular food detail.

        def path(name, start, commands, closed=False):
            members=[]
            for i, command in enumerate(commands):
                kind,end,*args=command
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,start,end)
                elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
                members.append(member)
                start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)

        path('wedge',(4,16),[('L',(28,8)),('C',(44,16),(36,8),(42,12)),('L',(44,40)),('L',(4,40)),('L',(4,16))],True)
        line('edge',(4,16),(44,16));join('edge','wedge')
        for i,x in enumerate((16,32)): oval(f'hole-{i}',x,28,3,3)
