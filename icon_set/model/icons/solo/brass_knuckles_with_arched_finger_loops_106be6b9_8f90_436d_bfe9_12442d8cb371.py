"""Brass Knuckles Weapon.

Symbol plan: Four equal arched finger openings as a shared series, a bowed palm outline below. Visible (2,6)-(46,42). Omit redundant surrounding rim.
Construction references: No useful direct Lucide subject match; geometric contour construction.
Original reference: SOURCE_PATH below; preserved subject, re-authored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '106be6b9-8f90-436d-bfe9-12442d8cb371'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/tools knuckle_106be6b9-8f90-436d-bfe9-12442d8cb371.svg'
AUTHOR = 'gpt-6'


class BrassKnucklesWithArchedFingerLoops(Solo48):
    icon_id = 'brass-knuckles-with-arched-finger-loops'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('brass', 'knuckles', 'with', 'arched', 'finger', 'loops')

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
            path(name, (x-r,y), [((x+r,y),r,r,True), ((x-r,y),r,r,True)], True)

        # Four lobes form a continuous knuckle silhouette and join the palm rail.
        path('guard',(4,24), [(4,16),((14,16),5,8,True),((24,16),5,8,True),((34,16),5,8,True),((44,16),5,8,True),(44,30),((34,40),10,10,True),(14,40),((4,30),10,10,True),(4,24)],True)
        self.add_line('rail',(4,24),(44,24))
        self.relate('connect','guard','rail')
        for j,x in enumerate((14,24,34)):
            self.add_line(f'finger-divider-{j}',(x,16),(x,24))
            self.relate('connect',f'finger-divider-{j}','guard')
            self.relate('connect',f'finger-divider-{j}','rail')
