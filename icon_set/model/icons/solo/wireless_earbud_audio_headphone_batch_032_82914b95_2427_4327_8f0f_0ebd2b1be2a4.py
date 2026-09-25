"""A single wireless earbud has a rounded listening head projecting left from a long upright stem. The stem ends in a rounded tip, and the visible silhouette has no interior markings."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82914b95-2427-4327-8f0f-0ebd2b1be2a4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/earpod_82914b95-2427-4327-8f0f-0ebd2b1be2a4.svg'
AUTHOR = 'gpt-6'


class Batch032Icon(Solo48):
    icon_id = 'wireless-earbud-audio-headphone-batch-032'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('wireless-earbud-audio-headphone',)
    keywords = ('batch-032',)

    def build(self):
        # Symbol plan: One left-projecting earbud head, right stem and semicircular foot; extrema (10,4)-(38,44).

        self.add_line('top',(20,4),(28,4))
        self.add_arc('head-right',(28,4),(38,14),radius_x=10)
        self.add_line('stem-right',(38,14),(38,38))
        self.add_arc('foot',(38,38),(26,38),radius_x=6)
        self.add_line('stem-left',(26,38),(26,24))
        self.add_bezier('head-bottom',(26,24),((20,28),(10,26),(10,20)))
        self.add_line('head-left',(10,20),(10,14))
        self.add_arc('head-top',(10,14),(20,4),radius_x=10)
        self.add_contour('earbud','top','head-right','stem-right','foot','stem-left','head-bottom','head-left','head-top',closed=True)
