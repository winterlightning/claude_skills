"""Fighter Jet, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '52c0aadd-f8f3-580e-ace0-9eb0f6f36a19'
SOURCE_PATH = 'pictographic-primitives/transportation/military plane_52c0aadd-f8f3-580e-ace0-9eb0f6f36a19.svg'
AUTHOR = 'gpt-6'

class FighterJet(Solo48):
    icon_id = 'fighter-jet'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('fighter jet', 'military plane', 'jet', 'aircraft', 'air force', 'aviation', 'airplane', 'top view')

    def build(self) -> None:
        # Current contract centerline extremes: (8,6)-(40,42).
        # A mirrored outline owns the swept wings, pointed nose and smaller tailplanes.
        right=[(24,6),(29,12),(29,18),(40,30),(40,34),(29,30),(29,36),(32,40),(32,42),(24,40)]
        left=[(48-x,y) for x,y in reversed(right[1:-1])]
        self.add_polyline('airframe',*(right+left),closed=True)
