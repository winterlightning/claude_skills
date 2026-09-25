"""A round face smartwatch with a yuan mark.

Plan: a six arc circular face, paired rear strap runs, and a centered yuan
glyph. Strap and face share four explicit attachment nodes. Lucide watch
informed the circle and band construction; the currency glyph follows source.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b1f2ce85-d591-4522-b2a6-64d3fc5c75f6"
SOURCE_PATH = 'pictographic-primitives/combination/smart watch circle yuan sign_b1f2ce85-d591-4522-b2a6-64d3fc5c75f6.svg'
AUTHOR = "gpt-6"


class SmartWatchYuanSymbol(Solo48):
    icon_id = "smart-watch-yuan-symbol"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("yuan smartwatch", "watch payment")
    keywords = ("watch", "smartwatch", "yuan", "currency", "payment")

    def build(self) -> None:
        # Round dial owns four strap endpoints. Omit the nonessential transverse end seams
        # rather than close the strap openings into tiny counters.
        curves=[((8,24),(8,17),(11,12),(16,10)),((16,10),(20,7),(28,7),(32,10)),((32,10),(37,12),(40,17),(40,24)),((40,24),(40,31),(37,36),(32,38)),((32,38),(28,41),(20,41),(16,38)),((16,38),(11,36),(8,31),(8,24))]
        for j,(a,c1,c2,b) in enumerate(curves):self.add_bezier(f'face-{j}',a,(c1,c2,b))
        self.add_contour('face',*(f'face-{j}' for j in range(6)),closed=True)
        for side,x in [('left',16),('right',32)]:
            for name,y,end in [('upper',10,4),('lower',38,44)]:
                n=f'{name}-strap-{side}';self.add_line(n,(x,y),(x,end));self.relate('connect','face',n)
        self.add_polyline('yuan-forks',(19,18),(24,25),(29,18))
        self.add_polyline('yuan-bar',(20,25),(24,25),(28,25))
        self.add_line('yuan-stem',(24,25),(24,32));self.relate('connect','yuan-forks','yuan-bar','yuan-stem')

