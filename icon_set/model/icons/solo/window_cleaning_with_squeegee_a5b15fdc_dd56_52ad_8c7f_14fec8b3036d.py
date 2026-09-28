'A square window contains a diagonal squeegee whose long handle reaches the lower-right corner. The short rectangular blade sits across the handle, with a separate diagonal wipe streak above it.\n\nConstruction: Squeegee lies diagonally against a window pane; one blade and handle are retained, reflection streak omitted. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5b15fdc-dd56-52ad-8c7f-14fec8b3036d'
SOURCE_PATH = 'pictographic-primitives/wayfinding/window mirror cleaning wiper_a5b15fdc-dd56-52ad-8c7f-14fec8b3036d.svg'
AUTHOR = 'gpt-6'

class WindowCleaningWithSqueegee(Solo48):
    icon_id = 'window-cleaning-with-squeegee'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('window', 'squeegee', 'cleaning', 'glass', 'wiper', 'tool')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('window-1', (6, 6), (42, 6))
        self.add_line('window-2', (42, 6), (42, 42))
        self.add_line('window-3', (42, 42), (6, 42))
        self.add_line('window-4', (6, 42), (6, 6))
        self.add_line('blade-1', (16, 28), (28, 16))
        self.add_line('blade-2', (28, 16), (34, 22))
        self.add_line('blade-3', (34, 22), (28, 28))
        self.add_line('blade-4', (28, 28), (22, 34))
        self.add_line('blade-5', (22, 34), (16, 28))
        self.add_line('handle', (28, 28), (42, 42))
        self.add_contour('window', 'window-1', 'window-2', 'window-3', 'window-4', closed=True)
        self.add_contour('blade', 'blade-1', 'blade-2', 'blade-3', 'blade-4', 'blade-5', closed=True)
        self.relate('connect', 'handle', 'blade')
        self.relate('connect', 'handle', 'window')
