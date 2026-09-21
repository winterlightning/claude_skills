"""15 (other), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '374885d3-0df3-4239-bb81-0f1c062cd2fb'
SOURCE_PATH = 'icons-json/other/15_374885d3-0df3-4239-bb81-0f1c062cd2fb.json'
AUTHOR = 'json_to_solo'

class Icon15(Solo48):
    icon_id = 'icon-15'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('other',)

    def build(self):
        self.add_line('e0', (12, 8), (12, 40))
        self.add_line('e1', (42, 8), (29, 8))
        self.add_line('e2', (29, 8), (27, 22))
        self.add_bezier('e3', (4, 14), ((4.009, 14), (4.009, 13.886), (4.018, 13.886)), ((4.018, 13.827), (4.791, 13.541), (4.855, 13.516)), ((5.673, 13.145), (6.473, 12.733), (7.236, 12.286)), ((9.191, 11.158), (10.464, 9.558), (12, 8)))
        self.add_bezier('e4', (27, 22), ((28.564, 20.88), (29.982, 20.303), (31.936, 19.907)), ((38.245, 18.653), (43.982, 22.644), (43.982, 28.682)), ((43.982, 28.867), (44, 29.061), (44, 29.255)), ((44, 29.259), (44, 29.262), (44, 29.266)), ((44, 29.507), (43.982, 29.747), (43.982, 29.987)), ((43.982, 34.931), (40.318, 39.992), (34.536, 39.992)), ((34.427, 40), (34.309, 40), (34.2, 40)), ((34.064, 40), (33.927, 39.992), (33.8, 39.992)), ((30.182, 39.992), (27.118, 38.183), (26, 35)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e4')
