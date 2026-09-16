"""A closed hardcover book with a rounded spine and a top page band.

VRECT_L fits the upright book: ink (8,0)-(56,64), centerline (10,2)-(54,62).
Reference: supplied failed SVG; Lucide book original and atomic-debug informed
rounded binding corners and a horizontal page band. The doubled inner spine
curl was removed so the binding has one clear outline. The binding remains
intentionally asymmetric.

Hosting (compose.py): plus valid; heart, check blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'closed-hardcover-book'
SOURCE_PATH = 'icon_set/dist/failed/container64/closed-hardcover-book.svg'
AUTHOR = 'gpt-6'


class ClosedHardcoverBook(Container64):
    icon_id = 'closed-hardcover-book'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('closed-hardcover-book-icon',)
    keywords = ('closed', 'hardcover', 'book')

    def build(self) -> None:
        # Plan: one rounded binding outline and a single top page divider.
        # Shared left/right walls own both divider attachments; no doubled spine.
        left, right, top, bottom, band_y, radius = 10, 54, 2, 62, 18, 8
        self.add_line('top', (left + radius, top), (right, top))
        self.add_line('right-upper', (right, top), (right, band_y))
        self.add_line('right-lower', (right, band_y), (right, bottom))
        self.add_line('bottom', (right, bottom), (left + radius, bottom))
        self.add_arc('spine-bottom', (left + radius, bottom), (left, bottom - radius), radius_x=radius)
        self.add_line('left-lower', (left, bottom - radius), (left, band_y))
        self.add_line('left-upper', (left, band_y), (left, top + radius))
        self.add_arc('spine-top', (left, top + radius), (left + radius, top), radius_x=radius)
        self.add_contour('cover', 'top', 'right-upper', 'right-lower', 'bottom', 'spine-bottom', 'left-lower', 'left-upper', 'spine-top', closed=True)
        self.add_line('page-band', (left, band_y), (right, band_y))
        self.relate('connect', 'page-band', 'cover')
