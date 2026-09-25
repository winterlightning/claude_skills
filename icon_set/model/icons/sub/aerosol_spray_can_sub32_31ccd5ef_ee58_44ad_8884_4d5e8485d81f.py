"""Aerosol Spray Can: user-requested grid-fitted 32px version of aerosol-spray-can-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='31ccd5ef-ee58-44ad-8884-4d5e8485d81f'
SOURCE_PATH='pictographic-primitives/other/spray can_31ccd5ef-ee58-44ad-8884-4d5e8485d81f.svg'
SOLO_SOURCE_ICON_ID='aerosol-spray-can-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='aerosol-spray-can-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'aerosol spray can')
    def build(self):
        self.add_line('can-0', (5, 10), (16, 10))
        self.add_arc('can-1', (16, 10), (19, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('can-2', (19, 13), (19, 27))
        self.add_arc('can-3', (19, 27), (16, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('can-4', (16, 30), (5, 30))
        self.add_arc('can-5', (5, 30), (2, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('can-6', (2, 27), (2, 13))
        self.add_arc('can-7', (2, 13), (5, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('nozzle-1', (7, 10), (7, 2))
        self.add_line('nozzle-2', (7, 2), (15, 2))
        self.add_line('nozzle-3', (15, 2), (15, 10))
        self.add_line('spray-top', (25, 4), (30, 2))
        self.add_line('spray-bottom', (25, 11), (30, 13))
        self.add_contour('can', 'can-0', 'can-1', 'can-2', 'can-3', 'can-4', 'can-5', 'can-6', 'can-7', closed=True)
        self.add_contour('nozzle', 'nozzle-1', 'nozzle-2', 'nozzle-3', closed=False)
        self.relate('connect', 'nozzle', 'can')
        self.add_anchor('center',(16, 16))
