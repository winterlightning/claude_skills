'Rebalanced the plant around one readable heart and two flowing side leaves; eliminated overlapping heart lobes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c669888e-0e1f-5c0a-8970-eb3689be7ae7'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/indoor plant_c669888e-0e1f-5c0a-8970-eb3689be7ae7.svg'
AUTHOR = 'gpt-6'


class HeartLeafPottedPlant(Solo48):
    icon_id = 'heart-leaf-potted-plant'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "decoration"
    categories = ("primitives", "decoration")
    aliases = ()
    keywords = ('plant', 'heart', 'leaves', 'pot', 'stems', 'foliage', 'decor')

    def build(self) -> None:
        # One generous heart leaf, with a mirrored pair of open lateral leaves.
        self.add_bezier('heart-left',(24,10),((22,7),(20,6),(17,6)),((12,6),(10,9),(10,14)),((10,20),(20,23),(24,26)))
        self.add_bezier('heart-right',(24,26),((28,23),(38,20),(38,14)),((38,9),(36,6),(31,6)),((28,6),(26,7),(24,10)))
        self.add_contour('heart','heart-left','heart-right',closed=True)
        self.add_line('stem',(24,26),(24,34))
        self.add_bezier('leaf-left',(6,23),((6,29),(16,34),(24,34)))
        self.add_bezier('leaf-right',(42,23),((42,29),(32,34),(24,34)))
        self.add_polyline('pot-top',(7,34),(24,34),(41,34))
        self.add_polyline('pot-sides',(41,34),(39,42),(9,42),(7,34))
        self.relate('connect','heart','stem')
        for part in ('stem','leaf-left','leaf-right','pot-top'):
         for other in ('stem','leaf-left','leaf-right','pot-top'):
          if part<other: self.relate('connect',part,other)
        self.relate('connect','pot-top','pot-sides')
