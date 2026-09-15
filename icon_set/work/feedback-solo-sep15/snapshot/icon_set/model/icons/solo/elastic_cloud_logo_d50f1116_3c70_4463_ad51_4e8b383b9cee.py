"""elastic-cloud-logo: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd50f1116-3c70-4463-ad51-4e8b383b9cee'
SOURCE_PATH = 'pictographic-primitives/logos/elastic cloud logo_d50f1116-3c70-4463-ad51-4e8b383b9cee.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class ElasticCloudLogo(Solo48):
    icon_id = 'elastic-cloud-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('elastic', 'cloud', 'logo', 'logos')

    def build(self):
        # VRECT_L (8,4)-(40,44); concentric circular bands and mirrored seam endpoints.
        # Construction reference: Lucide circle-check: coherent circular arcs; source retains the segmented C
        # 3-4-5 points give exact circle endpoints on the integer grid.
        self.add_arc('outer-top',(40,8),(12,12),radius_x=20,sweep=False)
        self.add_arc('outer-left',(12,12),(12,36),radius_x=20,sweep=False)
        self.add_arc('outer-bottom',(12,36),(40,40),radius_x=20,sweep=False)
        self.add_line('lower-tip',(40,40),(34,32))
        self.add_arc('inner-bottom',(34,32),(20,30),radius_x=10)
        self.add_arc('inner-left',(20,30),(20,18),radius_x=10)
        self.add_arc('inner-top',(20,18),(34,16),radius_x=10)
        self.add_line('upper-tip',(34,16),(40,8))
        self.add_contour('outline','outer-top','outer-left','outer-bottom','lower-tip','inner-bottom','inner-left','inner-top','upper-tip',closed=True)
        self.add_line('upper-seam',(12,12),(20,18))
        self.add_line('lower-seam',(12,36),(20,30))
        self.relate('connect','outline','upper-seam')
        self.relate('connect','outline','lower-seam')
