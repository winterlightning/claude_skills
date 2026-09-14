"""B Letter Underlined. Retains the identifying silhouette and visible features.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Lucide type, inspected earlier: coherent monoline lettering.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5597f318-b426-459a-89c5-29372f14b28f'
SOURCE_PATH = 'pictographic-primitives/symbol/b (text u)_5597f318-b426-459a-89c5-29372f14b28f.svg'
AUTHOR = 'gpt-6'

class BLetterUnderlinedVariant2(Solo48):
    icon_id = 'b-letter-underlined-v2'
    variant_of = 'b-letter-underlined'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbols/standalone'
    aliases = ()
    keywords = ('b', 'letter', 'text', 'underline', 'typography', 'alphabet', 'language')

    def build(self) -> None:
        self.add_line('b-top', (8, 4), (26, 4))
        self.add_arc('b-upper', (26, 4), (26, 18), radius_x=12, radius_y=7, sweep=True)
        self.add_arc('b-lower', (26, 18), (26, 32), radius_x=14, radius_y=7, sweep=True)
        self.add_line('b-back-1', (26, 32), (8, 32))
        self.add_line('b-back-2', (8, 32), (8, 18))
        self.add_line('b-back-3', (8, 18), (8, 4))
        self.add_contour('b', 'b-top', 'b-upper', 'b-lower', 'b-back-1', 'b-back-2', 'b-back-3', closed=True)
        self.add_line('b-bar', (8, 18), (26, 18))
        self.relate('connect', 'b', 'b-bar')
        self.add_line('underline', (8, 44), (40, 44))
