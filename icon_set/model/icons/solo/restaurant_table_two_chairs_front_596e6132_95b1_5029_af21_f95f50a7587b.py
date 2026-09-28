"""Restaurant Table and Chairs.

Restaurant pedestal table between two facing chairs, with a flat table foot. Centerline extremes (6,6)-(42,42). No close local Lucide scene match. Mirror the chairs and keep separate silhouettes; simplify narrow chair backs to single rails.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '596e6132-95b1-5029-af21-f95f50a7587b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/table restaurant_596e6132-95b1-5029-af21-f95f50a7587b.svg'
AUTHOR = 'gpt-6'

class RestaurantTableTwoChairsFront(Solo48):
    icon_id = 'restaurant-table-two-chairs-front'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('restaurant', 'table', 'and', 'chairs')

    def build(self):
        # Symbol plan: Restaurant pedestal table between two facing chairs, with a flat table foot. Centerline extremes (6,6)-(42,42). No close local Lucide scene match. Mirror the chairs and keep separate silhouettes; simplify narrow chair backs to single rails.

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
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def bilateral(name, start, right, closed=True):
            # One half owns geometry; mirror and reverse it about the shared axis.
            axis=24
            mirror=lambda p:(2*axis-p[0],p[1])
            segments=[]
            here=start
            for kind,end,*args in right:
                segments.append((kind,here,end,args));here=end
            left=[]
            for kind,begin,end,args in reversed(segments):
                if kind=='C': left.append((kind,mirror(begin),mirror(args[1]),mirror(args[0])))
                elif kind=='A': left.append((kind,mirror(begin),*args))
                else:left.append((kind,mirror(begin)))
            if closed:path(name,start,right+left,True)
            else:path(name,mirror(here),left+right)
        line=self.add_line
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)

        self.add_polyline('top',(14,18),(24,18),(34,18));self.add_polyline('stem',(24,18),(24,42));join('stem','top')
        self.add_polyline('foot',(20,42),(24,42),(28,42));join('foot','stem')
        for n,x,z in [('left',6,14),('right',42,34)]:
            self.add_polyline(n+'-chair',(x,6),(x,28),(x,42));self.add_polyline(n+'-seat',(x,28),(z,28),(z,34));join(n+'-chair',n+'-seat')
