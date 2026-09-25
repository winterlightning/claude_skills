"""Eyepatch Pirate beside Cutlass.

Symbol plan: Round pirate head with a curved eyepatch above an open shirt and a curved cutlass. Remove narrow neckline doubling.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: Shared human_ref/user.svg: circular jaw, broad smooth shoulders and zero-ink-gap head/body contact. Supplied reference defines headwear; tiny trim is omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'd051a0d5-d79e-45ac-8520-51d1f8577890'
SOURCE_PATH = 'pictographic-primitives/avatars/pirate_d051a0d5-d79e-45ac-8520-51d1f8577890.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'eyepatch-pirate-beside-cutlass'
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
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j in range(4): arc(n+str(j),pts[j],pts[j+1],r)
            join(n,*(n+str(j) for j in range(4)),closed=True)

        circle('face',18,18,12)
        path('strap',(6,18),(18,18),(30,18));connect('strap','face')
        arc('patch',(18,18),(30,18),6,s=False);connect('patch','strap');connect('patch','face')
        arc('body-left',(6,42),(18,34),12,8)
        arc('body-right',(18,34),(24,40),6)
        connect('body-left','body-right');connect('face','body-left');connect('face','body-right')
        arc('blade-tip',(38,6),(42,18),4,12)
        line('blade',(42,18),(42,32));connect('blade-tip','blade')
        line('handle',(42,32),(42,42));connect('handle','blade')
        line('guard',(34,32),(42,32));connect('blade','guard');connect('handle','guard')
