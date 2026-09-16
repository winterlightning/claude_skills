"""Bandana Pirate beside Cutlass.

Symbol plan: Bandana-wearing round face above broad shoulders, with a curved cutlass at right; one bold bandana tie replaces the thin double knot.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: Shared human_ref/user.svg: circular jaw, broad smooth shoulders and zero-ink-gap head/body contact. Supplied reference defines headwear; tiny trim is omitted. Cutlass belongs to the pirate; its position is intentionally asymmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '7fdf8a81-dbd1-4e7d-bd20-9a054112ef25'
SOURCE_PATH = 'pictographic-primitives/avatars/pirate_7fdf8a81-dbd1-4e7d-bd20-9a054112ef25.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bandana-pirate-beside-cutlass'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('cutlass', 'pirate', 'eyepatch', 'hat', 'person', 'portrait', 'seafarer', 'costume', 'adventure')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j in range(4): arc(n+str(j),pts[j],pts[j+1],r)
            join(n,*(n+str(j) for j in range(4)),closed=True)

        circle('face',20,16,10)
        line('bandana',(10,16),(30,16));connect('bandana','face')
        line('tie',(10,16),(6,16));connect('tie','face');connect('tie','bandana')
        arc('body-left',(6,42),(20,30),14,12)
        arc('body-right',(20,30),(26,36),6)
        connect('body-left','body-right');connect('face','body-left');connect('face','body-right')
        arc('blade-tip',(38,6),(42,18),4,12)
        line('blade',(42,18),(42,30));connect('blade-tip','blade')
        line('handle',(42,30),(42,42));connect('handle','blade')
        line('guard',(34,30),(42,30));connect('blade','guard');connect('handle','guard')
