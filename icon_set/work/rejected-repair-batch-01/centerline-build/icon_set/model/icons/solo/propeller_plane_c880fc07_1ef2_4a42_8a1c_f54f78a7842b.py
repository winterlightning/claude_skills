"""Propeller plane; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c880fc07-1ef2-4a42-8a1c-f54f78a7842b'
SOURCE_PATH = 'pictographic-primitives/transportation/propeller_c880fc07-1ef2-4a42-8a1c-f54f78a7842b.svg'
AUTHOR = 'gpt-6'

class PropellerPlane(Solo48):
    icon_id = 'propeller-plane'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('propeller plane', 'airplane', 'aircraft', 'plane', 'aviation', 'flight', 'light aircraft', 'propeller')

    def build(self) -> None:
        """Widen the lower tail-fin root and keep the intentional diagonal aircraft silhouette."""
        for name, a, b in [('upper', (30, 22), (36, 23)), ('upper-right', (36, 23), (40, 27)), ('lower-right', (40, 27), (30, 32)), ('lower', (30, 32), (24, 31)), ('lower-left', (24, 31), (20, 27)), ('upper-left', (20, 27), (30, 22))]:
            self.add_arc('disc-' + name, a, b, radius_x=10, radius_y=5)
        self.add_contour('propeller-disc', 'disc-upper', 'disc-upper-right', 'disc-lower-right', 'disc-lower', 'disc-lower-left', 'disc-upper-left', closed=True)
        self.add_polyline('airframe', (36, 23), (42, 12), (38, 6), (34, 6), (24, 14), (18, 14), (6, 6), (6, 18), (12, 26), (16, 28), (10, 40), (20, 42), (30, 32))
        self.relate('connect', 'airframe', 'propeller-disc')
