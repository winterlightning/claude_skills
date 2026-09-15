"""A capital G drawn as a double-line outline, the ring opening at the upper right and closing into a squared crossbar.

Plan: Open G built around a shared centre and 18-unit radius, with a squared bar.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: No useful brand match; shared circular letter construction.
Simplification: Double outline becomes one continuous G stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b10c303-e636-4c91-b96d-9caab31acd4b'
SOURCE_PATH = 'pictographic-primitives/logos/google search logo_1b10c303-e636-4c91-b96d-9caab31acd4b.svg'
AUTHOR = 'gpt-6'


class GoogleSearchLogo(Solo48):
    icon_id = 'google-search-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('google-search', 'google', 'search', 'letter-g', 'logo', 'brand', 'web')

    def build(self):
        self.add_bezier('top',(36,10),((33,7),(28,6),(24,6)))
        self.add_arc('left',(24,6),(24,42),radius_x=18,sweep=False)
        self.add_arc('lower',(24,42),(42,24),radius_x=18,sweep=False)
        self.add_line('bar',(42,24),(24,24))
        self.add_contour('g','top','left','lower','bar')
