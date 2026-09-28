"""house music: fresh SOLO48 repair.
Plan: Equal circular noteheads, tall stems and an ascending beam.
Keyshape: SQUARE. House surrounds a rising pair of notes.
Omissions: Notehead outlines reduced to small circles under the existing small-circle rule.
Construction reference: house: coherent enclosure; supplied reference: paired noteheads and rising beam.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3640f2f0-b0c0-4dbd-9d92-86762ff6cfbb'
SOURCE_PATH = 'pictographic-primitives/other/house music_3640f2f0-b0c0-4dbd-9d92-86762ff6cfbb.svg'
AUTHOR = 'gpt-6'
PARENT_SOURCE = 'icon_set/model/icons/solo/house_music_3640f2f0_b0c0_4dbd_9d92_86762ff6cfbb.py'

class Drawing(Solo48):
    icon_id = 'house-music'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/buildings'
    aliases = ()
    keywords = ('house', 'music')

    def circle(self, n, x, y, r):
        self.add_arc(n + '-a', (x - r, y), (x + r, y), radius_x=r)
        self.add_arc(n + '-b', (x + r, y), (x - r, y), radius_x=r)
        self.add_contour(n, n + '-a', n + '-b', closed=True)

    def house(self):
        self.add_line('roof-1', (6, 14), (24, 6))
        self.add_line('roof-2', (24, 6), (42, 14))
        self.add_line('wall-right', (42, 14), (42, 40))
        self.add_arc('corner-right', (42, 40), (40, 42), radius_x=2)
        self.add_line('floor', (40, 42), (8, 42))
        self.add_arc('corner-left', (8, 42), (6, 40), radius_x=2)
        self.add_line('wall-left', (6, 40), (6, 14))
        self.add_contour('house', 'roof-1', 'roof-2', 'wall-right', 'corner-right', 'floor', 'corner-left', 'wall-left', closed=True)

    def build(self):
        self.house()
        for n, x, y in [('left', 17, 31), ('right', 29, 29)]:
            self.circle(n + '-note', x, y, 2)
        self.add_polyline('beam', (19, 31), (19, 21), (31, 18), (31, 29))
        self.relate('connect', 'beam', 'left-note')
        self.relate('connect', 'beam', 'right-note')

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '9208668ffaf9942e8d4ca5f86f11251d731315dc25ee39944137f08607e3644b', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '3640f2f0-b0c0-4dbd-9d92-86762ff6cfbb'}
