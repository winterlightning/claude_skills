"""Hanging Rope Noose.

Symbol plan: Centered rope, broad collar and tapered loop. Visible (8,2)-(40,46). Omit individual wrap marks.
Construction references: No useful direct Lucide match; coherent geometric contours.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4126b84-a39b-541c-8b29-fdcdcbf4fe53'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/death noose_f4126b84-a39b-541c-8b29-fdcdcbf4fe53.svg'
AUTHOR = 'gpt-6'


class NooseWithWrappedCollar(Solo48):
    icon_id = 'noose-with-wrapped-collar'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('noose', 'with', 'wrapped', 'collar')

    def build(self):
        def path(name, start, steps, closed=False):
            ids = []
            point = start
            for i, step in enumerate(steps):
                member = f"{name}-{i}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                ids.append(member)
            self.add_contour(name, *ids, closed=closed)

        def circle(name, x, y, r):
            path(name, (x,y-r), [((x+r,y),r,r,True), ((x,y+r),r,r,True), ((x-r,y),r,r,True), ((x,y-r),r,r,True)], True)

        path('collar',(20,20),[(18,20),(18,12),(24,12),(30,12),(30,20),(28,20)])
        self.add_bezier('loop-right',(28,20),((28,25),(38,28),(38,34)))
        self.add_arc('loop-bottom',(38,34),(10,34),radius_x=14,radius_y=10)
        self.add_bezier('loop-left',(10,34),((10,28),(20,25),(20,20)))
        self.add_contour('loop','loop-right','loop-bottom','loop-left')
        self.add_line('seam',(20,20),(28,20))
        self.add_line('rope',(24,4),(24,12))
        for a,b in [('collar','loop'),('collar','seam'),('loop','seam'),('collar','rope')]:self.relate('connect',a,b)
