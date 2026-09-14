"""Organic tree (ecology), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20ca0045-a5f1-5d77-8e5b-2bce89d1e61d'
SOURCE_PATH = 'icons-json/ecology/organic tree_20ca0045-a5f1-5d77-8e5b-2bce89d1e61d.json'
AUTHOR = 'json_to_solo'

class OrganicTree20ca0045(Solo48):
    icon_id = 'organic-tree-20ca0045'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    aliases = ()
    keywords = ('organic', 'tree', 'ecology')

    def build(self):
        self.add_line('e0', (24, 19), (24, 44))
        self.add_line('e1', (19, 44), (29, 44))
        self.add_line('e2', (24, 33), (19, 33))
        self.add_bezier('e3', (19, 33), ((18.46, 33), (17.82, 32.909), (17.29, 32.8)), ((12.68, 31.882), (8.01, 27.973), (8.01, 23.418)), ((8.01, 23.275), (8, 23.132), (8, 22.989)), ((8, 22.986), (8, 22.984), (8, 22.982)), ((8, 22.773), (8.01, 22.573), (8.01, 22.364)), ((8.01, 20.236), (9.18, 18.1), (10.78, 16.6)), ((11.21, 16.191), (12.98, 14.864), (13.13, 14.582)), ((13.23, 14.409), (13.03, 13.745), (13.02, 13.536)), ((12.99, 12.564), (13.13, 11.591), (13.45, 10.664)), ((14.74, 6.882), (19.06, 4.009), (23.44, 4.009)), ((23.598, 4.009), (23.745, 4), (23.903, 4)), ((23.905, 4), (23.907, 4), (23.91, 4)), ((24.15, 4), (24.38, 4.009), (24.62, 4.009)), ((28.99, 4.009), (33.32, 6.9), (34.59, 10.682)), ((34.9, 11.609), (35.05, 12.582), (35.01, 13.555)), ((35, 13.764), (34.79, 14.427), (34.89, 14.6)), ((35.03, 14.845), (36.87, 16.236), (37.3, 16.645)), ((38.9, 18.236), (39.98, 20.536), (39.98, 22.709)), ((39.99, 22.843), (40, 22.986), (40, 23.121)), ((40, 23.123), (40, 23.125), (40, 23.127)), ((39.99, 23.209), (39.99, 23.291), (39.98, 23.364)), ((39.98, 25.009), (39.28, 26.727), (38.3, 28.082)), ((34.82, 32.927), (29.71, 33), (24, 33)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c0')
