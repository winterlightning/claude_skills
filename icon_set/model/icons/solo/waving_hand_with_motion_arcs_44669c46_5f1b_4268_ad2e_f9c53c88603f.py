"""Waving Hand with Motion Arcs.

Symbol plan: Waving palm with three visible extended digits and an open thumb, round fingertips and a smooth heel. Reduce the fourth finger and paired motion marks to preserve clear spacing.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: Lucide hand original and atomic-debug: repeated rounded fingertips and one broad palm curve. Shared human reference informs simple round-ended anatomy; wave direction is intentionally asymmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '44669c46-5f1b-4268-ad2e-f9c53c88603f'
SOURCE_PATH = 'pictographic-primitives/chat/photo motion sensor_44669c46-5f1b-4268-ad2e-f9c53c88603f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'waving-hand-with-motion-arcs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'chat'
    aliases = ()
    keywords = ('hand', 'gesture', 'palm', 'fingers', 'communication', 'touch', 'human', 'greeting')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)

        line('finger-left',(14,24),(14,14))
        arc('tip-left',(14,14),(22,14),4)
        line('finger-middle-left',(22,14),(22,10))
        arc('tip-middle',(22,10),(30,10),4)
        line('finger-middle-right',(30,10),(30,14))
        arc('tip-right',(30,14),(38,14),4)
        line('palm-right',(38,14),(38,21))
        arc('palm-heel',(38,21),(26,33),12)
        self.add_bezier('palm-left',(26,33),((18,33),(14,29),(10,25)))
        line('thumb',(10,25),(6,21))
        join('hand','finger-left','tip-left','finger-middle-left','tip-middle','finger-middle-right','tip-right','palm-right','palm-heel','palm-left','thumb')
        arc('motion-left',(6,12),(8,6),2,6)
        arc('motion-right',(42,34),(34,42),8)
