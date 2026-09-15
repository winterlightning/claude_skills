"""Nine plus signs on a shared 15-unit lattice with a larger central cross. Preserve all nine marks and bilateral symmetry; keep the peripheral strokes short."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e68275dd-d33b-48a4-97e7-8f4d17faf45b'
SOURCE_PATH = 'pictographic-primitives/logos/tableau logo_e68275dd-d33b-48a4-97e7-8f4d17faf45b.svg'
AUTHOR = 'gpt-6'

class TableauLogo(Solo48):
    icon_id = 'tableau-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('tableau', 'analytics', 'visualization', 'plus', 'logo', 'brand', 'data')

    def build(self):
        # Plan: Nine plus signs on a shared 15-unit lattice with a larger central cross. Preserve all nine marks and bilateral symmetry; keep the peripheral strokes short.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        for row,y in enumerate((9,24,39)):
            for col,x in enumerate((9,24,39)):
                r=4 if row==col==1 else 3
                n=f'plus-{row}-{col}'
                for k,p in enumerate([(x-r,y),(x+r,y),(x,y-r),(x,y+r)]):self.add_line(n+'-'+str(k),(x,y),p)
                for a in range(4):
                    for b in range(a+1,4):self.relate('connect',n+'-'+str(a),n+'-'+str(b))

