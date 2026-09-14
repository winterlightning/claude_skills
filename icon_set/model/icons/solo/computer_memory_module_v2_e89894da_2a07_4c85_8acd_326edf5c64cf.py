# Variant of computer-memory-module; parent file remains unchanged.
"""Horizontal memory board with two square chips and three contacts. HRECT_L visible bounds (2,6)-(46,42). Lucide memory-stick informed repeated contacts; the diagonal orientation is changed to make room for full-size chips."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e89894da-2a07-4c85-8acd-326edf5c64cf'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/computer ram_e89894da-2a07-4c85-8acd-326edf5c64cf.svg'
AUTHOR = 'gpt-6'

class ComputerMemoryModuleVariant2(Solo48):
    icon_id = 'computer-memory-module-v2'
    variant_of = 'computer-memory-module'
    variant_label = 'Roomier spacing — review 02'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('ram', 'memory', 'module', 'dimm', 'chip', 'hardware', 'computer', 'storage')

    def build(self) -> None:
        self.add_polyline('board',(4,8),(44,8),(44,32),(36,32),(24,32),(12,32),(4,32),closed=True)
        self.add_polyline('chip-left',(12,16),(20,16),(20,24),(12,24),closed=True)
        self.add_polyline('chip-right',(28,16),(36,16),(36,24),(28,24),closed=True)
        for i,x in enumerate((12,24,36)):
            self.add_line('contact-'+str(i),(x,32),(x,40))
            self.relate('connect','board','contact-'+str(i))
