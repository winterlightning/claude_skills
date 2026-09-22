"""Mandarin fruit with a left leaf and a short upright stem curving right. VRECT_L gives fruit a broad lower oval and budgets a readable leaf above. Shared stem node24,12 owns leaf attachment; smooth ellipse preserves citrus mass. Source contributes single fruit and left leaf; Lucide cherry informs stem and pointed two-curve leaf. Fruit slightly flattened for space; no surface texture added."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='c5d1605f-5da6-410f-99e1-810351f0fba4'
SOURCE_PATH='pictographic-primitives/_uncategorized_26/mandarin_c5d1605f-5da6-410f-99e1-810351f0fba4.svg'
AUTHOR="gpt-6-astra"
class Drawing(Solo48):
    icon_id='round-mandarin-with-small-left-leaf'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=("Mandarin Orange with Leaf",)
    keywords=("mandarin","orange","fruit","leaf","citrus")
    def build(self):
        self.add_arc('fruit-right',(24,20),(24,44),radius_x=16,radius_y=12)
        self.add_arc('fruit-left',(24,44),(24,20),radius_x=16,radius_y=12)
        self.add_contour('fruit','fruit-right','fruit-left',closed=True)
        self.add_bezier('leaf',(24,12),((24,4),(16,4),(10,4)),((10,12),(18,12),(24,12)))
        self.add_contour('leaf-outline','leaf',closed=True)
        self.add_line('stem-low',(24,20),(24,12))
        self.add_bezier('stem-high',(24,12),((24,8),(28,5),(30,4)))
        self.relate('connect','stem-low','fruit')
        self.relate('connect','stem-low','leaf-outline','stem-high')
