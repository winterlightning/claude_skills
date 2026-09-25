"""Mirrored triceratops head with three-point frill and tapered snout. Centerlines (6,6)-(42,42). Mirrored dot eyes; frill spikes are deliberate corners."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8815c76-ec33-41d4-8279-fe23287113c2'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur triceratop head_c8815c76-ec33-41d4-8279-fe23287113c2.svg'
AUTHOR = 'gpt-6'


class TriceratopsFrillHead(Solo48):
    icon_id = 'triceratops-frill-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('triceratops', 'dinosaur', 'head', 'frill', 'spikes', 'prehistoric', 'reptile', 'silhouette')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('frill-left', (6, 6), (24, 6), radius_x=13, radius_y=13, large_arc=False, sweep=False)
        self.add_arc('frill-right', (24, 6), (42, 6), radius_x=13, radius_y=13, large_arc=False, sweep=False)
        self.add_arc('side-right', (42, 6), (39, 18), radius_x=4, radius_y=16, large_arc=False, sweep=True)
        self.add_line('horn-right', (39, 18), (37, 23))
        self.add_bezier('cheek-right', (42, 27), *(((42, 28.54700538), (42, 30.45299462), (42, 32)),))
        self.add_bezier('jowl-right', (42, 32), *(((42, 33.97298648), (39.91841996, 35.67132939), (37, 36)),))
        self.add_bezier('chin-right', (37, 36), *(((34.78816497, 39.93781809), (29.55777253, 42), (24, 42)),))
        self.add_bezier('chin-left', (24, 42), *(((18.44222747, 42), (13.21183503, 39.93781809), (11, 36)),))
        self.add_bezier('jowl-left', (11, 36), *(((8.08158004, 35.67132939), (6, 33.97298648), (6, 32)),))
        self.add_bezier('cheek-left', (6, 32), *(((6, 30.45299462), (6, 28.54700538), (6, 27)),))
        self.add_line('horn-left', (11, 23), (9, 18))
        self.add_arc('side-left', (9, 18), (6, 6), radius_x=4, radius_y=16, large_arc=False, sweep=True)
        self.add_line('join-right', (37, 23), (42, 27))
        self.add_line('join-left', (6, 27), (11, 23))
        self.add_line('eye-left', (18, 27), (18, 27))
        self.add_line('eye-right', (30, 27), (30, 27))
        self.add_contour('outline', *('horn-left', 'side-left', 'frill-left', 'frill-right', 'side-right', 'horn-right', 'join-right', 'cheek-right', 'jowl-right', 'chin-right', 'chin-left', 'jowl-left', 'cheek-left', 'join-left'), closed=True)
