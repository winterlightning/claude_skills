"""Policewoman with Round Glasses.

Symbol plan: Rounded police hat and equal round lenses, flared bob and a central uniform seam with pocket cue. Simplify the tiny lens bridge and closed chest shield.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: Shared human_ref/user.svg: circular jaw at x24, smooth broad shoulders, head bottom plus HEAD_BODY_CENTERLINE_GAP gives 4 centerline units and zero ink gap. Lucide glasses original and atomic-debug inform equal lenses where present; the supplied reference defines the hat and hair.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '6b34cbad-4ecd-49c6-8fa7-dde6ddbf9011'
SOURCE_PATH = 'pictographic-primitives/avatars/police woman_6b34cbad-4ecd-49c6-8fa7-dde6ddbf9011.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'policewoman-with-round-glasses'
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


        line('crown-left',(12,16),(12,10));arc('crown-nw',(12,10),(18,4),6)
        line('crown-top',(18,4),(30,4));arc('crown-ne',(30,4),(36,10),6)
        line('crown-right',(36,10),(36,16));join('crown','crown-left','crown-nw','crown-top','crown-ne','crown-right')
        path('brim',(8,16),(12,16),(24,16),(36,16),(40,16));connect('crown','brim')
        arc('face',(36,16),(12,16),12);connect('face','brim');connect('face','crown')
        bottom=28

        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('hair-'+side,(24+sign*12,16),((24+sign*12,20),(24+sign*14,24),(24+sign*16,26)))
            connect('hair-'+side,'face');connect('hair-'+side,'brim');connect('hair-'+side,'crown')

        arc('lens-left',(12,16),(24,16),6,s=False);arc('lens-right',(24,16),(36,16),6,s=False)
        connect('lens-left','brim');connect('lens-right','brim');connect('lens-left','face');connect('lens-right','face');connect('lens-left','lens-right')
        connect('lens-left','hair-left');connect('lens-right','hair-right')

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
        line('body-pocket',(32,44),(40,44));connect('body-pocket','body-right')
