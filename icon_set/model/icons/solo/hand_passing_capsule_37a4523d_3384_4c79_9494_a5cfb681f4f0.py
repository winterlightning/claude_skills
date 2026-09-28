"""Hand Passing Capsule to Another Hand.

Symbol plan: Horizontal capsule passed between opposing hands. Rounded capsule at center; hand from upper right and palm from lower left. Visible (4,4)-(44,44). Omit tiny fingers and capsule seam.
Construction references: human_ref/full_body_ref.png: minimal rounded limb strokes; Lucide pill: capsule ends; hand-coins: open receiving palm.
Original reference: SOURCE_PATH below; preserved subject, re-authored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37a4523d-3384-4c79-9494-a5cfb681f4f0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/drugs dealer_37a4523d-3384-4c79-9494-a5cfb681f4f0.svg'
AUTHOR = 'gpt-6'


class HandPassingCapsule(Solo48):
    icon_id = 'hand-passing-capsule'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('hand', 'passing', 'capsule')

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

        path('capsule',(14,16),[(20,16),(26,16),((32,22),6,6,True),((26,28),6,6,True),(14,28),((14,16),6,6,True)],True)
        path('upper-hand',(42,6),[(34,8),(26,8),(20,16)])
        path('thumb',(42,18),[(36,22),(32,22)])
        self.relate('connect','upper-hand','capsule')
        self.relate('connect','thumb','capsule')
        path('lower-hand',(6,36),[(14,36),(22,42),(38,42)])
