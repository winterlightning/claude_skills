"""Independent 32px profile of atom.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '050a6fe7-76bf-492a-82d8-877ce640f913'
SOURCE_PATH = 'pictographic-primitives/symbol/atom_050a6fe7-76bf-492a-82d8-877ce640f913.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('050a6fe7-76bf-492a-82d8-877ce640f913', 'pictographic-primitives/symbol/atom_050a6fe7-76bf-492a-82d8-877ce640f913.svg'),)
PROFILE_SOURCE_KEYS = ('solo/atom',)
SOLO_SOURCE_ICON_IDS = ('atom',)
REFERENCE_EXPORT_SHA256 = '9fe04446709f1a61123d5f896fda56386268bffbc787cd15296091c6295b2839'

class Drawing(Sub32):
    icon_id = 'atom-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (5, 14), ((4, 13), (4, 11), (4, 10)))
        self.add_bezier('p1-r1-2', (4, 10), ((4, 8), (4, 6), (6, 4)))
        self.add_bezier('p1-r1-3', (6, 4), ((7, 3), (9, 2), (11, 2)))
        self.add_bezier('p1-r1-4', (11, 2), ((13, 2), (15, 3), (16, 4)))
        self.add_bezier('p1-r1-5', (16, 4), ((16, 4), (17, 4), (17, 4)))
        self.add_bezier('p1-r1-6', (17, 4), ((17, 5), (17, 5), (18, 5)))
        self.add_line('p1-r1-7', (18, 5), (27, 18))
        self.add_bezier('p1-r1-8', (27, 18), ((28, 19), (28, 21), (28, 22)))
        self.add_bezier('p1-r1-9', (28, 22), ((28, 24), (28, 26), (26, 28)))
        self.add_bezier('p1-r1-10', (26, 28), ((25, 29), (23, 30), (21, 30)))
        self.add_bezier('p1-r1-11', (21, 30), ((19, 30), (17, 29), (16, 28)))
        self.add_bezier('p1-r1-12', (16, 28), ((16, 28), (15, 28), (15, 28)))
        self.add_bezier('p1-r1-13', (15, 28), ((15, 27), (15, 27), (14, 27)))
        self.add_line('p1-r1-14', (14, 27), (5, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', closed=False)
        self.add_bezier('p2-r1-1', (14, 5), ((15, 5), (15, 5), (15, 4)))
        self.add_bezier('p2-r1-2', (15, 4), ((15, 4), (16, 4), (16, 4)))
        self.add_bezier('p2-r1-3', (16, 4), ((17, 3), (19, 2), (21, 2)))
        self.add_bezier('p2-r1-4', (21, 2), ((23, 2), (25, 3), (26, 4)))
        self.add_bezier('p2-r1-5', (26, 4), ((28, 6), (28, 8), (28, 10)))
        self.add_bezier('p2-r1-6', (28, 10), ((28, 11), (28, 13), (27, 14)))
        self.add_line('p2-r1-7', (27, 14), (18, 27))
        self.add_bezier('p2-r1-8', (18, 27), ((17, 27), (17, 27), (17, 28)))
        self.add_bezier('p2-r1-9', (17, 28), ((17, 28), (16, 28), (16, 28)))
        self.add_bezier('p2-r1-10', (16, 28), ((15, 29), (13, 30), (11, 30)))
        self.add_bezier('p2-r1-11', (11, 30), ((9, 30), (7, 29), (6, 28)))
        self.add_bezier('p2-r1-12', (6, 28), ((4, 26), (4, 24), (4, 22)))
        self.add_bezier('p2-r1-13', (4, 22), ((4, 21), (4, 19), (5, 18)))
        self.add_line('p2-r1-14', (5, 18), (14, 5))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', 'p2-r1-12', 'p2-r1-13', 'p2-r1-14', closed=False)
        self.add_line('p3-r1-1', (16, 16), (16, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-3')
        self.relate("connect", 'p1-r1-5', 'p2-r1-2')
        self.relate("connect", 'p1-r1-5', 'p2-r1-3')
        self.relate("connect", 'p1-r1-11', 'p2-r1-9')
        self.relate("connect", 'p1-r1-11', 'p2-r1-10')
        self.relate("connect", 'p1-r1-12', 'p2-r1-9')
        self.relate("connect", 'p1-r1-12', 'p2-r1-10')
