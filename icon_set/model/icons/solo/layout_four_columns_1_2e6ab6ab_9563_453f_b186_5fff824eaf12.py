"""layout-four-columns-1: approved original model.

Construction: Four equal columns on a nine-unit spacing grid; distinguish it from the existing three-column panel.
Keyshape: SQUARE; exact SOLO48 envelope.
Construction reference: layout-grid from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '2e6ab6ab-9563-453f-b186-5fff824eaf12'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout four columns 1_2e6ab6ab-9563-453f-b186-5fff824eaf12.svg'
AUTHOR = 'gpt-6'

class LayoutFourColumns1(Solo48):
    icon_id = 'layout-four-columns-1'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'four', 'columns', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self, 'frame', 6, 6, 42, 42, 4, xs=(15, 24, 33))
        for x in (15, 24, 33):
            line(self, f'column-{x}', (x, 6), (x, 42))
        contacts(self)
