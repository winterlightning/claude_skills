"""Independent 32px profile of state32-22b19b8b-2dbf-4961-8544-e875b0c1ab8a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '22b19b8b-2dbf-4961-8544-e875b0c1ab8a'
SOURCE_PATH = 'icon_set/assets/combination-state32/22b19b8b-2dbf-4961-8544-e875b0c1ab8a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('22b19b8b-2dbf-4961-8544-e875b0c1ab8a', 'icon_set/assets/combination-state32/22b19b8b-2dbf-4961-8544-e875b0c1ab8a.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '3a4d68f6e8d6053819ed28d319c8f9b0bbc4ba4d7768bab41f9cec30d02b232c'

class Drawing(Sub32):
    icon_id = 'state32-22b19b8b-2dbf-4961-8544-e875b0c1ab8a'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 3), (17, 17))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p1-r2-1', (17, 7), (17, 17))
        self.add_line('p1-r2-2', (17, 17), (6, 17))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.add_line('p2-r1-1', (20, 23), (29, 23))
        self.add_bezier('p2-r1-2', (29, 23), ((29.666666666666668, 23), (30, 23.333333333333332), (30, 24)))
        self.add_line('p2-r1-3', (30, 24), (30, 28))
        self.add_bezier('p2-r1-4', (30, 28), ((30, 28.666666666666668), (29.666666666666668, 29), (29, 29)))
        self.add_line('p2-r1-5', (29, 29), (20, 29))
        self.add_bezier('p2-r1-6', (20, 29), ((19.333333333333332, 29), (19, 28.666666666666668), (19, 28)))
        self.add_line('p2-r1-7', (19, 28), (19, 24))
        self.add_bezier('p2-r1-8', (19, 24), ((19, 23.333333333333332), (19.333333333333332, 23), (20, 23)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.relate("connect", 'p1-r1-1', 'p1-r2-1')
        self.relate("connect", 'p1-r1-1', 'p1-r2-2')
