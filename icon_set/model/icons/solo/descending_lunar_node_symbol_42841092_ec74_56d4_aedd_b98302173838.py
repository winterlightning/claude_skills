"""Descending lunar node with paired terminal circles. SQUARE (2,2)-(46,46). Equal radii and mirrored arms; source crossings reduced to edge attachments. No useful direct Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42841092-ec74-56d4-aedd-b98302173838'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/astrology tail node_42841092-ec74-56d4-aedd-b98302173838.svg'


class DescendingLunarNodeSymbol(Solo48):
    icon_id = 'descending-lunar-node-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('lunar node', 'astrology', 'descending', 'south node', 'symbol', 'horoscope', 'glyph', 'moon')

    def build(self) -> None:
        self.add_arc('left-ring-top', (2, 10), (18, 10), radius_x=8, sweep=True)
        self.add_arc('left-ring-bottom', (18, 10), (2, 10), radius_x=8, sweep=True)
        self.add_contour('left-ring', 'left-ring-top', 'left-ring-bottom', closed=True)
        self.add_arc('right-ring-top', (30, 10), (46, 10), radius_x=8, sweep=True)
        self.add_arc('right-ring-bottom', (46, 10), (30, 10), radius_x=8, sweep=True)
        self.add_contour('right-ring', 'right-ring-top', 'right-ring-bottom', closed=True)
        self.add_line('left-arm', (18,10), (14,36))
        self.add_arc('bowl', (14,36), (34,36), radius_x=10, sweep=False)
        self.add_line('right-arm', (34,36), (30,10))
        self.add_contour('node', 'left-arm', 'bowl', 'right-arm')
        self.relate('connect', 'node', 'left-ring')
        self.relate('connect', 'node', 'right-ring')
