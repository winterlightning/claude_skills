"""Hologram cube above a projector base. Square extremes 6/6/42/42. Lucide box face junctions; retain floating cube and two outward beams. Lens omitted to keep the cube and projector separated at native size."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '662b3074-f86b-483a-a095-4f5acc053b0c'
SOURCE_PATH = 'pictographic-primitives/technology/virtual box_662b3074-f86b-483a-a095-4f5acc053b0c.svg'
AUTHOR = 'gpt-6'

class HologramCubeProjector(Solo48):
    icon_id = 'hologram-cube-projector'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('hologram', 'projector', 'cube', 'virtual', '3d', 'projection', 'object')

    def build(self):
        # Plan: Increase all cube face heights together, retaining shared perspective junctions; base and projection beams remain detached with clearance.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        poly('cube',(14,10),(24,4),(34,10),(34,20),(24,26),(14,20),closed=True)
        poly('top-face',(14,10),(24,16),(34,10));join('top-face','cube')
        line('edge',(24,16),(24,26));join('edge','cube');join('edge','top-face')
        poly('base',(14,34),(34,34),(34,44),(14,44),closed=True)
        line('left-beam',(8,26),(8,28));line('right-beam',(40,26),(40,28))
