"""Pair of Shoe Footprints.

Symbol plan: Two same-size shoe-print definitions offset vertically by four. Rounded toes, tapered waist, detached heels. Visible (4,4)-(44,44). No tread detail.
Construction references: Lucide footprints: rounded forefoot and heel separated across the waist.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f949d05-2578-5bdd-a347-947d8f6e8632'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/police footsteps_5f949d05-2578-5bdd-a347-947d8f6e8632.svg'
AUTHOR = 'gpt-6'


class StaggeredShoePrints(Solo48):
    icon_id = 'staggered-shoe-prints'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('staggered', 'shoe', 'prints')

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

        for j,(x,y) in enumerate(((13,6),(35,10))):
         path(f'sole-{j}',(x-7,y+7),[((x,y),7,7,True),((x+7,y+7),7,7,True),(x+5,y+16),(x-5,y+16),(x-7,y+7)],True)
         path(f'heel-{j}',(x-4,y+24),[(x+4,y+24),(x+4,y+28),((x,y+32),4,4,True),((x-4,y+28),4,4,True),(x-4,y+24)],True)
