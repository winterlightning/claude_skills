'Two notched rectangular tickets overlap, with the front ticket tilted downward to the right. Semicircular cutouts interrupt the short sides of both otherwise plain tickets.\n\nConstruction: Two overlapping rectangular admission tickets with a perforation mark; omitted text and small edge notches. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd339f0a5-12c2-4dda-94d7-3128058c2dca'
SOURCE_PATH = 'pictographic-primitives/wayfinding/tickets_d339f0a5-12c2-4dda-94d7-3128058c2dca.svg'
AUTHOR = 'gpt-6'

class PairOfAdmissionTickets(Solo48):
    icon_id = 'pair-of-admission-tickets'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('ticket', 'admission', 'pair', 'pass', 'event', 'entry')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('front-0-joint-1', (9, 16), (16, 16))
        self.add_line('front-0-joint-2', (16, 16), (27, 16))
        self.add_arc('front-1', (27, 16), (30, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('front-2-joint-1', (30, 19), (30, 32))
        self.add_line('front-2-joint-2', (30, 32), (30, 39))
        self.add_arc('front-3', (30, 39), (27, 42), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('front-4', (27, 42), (9, 42))
        self.add_arc('front-5', (9, 42), (6, 39), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('front-6', (6, 39), (6, 19))
        self.add_arc('front-7', (6, 19), (9, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('rear-1', (16, 16), (16, 6))
        self.add_line('rear-2', (16, 6), (42, 6))
        self.add_line('rear-3', (42, 6), (42, 32))
        self.add_line('rear-4', (42, 32), (30, 32))
        self.add_line('perforation', (16, 32), (20, 32))
        self.add_contour('front', 'front-0-joint-1', 'front-0-joint-2', 'front-1', 'front-2-joint-1', 'front-2-joint-2', 'front-3', 'front-4', 'front-5', 'front-6', 'front-7', closed=True)
        self.add_contour('rear', 'rear-1', 'rear-2', 'rear-3', 'rear-4', closed=False)
        self.relate('connect', 'rear', 'front')
