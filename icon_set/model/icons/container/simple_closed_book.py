"""A closed book has a rounded lower binding and a recessed page edge.

VRECT_L fits the upright book: ink (8,0)-(56,64), centerline (10,2)-(54,62).
Reference: supplied failed SVG; Lucide book original and atomic-debug informed
rounded spine corners and a horizontal page band. The overlapping inner binding
curl was simplified into one junction. The binding and recessed right edge
remain intentionally asymmetric.

Hosting (compose.py): check valid; plus, heart blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'simple-closed-book'
SOURCE_PATH = 'icon_set/dist/failed/container64/simple-closed-book.svg'
AUTHOR = 'gpt-6'


class SimpleClosedBook(Container64):
    icon_id = 'simple-closed-book'
    keyshape = Keyshape.VRECT_L
    aliases = ('closed-book',)
    keywords = ('simple', 'closed', 'book')

    def build(self) -> None:
        # Plan: continuous outside binding, bottom page band and recessed fore-edge.
        # The band joins the spine once, removing the overlapping inner curl.
        left, right, top, bottom, band_y, radius = 10, 54, 2, 62, 48, 8
        self.add_line('cover-left', (left, band_y), (left, top + radius))
        self.add_arc('cover-nw', (left, top + radius), (left + radius, top), radius_x=radius)
        self.add_line('cover-top', (left + radius, top), (right, top))
        self.add_line('cover-right', (right, top), (right, band_y))
        self.add_arc('page-recess', (right, band_y), (right, bottom), radius_x=16, sweep=False)
        self.add_line('page-bottom', (right, bottom), (left + radius, bottom))
        self.add_arc('binding', (left + radius, bottom), (left, bottom - radius), radius_x=radius)
        self.add_line('binding-side', (left, bottom - radius), (left, band_y))
        self.add_contour('cover', 'cover-left', 'cover-nw', 'cover-top', 'cover-right', 'page-recess', 'page-bottom', 'binding', 'binding-side', closed=True)
        self.add_line('page-top', (left, band_y), (right, band_y))
        self.relate('connect', 'page-top', 'cover')
