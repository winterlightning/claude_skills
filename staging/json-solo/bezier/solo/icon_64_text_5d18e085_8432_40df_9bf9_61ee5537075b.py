"""64 (text) (text), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d18e085-8432-40df-9bf9-61ee5537075b'
SOURCE_PATH = 'icons-json/text/64 (text)_5d18e085-8432-40df-9bf9-61ee5537075b.json'
AUTHOR = 'json_to_solo'

class Icon64TextText(Solo48):
    icon_id = 'icon-64-text-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('text',)

    def build(self):
        self.add_line('e0', (44, 33), (29, 33))
        self.add_line('e1', (29, 33), (41, 8))
        self.add_line('e2', (41, 8), (41, 40))
        self.add_bezier('e3', (19, 13), ((17.582, 10.612), (14.918, 8.012), (12.509, 8.012)), ((12.436, 8.012), (12.355, 8), (12.273, 8)), ((12.109, 8), (11.955, 8.025), (11.791, 8.025)), ((10.809, 8.025), (9.755, 8.665), (8.9, 9.268)), ((5.291, 11.815), (4.018, 16.948), (4.018, 22.203)), ((4.018, 23.52), (4, 24.837), (4, 26.154)), ((4, 27.077), (4, 28.077), (4, 29)))
        self.add_bezier('e4', (4, 29), ((4.145, 30.526), (4.218, 32.049), (4.545, 33.538)), ((5.509, 37.846), (8.418, 39.988), (11.664, 39.988)), ((11.782, 40), (11.909, 40), (12.036, 40)), ((12.145, 40), (12.255, 40), (12.355, 39.988)), ((18.673, 39.988), (20.745, 27.889), (16.691, 22.535)), ((14.936, 20.209), (12.155, 19.606), (9.818, 20.234)), ((8.391, 20.615), (7.1, 21.588), (6.118, 23.04)), ((5.282, 24.258), (4.018, 27.04), (4.018, 28.812)), ((4.018, 28.849), (4, 28.963), (4, 29)))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e0', 'e1', 'e2')
        self.add_contour('c2', 'e4', closed=True)
        self.relate('connect', 'c0', 'c2')
