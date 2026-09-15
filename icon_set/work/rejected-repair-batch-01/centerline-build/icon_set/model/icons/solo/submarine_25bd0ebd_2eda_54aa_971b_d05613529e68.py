"""submarine: reconstructed on SOLO48 from its reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25bd0ebd-2eda-54aa-971b-d05613529e68'
SOURCE_PATH = 'pictographic-primitives/transportation/submarine_25bd0ebd-2eda-54aa-971b-d05613529e68.svg'
AUTHOR = 'gpt-6'


class Submarine(Solo48):
    icon_id = 'submarine'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('submarine', 'sub', 'underwater', 'navy', 'vessel', 'ocean', 'periscope', 'marine')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('hull-top-1',(4, 32),(14, 24))
        self.add_line('hull-top-2',(14, 24),(20, 24))
        self.add_line('hull-top-3',(20, 24),(30, 24))
        self.add_line('hull-top-4',(30, 24),(34, 24))
        self.add_bezier('nose-top',(34, 24),*(((39.91404021, 24.77178901), (44, 28.13791389), (44, 32)),))
        self.add_bezier('nose-bottom',(44, 32),*(((44, 35.86208611), (39.91404021, 39.22821099), (34, 40)),))
        self.add_line('hull-bottom-1',(34, 40),(14, 40))
        self.add_line('hull-bottom-2',(14, 40),(4, 32))
        self.add_line('tower-1',(20, 24),(20, 16))
        self.add_line('tower-2',(20, 16),(24, 16))
        self.add_line('tower-3',(24, 16),(30, 16))
        self.add_line('tower-4',(30, 16),(30, 24))
        self.add_line('periscope-1',(24, 16),(24, 8))
        self.add_line('periscope-2',(24, 8),(30, 8))
        self.add_line('tail-1',(4, 24),(4, 32))
        self.add_line('tail-2',(4, 32),(4, 40))
        self.add_contour('hull',*('hull-top-1', 'hull-top-2', 'hull-top-3', 'hull-top-4', 'nose-top', 'nose-bottom', 'hull-bottom-1', 'hull-bottom-2'),closed=True)
        self.add_contour('tower',*('tower-1', 'tower-2', 'tower-3', 'tower-4'),closed=False)
        self.add_contour('periscope',*('periscope-1', 'periscope-2'),closed=False)
        self.add_contour('tail',*('tail-1', 'tail-2'),closed=False)
        self.relate('connect',*('hull-top-1', 'hull-top-2'))
        self.relate('connect',*('hull-top-1', 'hull-bottom-2'))
        self.relate('connect',*('hull-top-1', 'tail-1'))
        self.relate('connect',*('hull-top-1', 'tail-2'))
        self.relate('connect',*('hull-top-2', 'hull-top-3'))
        self.relate('connect',*('hull-top-2', 'tower-1'))
        self.relate('connect',*('hull-top-3', 'hull-top-4'))
        self.relate('connect',*('hull-top-3', 'tower-1'))
        self.relate('connect',*('hull-top-3', 'tower-4'))
        self.relate('connect',*('hull-top-4', 'nose-top'))
        self.relate('connect',*('hull-top-4', 'tower-4'))
        self.relate('connect',*('nose-top', 'nose-bottom'))
        self.relate('connect',*('nose-bottom', 'hull-bottom-1'))
        self.relate('connect',*('hull-bottom-1', 'hull-bottom-2'))
        self.relate('connect',*('hull-bottom-2', 'tail-1'))
        self.relate('connect',*('hull-bottom-2', 'tail-2'))
        self.relate('connect',*('tower-1', 'tower-2'))
        self.relate('connect',*('tower-2', 'tower-3'))
        self.relate('connect',*('tower-2', 'periscope-1'))
        self.relate('connect',*('tower-3', 'tower-4'))
        self.relate('connect',*('tower-3', 'periscope-1'))
        self.relate('connect',*('periscope-1', 'periscope-2'))
        self.relate('connect',*('tail-1', 'tail-2'))
