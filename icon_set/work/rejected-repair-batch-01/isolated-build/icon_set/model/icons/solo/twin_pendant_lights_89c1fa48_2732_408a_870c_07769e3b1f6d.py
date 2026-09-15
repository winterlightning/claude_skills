"""Twin Pendant Lights. SQUARE centerlines (6,6)-(42,42): paired long shades and a shared mount. Omit the six light rays so the tall shades retain clear interiors.
Lucide lamp-ceiling / lamp-floor inform simple shades and explicit support joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89c1fa48-2732-408a-870c-07769e3b1f6d'
SOURCE_PATH = 'pictographic-primitives/lamps/lamp double_89c1fa48-2732-408a-870c-07769e3b1f6d.svg'
AUTHOR = 'gpt-6'


class TwinPendantLights(Solo48):
    icon_id = 'twin-pendant-lights'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/lighting'
    aliases = ()
    keywords = ('lamp', 'pendant', 'light', 'ceiling', 'twin', 'fixture')

    def build(self) -> None:
        self.add_polyline('mount', (6,6), (12,6), (36,6), (42,6))
        for x in (12,36):
            p=f'lamp-{x}'
            self.add_line(p+'-stem',(x,6),(x,18))
            self.add_arc(p+'-round-left',(x-6,24),(x,18),radius_x=6,sweep=True)
            self.add_arc(p+'-round-right',(x,18),(x+6,24),radius_x=6,sweep=True)
            self.add_line(p+'-right',(x+6,24),(x+6,42))
            self.add_line(p+'-bottom',(x+6,42),(x-6,42))
            self.add_line(p+'-left',(x-6,42),(x-6,24))
            self.add_contour(p+'-shade',*(p+s for s in ('-round-left','-round-right','-right','-bottom','-left')),closed=True)
            self.relate('connect',p+'-stem',p+'-shade')
            self.relate('connect',p+'-stem','mount')
