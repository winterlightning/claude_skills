"""A gender ring with two diagonal arrows, an upper-left crossbar, and a plain lower stem. Lucide transgender informs the shaft junctions; the source plain lower stem is preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '559ed38a-1f07-5d60-b238-2442afb4acae'
SOURCE_PATH = 'pictographic-primitives/users/gender transgender_559ed38a-1f07-5d60-b238-2442afb4acae.svg'
AUTHOR = 'gpt-6'


class TransgenderSymbolSource559Ed38A(Solo48):
    icon_id = 'transgender-symbol-source-559ed38a'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/identity"
    aliases = ()
    keywords = ('transgender', 'gender', 'symbol', 'identity', 'pride', 'trans', 'arrows')

    def build(self) -> None:
        # Square extremes (6,6)-(42,42); circular nodes use a 6-8-10 triangle.
        self.add_arc('ring-top',(18,18),(30,18),radius_x=10)
        self.add_arc('ring-right',(30,18),(24,36),radius_x=10)
        self.add_arc('ring-left',(24,36),(18,18),radius_x=10)
        self.add_contour('ring','ring-top','ring-right','ring-left',closed=True)
        self.add_polyline('left-shaft',(18,18),(13,13),(6,6))
        self.add_line('right-shaft',(30,18),(42,6))
        self.add_polyline('arrow-left',(6,13),(6,6),(13,6))
        self.add_polyline('arrow-right',(35,6),(42,6),(42,13))
        self.add_polyline('crossbar',(9,17),(13,13),(17,9))
        self.add_line('stem',(24,36),(24,42))
        for member in ('left-shaft','right-shaft','stem'):
            self.relate('connect','ring',member)
        self.relate('connect','left-shaft','arrow-left')
        self.relate('connect','right-shaft','arrow-right')
        self.relate('connect','left-shaft','crossbar')
