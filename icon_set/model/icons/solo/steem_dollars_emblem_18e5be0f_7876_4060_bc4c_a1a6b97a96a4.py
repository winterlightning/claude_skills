"""Three repeated S waves. SQUARE extremes (6,6)-(42,42). Collapse narrow doubled ribbons to single smooth strokes to preserve three distinct waves. Shared repeated definition and paired controls; no useful exact Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='18e5be0f-7876-4060-bc4c-a1a6b97a96a4'
SOURCE_PATH='pictographic-primitives/money/virtual coin crypto steem dollars_18e5be0f-7876-4060-bc4c-a1a6b97a96a4.svg'
AUTHOR='gpt-6'

class SteemDollarsEmblem(Solo48):
    icon_id='steem-dollars-emblem'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "money"
    aliases=()
    keywords=('steem', 'dollars', 'crypto', 'ribbon', 'wave', 'emblem')

    def build(self):
        for n,cx in enumerate((10,24,38)):
            self.add_bezier(f'wave-{n}',(cx+4,6),((cx,10),(cx-4,12),(cx-4,18)),((cx-4,24),(cx+4,24),(cx+4,30)),((cx+4,36),(cx,38),(cx-4,42)))
