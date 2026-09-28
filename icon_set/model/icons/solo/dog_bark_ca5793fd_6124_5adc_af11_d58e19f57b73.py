"""Dog bark (pets), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca5793fd-6124-5adc-af11-d58e19f57b73'
SOURCE_PATH = 'pictographic-primitives/pets/dog bark_ca5793fd-6124-5adc-af11-d58e19f57b73.svg'
AUTHOR = 'gpt-6'

class DogBark(Solo48):
    icon_id = 'dog-bark'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases = ()
    keywords = ('dog', 'bark', 'pets')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (34, 14), (26, 15))
        self.add_line('e1', (22, 18), (16, 18))
        self.add_line('e2', (23, 32), (30, 31))
        self.add_line('e3', (30, 31), (35, 40))
        self.add_line('e4', (44, 15), (44, 21))
        self.add_line('e5', (4, 13), (8, 16))
        self.add_line('e6', (4, 26), (9, 26))
        self.add_line('e7', (6, 37), (9, 34))
        self.add_arc('e8', (39, 8), (34, 14), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('e9', (26, 15), (22, 18))
        self.add_arc('e10-1', (16, 18), (17, 23), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('e10-2', (17, 23), (23, 25))
        self.add_arc('e10-3', (23, 25), (24, 26), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_bezier('e10-4',(24,26),((22,28),(20,29),(18,30)))
        self.add_bezier('e10-5',(18,30),((19,32),(21,32),(23,32)))
        self.add_arc('e11', (39, 8), (44, 15), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('c0', *('e8', 'e0', 'e9', 'e1', 'e10-1', 'e10-2', 'e10-3', 'e10-4', 'e10-5', 'e2', 'e3'), closed=False)
        self.add_contour('c1', *('e11', 'e4'), closed=False)
        self.add_contour('c2', *('e5',), closed=False)
        self.add_contour('c3', *('e6',), closed=False)
        self.add_contour('c4', *('e7',), closed=False)
        self.relate('connect', *('c0', 'c1'))
