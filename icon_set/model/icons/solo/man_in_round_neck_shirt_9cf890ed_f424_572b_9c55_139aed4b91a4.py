"""Man in Round-Neck Shirt.

Symbol plan: Centered circular head; mirrored shoulders and rounded closed shirt hem. Drop tiny neckline seams.
VRECT_L centerline extremes (8,4)-(40,44); envelope follows the subject's proportions.
Construction reference: human_ref/user.svg: circular head and tangent round shoulders; head bottom20, body top24, zero ink gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '9cf890ed-f424-572b-9c55-139aed4b91a4'
SOURCE_PATH = 'pictographic-primitives/avatars/man_9cf890ed-f424-572b-9c55-139aed4b91a4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'man-in-round-neck-shirt'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('man', 'in', 'round', 'neck', 'shirt')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,cx,cy,r):
            arc(n+'-top',(cx-r,cy),(cx+r,cy),r)
            arc(n+'-bottom',(cx+r,cy),(cx-r,cy),r)
            join(n,n+'-top',n+'-bottom',closed=True)

        cx,cy,r=24,12,8
        circle('head',cx,cy,r)
        top=cy+r+HEAD_BODY_CENTERLINE_GAP
        arc('shoulder-l',(8,36),(20,top),12)
        line('body-top',(20,top),(28,top))
        arc('shoulder-r',(28,top),(40,36),12)
        line('side-r',(40,36),(40,40))
        arc('hem-r',(40,40),(36,44),4)
        line('hem',(36,44),(12,44))
        arc('hem-l',(12,44),(8,40),4)
        line('side-l',(8,40),(8,36))
        join('shirt','shoulder-l','body-top','shoulder-r','side-r','hem-r','hem','hem-l','side-l',closed=True)
        connect('head','shirt')
