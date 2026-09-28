"""Square envelope; ended the repeated columns exactly at the common base.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
Lucide landmark: repeated columns sharing one base.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '194f3651-4280-5fce-8d9a-c4d0aaa5c514'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/minoan palace_194f3651-4280-5fce-8d9a-c4d0aaa5c514.svg'
AUTHOR = 'gpt-6'

class Landmark(Solo48):
    icon_id = 'minoan-palace'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    categories = ('landmarks', 'primitives')
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
