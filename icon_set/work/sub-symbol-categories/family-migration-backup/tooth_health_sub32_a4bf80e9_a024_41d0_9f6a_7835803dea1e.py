"""Independent 32px profile of tooth-health.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a4bf80e9-a024-41d0-9f6a-7835803dea1e'
SOURCE_PATH = 'pictographic-primitives/health/tooth_a4bf80e9-a024-41d0-9f6a-7835803dea1e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a4bf80e9-a024-41d0-9f6a-7835803dea1e', 'pictographic-primitives/health/tooth_a4bf80e9-a024-41d0-9f6a-7835803dea1e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/tooth-health',)
SOLO_SOURCE_ICON_IDS = ('tooth-health',)
REFERENCE_EXPORT_SHA256 = '47c20886b626a2ffe4bfa0a50299b60001c383839382e23aedb83109c54ee922'

class Drawing(Sub32):
    icon_id = 'tooth-health-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'health'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (12, 4), ((9, 4), (8, 2), (6, 2)))
        self.add_bezier('p1-r1-2', (6, 2), ((4, 2), (2, 5), (2, 9)))
        self.add_bezier('p1-r1-3', (2, 9), ((2, 13), (4, 17), (5, 20)))
        self.add_bezier('p1-r1-4', (5, 20), ((5, 26), (5, 30), (7, 30)))
        self.add_bezier('p1-r1-5', (7, 30), ((11, 30), (9, 19), (12, 19)))
        self.add_bezier('p1-r1-6', (12, 19), ((15, 19), (14, 30), (17, 30)))
        self.add_bezier('p1-r1-7', (17, 30), ((19, 30), (19, 26), (19, 20)))
        self.add_bezier('p1-r1-8', (19, 20), ((20, 17), (22, 13), (22, 9)))
        self.add_bezier('p1-r1-9', (22, 9), ((22, 5), (21, 2), (18, 2)))
        self.add_bezier('p1-r1-10', (18, 2), ((16, 2), (15, 4), (12, 4)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_bezier('p2-r1-1', (22, 9), ((27, 9), (28, 12), (28, 16)))
        self.add_line('p2-r1-2', (28, 16), (28, 25))
        self.add_bezier('p2-r1-3', (28, 25), ((28, 26), (29, 27), (29, 27)))
        self.add_bezier('p2-r1-4', (29, 27), ((30, 27), (30, 27), (30, 27)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
        self.relate("connect", 'p1-r1-9', 'p2-r1-1')
