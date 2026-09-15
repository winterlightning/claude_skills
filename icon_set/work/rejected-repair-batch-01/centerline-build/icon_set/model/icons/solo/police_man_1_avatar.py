"""police-man-1: uniform fastening and reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) allows vertical headwear budget.
Face centered x24 with equal circular radii; head bottom 30, shoulders 34,
zero painted gap. Shared human_ref/user.svg supplies curved shoulders;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine hat emblems and facial microdetails omitted for clarity at 48.
Body cue: uniform fastening. Hair and feather asymmetry follow the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-08/references/police-man-1.svg'
SOURCE_HEAD_ICON_ID = 'police-man-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class PoliceMan1Avatar(Solo48):
    icon_id = 'police-man-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('police', 'man', '1', 'portrait', 'bust')
    def build(self):
        cx = 24
        self.add_polyline('cap', (8, 12), (cx, 4), (40, 12), (34, 20), (14, 20), (8, 12))
        self.add_line('band', (8, 12), (40, 12))
        self.relate('connect', 'cap', 'band')
        self.add_arc('face', (34, 20), (14, 20), radius_x=10, radius_y=10)
        self.relate('connect', 'cap', 'face')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(18,top),radius_x=10,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top',(18,top),(24,top))
        self.add_line('body-top-right',(24,top),(30,top))
        self.add_arc('body-right-shoulder',(30,top),(40,42),radius_x=10,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect','body-left','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.add_line('body-fastening',(24,top),(24,44))
        self.relate('connect','body-fastening','body-top')
        self.relate('connect','body-fastening','body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
