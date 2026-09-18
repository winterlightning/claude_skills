"""Independent 32px profile of vertical-paperclip-attachment-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f9e485a4-15fe-4935-b76e-115de9c92c9b'
SOURCE_PATH = 'pictographic-primitives/other/attachment vertical_f9e485a4-15fe-4935-b76e-115de9c92c9b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f9e485a4-15fe-4935-b76e-115de9c92c9b', 'pictographic-primitives/other/attachment vertical_f9e485a4-15fe-4935-b76e-115de9c92c9b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/vertical-paperclip-attachment-solo',)
SOLO_SOURCE_ICON_IDS = ('vertical-paperclip-attachment-solo',)
REFERENCE_EXPORT_SHA256 = '78f02281fd34b2f90f08f0c33d7d81c8d2f8fa650498e209d2ec760487ecfeec'

class Drawing(Sub32):
    icon_id = 'vertical-paperclip-attachment-solo-profile32'
    keyshape = Keyshape.VRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (6, 12), (26, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (26, 12), (26, 24))
        self.add_bezier('p1-r1-3', (26, 24), ((26, 27), (23, 30), (20, 30)))
        self.add_bezier('p1-r1-4', (20, 30), ((16, 30), (13, 27), (13, 24)))
        self.add_line('p1-r1-5', (13, 24), (13, 13))
        self.add_arc('p1-r1-6', (13, 13), (19, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (19, 13), (19, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
