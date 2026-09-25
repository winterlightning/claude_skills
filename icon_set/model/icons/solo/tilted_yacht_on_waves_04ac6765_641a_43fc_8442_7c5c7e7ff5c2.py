"""tilted-yacht-on-waves: reconstructed on SOLO48 from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04ac6765-641a-43fc-8442-7c5c7e7ff5c2'
SOURCE_PATH = 'pictographic-primitives/transportation/yacht_04ac6765-641a-43fc-8442-7c5c7e7ff5c2.svg'
AUTHOR = 'gpt-6'


class TiltedYachtOnWaves(Solo48):
    icon_id = 'tilted-yacht-on-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('yacht', 'motor yacht', 'boat', 'speedboat', 'waves', 'sea', 'marine', 'nautical')

    def build(self) -> None:

        # Raised left bow and lowered right stern meet the water at exact shared nodes.
        self.add_polyline('hull',(14,38),(6,16),(20,20),(36,24),(42,26),(42,38))
        self.add_polyline('flybridge',(20,20),(30,8),(40,8),(36,16),(36,24))
        for i,x in enumerate([4,14,24,34]):
            self.add_arc(f'wave-{i}',(x,38),(x+10,38),radius_x=5,radius_y=2,sweep=bool(i%2))
        self.add_contour('water',*[f'wave-{i}' for i in range(4)])
        # Declare only true junctions, where endpoint coordinates match exactly.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
