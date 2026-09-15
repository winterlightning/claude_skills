"""Brain in side view with a short brainstem. Square extremes 6/6/42/42. Lucide brain informs rounded lobe construction; one interior fold retained, with intentional anatomical asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '33d2f3f9-a1db-477b-a0a6-a8d7321a8a1f'
SOURCE_PATH = 'pictographic-primitives/technology/study brain 1_33d2f3f9-a1db-477b-a0a6-a8d7321a8a1f.svg'
AUTHOR = 'gpt-6'

class BrainSideViewWithStem(Solo48):
    icon_id = 'brain-side-view-with-stem'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('brain', 'study', 'mind', 'neuroscience', 'thinking', 'learning', 'anatomy')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def chain(n,*p):
            for i,(a,b) in enumerate(zip(p,p[1:]),1): line(f'{n}-{i}',a,b)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x,y-r),(x+r,y),r)
            arc(n+'b',(x+r,y),(x,y+r),r)
            arc(n+'c',(x,y+r),(x-r,y),r)
            arc(n+'d',(x-r,y),(x,y-r),r)
            contour(n,n+'a',n+'b',n+'c',n+'d',closed=True)
        def box(n,l,t,r,b,rad=4):
            line(n+'t',(l+rad,t),(r-rad,t)); arc(n+'tr',(r-rad,t),(r,t+rad),rad)
            line(n+'r',(r,t+rad),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            line(n+'l',(l,b-rad),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r','br','b','bl','l','tl')],closed=True)
        arc('crown',(12,16),(32,16),10)
        arc('right-top',(32,16),(42,26),10)
        arc('right-bottom',(42,26),(32,36),10)
        chain('stem',(32,36),(34,42),(26,42),(22,34),(12,34))
        arc('left-bottom',(12,34),(6,24),6,10)
        arc('left-top',(6,24),(12,16),6,8)
        contour('brain','crown','right-top','right-bottom','stem-1','stem-2','stem-3','stem-4','left-bottom','left-top',closed=True)
        arc('fold',(18,24),(24,18),6)
