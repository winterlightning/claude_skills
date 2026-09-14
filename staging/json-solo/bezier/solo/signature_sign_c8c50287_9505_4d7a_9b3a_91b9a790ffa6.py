"""Signature sign (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8c50287-9505-4d7a-9b3a-91b9a790ffa6'
SOURCE_PATH = 'icons-json/interface-essential/signature sign_c8c50287-9505-4d7a-9b3a-91b9a790ffa6.json'
AUTHOR = 'json_to_solo'

class SignatureSignC8c50287(Solo48):
    icon_id = 'signature-sign-c8c50287'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('signature', 'sign', 'interface-essential')

    def build(self):
        self.add_line('e0', (36, 34), (38, 29))
        self.add_line('e1', (30, 28), (25, 36))
        self.add_line('e2', (19, 33), (25, 18))
        self.add_line('e3', (14, 15), (4, 40))
        self.add_bezier('e4', (44, 35), ((43.5, 35.825), (44, 34.892), (43.809, 35.68)), ((43.7, 35.877), (43.436, 36.062), (43.309, 36.222)), ((42.782, 36.849), (42.4, 37.698), (41.836, 38.302)), ((41.045, 39.151), (39.773, 39.975), (38.736, 39.975)), ((38.682, 39.988), (38.627, 39.988), (38.564, 40)), ((38.518, 40), (38.464, 39.988), (38.409, 39.988)), ((36.009, 39.988), (34.973, 36.782), (36, 34)))
        self.add_bezier('e5', (38, 29), ((39.082, 26.058), (37.782, 20.935), (34.709, 22.142)), ((32.764, 22.892), (31.236, 26.055), (30, 28)))
        self.add_bezier('e6', (25, 36), ((24.445, 36.874), (21.855, 40), (21.091, 40)), ((21.018, 40), (20.945, 40), (20.864, 39.988)), ((18.118, 39.988), (18.2, 35.178), (19, 33)))
        self.add_bezier('e7', (25, 18), ((26.282, 14.542), (26.464, 8.012), (22.455, 8.012)), ((22.293, 8.012), (22.124, 8), (21.954, 8)), ((21.951, 8), (21.948, 8), (21.945, 8)), ((21.509, 8), (21.073, 8.025), (20.636, 8.025)), ((17.809, 8.025), (15.255, 11.923), (14, 15)))
        self.add_contour('c0', 'e4', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3')
