"""Palm tree on a small island and waterline, reconstructed on SOLO48.

The source's coconuts, split frond tips, and sand texture are omitted at native
size.  Five clean fronds, one leaning trunk, a domed mound, and a single wavy
waterline retain the three-part tropical-island read.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Solo48

AUTHOR = 'astra-chatgpt'


class TropicalIslandWithPalmTree(Solo48):
    """A wind-bent palm rising from a domed island above wavy water."""

    icon_id = "tropical-island-with-palm-tree"
    keyshape = Keyshape.SQUARE
    category = "objects/nature"
    aliases = ("tropical-island", "palm-tree-island", "island-palm")
    keywords = (
        "island", "palm", "tree", "beach", "tropical", "vacation",
        "holiday", "sea", "sand", "water",
    )

    def build(self) -> None:
        # Two side pairs and one rising curved frond share a single crown.
        # The fifth leaf and trunk retain a natural lean; the top leaf
        # pins the SQUARE centreline top at y=2.
        self.add_arc("frond-upper-left", (24, 14), (5, 9), radius_x=21, sweep=False)
        self.add_arc("frond-upper-right", (24, 14), (43, 9), radius_x=21)
        self.add_arc("frond-lower-left", (24, 14), (5, 20), radius_x=19)
        self.add_arc("frond-lower-right", (24, 14), (43, 20), radius_x=19, sweep=False)
        self.add_arc("frond-top", (24, 14), (26, 2), radius_x=12, sweep=False)
        self.add_arc("trunk", (24, 14), (24, 30), radius_x=24)

        # Matching ellipse quarters meet horizontally at the mound's apex.
        self.add_arc("mound-left", (7, 40), (24, 30), radius_x=17, radius_y=10)
        self.add_arc("mound-right", (24, 30), (41, 40), radius_x=17, radius_y=10)
        self.add_contour("mound", "mound-left", "mound-right")

        # Five mirrored lobes share vertical tangents at their crossings and
        # horizontal tangents at each crest/trough. Split the outer crests at
        # the mound contacts so those connections have explicit endpoints.
        self.add_arc("water-crest-left-a", (2, 43), (7, 40), radius_x=5, radius_y=3)
        self.add_arc("water-crest-left-b", (7, 40), (12, 43), radius_x=5, radius_y=3)
        self.add_arc("water-trough-left", (12, 43), (20, 43), radius_x=4, radius_y=3, sweep=False)
        self.add_arc("water-crest-centre", (20, 43), (28, 43), radius_x=4, radius_y=3)
        self.add_arc("water-trough-right", (28, 43), (36, 43), radius_x=4, radius_y=3, sweep=False)
        self.add_arc("water-crest-right-a", (36, 43), (41, 40), radius_x=5, radius_y=3)
        self.add_arc("water-crest-right-b", (41, 40), (46, 43), radius_x=5, radius_y=3)
        self.add_contour(
            "waterline", "water-crest-left-a", "water-crest-left-b",
            "water-trough-left", "water-crest-centre", "water-trough-right",
            "water-crest-right-a", "water-crest-right-b",
        )

        for frond in (
            "frond-upper-left", "frond-upper-right",
            "frond-lower-left", "frond-lower-right", "frond-top",
        ):
            self.relate("connect", "trunk", frond)
        self.relate("connect", "trunk", "mound")
        self.relate("connect", "mound", "waterline")
