"""mine-worker-man-1: work jacket fastening with reference headwear/hair silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46); circular face x24,
head bottom 30, shoulders 34, zero painted gap. human_ref/user.svg supplies
curved shoulders; Lucide user-round original and atomic-debug guide arcs.
Fine trim is omitted for clarity at 48; body cue: work jacket fastening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-07/references/mine-worker-man-1.svg'
SOURCE_HEAD_ICON_ID = 'mine-worker-man-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class MineWorkerMan1Avatar(Solo48):
    icon_id = 'mine-worker-man-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('mine', 'worker', 'man', '1', 'portrait', 'bust')
    def build(self):
        self.add_arc('cap-left',(12,20),(20,8),radius_x=8,radius_y=12)
        self.add_arc('cap-right',(28,8),(36,20),radius_x=8,radius_y=12)
        self.add_arc('lamp-top',(20,8),(28,8),radius_x=4)
        self.add_arc('lamp-bottom',(28,8),(20,8),radius_x=4)
        self.add_contour('lamp','lamp-top','lamp-bottom',closed=True)
        self.relate('connect','lamp','cap-left')
        self.relate('connect','lamp','cap-right')
        self.add_polyline('brim',(8,20),(12,20),(14,20),(34,20),(36,20),(40,20))
        self.relate('connect','cap-left','brim')
        self.relate('connect','cap-right','brim')
        self.add_arc('face',(34,20),(14,20),radius_x=10)
        self.relate('connect','face','brim')
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
