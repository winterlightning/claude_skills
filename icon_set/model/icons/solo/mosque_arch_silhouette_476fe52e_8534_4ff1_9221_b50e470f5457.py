"""Empty ogee arch silhouette. Centerline extremes (5,2)-(43,46). Mirrored smooth shoulders; no interior additions."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '476fe52e-8534-4ff1-9221-b50e470f5457'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/mosque_476fe52e-8534-4ff1-9221-b50e470f5457.svg'
AUTHOR = 'gpt-6'

class MosqueArchSilhouette(Solo48):
    icon_id = 'mosque-arch-silhouette'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('mosque', 'arch', 'ogee', 'islamic', 'mihrab', 'silhouette', 'religion', 'architecture')

    def build(self) -> None:
        self.add_arc('upper-left', (24, 2), (15, 11), radius_x=18, radius_y=18, sweep=True)
        self.add_arc('bulb-left', (15, 11), (9, 29), radius_x=12, radius_y=12, sweep=False)
        self.add_polyline('walls', (9, 29), (5, 33), (5, 46), (43, 46), (43, 33), (39, 29), closed=False)
        self.add_arc('bulb-right', (39, 29), (33, 11), radius_x=12, radius_y=12, sweep=False)
        self.add_arc('upper-right', (33, 11), (24, 2), radius_x=18, radius_y=18, sweep=True)
        self.relate("connect", 'upper-left', 'bulb-left')
        self.relate("connect", 'upper-left', 'upper-right')
        self.relate("connect", 'bulb-left', 'walls')
        self.relate("connect", 'walls', 'bulb-right')
        self.relate("connect", 'bulb-right', 'upper-right')
