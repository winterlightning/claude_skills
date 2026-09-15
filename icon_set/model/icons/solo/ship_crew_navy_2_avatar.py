"""ship-crew-navy-2: curved sailor collar with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 26, shoulder top 30, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails are omitted for native 48px clarity.
Body cue: curved sailor collar. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-09/references/ship-crew-navy-2.svg'
SOURCE_HEAD_ICON_ID = 'ship-crew-navy-2'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26
class ShipCrewNavy2Avatar(Solo48):
    icon_id = 'ship-crew-navy-2-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('ship', 'crew', 'navy', '2', 'portrait', 'bust')
    def build(self):
        self.add_polyline('cap',(14,16),(12,4),(36,4),(34,16),(14,16))
        self.add_arc('face',(34,16),(14,16),radius_x=10)
        self.relate('connect','face','cap')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(16,top),radius_x=8,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (16,top), (24, top))
        self.add_line('body-top-right', (24, top), (32,top))
        self.add_arc('body-right-shoulder',(32,top),(40,42),radius_x=8,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_arc('body-sailor-collar',(16,top),(32,top),radius_x=8,radius_y=6,sweep=False)
        self.relate('connect', 'body-sailor-collar', 'body-top')
        self.relate('connect', 'body-sailor-collar', 'body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
