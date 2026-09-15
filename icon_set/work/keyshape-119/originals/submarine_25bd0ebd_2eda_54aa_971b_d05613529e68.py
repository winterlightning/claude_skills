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

        # Long rounded nose, tapered stern and two tail fins share the vessel outline.
        self.add_polyline('hull-top',(6,32),(14,24),(20,24),(30,24),(34,24))
        self.add_arc('nose-top',(34,24),(42,32),radius_x=10,radius_y=8)
        self.add_arc('nose-bottom',(42,32),(34,40),radius_x=10,radius_y=8)
        self.add_polyline('hull-bottom',(34,40),(14,40),(6,32))
        self.add_contour('hull','hull-top-1','hull-top-2','hull-top-3','hull-top-4','nose-top','nose-bottom','hull-bottom-1','hull-bottom-2',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ('hull-top','hull-bottom')]
        self.add_polyline('tower',(20,24),(20,16),(24,16),(30,16),(30,24))
        self.add_polyline('periscope',(24,16),(24,8),(30,8))
        self.add_polyline('tail',(6,24),(6,32),(6,40))
        # Declare only real junctions with exactly matching endpoints.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
