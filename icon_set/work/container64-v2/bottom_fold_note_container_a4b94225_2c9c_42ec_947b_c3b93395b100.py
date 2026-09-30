"""Reduce the folded corner to leave the central paper area clear.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (bottom-fold-note-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: fold kept at 12 so its triangle stays a legal hole.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'a4b94225-2c9c-42ec-947b-c3b93395b100'
SOURCE_PATH = 'pictographic-primitives/content/document_a4b94225-2c9c-42ec-947b-c3b93395b100.svg'
AUTHOR = 'claude-opus-5-5'


class BottomFoldNoteContainer(Container64):
    icon_id = 'bottom-fold-note-container'
    keyshape = Keyshape.SQUARE
    category = 'content'
    categories = ('content', 'other', 'primitives-generate')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('paper-1', (6, 6), (58, 6))
        self.add_line('paper-2', (58, 6), (58, 46))
        self.add_line('paper-3', (58, 46), (46, 58))
        self.add_line('paper-4', (46, 58), (6, 58))
        self.add_line('paper-5', (6, 58), (6, 6))
        self.add_line('fold-1', (46, 58), (46, 46))
        self.add_line('fold-2', (46, 46), (58, 46))
        self.add_contour('paper', 'paper-1', 'paper-2', 'paper-3', 'paper-4', 'paper-5', closed=True)
        self.add_contour('fold', 'fold-1', 'fold-2')
        self.relate('connect', 'fold', 'paper')
