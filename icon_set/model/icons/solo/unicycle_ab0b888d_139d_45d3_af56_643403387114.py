"""unicycle: reconstructed on SOLO48 from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab0b888d-139d-45d3-af56-643403387114'
SOURCE_PATH = 'pictographic-primitives/transportation/unicycle_ab0b888d-139d-45d3-af56-643403387114.svg'
AUTHOR = 'gpt-6'


class Unicycle(Solo48):
    icon_id = 'unicycle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('unicycle', 'cycle', 'wheel', 'circus', 'balance', 'ride', 'saddle', 'one wheel')

    def build(self) -> None:

        # Four equally spaced spokes leave open quadrants; saddle and post share the axis.
        pts=[(24,12),(40,28),(24,42),(8,28)]
        for i,p in enumerate(pts):
            self.add_arc(f'rim-{i}',p,pts[(i+1)%4],radius_x=16)
            self.add_line(f'spoke-{i}',(24,28),p)
        self.add_contour('rim',*[f'rim-{i}' for i in range(4)],closed=True)
        self.add_line('post',(24,6),(24,12))
        self.add_arc('saddle-left',(14,6),(24,6),radius_x=10,radius_y=2,sweep=False)
        self.add_arc('saddle-right',(24,6),(34,6),radius_x=10,radius_y=2,sweep=False)
        self.add_contour('saddle','saddle-left','saddle-right')
        # Declare only genuine shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
