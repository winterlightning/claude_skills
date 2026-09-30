"""Policewoman with Circular Cap Badge.

Symbol plan: Round helmet with a bold circular badge, circular jaw and flared side hair over a smooth uniform bust; reduce the narrow visor and badge outline.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: Shared human_ref/user.svg: circular jaw at x24, smooth broad shoulders, head bottom plus HEAD_BODY_CENTERLINE_GAP gives 4 centerline units and zero ink gap. Lucide glasses original and atomic-debug inform equal lenses where present; the supplied reference defines the hat and hair.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '4bd11fea-9076-4103-9fb2-9403c23d0d9b'
SOURCE_PATH = 'pictographic-primitives/avatars/police woman_4bd11fea-9076-4103-9fb2-9403c23d0d9b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'policewoman-with-circular-cap-badge'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('police', 'officer', 'uniform', 'hat', 'person', 'portrait', 'security', 'law enforcement')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)


        arc('crown-left',(12,21),(24,4),12,17);arc('crown-right',(24,4),(36,21),12,17);join('crown','crown-left','crown-right')
        path('brim',(12,21),(24,21),(36,21));connect('brim','crown')
        arc('face',(36,21),(12,21),12);connect('face','brim');connect('face','crown')
        self.add_dot('badge',(24,13))
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('hair-'+side,(24+sign*12,21),((24+sign*12,24),(24+sign*14,27),(24+sign*16,29)))
            connect('hair-'+side,'face');connect('hair-'+side,'brim');connect('hair-'+side,'crown')
        bottom=33

        top = bottom + HEAD_BODY_CENTERLINE_GAP
        line('body-left-side',(8,44),(8,42))
        arc('body-left-shoulder',(8,42),(18,top),10,42-top)
        join('body-left','body-left-side','body-left-shoulder')
        line('body-top',(18,top),(24,top));line('body-top-right',(24,top),(30,top))
        arc('body-right-shoulder',(30,top),(40,42),10,42-top)
        line('body-right-side',(40,42),(40,44));join('body-right','body-right-shoulder','body-right-side')
        connect('body-left','body-top');connect('body-top','body-top-right');connect('body-top-right','body-right')
        connect('face','body-top');connect('face','body-top-right')
        line('body-seam',(24,top),(24,44));connect('body-seam','body-top');connect('body-seam','body-top-right')
