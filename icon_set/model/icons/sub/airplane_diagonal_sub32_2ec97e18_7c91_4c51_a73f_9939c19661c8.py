"""Independent 32px profile of airplane-diagonal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2ec97e18-7c91-4c51-a73f-9939c19661c8'
SOURCE_PATH = 'pictographic-primitives/symbol/airplane_2ec97e18-7c91-4c51-a73f-9939c19661c8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2ec97e18-7c91-4c51-a73f-9939c19661c8', 'pictographic-primitives/symbol/airplane_2ec97e18-7c91-4c51-a73f-9939c19661c8.svg'), ('995ca841-d25b-4135-bff1-8fefd083a02d', 'pictographic-primitives/travel/plane_995ca841-d25b-4135-bff1-8fefd083a02d.svg'), ('b476e384-418f-4620-b003-0fd2cce07768', 'pictographic-primitives/travel/plane_b476e384-418f-4620-b003-0fd2cce07768.svg'))
PROFILE_SOURCE_KEYS = ('solo/airplane-diagonal', 'solo/diagonal-airplane-outline', 'solo/diagonal-airplane-pointed-wings')
SOLO_SOURCE_ICON_IDS = ('airplane-diagonal', 'diagonal-airplane-outline', 'diagonal-airplane-pointed-wings')
REFERENCE_EXPORT_SHA256 = 'fa4f6cf64f6dde13cf077a5be1fdf25b18812cf2e218238376c7ef860085eeb8'

class Drawing(Sub32):
    icon_id = 'airplane-diagonal-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (24, 2), (30, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (30, 8), (24, 16))
        self.add_line('p1-r1-3', (24, 16), (28, 22))
        self.add_bezier('p1-r1-4', (28, 22), ((29, 23), (30, 23), (30, 24)))
        self.add_bezier('p1-r1-5', (30, 24), ((30, 24), (29, 25), (28, 25)))
        self.add_line('p1-r1-6', (28, 25), (25, 28))
        self.add_bezier('p1-r1-7', (25, 28), ((25, 29), (24, 30), (24, 30)))
        self.add_bezier('p1-r1-8', (24, 30), ((23, 30), (23, 29), (22, 28)))
        self.add_line('p1-r1-9', (22, 28), (18, 21))
        self.add_line('p1-r1-10', (18, 21), (13, 25))
        self.add_line('p1-r1-11', (13, 25), (14, 28))
        self.add_bezier('p1-r1-12', (14, 28), ((14, 28), (14, 29), (14, 29)))
        self.add_bezier('p1-r1-13', (14, 29), ((14, 30), (13, 30), (11, 30)))
        self.add_line('p1-r1-14', (11, 30), (9, 30))
        self.add_arc('p1-r1-15', (9, 30), (7, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-16', (7, 28), (7, 25))
        self.add_line('p1-r1-17', (7, 25), (4, 25))
        self.add_bezier('p1-r1-18', (4, 25), ((2, 24), (2, 24), (2, 22)))
        self.add_line('p1-r1-19', (2, 22), (2, 18))
        self.add_bezier('p1-r1-20', (2, 18), ((2, 17), (2, 16), (3, 16)))
        self.add_bezier('p1-r1-21', (3, 16), ((3, 16), (3, 16), (4, 17)))
        self.add_line('p1-r1-22', (4, 17), (8, 18))
        self.add_line('p1-r1-23', (8, 18), (13, 13))
        self.add_line('p1-r1-24', (13, 13), (4, 8))
        self.add_bezier('p1-r1-25', (4, 8), ((3, 7), (2, 7), (2, 7)))
        self.add_bezier('p1-r1-26', (2, 7), ((2, 6), (3, 6), (4, 5)))
        self.add_line('p1-r1-27', (4, 5), (5, 4))
        self.add_bezier('p1-r1-28', (5, 4), ((6, 3), (6, 2), (7, 2)))
        self.add_bezier('p1-r1-29', (7, 2), ((7, 2), (8, 2), (8, 3)))
        self.add_line('p1-r1-30', (8, 3), (18, 8))
        self.add_line('p1-r1-31', (18, 8), (24, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', 'p1-r1-21', 'p1-r1-22', 'p1-r1-23', 'p1-r1-24', 'p1-r1-25', 'p1-r1-26', 'p1-r1-27', 'p1-r1-28', 'p1-r1-29', 'p1-r1-30', 'p1-r1-31', closed=False)
