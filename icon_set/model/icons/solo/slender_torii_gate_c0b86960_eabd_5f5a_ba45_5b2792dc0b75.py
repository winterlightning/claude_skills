'Upturned lintel and mirrored supports; Lucide landmark informs evenly spaced structural strokes. Thin double lintel reduced to one stroke.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c0b86960-eabd-5f5a-ba45-5b2792dc0b75'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/japan shrine_c0b86960-eabd-5f5a-ba45-5b2792dc0b75.svg'
AUTHOR = 'gpt-6'

class SlenderToriiGate(Solo48):
    icon_id = 'slender-torii-gate'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    aliases = ()
    keywords = ('torii', 'gate', 'shrine', 'japan', 'shinto', 'temple', 'landmark', 'religion')

    def build(self) -> None:
        # Shared axis 24; centerline envelope (8,6)-(40,42).
        axis, left, right, top, bottom = 24, 8, 40, 4, 44
        roof_y, beam_y, post_x = top + 3, 20, 15
        self.add_arc("eave-left", (left,top), (left+6,roof_y), radius_x=6, radius_y=3, sweep=False)
        points = list(dict.fromkeys([(left+6,roof_y), (post_x,roof_y), (axis,roof_y), (48-post_x,roof_y), (right-6,roof_y)]))
        points.sort()
        for n,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f"lintel-{n}", a, b)
        self.add_arc("eave-right", (right-6,roof_y), (right,top), radius_x=6, radius_y=3, sweep=False)
        self.add_contour("roof", "eave-left", *[f"lintel-{n}" for n in range(1,len(points))], "eave-right")
        self.add_polyline("beam", (left+2,beam_y), (post_x,beam_y), (axis,beam_y), (48-post_x,beam_y), (right-2,beam_y))
        for side, x in (("left",post_x),("right",48-post_x)):
            foot_x = x - 2 if side == "left" else x + 2
            self.add_polyline("post-"+side, (x,roof_y), (x,beam_y), (foot_x,bottom))
            self.relate("connect", "roof", "post-"+side)
            self.relate("connect", "beam", "post-"+side)

