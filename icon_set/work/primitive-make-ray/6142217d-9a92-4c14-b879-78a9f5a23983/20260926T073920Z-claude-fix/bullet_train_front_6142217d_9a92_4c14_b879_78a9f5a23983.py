"""Bullet train front; authored directly on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6142217d-9a92-4c14-b879-78a9f5a23983'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bullet-train-front/20260926T073831Z-thuan-mac/reference/railroad metro_6142217d-9a92-4c14-b879-78a9f5a23983.svg'
AUTHOR = "claude-opus-5-5"

class BulletTrainFront(Solo48):
    icon_id = 'bullet-train-front'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('bullet train', 'metro', 'train', 'front', 'railway', 'high speed', 'rail', 'subway')

    def build(self) -> None:
        # Redraw (no reviewer text; matched to the reference): an egg-shaped front - an r16 dome
        # about (24, 20), straight flanks x 8 and 40 down to y 32, r6 lower corners and a flat
        # base y 38 - with a closed trapezoid windshield, wide at the top as in the reference (top (18, 15)-(30, 15), bottom
        # (21, 23)-(27, 23), 8+ from the dome and flanks), an r3 headlight resting on the base at
        # (24, 38) (shared point) and two rails splaying from the base corners to (8, 44)/(40, 44).
        self.add_arc('roof-left', (8, 20), (24, 4), radius_x=16)
        self.add_arc('roof-right', (24, 4), (40, 20), radius_x=16)
        self.add_line('right-flank', (40, 20), (40, 32))
        self.add_arc('lower-right', (40, 32), (34, 38), radius_x=6)
        self.add_line('base-right', (34, 38), (24, 38))
        self.add_line('base-left', (24, 38), (14, 38))
        self.add_arc('lower-left', (14, 38), (8, 32), radius_x=6)
        self.add_line('left-flank', (8, 32), (8, 20))
        self.add_contour('body', 'roof-left', 'roof-right', 'right-flank', 'lower-right', 'base-right', 'base-left',
                         'lower-left', 'left-flank', closed=True)
        self.add_polyline('windshield', (18, 15), (30, 15), (27, 23), (21, 23), closed=True)
        self.add_arc('headlight-e', (24, 38), (27, 35), radius_x=3, sweep=False)
        self.add_arc('headlight-n', (27, 35), (24, 32), radius_x=3, sweep=False)
        self.add_arc('headlight-w', (24, 32), (21, 35), radius_x=3, sweep=False)
        self.add_arc('headlight-s', (21, 35), (24, 38), radius_x=3, sweep=False)
        self.add_contour('headlight', 'headlight-e', 'headlight-n', 'headlight-w', 'headlight-s', closed=True)
        self.relate('connect', 'body', 'headlight')
        self.add_line('left-rail', (14, 38), (8, 44))
        self.add_line('right-rail', (34, 38), (40, 44))
        self.relate('connect', 'left-rail', 'body')
        self.relate('connect', 'right-rail', 'body')
