'Six-leaf vine: six alternating curved leaves with clear counters and a shared stem, preserving the alternating rhythm.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5044236b-6b82-4b28-beb5-504a9abb027a'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/hanging plant 4_5044236b-6b82-4b28-beb5-504a9abb027a.svg'
AUTHOR = 'gpt-6'

class SixLeafHangingVine(Solo48):
    icon_id = 'six-leaf-hanging-vine'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('vine', 'hanging', 'leaves', 'stem', 'foliage', 'plant', 'botanical')

    def build(self) -> None:
        # Alternating pointed leaves share a stem. Leaf height is six; top/bottom apices are exact.
        self.add_polyline('stem',(24,7),(24,14),(24,21),(24,28),(24,35),(24,41))
        for j,y in enumerate((7,14,21,28,35,41)):
            tip=40 if j%2==0 else 8
            mid=(24+tip)/2
            self.add_bezier(f'leaf-{j}-a',(24,y),((mid,y-4),(tip,y-4),(tip,y)),((tip,y+4),(mid,y+4),(24,y)))
            self.add_contour(f'leaf-{j}',f'leaf-{j}-a',closed=True)
            self.relate('connect',f'leaf-{j}','stem')
