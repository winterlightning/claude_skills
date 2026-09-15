"""Mirrored figure-eight body owns its shared neck attachment; retain a round sound hole, omit bridge and strings. Extremes (8,4)-(40,44). Lucide guitar smooth bout transitions."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e3b9013-429e-4cb3-8093-1e76dd0f5307'
SOURCE_PATH = 'pictographic-primitives/music/guitar_2e3b9013-429e-4cb3-8093-1e76dd0f5307.svg'
AUTHOR = 'gpt-6'

class AcousticGuitar(Solo48):
    icon_id = 'acoustic-guitar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/music"
    aliases = ()
    keywords = ('guitar', 'acoustic', 'string', 'instrument', 'folk', 'music', 'strum')

    def build(self):
        axis=24
        start=(axis,16)
        segments=(((16,16),(10,18),(12,24)), ((13,27),(14,27),(12,30)), ((9,33),(8,34),(8,36)), ((8,42),(16,44),(axis,44)))
        self.add_bezier('body-left',start,*segments)
        mirror=lambda p:(2*axis-p[0],p[1])
        knots=(start,)+tuple(segment[2] for segment in segments)
        reverse=tuple((mirror(c2),mirror(c1),mirror(knots[n])) for n,(c1,c2,end) in reversed(tuple(enumerate(segments))))
        self.add_bezier('body-right',mirror(knots[-1]),*reverse)
        self.add_contour('body','body-left','body-right',closed=True)
        self.add_line('neck',(24,4),(24,16))
        self.add_line('peg',(24,4),(32,4))
        self.relate('connect','neck','body')
        self.relate('connect','neck','peg')
        cx, cy, radius = 24, 30, 3
        points = ((cx-radius,cy),(cx,cy-radius),(cx+radius,cy),(cx,cy+radius))
        for n in range(4):
            self.add_arc(f'sound-hole-{n}',points[n],points[(n+1)%4],radius_x=radius)
        self.add_contour('sound-hole', *[f'sound-hole-{n}' for n in range(4)], closed=True)
