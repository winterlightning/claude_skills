"""Right-facing beetle with a capsule shell and a broad hooked horn. Centerline extremes (6,8)-(42,40). Lucide bug informs attached legs; profile asymmetry preserves the source. No tiny eye or shell texture."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b5ef71c-5aa8-4146-809d-f56369f47fe4'
SOURCE_PATH = 'pictographic-primitives/animals/insect_3b5ef71c-5aa8-4146-809d-f56369f47fe4.svg'
AUTHOR = 'gpt-6'


class StagBeetle(Solo48):
    icon_id = 'stag-beetle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('stag beetle', 'beetle', 'insect', 'horn', 'bug', 'shell', 'profile', 'nature')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('shell-back',(12, 32),*(((7.35786438, 32.0), (4.0, 28.418278), (4, 24.0)), ((4, 19.581722), (7.35786438, 16.0), (12, 16))))
        self.add_line('shell-top',(12, 16),(28, 16))
        self.add_line('shell-front',(28, 16),(28, 32))
        self.add_line('belly-front',(28, 32),(24, 32))
        self.add_line('belly-middle',(24, 32),(14, 32))
        self.add_line('belly-back',(14, 32),(12, 32))
        self.add_bezier('head-rise',(28, 16),*(((28.0, 11.581722), (32.4771525, 8), (39, 8)),))
        self.add_bezier('horn-inner',(39, 8),*(((37.27927548, 10.05601453), (36.84458855, 12.63330042), (37.82264204, 14.98062879)), ((38.80069553, 17.32795716), (41.08140948, 19.18113615), (44, 20))))
        self.add_bezier('head-front',(44, 20),*(((44, 25.33504611), (40.30129534, 30.22736717), (34, 32)),))
        self.add_line('head-base',(34, 32),(28, 32))
        self.add_arc('leg-0',(14, 32),(10, 40),radius_x=10,radius_y=10,large_arc=False,sweep=True)
        self.add_bezier('leg-1',(34, 32),*(((34.0, 35.14757303), (35.85242697, 38.11145618), (39, 40)),))
        self.add_contour('shell',*('shell-back', 'shell-top', 'shell-front', 'belly-front', 'belly-middle', 'belly-back'),closed=True)
        self.add_contour('head',*('head-rise', 'horn-inner', 'head-front', 'head-base'),closed=False)
        self.relate('connect',*('shell', 'head'))
        self.relate('connect',*('shell', 'leg-0'))
        self.relate('connect',*('head', 'leg-1'))
