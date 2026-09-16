"""Police Officer with Sunglasses and Pocket.

Symbol plan: Police cap and round sunglasses over a circular jaw, central uniform seam and a pocket indicated by a right hem corner; omit the tiny closed chest shield.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: Shared human_ref/user.svg: circular jaw, broad smooth shoulders and zero-ink-gap head/body contact. Supplied reference defines headwear; tiny trim is omitted. Lucide glasses: equal round lenses and a common bridge.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'd0e6dfff-a50a-4157-9cf6-1c2c63ff4cb0'
SOURCE_PATH = 'pictographic-primitives/avatars/police man_d0e6dfff-a50a-4157-9cf6-1c2c63ff4cb0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'police-officer-with-sunglasses-and-pocket'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('police', 'officer', 'uniform', 'hat', 'person', 'portrait', 'security', 'law enforcement')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        path('crown',(12,16),(14,4),(34,4),(36,16))
        path('brim',(8,16),(12,16),(24,16),(36,16),(40,16));connect('crown','brim')
        arc('face',(36,16),(12,16),12);connect('face','brim');connect('face','crown')
        bottom=28

        arc('lens-left',(12,16),(24,16),6,s=False)
        arc('lens-right',(24,16),(36,16),6,s=False)
        connect('lens-left','brim');connect('lens-right','brim');connect('lens-left','face');connect('lens-right','face');connect('lens-left','lens-right')

        top = bottom + HEAD_BODY_CENTERLINE_GAP
        line('body-left-side',(8,44),(8,42))
        arc('body-left-shoulder',(8,42),(18,top),10,42-top)
        join('body-left','body-left-side','body-left-shoulder')
        line('body-top',(18,top),(24,top))
        line('body-top-right',(24,top),(30,top))
        arc('body-right-shoulder',(30,top),(40,42),10,42-top)
        line('body-right-side',(40,42),(40,44))
        join('body-right','body-right-shoulder','body-right-side')
        connect('body-left','body-top');connect('body-top','body-top-right');connect('body-top-right','body-right')
        connect('face','body-top');connect('face','body-top-right')

        line('body-seam',(24,top),(24,44));connect('body-seam','body-top');connect('body-seam','body-top-right')

        line('pocket',(32,44),(40,44));connect('pocket','body-right')
