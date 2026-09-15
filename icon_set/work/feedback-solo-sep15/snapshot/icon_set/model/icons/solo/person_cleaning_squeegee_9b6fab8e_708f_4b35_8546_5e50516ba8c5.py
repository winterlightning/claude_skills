"""person-cleaning-squeegee: reconstructed on SOLO48 from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b6fab8e-708f-4b35-8546-5e50516ba8c5'
SOURCE_PATH = 'pictographic-primitives/transportation/window washer and wiper_9b6fab8e-708f-4b35-8546-5e50516ba8c5.svg'
AUTHOR = 'gpt-6'


class PersonCleaningSqueegee(Solo48):
    icon_id = 'person-cleaning-squeegee'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('window washer', 'squeegee', 'cleaning', 'wiper', 'person', 'worker', 'car wash', 'service')

    def build(self) -> None:

        # Figure owns a raised arm; the grasp node joins the tool handle exactly.
        self.add_arc('head-top',(10,16),(18,16),radius_x=4)
        self.add_arc('head-bottom',(18,16),(10,16),radius_x=4)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_line('left-arm',(6,42),(6,37))
        self.add_arc('shoulder',(6,37),(14,29),radius_x=8)
        self.add_polyline('raised-arm',(14,29),(20,29),(28,21))
        self.add_line('torso',(20,29),(20,42))
        self.add_line('handle',(28,21),(34,9))
        self.add_polyline('blade',(28,6),(34,9),(42,13))
        # Declare only genuine shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
