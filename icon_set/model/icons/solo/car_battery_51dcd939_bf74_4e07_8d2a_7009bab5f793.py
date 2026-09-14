"""A car battery with two top terminals and an empty face. SQUARE ink (6,6)-(42,42) provides space below the terminal posts. Lucide car-battery informed the case and terminal hierarchy."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51dcd939-bf74-4e07-8d2a-7009bab5f793'
SOURCE_PATH = 'pictographic-primitives/transportation/car battery_51dcd939-bf74-4e07-8d2a-7009bab5f793.svg'
SOURCE_REFERENCES = (('51dcd939-bf74-4e07-8d2a-7009bab5f793', 'pictographic-primitives/transportation/car battery_51dcd939-bf74-4e07-8d2a-7009bab5f793.svg'),)
AUTHOR = 'gpt-6'

class CarBattery(Solo48):
    icon_id = 'car-battery'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('battery', 'car battery', 'power', 'charge', 'electric', 'terminal', 'vehicle', 'energy')

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
