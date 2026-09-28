"""Partly occluded record rim meets a broad hand in the lower right. Merge fine fingers into one extended group plus thumb; omit the obscured spindle hole and sheen. Centerline extremes (6,6)-(42,42). Human reference: full_body_ref.png continuous round-ended limbs; Lucide hand and disc. No detached head."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='65e3fe01-2acf-45bd-91bb-84820fe24a5a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dj-hand-on-record/20260927T133815Z-thuan-mac-1/reference/modern music dj tape_65e3fe01-2acf-45bd-91bb-84820fe24a5a.svg'
AUTHOR = "gpt-6"

class DjHandOnRecord(Solo48):
    icon_id='dj-hand-on-record'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    categories = ("primitives", "music")
    aliases=()
    keywords=('dj', 'turntable', 'record', 'scratch', 'hand', 'vinyl', 'mixing', 'music')

    def build(self):
        # An exposed vinyl rim wraps around three stepped fingertips.
        # The hand intentionally occludes the lower right side of the record.
        self.add_bezier('record', (39, 16),
                        ((35, 8), (30, 6), (24, 6)),
                        ((14, 6), (6, 14), (6, 24)),
                        ((6, 34), (11, 40), (18, 42)))
        self.add_dot('spindle', (20, 18))
        self.add_line('hand-base', (18, 42), (36, 42))
        self.add_bezier('hand-fingers', (36, 42),
                        ((42, 42), (42, 39), (42, 34)),
                        ((39, 29), (35, 24), (32, 22)),
                        ((28, 22), (27, 26), (28, 29)),
                        ((24, 26), (20, 28), (21, 32)),
                        ((22, 35), (22, 38), (18, 42)))
        self.add_contour('hand-outline', 'hand-base', 'hand-fingers', closed=True)
        self.relate('connect', 'record', 'hand-outline')
