"""Cyrillic Letter Ya.
User explicitly requested solo geometry for this symbol, independent of typeface.
Right stem and upper bowl share true nodes. Bounds (8,4)-(40,44). Bowl radii12; omit serifs; preserve diagonal lower leg.
Reference: pictographic-primitives/interface-essential/cyrillic alphabet_e10e748f-638c-5583-88b9-695922930c2d.svg. Source supplies topology and arrangement.
Lucide omega supplies coherent bowl-to-stem contour construction, not coordinates.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'e10e748f-638c-5583-88b9-695922930c2d'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cyrillic alphabet_e10e748f-638c-5583-88b9-695922930c2d.svg'
AUTHOR = 'gpt-6-astra'

class Symbol(Solo48):
    icon_id = 'cyrillic-letter-ya'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ('Cyrillic Letter Ya',)
    keywords = ('cyrillic', 'letter', 'ya')

    def build(self):
        self.add_line('bowl-top-1',(40,4),(20,4))
        self.add_arc('bowl-upper',(20,4),(8,16),radius_x=12,sweep=False)
        self.add_arc('bowl-lower',(8,16),(20,28),radius_x=12,sweep=False)
        self.add_line('bowl-bottom-1',(20,28),(24,28))
        self.add_line('bowl-bottom-2',(24,28),(40,28))
        self.add_line('upper-stem',(40,28),(40,4))
        self.add_contour('bowl','bowl-top-1','bowl-upper','bowl-lower','bowl-bottom-1','bowl-bottom-2','upper-stem',closed=True)
        self.add_line('lower-stem',(40,28),(40,44))
        self.add_line('leg',(24,28),(8,44))
        self.relate('connect','leg','bowl-bottom-1','bowl-bottom-2')
        self.relate('connect','lower-stem','upper-stem','bowl-bottom-2')
