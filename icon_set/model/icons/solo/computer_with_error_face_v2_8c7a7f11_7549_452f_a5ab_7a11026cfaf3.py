"""Computer error face with crossed eyes, mouth and an eight-unit stand. SQUARE centerline bounds (6,6)-(42,42). Lucide monitor-x informed stand and error strokes; corners use standard round joins."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8c7a7f11-7549-452f-a5ab-7a11026cfaf3'
SOURCE_PATH = 'pictographic-primitives/websites/server error desktop_8c7a7f11-7549-452f-a5ab-7a11026cfaf3.svg'
AUTHOR = 'gpt-6'

class ComputerWithErrorFaceVariant2(Solo48):
    icon_id = 'computer-with-error-face-v2'
    variant_of = 'computer-with-error-face'
    variant_label = 'Roomier spacing — review 03'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('computer', 'error', 'face', 'monitor', 'crash', 'tongue', 'desktop')

    def build(self):
        self.add_polyline('monitor', (6, 6), (42, 6), (42, 34), (24, 34), (6, 34), closed=True)
        for side, cx in (('left', 16), ('right', 32)):
            self.add_polyline(side + '-a', (cx - 2, 14), (cx, 16), (cx + 2, 18))
            self.add_polyline(side + '-b', (cx + 2, 14), (cx, 16), (cx - 2, 18))
            self.relate('connect', side + '-a', side + '-b')
        self.add_line('mouth', (18, 26), (30, 26))
        self.add_line('stand', (24, 34), (24, 42))
        self.add_polyline('foot', (14, 42), (24, 42), (34, 42))
        self.relate('connect', 'monitor', 'stand')
        self.relate('connect', 'stand', 'foot')
