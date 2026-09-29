"""A hand grips the handle beneath a right-facing megaphone. The rounded rear housing opens into a broad flared horn, while the wrist extends left below the handle.
Lucide megaphone rounded rear and flared horn. Physical hand wraps the handle; finger creases omitted. Deliberate right-facing asymmetry.
SQUARE: centerline extremes (6,6)-(42,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5587cff6-d8d9-4045-b4e0-05bcb4c1a7bc'
SOURCE_PATH = 'pictographic-primitives/work/labor megaphone_5587cff6-d8d9-4045-b4e0-05bcb4c1a7bc.svg'
AUTHOR = 'gpt-6'


class HandHoldingMegaphone(Solo48):
    icon_id = 'hand-holding-megaphone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    categories = ("work", "primitives")
    aliases = ()
    keywords = ('megaphone', 'hand', 'announcement', 'speaker', 'holding', 'labor')

    def build(self) -> None:
        self.add_line('horn-top', (14, 15), (22, 15))
        self.add_line('flare-top', (22, 15), (42, 6))
        self.add_line('mouth', (42, 6), (42, 30))
        self.add_line('flare-bottom', (42, 30), (22, 23))
        self.add_line('horn-bottom', (22, 23), (14, 23))
        self.add_arc('rear', (14, 23), (14, 15), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('horn', 'horn-top', 'flare-top', 'mouth', 'flare-bottom', 'horn-bottom', 'rear', closed=True)
        self.add_line('seam', (22, 15), (22, 23))
        self.relate("connect", 'seam', 'horn')
        self.add_line('handle', (22, 23), (25, 33))
        self.relate("connect", 'handle', 'horn')
        self.relate("connect", 'handle', 'seam')
        self.add_line('hand-1', (6, 33), (28, 33))
        self.add_line('hand-2', (28, 33), (28, 38))
        self.add_arc('palm', (28, 38), (24, 42), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('wrist', (24, 42), (6, 42))
        self.add_contour('grip', 'hand-1', 'hand-2', 'palm', 'wrist', closed=False)
        self.relate("connect", 'handle', 'grip')
