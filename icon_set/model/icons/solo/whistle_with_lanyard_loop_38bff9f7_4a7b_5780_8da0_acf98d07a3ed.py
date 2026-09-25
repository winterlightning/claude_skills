"""A side-view whistle has a circular chamber hole, mouthpiece and rear lanyard loop. No useful local Lucide whistle match; use a coherent elliptical chamber and a complete circular loop. Preserve all identity features; simplify the mouthpiece underside to a short diagonal. Deliberate rightward asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38bff9f7-4a7b-5780-8da0-acf98d07a3ed'
SOURCE_PATH = 'pictographic-primitives/protection/whistle_38bff9f7-4a7b-5780-8da0-acf98d07a3ed.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'whistle-with-lanyard-loop'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    categories = ("protection", "primitives")
    aliases = ()
    keywords = ('whistle', 'referee', 'sport', 'alarm', 'signal', 'coach', 'police', 'alert')

    def build(self):
        # HRECT_L centerline extremes (4, 8, 44, 40).

        # Whistle owns chamber, mouthpiece and a circular lanyard loop at the back.
        self.add_arc('chamber-upper',(10,24),(25,8),radius_x=15,radius_y=16)
        mouth_nodes = [(25,8),(44,8),(44,20),(40,24)]
        for i,(a,b) in enumerate(zip(mouth_nodes,mouth_nodes[1:]),1):self.add_line('mouthpiece-'+str(i),a,b)
        self.add_arc('chamber-lower',(40,24),(10,24),radius_x=15,radius_y=16)
        self.add_contour('outline','chamber-upper','mouthpiece-1','mouthpiece-2','mouthpiece-3','chamber-lower',closed=True)
        self.add_arc('hole-top',(20,24),(30,24),radius_x=5)
        self.add_arc('hole-bottom',(30,24),(20,24),radius_x=5)
        self.add_contour('hole','hole-top','hole-bottom',closed=True)
        self.add_arc('loop-top',(4,24),(10,24),radius_x=3)
        self.add_arc('loop-bottom',(10,24),(4,24),radius_x=3)
        self.add_contour('lanyard-loop','loop-top','loop-bottom',closed=True)
        self.relate('connect','lanyard-loop','outline')
