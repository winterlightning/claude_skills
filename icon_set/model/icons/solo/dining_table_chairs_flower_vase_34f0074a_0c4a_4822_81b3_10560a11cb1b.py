"""Dining Table with Chairs and Vase.

Dining table between two curved-back chairs with a flower vase centered on top. Centerline extremes (8,4)-(40,44). Lucide sprout informs branching stem; no close dining-scene match. Retain three round flower heads; simplify chair backs to rounded posts and the table to one edge on a central pedestal.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34f0074a-0c4a-4822-81b3-10560a11cb1b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/eating table_34f0074a-0c4a-4822-81b3-10560a11cb1b.svg'
AUTHOR = 'gpt-6'

class DiningTableChairsFlowerVase(Solo48):
    icon_id = 'dining-table-chairs-flower-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('dining', 'table', 'with', 'chairs', 'and', 'vase')

    def build(self):
        # Symbol plan: Dining table between two curved-back chairs with a flower vase centered on top. Centerline extremes (8,4)-(40,44). Lucide sprout informs branching stem; no close dining-scene match. Retain three round flower heads; simplify chair backs to rounded posts and the table to one edge on a central pedestal.

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

        self.add_polyline('table',(16,30),(20,30),(24,30),(28,30),(32,30))
        line('pedestal',(24,30),(24,44));join('pedestal','table')
        for n,x,z in [('left',8,16),('right',40,32)]:
            self.add_polyline(n+'-chair',(x,44),(x,38),(x,26));line(n+'-seat',(x,38),(z,38));join(n+'-chair',n+'-seat')
        self.add_polyline('vase',(20,30),(20,22),(24,22),(28,22),(28,30));join('vase','table')
        line('stem',(24,22),(24,8));join('stem','vase')
        for n,x in [('left',12),('middle',24),('right',36)]:
            oval(n+'-flower',x,6,2,2)
            if n=='middle':join(n+'-flower','stem')
            else:
                line(n+'-branch',(24,22),(x,8));join(n+'-branch','vase');join(n+'-branch','stem');join(n+'-branch',n+'-flower')
        join('left-branch','right-branch')
