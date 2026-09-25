"""Signature sign (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '854e9a2a-e250-5f3f-9ead-c9b63e43eb2f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/signature sign_854e9a2a-e250-5f3f-9ead-c9b63e43eb2f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class SignatureSign(Solo48):
    icon_id = 'signature-sign'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('signature', 'sign', 'interface-essential')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (39, 31), (38, 28))
        self.add_line('e1', (25, 30), (26, 25))
        self.add_line('e2', (20, 21), (15, 24))
        self.add_bezier('e3', (44, 32), ((42.555, 32.354), (40.209, 33.524), (39.118, 32.109)), ((38.809, 31.714), (39.164, 31.446), (39, 31)))
        self.add_bezier('e4', (38, 28), ((37.755, 27.739), (37.118, 27.436), (36.755, 27.309)), ((36.182, 27.124), (34.791, 28.261), (34.409, 28.573)), ((32.6, 30.013), (30.945, 31.722), (28.718, 32.615)), ((25.991, 33.709), (24.491, 32.813), (25, 30)))
        self.add_bezier('e5', (26, 25), ((26.436, 22.6), (24.709, 20.909), (22.145, 21.103)), ((21.555, 21.154), (20.5, 20.773), (20, 21)))
        self.add_bezier('e6', (15, 24), ((14.455, 24.253), (13.845, 24.648), (13.336, 24.96)), ((10.427, 26.728), (7.809, 28.859), (5.855, 31.554)), ((5, 32.741), (4, 34.265), (4, 35.756)), ((4.009, 36.042), (4.009, 36.168), (4.018, 36.295)), ((4.018, 37.912), (5.3, 40), (7.291, 40)), ((10.482, 39.992), (12.573, 37.069), (13.818, 34.863)), ((15.727, 31.495), (16.864, 26.636), (17.127, 22.821)), ((17.218, 21.558), (17.109, 20.244), (17.064, 18.981)), ((17.027, 17.819), (17.027, 16.615), (16.827, 15.469)), ((16.355, 12.758), (15.055, 9.491), (12.073, 8.396)), ((11.682, 8.253), (11.145, 8.017), (10.718, 8.017)), ((10.582, 8.008), (10.436, 8.008), (10.3, 8)), ((10.15, 8), (10.007, 8.008), (9.873, 8.008)), ((9.073, 8.008), (8.364, 8.261), (7.673, 8.615)), ((4.836, 10.063), (4, 13.331), (4.509, 16.152)), ((4.864, 17.575), (6, 18.922), (7, 20)))
        self.add_contour('c0', 'e3', 'e0', 'e4', 'e1', 'e5', 'e2', 'e6', closed=False)
