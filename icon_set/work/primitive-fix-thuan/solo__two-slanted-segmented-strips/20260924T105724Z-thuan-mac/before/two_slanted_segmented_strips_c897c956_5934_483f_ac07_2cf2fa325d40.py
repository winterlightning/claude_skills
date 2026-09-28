"""Movie Clapperboard.

Symbol plan: Two separate segmented strips, opposing shallow slopes; two regular diagonal divisions per strip. Visible (2,6)-(46,42). Preserve literal uncertain subject; do not invent a board or hinge.
Construction references: Lucide clapperboard: segmented-strip construction only; original reference does not establish a complete clapperboard.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c897c956-5934-483f-ac07-2cf2fa325d40'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/scene_c897c956-5934-483f-ac07-2cf2fa325d40.svg'
AUTHOR = 'gpt-6'


class TwoSlantedSegmentedStrips(Solo48):
    icon_id = 'two-slanted-segmented-strips'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('two', 'slanted', 'segmented', 'strips')

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

        for name,top,bottom in [('upper',[(4,10),(24,9),(44,8)],[(4,19),(24,18),(44,17)]),('lower',[(4,29),(24,30),(44,31)],[(4,38),(24,39),(44,40)])]:
         self.add_polyline(name+'-top',*top)
         self.add_polyline(name+'-bottom',*bottom)
         for j in range(2):
          self.add_line(f'{name}-divider-{j}',top[j+1],bottom[j])
          self.relate('connect',f'{name}-divider-{j}',name+'-top')
          self.relate('connect',f'{name}-divider-{j}',name+'-bottom')
