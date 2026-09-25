"""A notched tulip bloom on a stem with paired closed pointed leaves. VRECT extrema (8,4)-(40,44); mirrored leaf lenses and a shared stem node preserve equality.
Reduction: Removed the tiny tip diamond and overlapping petal seam; retained closed pointed leaves.
Lucide construction: flower-2, leaf
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '877eab6e-11b5-5b08-a6d1-b6c6a5072103'
SOURCE_PATH = 'pictographic-primitives/nature/flower_877eab6e-11b5-5b08-a6d1-b6c6a5072103.svg'
AUTHOR = 'gpt-6'


class TulipWithLeaves(Solo48):
    icon_id = 'tulip-with-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('tulip', 'flower', 'bloom', 'stem', 'leaves', 'spring', 'garden', 'nature')

    def build(self) -> None:
        # Mirrored cup: one V notch and two matching quarter-circle shoulders.
        nodes=[(12,12),(12,4),(24,10),(36,4),(36,12)]
        for i,(a,b) in enumerate(zip(nodes,nodes[1:]),1):
            self.add_line(f"crown-{i}",a,b)
        self.add_arc("cup-right", (36,12), (24,24), radius_x=12)
        self.add_arc("cup-left", (24,24), (12,12), radius_x=12)
        self.add_contour("bloom", "crown-1", "crown-2", "crown-3", "crown-4", "cup-right", "cup-left", closed=True)
        self.add_line("stem", (24,24), (24,44))
        self.relate("connect", "cup-right", "stem")
        self.relate("connect", "cup-left", "stem")
        # Mirrored pointed leaf lenses share one stem endpoint.
        for side,tip in (("left",(8,30)),("right",(40,30))):
            sweep=side=="left"
            self.add_arc(side+"-outer",tip,(24,44),radius_x=16,radius_y=14,sweep=sweep)
            self.add_arc(side+"-inner",(24,44),tip,radius_x=16,radius_y=14,sweep=sweep)
            self.add_contour(side+"-leaf",side+"-outer",side+"-inner",closed=True)
            self.relate("connect","stem",side+"-outer")
            self.relate("connect","stem",side+"-inner")
