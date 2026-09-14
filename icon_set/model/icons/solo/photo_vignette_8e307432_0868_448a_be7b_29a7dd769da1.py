"""Photo vignette (photography), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e307432-0868-448a-be7b-29a7dd769da1'
SOURCE_PATH = 'icons-json/photography/photo vignette_8e307432-0868-448a-be7b-29a7dd769da1.json'
AUTHOR = 'gpt-6'

class PhotoVignette(Solo48):
    icon_id = 'photo-vignette'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('photo', 'vignette', 'photography')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e1', (24, 14), (24, 13), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_arc('e2', (24, 35), (24, 34), radius_x=36, radius_y=36, large_arc=False, sweep=False)
        self.add_arc('e3', (15, 19), (15, 18), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('e4', (33, 19), (33, 18))
        self.add_arc('e5', (15, 29), (15, 28), radius_x=34, radius_y=34, large_arc=False, sweep=True)
        self.add_arc('e6', (33, 29), (33, 28), radius_x=28, radius_y=28, large_arc=False, sweep=True)
        self.add_contour('c0', *('e1',), closed=False)
        self.add_contour('c1', *('e2',), closed=False)
        self.add_contour('c2', *('e3',), closed=False)
        self.add_contour('c3', *('e4',), closed=False)
        self.add_contour('c4', *('e5',), closed=False)
        self.add_contour('c5', *('e6',), closed=False)
        self.add_contour('e0', *('e0-top', 'e0-bottom'), closed=True)
