"""Man with Short Hair and Open Shoulders.

Symbol plan: Rounded short-hair roof over circular jaw; mirrored open shoulders. Omit tiny ear notches and neck.
VRECT_L centerline extremes (8,4)-(40,44); envelope follows the subject's proportions.
Construction reference: human_ref/user.svg: circular jaw and tangent shoulder curves; jaw bottom24, shoulder top28, zero ink gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'ccad9539-3f9e-4f75-8205-11baacf5298e'
SOURCE_PATH = 'pictographic-primitives/avatars/man_ccad9539-3f9e-4f75-8205-11baacf5298e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'man-with-short-hair-and-open-shoulders'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'with', 'short', 'hair', 'and', 'open', 'shoulders')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        line('hair-top',(18,4),(30,4))
        arc('hair-r',(30,4),(34,8),4)
        line('temple-r',(34,8),(34,14))
        arc('jaw',(34,14),(14,14),10)
        line('temple-l',(14,14),(14,8))
        arc('hair-l',(14,8),(18,4),4)
        join('head','hair-top','hair-r','temple-r','jaw','temple-l','hair-l',closed=True)
        top=14+10+HEAD_BODY_CENTERLINE_GAP
        line('left',(8,44),(8,40))
        arc('shoulder-l',(8,40),(20,top),12)
        line('body-top',(20,top),(28,top))
        arc('shoulder-r',(28,top),(40,40),12)
        line('right',(40,40),(40,44))
        join('body','left','shoulder-l','body-top','shoulder-r','right')
        connect('head','body')
