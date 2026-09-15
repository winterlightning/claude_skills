"""An airplane points upward with a long rounded fuselage tapering toward its tail. Broad wings project to either side with visible inner boundaries, and two short tailplanes flare outward near the bottom."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94d6385f-007c-5de3-b7a9-d9483583e910'
SOURCE_PATH = 'pictographic-primitives/mobile/airplane plane mode_94d6385f-007c-5de3-b7a9-d9483583e910.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'airplane-top-view-fuselage'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/mobile"
    aliases = ()
    keywords = ('airplane', 'plane', 'flight', 'wings', 'aircraft', 'aviation', 'top-view')

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
        # Plan: mirror wings and tail around x=24; rounded nose and broad neck.
        # VRECT_L extremes (8,4)-(40,44). Lucide plane: coherent silhouette.
        axis = 24
        left = [(20,8),(20,18),(8,20),(8,28),(20,28),(20,36),(14,36),(14,44),(24,44)]
        points = left + [(2*axis-x,y) for x,y in reversed(left[:-1])]
        commands = [('L',p) for p in points[1:]]
        commands += [('A',(24,4),4,4,False),('A',left[0],4,4,False)]
        path('airframe',left[0],commands,True)
