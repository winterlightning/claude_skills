"""Independent 32px profile of exclamation-point-warning-triangle-solo-v2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '42f29bd3-1507-484e-98bb-b90c40309892'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/42f29bd3-1507-484e-98bb-b90c40309892.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('42f29bd3-1507-484e-98bb-b90c40309892', 'icon_set/dist/gallery/combination-originals/42f29bd3-1507-484e-98bb-b90c40309892.svg'),)
PROFILE_SOURCE_KEYS = ('solo/exclamation-point-warning-triangle-solo-v2',)
SOLO_SOURCE_ICON_IDS = ('exclamation-point-warning-triangle-solo-v2',)
REFERENCE_EXPORT_SHA256 = '4590b53d1c8d1934780eeeb743d624bcedcd031ad32e3d4f45a811dbc027a946'

class Drawing(Sub32):
    icon_id = 'exclamation-point-warning-triangle-solo-v2-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (30, 30))
        self.add_line('p1-r1-2', (30, 30), (2, 30))
        self.add_line('p1-r1-3', (2, 30), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (16, 16), (16, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 24), (16, 24))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
