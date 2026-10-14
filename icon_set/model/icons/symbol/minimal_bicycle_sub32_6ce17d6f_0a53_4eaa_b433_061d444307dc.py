"""Independent 32px profile of minimal-bicycle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '6ce17d6f-0a53-4eaa-b433-061d444307dc'
SOURCE_PATH = 'pictographic-primitives/transportation/bicycle_6ce17d6f-0a53-4eaa-b433-061d444307dc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6ce17d6f-0a53-4eaa-b433-061d444307dc', 'pictographic-primitives/transportation/bicycle_6ce17d6f-0a53-4eaa-b433-061d444307dc.svg'), ('809ac450-efd8-4c1a-94b3-ed96c86e92df', 'pictographic-primitives/transportation/bicycle_809ac450-efd8-4c1a-94b3-ed96c86e92df.svg'), ('c94a3698-f47d-459c-afbc-fc5e64f7a783', 'pictographic-primitives/transportation/bicycle_c94a3698-f47d-459c-afbc-fc5e64f7a783.svg'))
PROFILE_SOURCE_KEYS = ('solo/minimal-bicycle',)
SOLO_SOURCE_ICON_IDS = ('minimal-bicycle',)
REFERENCE_EXPORT_SHA256 = '7f06baf7c6780552417fb90b8fa9b33d437205f144d459b08e213215ac3fdc63'

class Drawing(Sub32):
    icon_id = 'minimal-bicycle-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Bicycle: two wheels, frame from the rear hub over a top tube to the front fork, seat and handlebar.
        for k, x in enumerate((7, 25)):
            self.add_arc(f'wheel-{k}-1', (x - 5, 23), (x + 5, 23), radius_x=5, radius_y=5, large_arc=False, sweep=True)
            self.add_arc(f'wheel-{k}-2', (x + 5, 23), (x - 5, 23), radius_x=5, radius_y=5, large_arc=False, sweep=True)
            self.add_contour(f'wheel-{k}', f'wheel-{k}-1', f'wheel-{k}-2', closed=True)
        self.add_polyline('frame', (10, 19), (13, 11), (21, 10), (22, 19))
        self.add_line('seat-post', (13, 11), (10, 4))
        self.add_line('seat', (8, 4), (12, 4))
        self.add_line('stem', (21, 10), (20, 4))
        self.add_line('bar', (20, 4), (24, 4))
        for a, b in (('frame', 'wheel-0'), ('frame', 'wheel-1'), ('frame', 'seat-post'), ('seat-post', 'seat'), ('frame', 'stem'), ('stem', 'bar')):
            self.relate('connect', a, b)
