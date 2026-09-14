"""Concentric tape roll with a left-unrolling notched strip; narrow tape end broadened."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14c7e37b-22e9-5795-afe4-6e9dfe2e84a2'
SOURCE_PATH = 'pictographic-primitives/tools/duct tape_14c7e37b-22e9-5795-afe4-6e9dfe2e84a2.svg'
AUTHOR = 'gpt-6'

class TapeRollNotchedStrip(Solo48):
    icon_id = 'tape-roll-notched-strip'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('tape', 'duct tape', 'roll', 'adhesive', 'sticky', 'strip', 'repair', 'packing')

    def build(self) -> None:

        def circle(n, x, y, r):
            self.add_arc(n+'-a', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(n+'-b', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)

        circle('roll',28,24,16)
        circle('core',28,24,7)
        self.add_polyline('strip',(12,24),(6,24),(9,32),(6,40),(28,40))
        self.relate('connect','strip','roll')
