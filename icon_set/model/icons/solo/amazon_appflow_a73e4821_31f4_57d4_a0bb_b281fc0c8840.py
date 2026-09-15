"""Amazon AppFlow.

Plan: SQUARE centerlines (6,6)-(42,42); two open angular flow paths related by a half turn, each terminating at an inward arrowhead.
Construction references: Lucide repeat-2: paired return paths and shared arrow-tip attachment; source owns the diagonal interlock.
Reduction: Shortened the two loose outer ends and opened the arrowhead spacing to preserve the interlocked flow at 48px.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a73e4821-31f4-57d4-a0bb-b281fc0c8840'
SOURCE_PATH = 'pictographic-primitives/apps/amazon appflow_a73e4821-31f4-57d4-a0bb-b281fc0c8840.svg'
SOURCE_ICON_IDS = ('a73e4821-31f4-57d4-a0bb-b281fc0c8840',)
SOURCE_PATHS = ('pictographic-primitives/apps/amazon appflow_a73e4821-31f4-57d4-a0bb-b281fc0c8840.svg',)
AUTHOR = 'gpt-6'


class AmazonAppflow(Solo48):
    icon_id = 'amazon-appflow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'apps'
    aliases = ()
    keywords = ('amazon', 'appflow')

    def build(self) -> None:
        for side in range(2):
            def point(x,y): return (x,y) if side == 0 else (48-x,48-y)
            k=f"flow-{side}"
            points=[(42,18),(30,6),(22,8),(16,28)]
            self.add_polyline(k,*[point(*p) for p in points])
            self.add_polyline(k+"-head",point(12,20),point(16,28),point(20,28))
            self.relate("connect",k,k+"-head")
