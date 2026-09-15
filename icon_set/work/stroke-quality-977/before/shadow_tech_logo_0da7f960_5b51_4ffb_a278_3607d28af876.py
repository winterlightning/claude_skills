"""Shadow tech logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0da7f960-5b51-4ffb-a278-3607d28af876'
SOURCE_PATH = 'pictographic-primitives/logos/shadow tech logo_0da7f960-5b51-4ffb-a278-3607d28af876.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ShadowTechLogo(Solo48):
    icon_id = 'shadow-tech-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('shadow', 'tech', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (25, 42), (23, 42))
        self.add_bezier('e1', (23, 42), ((24.865, 39.889), (26.765, 38.024), (26.88, 35.07)), ((27.109, 28.868), (21.202, 24.344), (15.27, 26.135)), ((12.987, 26.823), (11.105, 28.41), (10.009, 30.529)), ((9.633, 31.249), (8.806, 33.671), (8.725, 33.679)), ((8.405, 33.008), (8.095, 32.329), (7.775, 31.658)), ((7.767, 31.634), (7.751, 31.601), (7.743, 31.576)), ((6.736, 29.367), (6.008, 26.954), (6.008, 24.507)), ((6.008, 24.419), (6, 24.322), (6, 24.233)), ((6, 24.232), (6, 24.23), (6, 24.229)), ((6, 23.975), (6.008, 23.714), (6.008, 23.46)), ((6.008, 14.255), (14.19, 6.008), (23.419, 6.008)), ((23.516, 6.008), (23.604, 6), (23.701, 6)), ((23.702, 6), (23.704, 6), (23.705, 6)), ((23.992, 6), (24.286, 6.008), (24.573, 6.008)), ((33.646, 6.008), (41.992, 14.01), (41.992, 23.165)), ((41.992, 23.262), (42, 23.359), (42, 23.455)), ((42, 23.457), (42, 23.458), (42, 23.46)), ((42, 23.779), (41.992, 24.098), (41.992, 24.417)), ((41.992, 31.936), (36.551, 38.4), (29.752, 40.977)), ((28.353, 41.509), (26.643, 41.992), (25.129, 41.992)), ((25.023, 41.992), (25.106, 42), (25, 42)))
        self.add_contour('c0', 'e1', 'e0', closed=True)
