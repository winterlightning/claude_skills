"""A heart outline contains a heartbeat peak and dip joined to both sides. HRECT_L extremes (6,8)-(42,40). Lucide heart-pulse informs the shared side junctions and coherent wave; widen the lobes and reduce peak height for clear enclosed spaces. Preserve the asymmetric pulse direction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ec61357-503d-46af-90a8-2fa210293e19'
SOURCE_PATH = 'pictographic-primitives/symbol/heart throb_3ec61357-503d-46af-90a8-2fa210293e19.svg'
AUTHOR = 'gpt-6'


class HeartPulse(Solo48):
    icon_id = 'heart-pulse'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('heart', 'pulse', 'heartbeat', 'health', 'cardio', 'medical', 'rate', 'life')

    def build(self) -> None:
        self.add_arc('left-lobe',(6,13),(24,13),radius_x=10,radius_y=5)
        self.add_arc('right-lobe',(24,13),(42,13),radius_x=10,radius_y=5)
        self.add_arc('right-shoulder',(42,13),(40,25),radius_x=20)
        self.add_line('right-tip',(40,25),(24,40))
        self.add_line('left-tip',(24,40),(8,25))
        self.add_arc('left-shoulder',(8,25),(6,13),radius_x=20)
        self.add_contour('heart','left-lobe','right-lobe','right-shoulder','right-tip','left-tip','left-shoulder',closed=True)
        self.add_polyline('pulse',(8,25),(12,25),(16,18),(24,31),(29,23),(33,25),(40,25))
        self.relate('connect','heart','pulse')
