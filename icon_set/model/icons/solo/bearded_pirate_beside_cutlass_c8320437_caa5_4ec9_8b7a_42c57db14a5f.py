"""Bearded Pirate beside Cutlass.

Symbol plan: Smooth lobed pirate hat, circular face and long pointed beard beside a curved cutlass; reduce the narrow blade to a curved stroke and omit tiny shoulders.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: Shared human_ref/user.svg: circular jaw, broad smooth shoulders and zero-ink-gap head/body contact. Supplied reference defines headwear; tiny trim is omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'c8320437-caa5-4ec9-8b7a-42c57db14a5f'
SOURCE_PATH = 'pictographic-primitives/avatars/pirate_c8320437-caa5-4ec9-8b7a-42c57db14a5f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bearded-pirate-beside-cutlass'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('cutlass', 'pirate', 'eyepatch', 'hat', 'person', 'portrait', 'seafarer', 'costume', 'adventure')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        self.add_bezier('hat-crown',(6,18),((6,14),(8,12),(12,12)),((14,12),(12,6),(18,6)),((24,6),(22,12),(24,12)),((28,12),(30,14),(30,18)))
        path('hat-brim',(30,18),(26,20),(10,20),(6,18));connect('hat-crown','hat-brim')

        arc('face',(26,20),(10,20),8);connect('face','hat-brim')
        line('beard-left',(10,20),(10,34));line('beard-right',(26,34),(26,20))
        self.add_bezier('beard-tip-left',(10,34),((10,38),(14,40),(18,42)))
        self.add_bezier('beard-tip-right',(18,42),((22,40),(26,38),(26,34)))
        join('beard','beard-left','beard-tip-left','beard-tip-right','beard-right');connect('beard','face');connect('beard','hat-brim')
        arc('blade-tip',(38,6),(42,18),4,12)
        line('blade',(42,18),(42,30));connect('blade-tip','blade')
        line('handle',(42,30),(42,42));connect('handle','blade')
        line('guard',(34,30),(42,30));connect('blade','guard');connect('handle','guard')
