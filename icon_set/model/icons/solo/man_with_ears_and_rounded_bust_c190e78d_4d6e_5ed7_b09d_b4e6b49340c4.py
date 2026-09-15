"""Man with Ears and Rounded Bust.

Symbol plan: Bald crown, integrated paired ears, circular jaw; broad rounded bust. Omit separate neck and collar.
VRECT_L centerline extremes (8,4)-(40,44); envelope follows the subject's proportions.
Construction reference: human_ref/user.svg: round shoulder construction. Circular jaw bottom28, shoulder top32: zero ink gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'c190e78d-4d6e-5ed7-b09d-b4e6b49340c4'
SOURCE_PATH = 'pictographic-primitives/avatars/man_c190e78d-4d6e-5ed7-b09d-b4e6b49340c4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'man-with-ears-and-rounded-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'with', 'ears', 'and', 'rounded', 'bust')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        arc('crown',(16,12),(32,12),8)
        arc('ear-r',(32,12),(32,20),4)
        arc('jaw',(32,20),(16,20),8)
        arc('ear-l',(16,20),(16,12),4)
        join('head','crown','ear-r','jaw','ear-l',closed=True)
        top=20+8+HEAD_BODY_CENTERLINE_GAP
        line('left',(8,44),(8,40))
        arc('shoulder-l',(8,40),(16,top),8)
        line('body-top',(16,top),(32,top))
        arc('shoulder-r',(32,top),(40,40),8)
        line('right',(40,40),(40,44))
        join('body','left','shoulder-l','body-top','shoulder-r','right')
        connect('head','body')
