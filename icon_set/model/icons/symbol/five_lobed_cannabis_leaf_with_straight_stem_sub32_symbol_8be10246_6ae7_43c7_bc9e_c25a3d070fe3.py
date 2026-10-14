"""Cannabis Plant Leaf Symbol: user-requested grid-fitted 32px version of five-lobed-cannabis-leaf-with-straight-stem.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8be10246-6ae7-43c7-bc9e-c25a3d070fe3'
SOURCE_PATH = 'pictographic-primitives/cannabis/cannabis_8be10246-6ae7-43c7-bc9e-c25a3d070fe3.svg'
SOLO_SOURCE_ICON_ID = 'five-lobed-cannabis-leaf-with-straight-stem'
AUTHOR = 'gpt-6'

class DrawingContainerSymbol(Sub32):
    icon_id = 'five-lobed-cannabis-leaf-with-straight-stem-sub32-symbol'
    related_origin_icon_id = 'five-lobed-cannabis-leaf-with-straight-stem-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/five-lobed-cannabis-leaf-with-straight-stem-sub32'
    counterpart_icon_id = 'five-lobed-cannabis-leaf-with-straight-stem-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'cannabis'
    categories = ('primitives', 'cannabis')
    tags = ('sub icon',)
    keywords = ('sub icon', 'grid fitted', 'cannabis plant leaf symbol')

    def build(self):
        # Leaf as leaflet strokes fanning from one base, with a stem.
        self.add_line('leaflet-0', (16, 22), (2, 16))
        self.add_line('leaflet-1', (16, 22), (6, 5))
        self.add_line('leaflet-2', (16, 22), (16, 2))
        self.add_line('leaflet-3', (16, 22), (26, 5))
        self.add_line('leaflet-4', (16, 22), (30, 16))
        self.add_line('stem', (16, 22), (16, 30))
        self.relate('connect', 'leaflet-0', 'leaflet-1')
        self.relate('connect', 'leaflet-0', 'leaflet-2')
        self.relate('connect', 'leaflet-0', 'leaflet-3')
        self.relate('connect', 'leaflet-0', 'leaflet-4')
        self.relate('connect', 'leaflet-0', 'stem')
        self.relate('connect', 'leaflet-1', 'leaflet-2')
        self.relate('connect', 'leaflet-1', 'leaflet-3')
        self.relate('connect', 'leaflet-1', 'leaflet-4')
        self.relate('connect', 'leaflet-1', 'stem')
        self.relate('connect', 'leaflet-2', 'leaflet-3')
        self.relate('connect', 'leaflet-2', 'leaflet-4')
        self.relate('connect', 'leaflet-2', 'stem')
        self.relate('connect', 'leaflet-3', 'leaflet-4')
        self.relate('connect', 'leaflet-3', 'stem')
        self.relate('connect', 'leaflet-4', 'stem')
