"""Independent 32px profile of book-open-1421392c.
Reauthored from the requested reference for SYMBOL32; see construction plan.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32
SOURCE_ICON_ID = '1421392c-5884-4c7e-bf5c-1082165dfba9'
SOURCE_PATH = 'pictographic-primitives/content/book open_1421392c-5884-4c7e-bf5c-1082165dfba9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1421392c-5884-4c7e-bf5c-1082165dfba9', 'pictographic-primitives/content/book open_1421392c-5884-4c7e-bf5c-1082165dfba9.svg'), ('df25e3f8-0308-43ac-83b9-5a03a38cf7f5', 'pictographic-primitives/content/book open 1_df25e3f8-0308-43ac-83b9-5a03a38cf7f5.svg'), ('a147931e-057f-4518-b391-cf08f66084de', 'pictographic-primitives/content/book open_a147931e-057f-4518-b391-cf08f66084de.svg'))
PROFILE_SOURCE_KEYS = ('solo/book-open-1421392c', 'solo/book-open-1-df25e3f8', 'solo/book-open-a147931e')
SOLO_SOURCE_ICON_IDS = ('book-open-1421392c', 'book-open-1-df25e3f8', 'book-open-a147931e')
REFERENCE_EXPORT_SHA256 = '1bae9a15dc9fe7fdec94acae5090512df80fbbba3b114ec69ff3eeeda1a1eec5'

class DrawingContainerSymbol(Symbol32):
    icon_id = 'book-open-1421392c-sub32-symbol'
    related_origin_icon_id = 'book-open-1421392c-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/book-open-1421392c-sub32'
    counterpart_icon_id = 'book-open-1421392c-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'content'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):

        # Plan: mirrored leaves own equal top/bottom page curves; one gutter
        # joins their shared central nodes. Lucide book-open informs the curved
        # leaf edges and blank pages. Centerline bounds (2,4)-(30,28).
        # Omit page text and the redundant left inner line at this size.
        axis, page_radius = 16, 10
        top, bottom = (axis, 8), (axis, 28)
        self.add_line('top-left', (2, 4), (8, 4))
        self.add_arc('top-left-curve', (8, 4), top, radius_x=page_radius)
        self.add_arc('top-right-curve', top, (24, 4), radius_x=page_radius)
        self.add_polyline('right-edge', (24, 4), (30, 4), (30, 24), (24, 24))
        self.add_arc('bottom-right-curve', (24, 24), bottom, radius_x=page_radius, sweep=False)
        self.add_arc('bottom-left-curve', bottom, (8, 24), radius_x=page_radius, sweep=False)
        self.add_polyline('left-edge', (8, 24), (2, 24), (2, 4))
        self.contours.clear()
        self.add_contour('pages', 'top-left', 'top-left-curve', 'top-right-curve',
                         'right-edge-1', 'right-edge-2', 'right-edge-3',
                         'bottom-right-curve', 'bottom-left-curve', 'left-edge-1', 'left-edge-2', closed=True)
        self.add_line('gutter', top, bottom)
        for curve in ('top-left-curve', 'top-right-curve', 'bottom-left-curve', 'bottom-right-curve'):
            self.relate('connect', 'gutter', curve)
