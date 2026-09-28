"""Deep learning amis: a vertical chain of three network nodes joined by short
links -- the layered-network mark of the original.

Revision (disapproved, reason not recorded): the rejected drawing squeezed the
three nodes into touching circles inside a rounded tile, where they fused into one
blob and the linked chain of the original did not read. The nodes are now
separate rings with visible links between them.

Symbol plan: mirror axis x=24. Three radius-5 rings on x=24 at y=9, 24 and 39,
joined by 5-unit links; the chain's ends touch radius 20 about (24,24), the
CIRCLE keyshape. Radius 5 keeps the rings as large as the reference's circles (a radius-3
attempt, attempts/radius3-rings-attempt.py.txt, read as dots on a rod).
Omissions: the rounded tile around the chain. Inside a 36-unit tile three
separate rings need 8 clearance to the tile at both ends and visible links
(about 46 units); attempts/tile-chain-attempt.py.txt kept the tile and failed the
build gate's ring-to-tile spacing.
Lucide construction: 'git-commit-vertical' ring-on-line.
Keyshape CIRCLE: the chain's top (24,4) and bottom (24,44) sit on radius 20.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7a5b5f1c-a452-53d7-9ba0-6715c718230c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__deep-learning-amis/20260926T182653Z-thuan-mac-1/reference/deep learning amis_7a5b5f1c-a452-53d7-9ba0-6715c718230c.svg"
AUTHOR = "claude-opus-5-5"

CX, NODE_R = 24, 5
NODES = (9, 24, 39)


class DeepLearningAmis(Solo48):
    icon_id = "deep-learning-amis"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology"
    aliases = ("neural-chain", "deep-learning")
    keywords = ("deep", "learning", "neural", "network", "nodes", "ai", "machine", "learning")

    def build(self) -> None:
        for i, y in enumerate(NODES):
            n = f"node-{i}"
            self.add_arc(f"{n}-a", (CX, y - NODE_R), (CX + NODE_R, y), radius_x=NODE_R)
            self.add_arc(f"{n}-b", (CX + NODE_R, y), (CX, y + NODE_R), radius_x=NODE_R)
            self.add_arc(f"{n}-c", (CX, y + NODE_R), (CX - NODE_R, y), radius_x=NODE_R)
            self.add_arc(f"{n}-d", (CX - NODE_R, y), (CX, y - NODE_R), radius_x=NODE_R)
            self.add_contour(n, f"{n}-a", f"{n}-b", f"{n}-c", f"{n}-d", closed=True)
        for i in range(2):
            link = f"link-{i}"
            self.add_line(link, (CX, NODES[i] + NODE_R), (CX, NODES[i + 1] - NODE_R))
            self.relate("connect", link, f"node-{i}")
            self.relate("connect", link, f"node-{i + 1}")
