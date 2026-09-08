"""Insect head; centerline extremes (2,2)-(46,46). Mirrored antennae, cheek eyes and open palps. Lucide bug informs rounded face and bilateral appendages; oval eyes simplified to dots."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48b9ec2f-d1e5-4c68-a4c7-5794c4616469'
SOURCE_PATH = 'pictographic-primitives/animals/insect cricket_48b9ec2f-d1e5-4c68-a4c7-5794c4616469.svg'
AUTHOR = 'gpt-6'


class InsectHeadWithAntennae(Solo48):
    icon_id = 'insect-head-with-antennae'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('insect', 'head', 'antennae', 'eyes', 'bug', 'cricket', 'face', 'nature')

    def build(self) -> None:
        # Insect head; centerline extremes (2,2)-(46,46). Mirrored antennae, cheek eyes and open palps. Lucide bug informs rounded face and bilateral appendages; oval eyes simplified to dots.
        self.add_arc('face-top', (19, 17), (29, 17), radius_x=13, radius_y=13, sweep=True)
        self.add_arc('face-right', (29, 17), (29, 41), radius_x=13, radius_y=13, sweep=True)
        self.add_arc('face-bottom', (29, 41), (19, 41), radius_x=13, radius_y=13, sweep=True)
        self.add_arc('face-left', (19, 41), (19, 17), radius_x=13, radius_y=13, sweep=True)
        self.add_contour('face', 'face-top', 'face-right', 'face-bottom', 'face-left', closed=True)
        self.add_line('antenna-stem-left', (19, 17), (14, 8))
        self.add_arc('antenna-arch-left', (14, 8), (2, 8), radius_x=6, radius_y=6, sweep=False)
        self.add_contour('antenna-left', 'antenna-stem-left', 'antenna-arch-left', closed=False)
        self.relate("connect", 'face', 'antenna-left')
        self.add_dot('eye-left', (18, 29))
        self.add_line('palp-left', (19, 41), (17, 46))
        self.relate("connect", 'face', 'palp-left')
        self.add_line('antenna-stem-right', (29, 17), (34, 8))
        self.add_arc('antenna-arch-right', (34, 8), (46, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('antenna-right', 'antenna-stem-right', 'antenna-arch-right', closed=False)
        self.relate("connect", 'face', 'antenna-right')
        self.add_dot('eye-right', (30, 29))
        self.add_line('palp-right', (29, 41), (31, 46))
        self.relate("connect", 'face', 'palp-right')
