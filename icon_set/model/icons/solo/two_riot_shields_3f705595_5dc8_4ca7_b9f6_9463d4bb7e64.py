"""Two upright riot shields stand side by side. Lucide shield informs the clear silhouette; repeated perspective panels share dimensions. Reduce each window and inset slot to one viewing-panel seam."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f705595-5dc8-4ca7-b9f6-9463d4bb7e64'
SOURCE_PATH = 'pictographic-primitives/protection/protest police shield_3f705595-5dc8-4ca7-b9f6-9463d4bb7e64.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'two-riot-shields'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    aliases = ()
    keywords = ('riot shield', 'police', 'protest', 'shields', 'defence', 'barrier', 'law', 'security')

    def build(self):
        # HRECT_L centerline extremes (4, 8, 44, 40).

        # Equal shield instances retain their slight perspective and viewport seam.
        for i,x in enumerate((4,29)):
            self.add_polyline(f'shield-{i}',(x,8),(x+15,12),(x+15,24),(x+15,40),(x,36),(x,20),closed=True)
            self.add_line(f'viewport-{i}',(x,20),(x+15,24))
            self.relate('connect',f'viewport-{i}',f'shield-{i}')
