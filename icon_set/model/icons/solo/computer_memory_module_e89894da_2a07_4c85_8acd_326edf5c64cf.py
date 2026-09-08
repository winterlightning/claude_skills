"""A diagonal memory board with two diamond chips and three edge contacts.

SQUARE extremes (2,2)-(46,46) accommodate the diagonal silhouette. Lucide
memory-stick informs repeated edge contacts; source rotation is deliberate.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e89894da-2a07-4c85-8acd-326edf5c64cf'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/computer ram_e89894da-2a07-4c85-8acd-326edf5c64cf.svg'


class ComputerMemoryModule(Solo48):
    icon_id = 'computer-memory-module'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('ram', 'memory', 'module', 'dimm', 'chip', 'hardware', 'computer', 'storage')

    def build(self) -> None:
        self.add_polyline('board', (2, 30), (30, 2), (46, 18), (18, 46), closed=True)
        self.add_polyline('chip-lower', (16, 25), (21, 30), (16, 35), (11, 30), closed=True)
        self.add_polyline('chip-upper', (30, 11), (35, 16), (30, 21), (25, 16), closed=True)
        self.add_line('contact-0', (25, 39), (27, 41))
        self.relate('connect', 'board', 'contact-0')
        self.add_line('contact-1', (31, 33), (33, 35))
        self.relate('connect', 'board', 'contact-1')
        self.add_line('contact-2', (37, 27), (39, 29))
        self.relate('connect', 'board', 'contact-2')
