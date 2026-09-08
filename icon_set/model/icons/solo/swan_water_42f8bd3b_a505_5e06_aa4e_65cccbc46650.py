"""Swan on a separate wavy waterline with raised wing. Bounds (2,5)-(46,43). Lucide bird: open wing and simple head; omit eye and extra ripples."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42f8bd3b-a505-5e06-aa4e-65cccbc46650'
SOURCE_PATH = 'pictographic-primitives/animals/swan water_42f8bd3b-a505-5e06-aa4e-65cccbc46650.svg'
AUTHOR = 'gpt-6'


class SwanOnWater(Solo48):
    icon_id = 'swan-on-water'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('swan', 'water', 'float', 'pond', 'bird', 'waterfowl', 'waves', 'elegant')

    def build(self) -> None:
        self.add_line('beak',(46,18),(42,15))
        self.add_arc('head-right',(42,15),(32,5),radius_x=10,sweep=False)
        self.add_arc('head-left',(32,5),(22,15),radius_x=10,sweep=False)
        self.add_arc('neck',(22,15),(28,27),radius_x=15,sweep=False)
        self.add_arc('neck-return',(28,27),(22,31),radius_x=4,sweep=True)
        self.add_arc('wing-top',(22,31),(7,21),radius_x=20,sweep=False)
        self.add_arc('wing-back',(7,21),(15,29),radius_x=12,sweep=False)
        self.add_contour('neck-wing','head-right','head-left','neck','neck-return','wing-top','wing-back')
        self.relate('connect','beak','neck-wing')
        self.add_arc('head-inner',(42,15),(34,17),radius_x=7,sweep=True)
        self.add_arc('inner-neck',(34,17),(40,27),radius_x=15,sweep=False)
        self.add_arc('front',(40,27),(30,34),radius_x=10,radius_y=7,sweep=True)
        self.add_contour('front-neck','head-inner','inner-neck','front')
        self.relate('connect','neck-wing','front-neck')
        self.add_line('hull-base',(30,34),(20,34))
        self.add_arc('hull-back',(20,34),(2,21),radius_x=18,radius_y=13,sweep=True)
        self.add_line('tail',(2,21),(7,21))
        self.add_contour('hull','hull-base','hull-back','tail')
        self.relate('connect','hull','front-neck')
        self.relate('connect','hull','neck-wing')
        self.add_arc('wave-left',(2,42),(14,42),radius_x=6,radius_y=1,sweep=False)
        self.add_arc('wave-middle',(14,42),(24,42),radius_x=5,radius_y=1,sweep=True)
        self.add_arc('wave-right',(24,42),(36,42),radius_x=6,radius_y=1,sweep=False)
        self.add_arc('wave-end',(36,42),(46,42),radius_x=5,radius_y=1,sweep=True)
        self.add_contour('water','wave-left','wave-middle','wave-right','wave-end')
