"""A notched tulip cup on a straight stem with paired curved leaves. VRECT extremes (8,4)-(40,44).
Reduction: None.
Lucide construction: flower-2, leaf
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d724858-fd0e-4b7f-a29c-165c62b8e0f2'
SOURCE_PATH = 'pictographic-primitives/nature/flower_3d724858-fd0e-4b7f-a29c-165c62b8e0f2.svg'
AUTHOR = 'gpt-6'


class TulipWithCurvedLeaves(Solo48):
    icon_id = 'tulip-with-curved-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('tulip', 'flower', 'bloom', 'stem', 'leaves', 'spring', 'garden', 'nature')

    def build(self) -> None:
        # Mirrored cup: one V notch and two matching quarter-circle shoulders.
        nodes=[(12,16),(12,4),(24,12),(36,4),(36,16)]
        for i,(a,b) in enumerate(zip(nodes,nodes[1:]),1):
            self.add_line(f"crown-{i}",a,b)
        self.add_arc("cup-right", (36,16), (24,28), radius_x=12)
        self.add_arc("cup-left", (24,28), (12,16), radius_x=12)
        self.add_contour("bloom", "crown-1", "crown-2", "crown-3", "crown-4", "cup-right", "cup-left", closed=True)
        self.add_line("stem", (24,28), (24,44))
        self.relate("connect", "cup-right", "stem")
        self.relate("connect", "cup-left", "stem")
        # Paired open leaf strokes retain broad negative space at the stem.
        self.add_arc("leaf-left", (8,34), (24,44), radius_x=16, radius_y=10)
        self.add_arc("leaf-right", (24,44), (40,34), radius_x=16, radius_y=10)
        self.relate("connect", "stem", "leaf-left")
        self.relate("connect", "stem", "leaf-right")
