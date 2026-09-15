"""Thirteen evenly spaced dots form a diamond; simplify the tiny rings to dots so the full five-row rhythm survives; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'abcdc85a-f04e-454d-b20e-0df7a6a03e51'
SOURCE_PATH = 'pictographic-primitives/logos/fitbit logo_abcdc85a-f04e-454d-b20e-0df7a6a03e51.svg'
AUTHOR = 'gpt-6'

class FitbitLogo(Solo48):
    icon_id = 'fitbit-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('fitbit', 'fitness', 'dots', 'logo', 'brand', 'wearable', 'health')

    def build(self):
        # Plan: Thirteen evenly spaced dots form a diamond; simplify the tiny rings to dots so the full five-row rhythm survives; extremes (6,6)-(42,42).
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

        for row in range(-2,3):
         for col in range(-(2-abs(row)),3-abs(row)):
          self.add_dot(f'dot-{row+2}-{col+2}',(24+9*col,24+9*row))
