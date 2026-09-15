"""A low open sports car with windscreen and headrest strokes. Lucide bus and car-front informed rounded body and wheel joins. Broad keyshape suits its long silhouette; hubs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '756eeed2-8118-5bdb-a761-c87c710659d8'
SOURCE_PATH = 'pictographic-primitives/transportation/car sports_756eeed2-8118-5bdb-a761-c87c710659d8.svg'
SOURCE_REFERENCES = (('756eeed2-8118-5bdb-a761-c87c710659d8', 'pictographic-primitives/transportation/car sports_756eeed2-8118-5bdb-a761-c87c710659d8.svg'),)
AUTHOR = 'gpt-6'

class OpenTopSportsCar(Solo48):
    icon_id = 'open-top-sports-car'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('sports car', 'convertible', 'roadster', 'car', 'open top', 'fast', 'vehicle', 'side view')

    def build(self) -> None:
        self.add_line('back',(4,33),(4,24))
        self.add_arc('back-corner',(4,24),(8,20),radius_x=4)
        self.add_line('top-0',(8,20),(14,20))
        self.add_line('top-1',(14,20),(28,20))
        self.add_line('top-2',(28,20),(34,20))
        self.add_arc('nose',(34,20),(44,30),radius_x=10)
        self.add_line('front',(44,30),(44,33))
        self.add_contour('body','back','back-corner','top-0','top-1','top-2','nose','front')

        for side,x in [('rear',11),('front',37)]:
            self.add_arc(side+'-upper',(x-7,33),(x+7,33),radius_x=7)
            self.add_arc(side+'-lower',(x+7,33),(x-7,33),radius_x=7)
            self.add_contour(side+'-wheel',side+'-upper',side+'-lower',closed=True)
        self.add_line('chassis',(18,33),(30,33))
        for wheel in ['rear-wheel','front-wheel']:
            self.relate('connect','body',wheel)
            self.relate('connect','chassis',wheel)

        self.add_line('screen',(28,20),(24,8))
        self.add_line('headrest',(14,20),(11,16))
        self.relate('connect','screen','body')
        self.relate('connect','headrest','body')
