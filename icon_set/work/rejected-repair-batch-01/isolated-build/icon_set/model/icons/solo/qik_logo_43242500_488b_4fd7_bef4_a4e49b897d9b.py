"""Qik logo (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43242500-488b-4fd7-bef4-a4e49b897d9b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/qik logo_43242500-488b-4fd7-bef4-a4e49b897d9b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class QikLogo(Solo48):
    icon_id = 'qik-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('qik', 'logo', '_uncategorized')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (42, 42), (33, 33))
        self.add_bezier('e1', (33, 33), ((29.981, 35.471), (27.494, 37.181), (23.542, 37.705)), ((16.53, 38.629), (9.796, 34.522), (7.145, 28.009)), ((6.466, 26.34), (6.008, 24.458), (6.008, 22.65)), ((6.008, 22.505), (6, 22.352), (6, 22.207)), ((6, 21.905), (6.008, 21.619), (6.008, 21.325)), ((6.008, 13.429), (12.938, 6.008), (20.932, 6.008)), ((21.004, 6.008), (21.077, 6), (21.149, 6)), ((21.439, 6), (21.734, 6.008), (22.02, 6.008)), ((23.558, 6.008), (25.121, 6.368), (26.561, 6.892)), ((32.689, 9.134), (36.845, 14.943), (36.96, 21.464)), ((37.034, 25.735), (35.414, 29.555), (33, 33)))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=True)
        self.relate('connect', 'c0', 'c1')
