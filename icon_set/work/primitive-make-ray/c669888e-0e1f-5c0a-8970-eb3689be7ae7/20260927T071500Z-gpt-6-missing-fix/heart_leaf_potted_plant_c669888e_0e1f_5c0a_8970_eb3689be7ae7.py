'Rebalanced the plant around one readable heart and two flowing side leaves; eliminated overlapping heart lobes.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c669888e-0e1f-5c0a-8970-eb3689be7ae7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__heart-leaf-potted-plant/20260927T061835Z-thuan-mac-1/reference/indoor plant_c669888e-0e1f-5c0a-8970-eb3689be7ae7.svg'
AUTHOR = "gpt-6"


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
        # Smaller terminal heart and a taller tapered pot restore the source's
        # three-part plant proportion, while the side leaves stay open at 48px.
        self.add_bezier('heart-left',(24,10),((22,7),(20,6),(18,6)),((14,6),(13,9),(14,13)),((15,17),(21,20),(24,23)))
        self.add_bezier('heart-right',(24,23),((27,20),(33,17),(34,13)),((35,9),(34,6),(30,6)),((28,6),(26,7),(24,10)))
        self.add_contour('heart','heart-left','heart-right',closed=True)
        self.add_line('stem',(24,23),(24,33))
        self.add_bezier('leaf-left',(6,23),((6,29),(16,33),(24,33)))
        self.add_bezier('leaf-right',(42,23),((42,29),(32,33),(24,33)))
        self.add_polyline('pot-top',(12,33),(24,33),(36,33))
        self.add_polyline('pot-sides',(36,33),(33,42),(15,42),(12,33))
        self.relate('connect','heart','stem')
        for part in ('stem','leaf-left','leaf-right','pot-top'):
         for other in ('stem','leaf-left','leaf-right','pot-top'):
          if part<other: self.relate('connect',part,other)
        self.relate('connect','pot-top','pot-sides')
