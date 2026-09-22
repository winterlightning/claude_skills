"""A clipped document encloses a two-column spreadsheet grid. Grid spacing is eight units; two rows retain spreadsheet meaning at 48 pixels. Lucide file-spreadsheet informed simple document contour and separated content.
Whole subject explicitly authorized by user; preserve saved family.
Keyshape: VRECT_L; fine source details simplified only for native readability.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'f5ecf7d0-0a84-4271-be46-4c06dc377bd8'
SOURCE_PATH = 'pictographic-primitives/files/file sheet_f5ecf7d0-0a84-4271-be46-4c06dc377bd8.svg'
AUTHOR = "gpt-6"

class Icon(Solo48):
    icon_id = 'spreadsheet-document'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'files'
    aliases = ('Spreadsheet Document',)
    keywords = ('spreadsheet', 'document')
    def build(self):
        self.add_polyline("page",(8,4),(30,4),(40,14),(40,44),(8,44),closed=True)
        self.add_polyline("grid",(16,20),(24,20),(32,20),(32,28),(32,36),(24,36),(16,36),(16,28),closed=True)
        self.add_line("column-top",(24,20),(24,28))
        self.add_line("column-bottom",(24,28),(24,36))
        self.add_line("row-left",(16,28),(24,28))
        self.add_line("row-right",(24,28),(32,28))
        for name in ("column-top","column-bottom","row-left","row-right"):
            self.relate("connect","grid",name)
        self.relate("connect","column-top","column-bottom","row-left","row-right")
