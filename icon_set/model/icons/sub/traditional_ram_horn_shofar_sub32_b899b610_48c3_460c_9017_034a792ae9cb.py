"""Traditional Ram Horn Shofar: user-requested grid-fitted 32px version of traditional-ram-horn-shofar-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='b899b610-48c3-460c-9017-034a792ae9cb'
SOURCE_PATH='pictographic-primitives/other/shofar_b899b610-48c3-460c-9017-034a792ae9cb.svg'
SOLO_SOURCE_ICON_ID='traditional-ram-horn-shofar-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='traditional-ram-horn-shofar-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'traditional ram horn shofar')
    def build(self):
        self.add_line('mouth-0', (16, 2), (27, 2))
        self.add_arc('mouth-1', (27, 2), (30, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('mouth-2', (30, 5), (30, 5))
        self.add_arc('mouth-3', (30, 5), (27, 10), radius_x=3, radius_y=5, large_arc=False, sweep=True)
        self.add_line('mouth-4', (27, 10), (16, 10))
        self.add_arc('mouth-5', (16, 10), (13, 5), radius_x=3, radius_y=5, large_arc=False, sweep=True)
        self.add_line('mouth-6', (13, 5), (13, 5))
        self.add_arc('mouth-7', (13, 5), (16, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('outer', (25, 10), ((25, 25), (18, 25), (7, 25)))
        self.add_bezier('inner', (7, 18), ((14, 19), (18, 18), (18, 10)))
        self.add_line('bell-0', (5, 18), (5, 18))
        self.add_arc('bell-1', (5, 18), (10, 21), radius_x=5, radius_y=3, large_arc=False, sweep=True)
        self.add_line('bell-2', (10, 21), (10, 27))
        self.add_arc('bell-3', (10, 27), (5, 30), radius_x=5, radius_y=3, large_arc=False, sweep=True)
        self.add_line('bell-4', (5, 30), (5, 30))
        self.add_arc('bell-5', (5, 30), (2, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('bell-6', (2, 27), (2, 21))
        self.add_arc('bell-7', (2, 21), (5, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('mouth', 'mouth-0', 'mouth-1', 'mouth-2', 'mouth-3', 'mouth-4', 'mouth-5', 'mouth-6', 'mouth-7', closed=True)
        self.add_contour('bell', 'bell-0', 'bell-1', 'bell-2', 'bell-3', 'bell-4', 'bell-5', 'bell-6', 'bell-7', closed=True)
        self.relate('connect', 'mouth', 'outer', 'inner')
        self.relate('connect', 'bell', 'outer', 'inner')
        self.add_anchor('center',(16, 16))
