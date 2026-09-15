"""Four mirrored smooth bulging diamond quadrants surround one small sharp diamond; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a61cded-9b51-409a-b3a1-97f02788c989'
SOURCE_PATH = 'pictographic-primitives/logos/claris logo_4a61cded-9b51-409a-b3a1-97f02788c989.svg'
AUTHOR = 'gpt-6'

class ClarisLogo(Solo48):
    icon_id = 'claris-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('claris', 'filemaker', 'logo', 'brand', 'diamond', 'software', 'database')

    def build(self):
        # Plan: Four mirrored smooth bulging diamond quadrants surround one small sharp diamond; extremes (6,6)-(42,42).
        # Construction reference: No useful subject match found; source brand render informs the geometry.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i, command in enumerate(commands):
                kind, end, *args=command
                part=f"{name}-{i}"
                if kind=='L': self.add_line(part,here,end)
                elif kind=='A':
                    rx,ry,sweep=args
                    self.add_arc(part,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif kind=='C': self.add_bezier(part,here,(args[0],args[1],end))
                members.append(part); here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def c_ring(name):
            # Exact radius-20 points on the circle about (24,24).
            self.add_arc(name,(36,8),(36,40),radius_x=20,large_arc=True,sweep=False)
        poly=self.add_polyline
        line=self.add_line
        join=lambda a,b:self.relate('connect',a,b)

        axis=24
        # One quarter definition is rotated four times about the common centre.
        def rot(p,n):
            x,y=p[0]-axis,p[1]-axis
            for _ in range(n): x,y=-y,x
            return (axis+x,axis+y)
        for i in range(4):
            self.add_bezier(f'outer-{i}',rot((24,6),i),(rot((31,6),i),rot((42,17),i),rot((42,24),i)))
        self.add_contour('outer',*(f'outer-{i}' for i in range(4)),closed=True)
        poly('diamond',(24,16),(32,24),(24,32),(16,24),closed=True)
