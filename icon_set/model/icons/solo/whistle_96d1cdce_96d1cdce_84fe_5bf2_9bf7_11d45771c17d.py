"""A plain side-view whistle has a round chamber and rectangular mouthpiece. No useful local Lucide whistle match; use tangent quarter- and semicircles with a concentric hole. Preserve all main features and deliberate rightward asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96d1cdce-84fe-5bf2-9bf7-11d45771c17d'
SOURCE_PATH = 'pictographic-primitives/protection/whistle_96d1cdce-84fe-5bf2-9bf7-11d45771c17d.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'whistle-96d1cdce'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    categories = ("protection", "primitives")
    aliases = ()
    keywords = ('whistle', 'referee', 'sport', 'alarm', 'signal', 'coach', 'police', 'alert')

    def build(self):
        # HRECT_L centerline extremes (4, 8, 44, 40).

        # Round chamber flows into a flat mouthpiece; its hole shares the chamber axis.
        self.add_arc('chamber-upper',(4,24),(20,8),radius_x=16)
        mouth_nodes = [(20,8),(44,8),(44,20),(36,24)]
        for i,(a,b) in enumerate(zip(mouth_nodes,mouth_nodes[1:]),1):self.add_line('mouthpiece-'+str(i),a,b)
        self.add_arc('chamber-lower',(36,24),(4,24),radius_x=16)
        self.add_contour('outline','chamber-upper','mouthpiece-1','mouthpiece-2','mouthpiece-3','chamber-lower',closed=True)
        self.add_arc('hole-top',(14,24),(26,24),radius_x=6)
        self.add_arc('hole-bottom',(26,24),(14,24),radius_x=6)
        self.add_contour('hole','hole-top','hole-bottom',closed=True)
