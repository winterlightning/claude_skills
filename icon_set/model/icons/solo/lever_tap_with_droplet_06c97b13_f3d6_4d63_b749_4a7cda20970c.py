'A tap has a tall upright body, a long lever sloping upward to the right and a horizontal spout. A single large droplet hangs directly beneath the spout outlet.\n\nConstruction: Upright mixer tap with an angled lever and one detached water drop. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '06c97b13-f3d6-4d63-b749-4a7cda20970c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/water fountain drop_06c97b13-f3d6-4d63-b749-4a7cda20970c.svg'
AUTHOR = 'gpt-6'

class LeverTapWithDroplet(Solo48):
    icon_id = 'lever-tap-with-droplet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('tap', 'faucet', 'water', 'drop', 'lever', 'plumbing')

    def build(self):
        # Plan: A clean single-stroke operating lever replaces the narrow outlined blade; broad tap body and rounded drop retain identity.

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
        poly('body',(8,44),(8,16),(36,16),(36,26),(18,26),(18,44),closed=True)
        poly('lever',(8,16),(8,8),(40,4));join('lever','body')
        path('drop',(30,40), [('L',(34,35)),('L',(38,40)),('A',(30,40),4,4,True)],True)
