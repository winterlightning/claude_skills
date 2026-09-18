"""Simple Monthly Calendar: user-requested grid-fitted 32px version of simple-monthly-calendar-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='a86ac0fa-cb10-444a-8f9c-cea48309d64f'
SOURCE_PATH='pictographic-primitives/interface-essential/calendar_a86ac0fa-cb10-444a-8f9c-cea48309d64f.svg'
SOLO_SOURCE_ICON_ID='simple-monthly-calendar-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='simple-monthly-calendar-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'simple monthly calendar')
    def build(self):
        self.add_line('calendar-0', (5, 7), (27, 7))
        self.add_arc('calendar-1', (27, 7), (30, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('calendar-2', (30, 10), (30, 27))
        self.add_arc('calendar-3', (30, 27), (27, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('calendar-4', (27, 30), (5, 30))
        self.add_arc('calendar-5', (5, 30), (2, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('calendar-6', (2, 27), (2, 10))
        self.add_arc('calendar-7', (2, 10), (5, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('binding-15', (9, 2), (9, 10))
        self.add_line('binding-33', (23, 2), (23, 10))
        self.add_line('header', (2, 16), (30, 16))
        self.add_contour('calendar', 'calendar-0', 'calendar-1', 'calendar-2', 'calendar-3', 'calendar-4', 'calendar-5', 'calendar-6', 'calendar-7', closed=True)
        self.relate('connect', 'calendar', 'binding-15')
        self.relate('connect', 'calendar', 'binding-33')
        self.relate('connect', 'calendar', 'header')
        self.add_anchor('center',(16, 16))
