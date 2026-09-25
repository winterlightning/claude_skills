"""A flat-top hexagon surrounding a smaller point-top hexagon; matched mirrored vertices and rounded stroke joins; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '443ea993-bbdb-4776-8967-d346329a2def'
SOURCE_PATH = 'pictographic-primitives/logos/eslint logo_443ea993-bbdb-4776-8967-d346329a2def.svg'
AUTHOR = 'gpt-6'

class EslintLogo(Solo48):
    icon_id = 'eslint-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('eslint', 'linting', 'javascript', 'hexagon', 'logo', 'brand', 'developer')

    def build(self):
        # Plan: A flat-top hexagon surrounding a smaller point-top hexagon; matched mirrored vertices and rounded stroke joins; extremes (6,6)-(42,42).
        # Construction reference: Lucide hexagon: balanced polygon with rounded joins.

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

        poly('outer',(14,6),(34,6),(42,24),(34,42),(14,42),(6,24),closed=True)
        poly('inner',(24,16),(31,20),(31,28),(24,32),(17,28),(17,20),closed=True)
