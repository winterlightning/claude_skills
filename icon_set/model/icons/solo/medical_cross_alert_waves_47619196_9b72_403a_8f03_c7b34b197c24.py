"""Medical cross with radiating alert arcs. Square standalone signal; one arc on each side and broad cross arms replace small repeated waves."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '47619196-9b72-403a-8f03-c7b34b197c24'
SOURCE_PATH = 'pictographic-primitives/technology/health emergency signal_47619196-9b72-403a-8f03-c7b34b197c24.svg'
AUTHOR = 'gpt-6'

class MedicalCrossAlertWaves(Solo48):
    icon_id = 'medical-cross-alert-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('medical', 'emergency', 'cross', 'health', 'alert', 'signal', 'alarm', 'first-aid')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def chain(n,*p):
            for i,(a,b) in enumerate(zip(p,p[1:]),1): line(f'{n}-{i}',a,b)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x,y-r),(x,y+r),r)
            arc(n+'b',(x,y+r),(x,y-r),r)
            contour(n,n+'a',n+'b',closed=True)
        def box(n,l,t,r,b,rad=4):
            line(n+'t',(l+rad,t),(r-rad,t)); arc(n+'tr',(r-rad,t),(r,t+rad),rad)
            line(n+'r',(r,t+rad),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            line(n+'l',(l,b-rad),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r','br','b','bl','l','tl')],closed=True)
        poly('cross',(19,16),(29,16),(29,26),(38,26),(38,36),(29,36),(29,42),(19,42),(19,36),(10,36),(10,26),(19,26),closed=True)
        arc('wave-left',(6,17),(14,6),12)
        arc('wave-right',(34,6),(42,17),12)
