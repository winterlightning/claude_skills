"""Pod on elevated track, with shared rail/leg junctions. Wide envelope; Lucide train-front vehicle/rail relationship. One leg per side replaces double supports."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '92e4f6ba-4d5d-48a4-8318-02d1f6e40faf'
SOURCE_PATH = 'pictographic-primitives/technology/hyperloop track_92e4f6ba-4d5d-48a4-8318-02d1f6e40faf.svg'
AUTHOR = 'gpt-6'

class HyperloopPodOnTrack(Solo48):
    icon_id = 'hyperloop-pod-on-track'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('hyperloop', 'pod', 'track', 'rail', 'train', 'transport', 'maglev')

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
        line('top',(10,8),(24,8))
        arc('nose-top',(24,8),(42,18),20,10)
        line('nose-tip',(42,18),(42,22));arc('nose-bottom',(42,22),(38,28),6)
        chain('floor',(38,28),(32,28),(16,28),(10,28))
        arc('rear-bottom',(10,28),(6,22),6);line('rear',(6,22),(6,14));arc('rear-top',(6,14),(10,8),6)
        contour('pod','top','nose-top','nose-tip','nose-bottom','floor-1','floor-2','floor-3','rear-bottom','rear','rear-top',closed=True)
        arc('window-curve',(24,8),(34,18),10,sweep=False)
        line('window-bottom',(34,18),(42,18));contour('window','window-curve','window-bottom');connect('window','pod')
        poly('leg-left',(16,28),(11,38),(10,40));connect('leg-left','pod')
        poly('leg-right',(32,28),(37,38),(38,40));connect('leg-right','pod')
        poly('rail',(6,38),(11,38),(37,38),(42,38));connect('rail','leg-left');connect('rail','leg-right')
