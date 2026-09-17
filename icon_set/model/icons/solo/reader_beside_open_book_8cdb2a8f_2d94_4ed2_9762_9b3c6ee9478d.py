"""A left-facing reader beside an open book.

Symbol plan: circular crown, angular nose and rounded chin flow into a continuous
neck and shoulder, as in the supplied profile reference. The book owns two
mirrored page outlines and their shared spine at x32. SQUARE centerline extremes
(6,6)-(42,42). Intentional asymmetry preserves the left-facing profile and book.
Lucide book-open original/atomic-debug informs paired page contours and spine.
Shared human_ref/user.svg informs circular head and smooth shoulder construction;
full_body_ref.png was inspected. The source's continuous neck is retained, so
there is no detached head/body gap. Omit ear, hair waves and writing marks to
keep the profile and pages open at 48 pixels. No text glyphs are authored.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8cdb2a8f-2d94-4ed2-9762-9b3c6ee9478d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/culture/batch-02/greek mythology_8cdb2a8f-2d94-4ed2-9762-9b3c6ee9478d.svg'
AUTHOR = 'gpt-6'


class ReaderBesideOpenBook(Solo48):
    icon_id = 'reader-beside-open-book'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ('reader-profile',)
    keywords = ('reader', 'person', 'book', 'reading', 'profile', 'pages')

    def build(self):
        self.add_arc('crown',(10,18),(34,18),radius_x=12)
        self.add_line('head-back',(34,18),(32,28))
        self.add_contour('head-back-outline','crown','head-back')
        self.add_polyline('nose',(10,18),(6,24),(10,24),(10,28))
        self.add_arc('chin',(10,28),(12,30),radius_x=2,sweep=False)
        self.add_line('neck',(12,30),(12,32))
        self.add_arc('shoulder',(12,32),(6,38),radius_x=6,sweep=False)
        self.add_line('body-side',(6,38),(6,42))
        self.add_contour('neck-shoulder','chin','neck','shoulder','body-side')
        self.relate('connect','head-back-outline','nose')
        self.relate('connect','nose','neck-shoulder')
        spine, half_width = 32, 10
        self.add_polyline('pages',(spine-half_width,24),(spine,28),
                          (spine+half_width,24),(spine+half_width,38),
                          (spine,42),(spine-half_width,38),closed=True)
        self.add_line('spine',(spine,28),(spine,42))
        self.relate('connect','pages','spine')
        self.relate('connect','head-back-outline','pages')
        self.relate('connect','head-back-outline','spine')
