"""Minimalist Residential Home: user-requested grid-fitted 32px version of house-with-door-division.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5ae6e559-27d0-490b-b13a-e0950315fc03'
SOURCE_PATH = 'pictographic-primitives/interface-essential/house_5ae6e559-27d0-490b-b13a-e0950315fc03.svg'
SOLO_SOURCE_ICON_ID = 'house-with-door-division'
AUTHOR = 'gpt-6'

class DrawingContainerSymbol(Sub32):
    icon_id = 'house-with-door-division-sub32-symbol'
    related_origin_icon_id = 'house-with-door-division-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/house-with-door-division-sub32'
    counterpart_icon_id = 'house-with-door-division-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'grid fitted', 'minimalist residential home')

    def build(self):
        self.add_line('roof-1', (2, 16), (5, 13))
        self.add_line('roof-2', (5, 13), (16, 2))
        self.add_line('roof-3', (16, 2), (27, 13))
        self.add_line('roof-4', (27, 13), (30, 16))
        self.add_line('walls-1', (5, 13), (5, 30))
        self.add_line('walls-2', (5, 30), (16, 30))
        self.add_line('walls-3', (16, 30), (27, 30))
        self.add_line('walls-4', (27, 30), (27, 13))
        self.add_line('door-division', (16, 21), (16, 30))
        self.add_contour('roof', 'roof-1', 'roof-2', 'roof-3', 'roof-4', closed=False)
        self.add_contour('walls', 'walls-1', 'walls-2', 'walls-3', 'walls-4', closed=False)
        self.relate('connect', 'roof', 'walls')
        self.relate('connect', 'door-division', 'walls')
        self.add_anchor('center', (16, 16))
