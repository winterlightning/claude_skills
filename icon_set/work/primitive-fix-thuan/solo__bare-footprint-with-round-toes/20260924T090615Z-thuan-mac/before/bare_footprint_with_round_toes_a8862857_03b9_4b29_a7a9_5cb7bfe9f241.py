"""Human Bare Footprint Symbol.

Symbol plan: Asymmetric forefoot and indented arch; four toe marks grow toward right. Visible (6,2)-(42,46). Reduce five toes to four for clearance.
Construction references: Lucide footprints: continuous sole and inward arch. Shared human references inspected for human-part vocabulary.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8862857-03b9-4b29-a7a9-5cb7bfe9f241'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/police footstep_a8862857-03b9-4b29-a7a9-5cb7bfe9f241.svg'
AUTHOR = 'gpt-6'


class BareFootprintWithRoundToes(Solo48):
    icon_id = 'bare-footprint-with-round-toes'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('bare', 'footprint', 'with', 'round', 'toes')

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

        for j,p in enumerate(((8,14),(16,6),(26,4))):self.add_dot(f'toe-{j}',p)
        circle('big-toe',37,10,3)
        path('sole',(10,28),[((22,20),12,8,True),((34,28),12,8,True),((26,36),8,8,False),((18,44),8,8,True),((10,36),8,8,True),(10,28)],True)
