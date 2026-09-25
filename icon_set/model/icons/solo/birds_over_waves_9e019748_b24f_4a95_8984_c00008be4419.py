"""Three V-shaped birds fly over two rows of waves. HRECT extremes (4,8)-(44,40); mirrored outer birds frame the lower middle bird, and waves share one repeat definition.
Reduction: Reduced three wave rows to two.
Lucide construction: waves-horizontal
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e019748-b24f-4a95-8984-c00008be4419'
SOURCE_PATH = 'pictographic-primitives/nature/outdoors water birds_9e019748-b24f-4a95-8984-c00008be4419.svg'
AUTHOR = 'gpt-6'


class BirdsOverWaves(Solo48):
    icon_id = 'birds-over-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    categories = ("nature", "primitives")
    aliases = ()
    keywords = ('birds', 'sea', 'waves', 'water', 'ocean', 'seagull', 'outdoors', 'coast')

    def build(self) -> None:
        for i,(x,y) in enumerate(((4,8),(20,10),(36,8))):
            self.add_polyline(f"bird-{i}",(x,y),(x+4,y+4),(x+8,y))
        for row,y in enumerate((25,37)):
            names=[]
            for i in range(4):
                n=f"wave-{row}-{i}"
                self.add_arc(n,(4+i*10,y),(14+i*10,y),radius_x=5,radius_y=3,sweep=i%2==0)
                names.append(n)
            self.add_contour(f"wave-row-{row}",*names)
