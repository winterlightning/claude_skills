"""passport: repaired SOLO48 composition.
Plan: Shared pole/equator intersections within a book cover.
Keyshape: SQUARE maximizes balanced globe clearance inside the cover.
Reduction: Rear-cover reveal omitted. Two curved meridians replaced by one central meridian; globe quadrants broadened slightly.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1f180a84-a846-4671-b767-dbb6041f800a'
SOURCE_PATH = 'pictographic-primitives/travel/passport_1f180a84-a846-4671-b767-dbb6041f800a.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = 'globe, book'

class Drawing(Solo48):
    icon_id = 'passport'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('passport',)

    def build(self):
        self.add_polyline('cover', (6, 6), (42, 6), (42, 42), (6, 42), closed=True)
        self.add_bezier('globe-ne', (24, 15), ((30, 15), (33, 18), (33, 24)))
        self.add_bezier('globe-se', (33, 24), ((33, 30), (30, 33), (24, 33)))
        self.add_bezier('globe-sw', (24, 33), ((18, 33), (15, 30), (15, 24)))
        self.add_bezier('globe-nw', (15, 24), ((15, 18), (18, 15), (24, 15)))
        self.add_contour('globe', 'globe-ne', 'globe-se', 'globe-sw', 'globe-nw', closed=True)
        self.add_polyline('equator', (15, 24), (24, 24), (33, 24))
        self.add_polyline('meridian', (24, 15), (24, 24), (24, 33))
        self.relate('connect', 'globe', 'equator', 'meridian')
