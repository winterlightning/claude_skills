'Three spreading toes meet at one lower joint. SQUARE preserves long center toe and mirrored diagonal toes around x=24; shared junction is the sole attachment. Reference supplies three-toe arrangement; no useful exact Lucide match. Outline thickness reduced to round-ended strokes, with no rear toe added.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad358c09-b960-43ca-954d-80c6af3ca0cb'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/chicken footstep_ad358c09-b960-43ca-954d-80c6af3ca0cb.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'three-toed-bird-track'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Three Toed Bird Track',)
    keywords = ('bird', 'footprint', 'track', 'toes', 'animal', 'mark', 'nature')
    def build(self):
        joint=(24,42)
        for name,tip in (('left',(6,14)),('center',(24,6)),('right',(42,14))):
            self.add_line(name,joint,tip)
        self.relate('connect','left','center','right')
