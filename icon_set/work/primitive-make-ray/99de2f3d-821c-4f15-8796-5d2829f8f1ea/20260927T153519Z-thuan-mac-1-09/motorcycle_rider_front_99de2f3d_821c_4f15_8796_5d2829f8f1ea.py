"""Motorcycle rider front, authored on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='99de2f3d-821c-4f15-8796-5d2829f8f1ea'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__motorcycle-rider-front/20260927T153322Z-thuan-mac-1/reference/racing_99de2f3d-821c-4f15-8796-5d2829f8f1ea.svg'
AUTHOR="gpt-6"

class MotorcycleRiderFront(Solo48):
    icon_id='motorcycle-rider-front'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('motorcycle', 'rider', 'front')
    def build(self):
        # Larger helmet and distinct grips, wheel, and rider shoulder line.
        self.add_arc('helmet-a', (24,4), (24,16), radius_x=6, sweep=True)
        self.add_arc('helmet-b', (24,16), (24,4), radius_x=6, sweep=True)
        self.add_contour('helmet','helmet-a','helmet-b',closed=True)
        self.add_polyline('shoulders',(8,31),(13,24),(24,24),(35,24),(40,31))
        self.add_polyline('left-grip',(8,31),(10,36),(10,44))
        self.add_polyline('right-grip',(40,31),(38,36),(38,44))
        self.relate('connect','shoulders','left-grip')
        self.relate('connect','shoulders','right-grip')
        self.add_polyline('front-wheel',(20,44),(20,34),(28,34),(28,44),closed=True)
