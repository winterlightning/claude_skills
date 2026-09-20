"""A diagonal skeleton key with a round bow at lower left and a thin shaft rising to upper right, ending in short teeth. Exclude the smartphone and avoid a solid key-tag blade.

Plan: Round bow with a rising diagonal shaft and two teeth; source orientation preserved. Bounds (2,2)-(30,30).
Construction reference: Lucide key-round: round bow and connected shaft; source owns orientation and teeth."""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '45efdc96-5aab-49eb-ac68-b0e1ceb428c9'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone key_45efdc96-5aab-49eb-ac68-b0e1ceb428c9.svg'
SOURCE_ICON_IDS = ('45efdc96-5aab-49eb-ac68-b0e1ceb428c9',)
AUTHOR = 'gpt-6'

class DiagonalRoundBowKeySymbol(Symbol32):
    icon_id = 'diagonal-round-bow-key-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('diagonal', 'round', 'bow', 'key', 'symbol')

    def build(self) -> None:
        # Bow has radius ten and an exact 6-8-10 shaft attachment at (18,12).
        self.add_arc('bow-a',(18,12),(6,28),radius_x=10)
        self.add_arc('bow-b',(6,28),(18,12),radius_x=10)
        self.add_contour('bow','bow-a','bow-b',closed=True)
        self.add_polyline('shaft',(18,12),(24,6),(30,2))
        self.add_line('tooth-top',(30,2),(26,2))
        self.add_line('tooth-lower',(24,6),(20,2))
        self.relate('connect','bow','shaft')
        self.relate('connect','shaft','tooth-top')
        self.relate('connect','shaft','tooth-lower')
