"""user-visor: suit fastening with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 30, shoulder top 34, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: suit fastening. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-12/references/user-visor.svg'
SOURCE_HEAD_ICON_ID = 'user-visor'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class UserVisorAvatar(Solo48):
    icon_id = 'user-visor-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('user', 'visor', 'portrait', 'bust')
    def build(self):
        # Circular runs split at the actual visor junctions.
        self.add_arc('crown',(12,12),(36,12),radius_x=13)
        self.add_arc('right',(36,12),(36,22),radius_x=13)
        self.add_arc('jaw',(36,22),(12,22),radius_x=13)
        self.add_arc('left',(12,22),(12,12),radius_x=13)
        self.add_contour('head','crown','right','jaw','left',closed=True)
        for name,y in [('top',12),('bottom',22)]:
            self.add_line('visor-'+name,(12,y),(36,y))
            self.relate('connect','visor-'+name,'head')
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

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
