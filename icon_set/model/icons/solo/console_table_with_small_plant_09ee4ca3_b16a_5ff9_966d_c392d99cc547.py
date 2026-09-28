"""Console Table with Potted Plant.

Console table with left drawer, open right shelf and small potted two-leaf plant. Centerline extremes (6,6)-(42,42). Lucide sprout informs a shared stem junction. Simplify leaf outlines to two strokes and omit the tiny drawer pull; preserve pot and shelf.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09ee4ca3-b16a-5ff9-966d-c392d99cc547'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/console table_09ee4ca3-b16a-5ff9-966d-c392d99cc547.svg'
AUTHOR = 'gpt-6'

class ConsoleTableWithSmallPlant(Solo48):
    icon_id = 'console-table-with-small-plant'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('console', 'table', 'with', 'potted', 'plant')

    def build(self):
        # Symbol plan: Console table with left drawer, open right shelf and small potted two-leaf plant. Centerline extremes (6,6)-(42,42). Lucide sprout informs a shared stem junction. Simplify leaf outlines to two strokes and omit the tiny drawer pull; preserve pot and shelf.

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

        self.add_polyline('table',(6,24),(24,24),(30,24),(38,24),(42,24),(40,34),(32,34),(24,34),(14,34),(8,34),(6,24))
        line('divider',(24,24),(24,34));join('divider','table')
        for n,a,z in [('left',(14,34),(10,42)),('right',(32,34),(36,42))]:line(n+'-leg',a,z);join(n+'-leg','table')
        self.add_polyline('pot',(30,24),(28,16),(34,16),(40,16),(38,24));join('pot','table')
        self.add_polyline('stem',(34,16),(34,12),(34,6));join('stem','pot')
        for n,p in [('left',(26,6)),('right',(42,6))]:line(n+'-leaf',(34,12),p);join(n+'-leaf','stem')
        join('left-leaf','right-leaf')
