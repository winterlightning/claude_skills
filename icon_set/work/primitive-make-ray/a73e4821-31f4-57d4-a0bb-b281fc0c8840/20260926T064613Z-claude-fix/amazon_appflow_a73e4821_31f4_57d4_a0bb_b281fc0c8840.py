"""Amazon AppFlow.

Plan: SQUARE centerlines (6,6)-(42,42); two open angular flow paths related by a half turn, each terminating at an inward arrowhead.
Construction references: Lucide repeat-2: paired return paths and shared arrow-tip attachment; source owns the diagonal interlock.
Reduction: Shortened the two loose outer ends and opened the arrowhead spacing to preserve the interlocked flow at 48px.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a73e4821-31f4-57d4-a0bb-b281fc0c8840'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__amazon-appflow/20260926T064521Z-thuan-mac/reference/amazon appflow_a73e4821-31f4-57d4-a0bb-b281fc0c8840.svg'
SOURCE_ICON_IDS = ('a73e4821-31f4-57d4-a0bb-b281fc0c8840',)
SOURCE_PATHS = ('pictographic-primitives/apps/amazon appflow_a73e4821-31f4-57d4-a0bb-b281fc0c8840.svg',)
AUTHOR = "claude-opus-5-5"


class AmazonAppflow(Solo48):
    icon_id = 'amazon-appflow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('amazon', 'appflow')

    def build(self) -> None:
        # Revision per review: each path is now the full outer half-hexagon of the reference -
        # a long diagonal shaft, the top edge, the corner, the side segment and a short
        # inward-facing end - and the two paths are point-symmetric about (24, 24)
        # (P -> (48 - x, 48 - y)). The arrowheads are small chevrons (arms about 4 long, about
        # 45 degrees either side of the shaft) aligned with the shafts, and the shafts are
        # longer and further apart (about 13 between them).
        for side in range(2):
            def point(x, y):
                return (x, y) if side == 0 else (48 - x, 48 - y)
            k = f"flow-{side}"
            points = [(17, 32), (22, 10), (33, 6), (42, 14), (40, 28), (37, 29)]
            self.add_polyline(k, *[point(*p) for p in points])
            self.add_polyline(k + "-head", point(*(15, 29)), point(*points[0]), point(*(19, 30)))
            self.relate("connect", k, k + "-head")
