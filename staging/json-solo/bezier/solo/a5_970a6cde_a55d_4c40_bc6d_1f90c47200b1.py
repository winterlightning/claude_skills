"""A5 (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '970a6cde-a55d-4c40-bc6d-1f90c47200b1'
SOURCE_PATH = 'icons-json/state/A5_970a6cde-a55d-4c40-bc6d-1f90c47200b1.json'
AUTHOR = 'json_to_solo'

class A5State(Solo48):
    icon_id = 'a5-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('a5', 'state')

    def build(self):
        self.add_line('e0', (21, 40), (15, 10))
        self.add_line('e1', (11, 9), (4, 40))
        self.add_line('e2', (7, 29), (19, 29))
        self.add_line('e3', (43, 8), (33, 8))
        self.add_line('e4', (33, 8), (31, 23))
        self.add_bezier('e5', (15, 10), ((14.682, 8.535), (14.145, 8.012), (12.936, 8.012)), ((12.818, 8.012), (12.7, 8), (12.591, 8)), ((12.527, 8.012), (12.473, 8.012), (12.418, 8.025)), ((11.827, 8.025), (11.182, 8.249), (11, 9)))
        self.add_bezier('e6', (31, 23), ((32.355, 21.683), (34.055, 20.431), (35.718, 20.025)), ((40, 18.978), (43.991, 22.511), (43.991, 28.665)), ((43.991, 28.846), (44, 29.028), (44, 29.21)), ((44, 29.213), (44, 29.216), (44, 29.218)), ((44, 29.477), (43.991, 29.748), (43.991, 30.006)), ((43.991, 34.646), (41.509, 39.975), (37.745, 39.975)), ((37.645, 39.988), (37.536, 39.988), (37.436, 40)), ((37.327, 40), (37.218, 40), (37.109, 40)), ((34.427, 40), (31.973, 38.36), (31, 35)))
        self.add_contour('c0', 'e0', 'e5', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e4', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
