"""Woman Spy with Flared Bob.

Symbol plan: Smooth notched hat over a blank circular face, two flared hair locks and a wrapping coat lapel; omit doubled coat lines and close bob ends.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: Shared human_ref/user.svg: circular jaw at x24, smooth broad shoulders, head bottom plus HEAD_BODY_CENTERLINE_GAP gives 4 centerline units and zero ink gap. Lucide glasses original and atomic-debug inform equal lenses where present; the supplied reference defines the hat and hair.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '26f0891f-367a-4475-acf4-7e2be5fb26dd'
SOURCE_PATH = 'pictographic-primitives/avatars/police woman spy_26f0891f-367a-4475-acf4-7e2be5fb26dd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'woman-spy-with-flared-bob'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('spy', 'hat', 'sunglasses', 'person', 'portrait', 'disguise', 'agent', 'detective')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)


        self.add_bezier('crown',(12,16),((13,10),(14,4),(18,4)),((21,4),(20,8),(24,8)),((28,8),(27,4),(30,4)),((34,4),(35,10),(36,16)))
        path('brim',(8,16),(12,16),(24,16),(36,16),(40,16));connect('crown','brim')
        arc('face',(36,16),(12,16),12);connect('face','brim');connect('face','crown')
        bottom=28

        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('hair-'+side,(24+sign*12,16),((24+sign*12,20),(24+sign*14,24),(24+sign*16,26)))
            connect('hair-'+side,'face');connect('hair-'+side,'brim');connect('hair-'+side,'crown')

        top = bottom + HEAD_BODY_CENTERLINE_GAP
        line('body-left-side',(8,44),(8,42))
        arc('body-left-shoulder',(8,42),(18,top),10,42-top)
        join('body-left','body-left-side','body-left-shoulder')
        line('body-top',(18,top),(24,top));line('body-top-right',(24,top),(30,top))
        arc('body-right-shoulder',(30,top),(40,42),10,42-top)
        line('body-right-side',(40,42),(40,44));join('body-right','body-right-shoulder','body-right-side')
        connect('body-left','body-top');connect('body-top','body-top-right');connect('body-top-right','body-right')
        connect('face','body-top');connect('face','body-top-right')
        line('body-wrap',(30,top),(18,44));connect('body-wrap','body-top-right')
