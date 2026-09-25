'Police officer bust with peaked cap and uniform badge. VRECT_L budgets cap, circular face and curved broad shoulders. Human reference user.svg owns shoulder construction; circular jaw radius 8 centered (24,18), shoulders apex y30 gives exact 4 centerline / zero ink gap. Shared vertical axis; mirrored cap and shoulders. Omit cap insignia, lapels and seam to preserve clearance; keep one chest badge. No useful Lucide police-specific match; human reference supplies anatomy.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ed60c884-6e26-4a90-9170-23473b0ad667'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/policeman_ed60c884-6e26-4a90-9170-23473b0ad667.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'police-officer-in-peaked-cap'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ['Uniformed Police Officer Avatar']
    keywords = []
    def build(self):
        self.add_polyline('cap',(16,18),(12,10),(24,4),(36,10),(32,18),(16,18),closed=True)
        self.add_arc('jaw',(32,18),(16,18),radius_x=8,sweep=True)
        self.relate('connect','cap','jaw')
        self.add_arc('body-top',(8,44),(24,30),radius_x=16,radius_y=14,sweep=True)
        self.add_arc('body-right',(24,30),(40,44),radius_x=16,radius_y=14,sweep=True)
        self.add_contour('body','body-top','body-right')
        self.relate('connect','jaw','body')
        self.add_arc('body-badge-top',(22,41),(26,41),radius_x=2,sweep=True)
        self.add_arc('body-badge-bottom',(26,41),(22,41),radius_x=2,sweep=True)
        self.add_contour('body-badge','body-badge-top','body-badge-bottom',closed=True)
