"""Flower Vase on Table.

Low table with slanted legs and a centered tall vase holding three spreading stems. Centerline extremes (6,6)-(42,42). Lucide sprout informs a shared plant junction. Omit tiny branching tips; retain the thick tabletop and narrow vase.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd77a5e6-c9d2-43d4-84f8-48a0a2828054'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/flowers table_dd77a5e6-c9d2-43d4-84f8-48a0a2828054.svg'
AUTHOR = 'gpt-6'

class FlowerVaseOnLowTable(Solo48):
    icon_id = 'flower-vase-on-low-table'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('flower', 'vase', 'on', 'table')

    def build(self):
        # Symbol plan: Low table with slanted legs and a centered tall vase holding three spreading stems. Centerline extremes (6,6)-(42,42). Lucide sprout informs a shared plant junction. Omit tiny branching tips; retain the thick tabletop and narrow vase.

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

        self.add_polyline('table',(6,26),(20,26),(28,26),(42,26),(42,34),(34,34),(14,34),(6,34),closed=True)
        for n,a,z in [('left',(14,34),(10,42)),('right',(34,34),(38,42))]:line(n,a,z);join(n,'table')
        self.add_polyline('vase',(20,26),(20,16),(24,16),(28,16),(28,26));join('vase','table')
        for n,x in [('left',14),('middle',24),('right',34)]:
            path(n+'-stem',(24,16),[('C',(x,6),(24,12),(x,10))]);join(n+'-stem','vase')
        for a,b in [('left','middle'),('left','right'),('middle','right')]:join(a+'-stem',b+'-stem')
