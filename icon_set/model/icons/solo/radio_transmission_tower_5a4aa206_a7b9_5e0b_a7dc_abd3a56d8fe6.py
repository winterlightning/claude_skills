"""Radio Transmission Tower.

Symbol plan: Transmission mast with a round emitter, two mirrored broadcast arcs and one shared tower crossbar. Reduce the outer duplicate waves and crossed truss.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: Lucide radio-receiver original and atomic-debug also informed tangent quarter-circle casing corners during final review. Lucide radio-tower original and atomic-debug: circular emitter, splayed mast and equal broadcast arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '5a4aa206-a7b9-5e0b-a7dc-abd3a56d8fe6'
SOURCE_PATH = 'pictographic-primitives/audio/radio antenna_5a4aa206-a7b9-5e0b-a7dc-abd3a56d8fe6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'radio-transmission-tower'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('radio tower', 'transmission', 'radio', 'broadcast', 'audio', 'receiver', 'antenna', 'speaker', 'signal', 'tuning')

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


        circle('emitter',24,14,4)
        path('tower',(12,42),(16,34),(24,18),(32,34),(36,42));connect('tower','emitter')
        line('crossbar',(16,34),(32,34));connect('crossbar','tower')
        arc('wave-left',(12,6),(6,18),6,12,s=False)
        arc('wave-right',(42,18),(36,6),6,12,s=False)
