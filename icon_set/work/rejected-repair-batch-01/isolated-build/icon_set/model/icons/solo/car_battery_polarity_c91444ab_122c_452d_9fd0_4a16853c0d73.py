"""A car battery with two top terminals and intrinsic polarity marks. SQUARE ink (6,6)-(42,42) provides space below the terminal posts. Lucide car-battery informed the case and terminal hierarchy."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c91444ab-122c-452d-9fd0-4a16853c0d73'
SOURCE_PATH = 'pictographic-primitives/transportation/car battery_c91444ab-122c-452d-9fd0-4a16853c0d73.svg'
SOURCE_REFERENCES = (('c91444ab-122c-452d-9fd0-4a16853c0d73', 'pictographic-primitives/transportation/car battery_c91444ab-122c-452d-9fd0-4a16853c0d73.svg'),)
AUTHOR = 'gpt-6'

class CarBatteryPolarity(Solo48):
    icon_id = 'car-battery-polarity'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('battery', 'car battery', 'polarity', 'plus', 'minus', 'charge', 'electric', 'vehicle')

    def build(self) -> None:
        self.add_line('case-top-0',(10, 14),(18, 14))
        self.add_line('case-top-1',(18, 14),(30, 14))
        self.add_line('case-top-2',(30, 14),(38, 14))
        self.add_arc('case-top-corner',(38, 14),(42, 18),radius_x=4)
        self.add_line('case-right-0',(42, 18),(42, 38))
        self.add_arc('case-right-corner',(42, 38),(38, 42),radius_x=4)
        self.add_line('case-bottom-0',(38, 42),(10, 42))
        self.add_arc('case-bottom-corner',(10, 42),(6, 38),radius_x=4)
        self.add_line('case-left-0',(6, 38),(6, 18))
        self.add_arc('case-left-corner',(6, 18),(10, 14),radius_x=4)
        self.add_contour('case','case-top-0','case-top-1','case-top-2','case-top-corner','case-right-0','case-right-corner','case-bottom-0','case-bottom-corner','case-left-0','case-left-corner',closed=True)

        for side,x in [('left',10),('right',30)]:
            self.add_polyline(side+'-terminal',(x,14),(x,6),(x+8,6),(x+8,14))
            self.relate('connect',side+'-terminal','case')

        self.add_line('minus',(15,28),(19,28))
        self.add_polyline('plus-horizontal',(27,28),(30,28),(33,28))
        self.add_polyline('plus-vertical',(30,25),(30,28),(30,31))
        self.relate('connect','plus-horizontal','plus-vertical')
