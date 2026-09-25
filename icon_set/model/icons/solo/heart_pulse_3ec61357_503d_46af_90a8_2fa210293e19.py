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
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('heart', 'pulse', 'heartbeat', 'health', 'cardio', 'medical', 'rate', 'life', 'sub icon')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_arc('left-lobe',(4, 13),(24, 13),radius_x=10,radius_y=5)
        self.add_arc('right-lobe',(24, 13),(44, 13),radius_x=10,radius_y=5)
        self.add_bezier('right-shoulder',(44, 13),*(((44, 16.88829393), (43.87069971, 21.30472048), (42, 25)),))
        self.add_line('right-tip',(42, 25),(24, 40))
        self.add_line('left-tip',(24, 40),(6, 25))
        self.add_bezier('left-shoulder',(6, 25),*(((4.12930029, 21.30472048), (4, 16.88829393), (4, 13)),))
        self.add_line('pulse-1',(6, 25),(12, 25))
        self.add_line('pulse-2',(12, 25),(16, 18))
        self.add_line('pulse-3',(16,18),(24,27))
        self.add_line('pulse-4',(24,27),(29,19))
        self.add_line('pulse-5',(29,19),(33,25))
        self.add_line('pulse-6',(33, 25),(42, 25))
        self.add_contour('heart',*('left-lobe', 'right-lobe', 'right-shoulder', 'right-tip', 'left-tip', 'left-shoulder'),closed=True)
        self.add_contour('pulse',*('pulse-1', 'pulse-2', 'pulse-3', 'pulse-4', 'pulse-5', 'pulse-6'),closed=False)
        self.relate('connect',*('heart', 'pulse'))


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('a9dc34df-bbc3-4ab4-a859-ebdb7d92a804', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/sports/heart rate_a9dc34df-bbc3-4ab4-a859-ebdb7d92a804.svg'), ('468beab8-6edf-4e7f-9ee2-0f23f5c3b360', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/sports/heart rate_468beab8-6edf-4e7f-9ee2-0f23f5c3b360.svg')]

# Visually reviewed equivalent content reference, explicitly requested for reuse.
SOURCE_REFERENCES = tuple(globals().get("SOURCE_REFERENCES", ())) + (('a954f676-1cce-4e19-81eb-ec067ec52edc', 'icon_set/dist/gallery/combination-originals/a954f676-1cce-4e19-81eb-ec067ec52edc.svg'),)
