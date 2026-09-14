"""seaplane-front-view: reconstructed on SOLO48 from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dab4ca56-6767-512c-97c3-5d42d7522f62'
SOURCE_PATH = 'pictographic-primitives/transportation/water plane_dab4ca56-6767-512c-97c3-5d42d7522f62.svg'
AUTHOR = 'gpt-6'


class SeaplaneFrontView(Solo48):
    icon_id = 'seaplane-front-view'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('seaplane', 'water plane', 'floatplane', 'aircraft', 'plane', 'water', 'aviation', 'front view')

    def build(self) -> None:

        # Central fuselage, symmetrical wing arms, overhead propeller and one water wave.
        pts=[(24,16),(30,22),(24,28),(18,22)]
        for i,p in enumerate(pts): self.add_arc(f'body-{i}',p,pts[(i+1)%4],radius_x=6)
        self.add_contour('body',*[f'body-{i}' for i in range(4)],closed=True)
        self.add_line('wing-left',(6,22),(18,22))
        self.add_line('wing-right',(30,22),(42,22))
        self.add_line('propeller-post',(24,8),(24,16))
        self.add_polyline('propeller',(18,8),(24,8),(30,8))
        for i,x in enumerate([4,14,24,34]):
            self.add_arc(f'wave-{i}',(x,39),(x+10,39),radius_x=5,radius_y=1,sweep=bool(i%2))
        self.add_contour('water',*[f'wave-{i}' for i in range(4)])
        # Declare only genuine shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
