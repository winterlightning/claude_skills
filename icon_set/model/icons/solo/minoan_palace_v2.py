# Variant of minoan-palace; parent file remains unchanged.
'Minoan palace without the two interior window marks. HRECT_XL retains the raised hall and column rhythm. Lucide landmark informs geometric structural spacing.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '194f3651-4280-5fce-8d9a-c4d0aaa5c514'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/minoan palace_194f3651-4280-5fce-8d9a-c4d0aaa5c514.svg'
AUTHOR = 'gpt-6'

class LandmarkVariant2(Solo48):
    icon_id = 'minoan-palace-v2'
    variant_of = 'minoan-palace'
    variant_label = 'Remove interior marks'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('minoan', 'palace', 'knossos', 'crete', 'greece', 'ancient', 'columns', 'ruins', 'heritage')

    def build(self):
        self.add_polyline('roof', (2, 13), (24, 5), (46, 13))
        self.add_polyline('hall', (2, 13), (2, 29), (12, 29), (20, 29), (28, 29), (36, 29), (46, 29), (46, 13))
        self.add_polyline('base', (2, 43), (12, 43), (20, 43), (28, 43), (36, 43), (46, 43))
        for x in (12, 20, 28, 36):
            self.add_line(f'column-{x}', (x, 29), (x, 43))
            self.relate('connect', f'column-{x}', 'hall')
            self.relate('connect', f'column-{x}', 'base')
        self.relate('connect', 'roof', 'hall')
