from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '194f3651-4280-5fce-8d9a-c4d0aaa5c514'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/minoan palace_194f3651-4280-5fce-8d9a-c4d0aaa5c514.svg'
AUTHOR = 'gpt-6'

class LandmarkVariant3(Solo48):
    icon_id = 'minoan-palace-v3'
    variant_of = 'minoan-palace-v2'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('minoan', 'palace', 'knossos', 'crete', 'greece', 'ancient', 'columns', 'ruins', 'heritage')

    def build(self):
        self.add_polyline('roof', (6, 13), (24, 6), (42, 13))
        self.add_polyline('hall', (6, 13), (6, 29), (12, 29), (20, 29), (28, 29), (36, 29), (42, 29), (42, 13))
        self.add_polyline('base', (6, 42), (12, 42), (20, 42), (28, 42), (36, 42), (42, 42))
        for x in (12, 20, 28, 36):
            self.add_line(f'column-{x}', (x, 29), (x, 42))
            self.relate('connect', f'column-{x}', 'hall')
            self.relate('connect', f'column-{x}', 'base')
        self.relate('connect', 'roof', 'hall')
