"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '5bd8438c-94c0-4326-8e22-5188c667350d'
SOURCE_PATH = 'icon_set/model/icons/symbol/file_emails_sub32_symbol_5bd8438c_94c0_4326_8e22_5188c667350d.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3a0d8a6c330cc57b40f528bfa1ed73c9c7fa335c60f60b7b04e091d497afec40'
SOURCE_REFERENCES = (('5bd8438c-94c0-4326-8e22-5188c667350d', 'pictographic-primitives/emails/file_5bd8438c-94c0-4326-8e22-5188c667350d.svg'), ('ee647811-20d2-4d87-9000-0d11db8aa255', 'pictographic-primitives/files/document_ee647811-20d2-4d87-9000-0d11db8aa255.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'file-emails-sub32-symbol-resize'
    variant_of = 'file-emails-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'emails'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (6, 10), (14, 10))
        self.add_line('p2-r1-1', (6, 15), (14, 15))
        self.add_line('p3-r1-1', (2, 2), (14, 2))
        self.add_line('p3-r1-2', (14, 2), (18, 6))
        self.add_line('p3-r1-3', (18, 6), (18, 22))
        self.add_line('p3-r1-4', (18, 22), (2, 22))
        self.add_line('p3-r1-5', (2, 22), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
