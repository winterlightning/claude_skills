"""A circular charging puck with a smaller concentric centre connects to a looping cable. The cord descends from the puck, curves upward, and ends in a rectangular connector on the right."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '337040ae-1b90-42ff-b8d3-f52f2db434b8'
SOURCE_PATH = 'pictographic-primitives/mobile/charging wireless charging port_337040ae-1b90-42ff-b8d3-f52f2db434b8.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'charging-puck-and-cable'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/mobile"
    aliases = ()
    keywords = ('charger', 'puck', 'cable', 'connector', 'wireless', 'charging', 'power')

    def build(self):
        # Typed paths keep continuous joins; dimensions belong to each symbol.
        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                ident = f"{name}-{i}"
                if kind == "L":
                    self.add_line(ident, here, end)
                else:
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0+r,y0), [
                ('L',(x1-r,y0)), ('A',(x1,y0+r),r,r,True),
                ('L',(x1,y1-r)), ('A',(x1-r,y1),r,r,True),
                ('L',(x0+r,y1)), ('A',(x0,y1-r),r,r,True),
                ('L',(x0,y0+r)), ('A',(x0+r,y0),r,r,True)], True)
        # Plan: circular puck, U cable, rectangular plug; actual contacts share nodes.
        # SQUARE extremes (6,6)-(42,42). Lucide cable: tangent U bend and attached plug.
        cx, cy, radius = 16,16,10
        path('puck',(16,26), [('A',(16,6),radius,radius,True),('A',(16,26),radius,radius,True)],True)
        path('cord',(16,26), [('L',(16,31)),('A',(27,42),11,11,False),('A',(38,31),11,11,False),('L',(38,16))])
        self.add_polyline('plug',(38,16),(34,16),(34,6),(42,6),(42,16),(38,16))
        self.relate('connect','puck','cord')
        self.relate('connect','cord','plug')
