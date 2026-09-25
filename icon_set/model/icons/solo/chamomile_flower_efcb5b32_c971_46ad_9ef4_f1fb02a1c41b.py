"""A front-facing flower with eight rounded radial lobes. SQUARE extremes (6,6)-(42,42).
Reduction: Reduced twelve narrow petals to eight broader petals; removed radial separators.
Lucide construction: flower
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'efcb5b32-c971-46ad-9ef4-f1fb02a1c41b'
SOURCE_PATH = 'pictographic-primitives/nature/chamomile_efcb5b32-c971-46ad-9ef4-f1fb02a1c41b.svg'
AUTHOR = 'gpt-6'


class ChamomileFlower(Solo48):
    icon_id = 'chamomile-flower'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('chamomile', 'daisy', 'flower', 'petals', 'bloom', 'herbal', 'nature', 'botanical')

    def build(self) -> None:
        # Eight radial lobes in a quarter-turn symmetric series.
        nodes = [(18,12),(30,12),(36,18),(36,30),(30,36),(18,36),(12,30),(12,18)]
        members=[]
        for i,start in enumerate(nodes):
            end=nodes[(i+1)%len(nodes)]
            name=f"petal-{i}"
            self.add_arc(name,start,end,radius_x=6 if i%2==0 else 5,large_arc=bool(i%2))
            members.append(name)
        self.add_contour("petals",*members,closed=True)
        self.add_arc("disc-a", (19,24), (29,24), radius_x=5)
        self.add_arc("disc-b", (29,24), (19,24), radius_x=5)
        self.add_contour("disc", "disc-a", "disc-b", closed=True)
