"""A front-facing flower with eight rounded radial lobes. SQUARE extremes (6,6)-(42,42). Shallow petals make room for the eyes and smile.
Reduction: Removed the extra circular face border; retained eyes and curved smile.
Lucide construction: flower
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f439cc7d-8e34-5beb-ab1a-9677f1869dce'
SOURCE_PATH = 'pictographic-primitives/nature/flower_f439cc7d-8e34-5beb-ab1a-9677f1869dce.svg'
AUTHOR = 'gpt-6'


class SmilingFlower(Solo48):
    icon_id = 'smiling-flower'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-01"
    aliases = ()
    keywords = ('flower', 'smile', 'happy', 'face', 'petals', 'cheerful', 'kids', 'nature')

    def build(self) -> None:
        # Eight radial lobes in a quarter-turn symmetric series.
        nodes = [(16,10),(32,10),(38,16),(38,32),(32,38),(16,38),(10,32),(10,16)]
        members=[]
        for i,start in enumerate(nodes):
            end=nodes[(i+1)%len(nodes)]
            name=f"petal-{i}"
            if i%2:
                self.add_arc(name,start,end,radius_x=5)
            else:
                self.add_arc(name,start,end,radius_x=8 if i%4==0 else 4,radius_y=4 if i%4==0 else 8)
            members.append(name)
        self.add_contour("petals",*members,closed=True)
        self.add_dot("eye-left",(19,20))
        self.add_dot("eye-right",(29,20))
        self.add_arc("smile",(28,28),(20,28),radius_x=4)
