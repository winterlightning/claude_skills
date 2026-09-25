"""Twin-Shade Floor Lamp. SQUARE centerlines (6,6)-(42,42): two tapered shades, mirrored quarter-circle branches and a centered foot. Reduce the long S-curves to tangent quarter-circle bends.
Lucide lamp-ceiling / lamp-floor inform simple shades and explicit support joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '931c3447-04df-50d9-bd21-9f0f9565712a'
SOURCE_PATH = 'pictographic-primitives/lamps/standing lamp double_931c3447-04df-50d9-bd21-9f0f9565712a.svg'
AUTHOR = 'gpt-6'


class TwinShadeFloorLamp(Solo48):
    icon_id = 'twin-shade-floor-lamp'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'lamps'
    categories = ('lamps', 'primitives')
    aliases = ()
    keywords = ('lamp', 'floor', 'standing', 'shade', 'twin', 'lighting')

    def build(self) -> None:
        for x in (12,36):
            p=f'lamp-{x}'
            self.add_polyline(p+'-shade',(x-4,6),(x+4,6),(x+6,19),(x,19),(x-6,19),closed=True)
            self.add_line(p+'-upright',(x,19),(x,24))
            inner=x+6 if x<24 else x-6
            self.add_arc(p+'-bend',(x,24),(inner,30),radius_x=6,sweep=x>24)
            self.add_line(p+'-arm',(inner,30),(24,30))
            self.add_contour(p+'-branch',p+'-upright',p+'-bend',p+'-arm')
            self.relate('connect',p+'-branch',p+'-shade')
        self.relate('connect','lamp-12-branch','lamp-36-branch')
        self.add_line('stand',(24,30),(24,42))
        for x in (12,36): self.relate('connect','stand',f'lamp-{x}-branch')
        self.add_polyline('foot',(16,42),(24,42),(32,42))
        self.relate('connect','stand','foot')
