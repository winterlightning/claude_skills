"""A broad three-lobed bonsai with a gently curved trunk in a shallow rounded pot."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1186f9b-7f40-5c04-a52b-582661eef1cc'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/bonsai_e1186f9b-7f40-5c04-a52b-582661eef1cc.svg'
AUTHOR = 'gpt-6'


class CurvedTrunkBonsai(Solo48):
    icon_id = 'curved-trunk-bonsai'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('bonsai', 'tree', 'plant', 'pot', 'foliage', 'garden', 'decor')

    def build(self) -> None:
        self.add_arc('crown-left', (2,16), (12,6), radius_x=10)
        self.add_line('crown-step-left', (12,6), (16,6))
        self.add_arc('crown-top', (16,6), (32,6), radius_x=8, radius_y=4)
        self.add_line('crown-step-right', (32,6), (36,6))
        self.add_arc('crown-right', (36,6), (46,16), radius_x=10)
        self.add_arc('crown-lower-right', (46,16), (40,22), radius_x=6)
        self.add_line('crown-base-right', (40,22), (20,22))
        self.add_line('crown-base-left', (20,22), (8,22))
        self.add_arc('crown-lower-left', (8,22), (2,16), radius_x=6)
        self.add_contour('crown', 'crown-left','crown-step-left','crown-top','crown-step-right','crown-right','crown-lower-right','crown-base-right','crown-base-left','crown-lower-left', closed=True)
        self.add_polyline('pot-rim', (6,36), (24,36), (42,36))
        self.add_arc('pot-right', (42,36), (32,46), radius_x=10)
        self.add_line('pot-bottom', (32,46), (16,46))
        self.add_arc('pot-left', (16,46), (6,36), radius_x=10)
        self.add_contour('pot-bowl','pot-right','pot-bottom','pot-left')
        self.relate('connect','pot-rim','pot-bowl')
        
        self.add_arc('trunk-upper', (20,22), (22,29), radius_x=13, sweep=False)
        self.add_arc('trunk-lower', (22,29), (24,36), radius_x=13)
        self.add_contour('trunk','trunk-upper','trunk-lower')
        self.relate('connect','trunk','crown')
        self.relate('connect','trunk','pot-rim')
