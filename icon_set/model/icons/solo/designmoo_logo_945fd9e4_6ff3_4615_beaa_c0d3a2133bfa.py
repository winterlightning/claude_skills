"""A slanted lowercase d with a returning terminal and one four-point sparkle; omit the two smallest sparkles; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '945fd9e4-6ff3-4615-beaa-c0d3a2133bfa'
SOURCE_PATH = 'pictographic-primitives/logos/designmoo logo_945fd9e4-6ff3-4615-beaa-c0d3a2133bfa.svg'
AUTHOR = 'gpt-6'

class DesignmooLogo(Solo48):
    icon_id = 'designmoo-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('designmoo', 'letter-d', 'sparkle', 'logo', 'brand', 'design', 'resources')

    def build(self):
        # Plan: A slanted lowercase d with a returning terminal and one four-point sparkle; omit the two smallest sparkles; extremes (6,6)-(42,42).
        # Construction reference: No useful subject-specific Lucide match; construction follows the supplied brand render.

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

        def graph(edges):
            for name,a,b in edges: line(name,a,b)
            for i,(name,a,b) in enumerate(edges):
                for other,c,d in edges[:i]:
                    if {a,b}&{c,d}: join(name,other)

        circle('bowl',20,32,10)
        path('stem',(38,6),[('L',(30,32)),('C',(42,34),(27,42),(36,42))])
        join('bowl','stem')
        graph([('spark-left',(6,10),(10,10)),('spark-right',(10,10),(14,10)),('spark-top',(10,6),(10,10)),('spark-bottom',(10,10),(10,14))])
