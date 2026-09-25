"""A top capsule, two left lobes and a detached right ring form the Figma mark; widen the separation around the ring; extremes (8,4)-(40,44)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '525b0d85-724f-441b-b555-248547aa5d2c'
SOURCE_PATH = 'pictographic-primitives/logos/figma logo_525b0d85-724f-441b-b555-248547aa5d2c.svg'
AUTHOR = 'gpt-6'

class FigmaLogo(Solo48):
    icon_id = 'figma-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('figma', 'design', 'prototype', 'logo', 'brand', 'ui', 'collaboration')

    def build(self):
        # Plan: A top capsule, two left lobes and a detached right ring form the Figma mark; widen the separation around the ring; extremes (8,4)-(40,44).
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

        path('top',(22,4),[('L',(34,4)),('A',(34,16),6,6,True),('L',(22,16)),('L',(15,16)),('A',(15,4),6,6,True),('L',(22,4))],True)
        line('top-seam',(22,4),(22,16));join('top','top-seam')
        path('left',(15,16),[('A',(15,30),7,7,False),('L',(22,30)),('L',(22,37)),('A',(8,37),7,7,True),('A',(15,30),7,7,True)])
        line('spine',(22,16),(22,30));join('left','spine');join('top','spine');join('top','left');join('top-seam','spine')
        circle('right',36,30,4)
