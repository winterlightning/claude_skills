"""A simple circular bug body crossed by a horizontal stroke, with two short diagonal antennae above and two short diagonal legs below. Exclude phone/browser framing; do not substitute a segmented beetle.

Plan: Circular body, horizontal crossbar, and four mirrored diagonal appendages. Bounds (2,2)-(30,30).
Construction reference: Lucide bug: mirrored attached appendages; retain the source circular body and crossbar."""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '600bc5a2-131a-4e43-b134-f5e672684c21'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone bug_600bc5a2-131a-4e43-b134-f5e672684c21.svg'
SOURCE_ICON_IDS = ('600bc5a2-131a-4e43-b134-f5e672684c21', '0a0feef2-02cf-4796-98f1-93d8a372ce93')
AUTHOR = 'gpt-6'

class RoundBugWithCrossbarSymbol(Symbol32):
    icon_id = 'round-bug-with-crossbar-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('round', 'bug', 'with', 'crossbar', 'symbol')

    def build(self) -> None:
        # Radius ten, exact diagonal attachment points at offsets 6,8.
        points=[(10,8),(22,8),(26,16),(22,24),(10,24),(6,16)]
        for i,p in enumerate(points):
            self.add_arc(f'body-{i}',p,points[(i+1)%len(points)],radius_x=10)
        self.add_contour('body',*(f'body-{i}' for i in range(len(points))),closed=True)
        self.add_line('crossbar',(2,16),(30,16))
        self.relate('connect','body','crossbar')
        for i,(a,b) in enumerate([((10,8),(4,2)),((22,8),(28,2)),((10,24),(4,30)),((22,24),(28,30))]):
            self.add_line(f'leg-{i}',a,b)
            self.relate('connect','body',f'leg-{i}')
