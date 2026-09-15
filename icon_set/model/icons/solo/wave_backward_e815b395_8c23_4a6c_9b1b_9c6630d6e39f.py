"""wave-backward-interface-essential: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e815b395-8c23-4a6c-9b1b-9c6630d6e39f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/wave backward_e815b395-8c23-4a6c-9b1b-9c6630d6e39f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class WaveBackwardInterfaceEssential(Solo48):
    icon_id = 'wave-backward-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('wave', 'backward', 'interface-essential')

    def build(self):
        # Plan: VRECT_L; each wave is a single smooth run mirrored about its horizontal axis.
        # Reference: Geometric mirrored cubic wave construction.
        mirror = False

        def p(x,y):return (48-x,y) if mirror else (x,y)
        self.add_bezier('outer',p(22,4),(p(14,9),p(8,16),p(8,24)),(p(8,32),p(14,39),p(22,44)))
        self.add_bezier('inner',p(40,10),(p(34,14),p(30,19),p(30,24)),(p(30,29),p(34,34),p(40,38)))
