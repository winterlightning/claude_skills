"""A tapering lighthouse with domed lantern, mast and two detached light rays. Paired rays preserve the source signal."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55a6ebde-c6ce-4e42-b15c-0803f5faeb14'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/lighthouse_55a6ebde-c6ce-4e42-b15c-0803f5faeb14.svg'
AUTHOR = 'gpt-6'


class LighthouseWithBeams(Solo48):
    icon_id = 'lighthouse-with-beams'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('lighthouse', 'beacon', 'light', 'beam', 'coast', 'navigation', 'maritime', 'tower')

    def build(self) -> None:
        # Centerline extremes (2,2)-(46,46).
        self.add_polyline("left-tower", (10,46), (17,22), (17,15))
        self.add_arc("cap-left", (17,15), (24,8), radius_x=7)
        self.add_arc("cap-right", (24,8), (31,15), radius_x=7)
        self.add_polyline("right-tower", (31,15), (31,22), (38,46))
        self.add_contour("cap", "cap-left", "cap-right")
        self.add_line("band", (17,22), (31,22))
        self.add_line("mast", (24,2), (24,8))
        self.add_polyline("ground", (10,46), (24,46), (38,46))
        self.add_line("door", (24,36), (24,46))
        for a,b in (("left-tower","cap"),("right-tower","cap"),("mast","cap"),("band","left-tower"),("band","right-tower"),("ground","left-tower"),("ground","right-tower"),("door","ground")):
            self.relate("connect", a,b)
        self.add_line("beam-left", (2,12), (8,15))
        self.add_line("beam-right", (40,15), (46,12))
