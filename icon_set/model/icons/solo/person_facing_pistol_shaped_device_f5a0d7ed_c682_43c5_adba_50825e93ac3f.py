"""Forehead Temperature Scan.

Symbol plan: Physical scene preserved without asserting device identity. Detached circular head above open shoulders; device on right. Visible (4,4)-(44,44). Omit rays for spacing. Head bottom=22; body top=30, exact 4 ink gap.
Construction references: human_ref/user.svg and full_body_ref.png: circular head, coherent open shoulder stroke.
Original reference: SOURCE_PATH below; preserved subject, re-authored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5a0d7ed-c682-43c5-adba-50825e93ac3f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/headshot_f5a0d7ed-c682-43c5-adba-50825e93ac3f.svg'
AUTHOR = 'gpt-6'


class PersonFacingPistolShapedDevice(Solo48):
    icon_id = 'person-facing-pistol-shaped-device'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('person', 'facing', 'pistol', 'shaped', 'device')

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

        circle('head',13,15,7)
        path('shoulders',(6,42),[(6,37),((13,30),7,7,True),((26,42),13,12,True)])
        path('device',(28,6),[(42,6),(42,26),(34,26),(34,14),(28,14),(28,6)],True)
