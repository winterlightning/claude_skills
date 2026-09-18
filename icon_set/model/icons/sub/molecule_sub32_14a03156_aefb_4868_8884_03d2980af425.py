"""Independent 32px profile of molecule.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '14a03156-aefb-4868-8884-03d2980af425'
SOURCE_PATH = 'pictographic-primitives/science/molecule_14a03156-aefb-4868-8884-03d2980af425.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14a03156-aefb-4868-8884-03d2980af425', 'pictographic-primitives/science/molecule_14a03156-aefb-4868-8884-03d2980af425.svg'), ('bd75597b-ada9-478f-9eb1-91e31b7ac0c2', 'pictographic-primitives/science/molecule_bd75597b-ada9-478f-9eb1-91e31b7ac0c2.svg'))
PROFILE_SOURCE_KEYS = ('solo/molecule', 'solo/molecule-bd75597b')
SOLO_SOURCE_ICON_IDS = ('molecule', 'molecule-bd75597b')
REFERENCE_EXPORT_SHA256 = 'e49186f3373fa44de7dc9fb13f2112688b227299417d6bab5bd5ebcd7109b5f7'

class Drawing(Sub32):
    icon_id = 'molecule-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'science'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (12, 9), (20, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (20, 9), (12, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (22, 24), (30, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-2', (30, 24), ((30, 26), (28, 27), (26, 27)))
        self.add_bezier('p2-r1-3', (26, 27), ((24, 27), (22, 26), (22, 24)))
        self.add_line('p2-r1-4', (22, 24), (22, 24))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_arc('p3-r1-1', (10, 24), (2, 24), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_bezier('p3-r1-2', (2, 24), ((2, 26), (4, 27), (6, 27)))
        self.add_bezier('p3-r1-3', (6, 27), ((8, 27), (10, 26), (10, 24)))
        self.add_line('p3-r1-4', (10, 24), (10, 24))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (21, 24), (11, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (24, 19), (18, 12))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (8, 19), (13, 12))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
