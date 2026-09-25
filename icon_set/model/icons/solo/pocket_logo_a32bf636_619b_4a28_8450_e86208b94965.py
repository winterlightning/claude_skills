"""Symmetric pocket silhouette with a centered downward chevron. Reduce the double-outlined chevron to one stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a32bf636-619b-4a28-8450-e86208b94965'
SOURCE_PATH = 'pictographic-primitives/logos/pcoket logo_a32bf636-619b-4a28-8450-e86208b94965.svg'
AUTHOR = 'gpt-6'

class PocketLogo(Solo48):
    icon_id = 'pocket-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('pocket', 'read-later', 'save', 'chevron', 'logo', 'brand', 'bookmarks')

    def build(self):
        # Plan: Symmetric pocket silhouette with a centered downward chevron. Reduce the double-outlined chevron to one stroke.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_line('top',(10,6),(38,6))
        self.add_arc('top-right',(38,6),(42,10),radius_x=4)
        self.add_line('right',(42,10),(42,24))
        self.add_arc('bottom',(42,24),(6,24),radius_x=18)
        self.add_line('left',(6,24),(6,10))
        self.add_arc('top-left',(6,10),(10,6),radius_x=4)
        self.add_contour('pocket','top','top-right','right','bottom','left','top-left',closed=True)
        self.add_polyline('chevron',(16,19),(24,27),(32,19))

