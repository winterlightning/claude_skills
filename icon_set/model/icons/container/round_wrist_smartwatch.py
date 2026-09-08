"""A round display enclosure framed by short rounded wristband attachments.
The blank reference face stays blank; no clock hands are introduced.

Keyshape VRECT_L; centerline extremes recorded in build below.
Lucide watch informs the circular face and mirrored straps. Rebuilt on CONTAINER64 with integer geometry.
Hosting measured with compose.py: plus does not clear, heart passes, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class RoundWristSmartwatch(Container64):
    icon_id = 'round-wrist-smartwatch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('round', 'wrist', 'smartwatch')

    def build(self) -> None:
        # VRECT_L centerline extremes (10,2)-(54,62).
        # Near-circular case: radius-20 halves joined by four-unit tangents.
        # The 12/16/20 triangle gives exact, mirrored strap junctions.
        self.add_arc("face-nw", (10, 32), (18, 16), radius_x=20)
        self.add_arc("face-nw-top", (18, 16), (30, 12), radius_x=20)
        self.add_line("face-top", (30, 12), (34, 12))
        self.add_arc("face-ne-top", (34, 12), (46, 16), radius_x=20)
        self.add_arc("face-ne", (46, 16), (54, 32), radius_x=20)
        self.add_arc("face-se", (54, 32), (46, 48), radius_x=20)
        self.add_arc("face-se-bottom", (46, 48), (34, 52), radius_x=20)
        self.add_line("face-bottom", (34, 52), (30, 52))
        self.add_arc("face-sw-bottom", (30, 52), (18, 48), radius_x=20)
        self.add_arc("face-sw", (18, 48), (10, 32), radius_x=20)
        self.add_contour("face", "face-nw", "face-nw-top", "face-top", "face-ne-top", "face-ne", "face-se", "face-se-bottom", "face-bottom", "face-sw-bottom", "face-sw", closed=True)
        for label, mirror in (("upper", False), ("lower", True)):
            def point(x, y):
                return (x, 64-y if mirror else y)
            self.add_line(label+"-left", point(18,16), point(18,7))
            self.add_arc(label+"-nw", point(18,7), point(23,2), radius_x=5, sweep=not mirror)
            self.add_line(label+"-top", point(23,2), point(41,2))
            self.add_arc(label+"-ne", point(41,2), point(46,7), radius_x=5, sweep=not mirror)
            self.add_line(label+"-right", point(46,7), point(46,16))
            self.add_contour(label, *(label+suffix for suffix in ("-left", "-nw", "-top", "-ne", "-right")))
            self.relate("connect", "face", label)
