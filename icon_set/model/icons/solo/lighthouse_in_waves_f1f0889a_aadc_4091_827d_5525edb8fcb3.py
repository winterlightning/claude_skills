"""A domed lighthouse above rolling water. One lantern band retained; crowded tower bands and window omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1f0889a-aadc-4091-827d-5525edb8fcb3'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/lighthouse bird_f1f0889a-aadc-4091-827d-5525edb8fcb3.svg'
AUTHOR = 'gpt-6'


class LighthouseInWaves(Solo48):
    icon_id = 'lighthouse-in-waves'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('lighthouse', 'beacon', 'sea', 'waves', 'coast', 'navigation', 'maritime', 'tower')

    def build(self) -> None:
        # Centerline extremes (5,2)-(43,46).
        self.add_polyline("left-tower", (14,36), (17,23), (17,15))
        self.add_arc("cap-left", (17,15), (24,8), radius_x=7)
        self.add_arc("cap-right", (24,8), (31,15), radius_x=7)
        self.add_polyline("right-tower", (31,15), (31,23), (34,36))
        self.add_contour("cap", "cap-left", "cap-right")
        self.add_line("lantern-band", (17,23), (31,23))
        self.add_line("mast", (24,2), (24,8))
        self.relate("connect", "left-tower", "cap")
        self.relate("connect", "right-tower", "cap")
        self.relate("connect", "mast", "cap")
        self.relate("connect", "lantern-band", "left-tower")
        self.relate("connect", "lantern-band", "right-tower")
        self.add_arc("wave-left", (5,43), (17,43), radius_x=6, radius_y=3, sweep=False)
        self.add_arc("wave-middle", (17,43), (31,43), radius_x=7, radius_y=3, sweep=False)
        self.add_arc("wave-right", (31,43), (43,43), radius_x=6, radius_y=3, sweep=False)
        self.add_contour("water", "wave-left", "wave-middle", "wave-right")
