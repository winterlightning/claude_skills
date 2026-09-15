"""A right-facing double-decker with two rows of three windows and matched wheels. SQUARE ink (6,6)-(42,42). Lucide bus informed shared window divisions and body/wheel joins; four windows per row reduced to three."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47f6d9ed-04c4-4238-949c-a9ac76819d28'
SOURCE_PATH = 'pictographic-primitives/transportation/bus double 1_47f6d9ed-04c4-4238-949c-a9ac76819d28.svg'
SOURCE_REFERENCES = (('47f6d9ed-04c4-4238-949c-a9ac76819d28', 'pictographic-primitives/transportation/bus double 1_47f6d9ed-04c4-4238-949c-a9ac76819d28.svg'),)
AUTHOR = 'gpt-6'

class DoubleDeckerBus(Solo48):
    icon_id = 'double-decker-bus'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('bus', 'double decker', 'double-decker', 'public transport', 'london', 'vehicle', 'sightseeing', 'transit')

    def build(self) -> None:
        for side,x in [('rear',11),('front',37)]:
            self.add_arc(side+'-upper',(x-5,37),(x+5,37),radius_x=5)
            self.add_arc(side+'-lower',(x+5,37),(x-5,37),radius_x=5)
            self.add_contour(side+'-wheel',side+'-upper',side+'-lower',closed=True)
        self.add_line('body-left-lower',(6,37),(6,23))
        self.add_line('body-left-middle',(6,23),(6,14))
        self.add_line('body-left-upper',(6,14),(6,9))
        self.add_arc('body-back-corner',(6,9),(9,6),radius_x=3)
        self.add_line('roof-back',(9,6),(18,6))
        self.add_line('roof-middle',(18,6),(30,6))
        self.add_line('roof-front',(30,6),(36,6))
        self.add_arc('body-front-corner',(36,6),(42,12),radius_x=6)
        self.add_line('body-right-upper',(42,12),(42,14))
        self.add_line('body-right-middle',(42,14),(42,23))
        self.add_line('body-right-lower',(42,23),(42,37))
        self.add_contour('body','body-left-lower','body-left-middle','body-left-upper','body-back-corner','roof-back','roof-middle','roof-front','body-front-corner','body-right-upper','body-right-middle','body-right-lower')
        for i,y in enumerate((14,23)):
            self.add_polyline(f'floor-{i}',(6,y),(18,y),(30,y),(42,y))
            self.relate('connect',f'floor-{i}','body')
        for i,x in enumerate((18,30)):
            self.add_polyline(f'windows-{i}',(x,6),(x,14),(x,23))
            for part in ['body','floor-0','floor-1']:
                self.relate('connect',f'windows-{i}',part)
        self.add_line('chassis',(16,37),(32,37))
        for wheel in ['rear-wheel','front-wheel']:
            self.relate('connect','body',wheel)
            self.relate('connect','chassis',wheel)
