"""mine-worker-woman-1: work apron with reference headwear/hair silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46); circular face x24,
head bottom 30, shoulders 34, zero painted gap. human_ref/user.svg supplies
curved shoulders; Lucide user-round original and atomic-debug guide arcs.
Fine trim is omitted for clarity at 48; body cue: work apron.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '5c36abfd-613c-4687-9411-db57779ca5c7'
SOURCE_PATH = 'pictographic-primitives/avatars/mine worker woman_5c36abfd-613c-4687-9411-db57779ca5c7.svg'
SOURCE_HEAD_ICON_ID = 'mine-worker-woman-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class MineWorkerWoman1Avatar(Solo48):
    icon_id = 'mine-worker-woman-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('mine', 'worker', 'woman', '1', 'portrait', 'bust')
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
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('hair-'+side,(24+sign*10,20),((24+sign*12,22),(24+sign*14,24),(24+sign*16,24)))
            self.relate('connect','hair-'+side,'face')
            self.relate('connect','hair-'+side,'brim')
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
        self.add_polyline('body-bib',(18,top),(18,44),(30,44),(30,top))
        self.relate('connect','body-bib','body-top')
        self.relate('connect','body-bib','body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
