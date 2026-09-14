"""Half-disc optical clarity symbol with four beams; HRECT_L matches the horizontal layout. No useful exact Lucide match; shared ray start and clear spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a9506b8e-9c3c-514f-a343-98e61ffe7e14'
SOURCE_PATH = 'pictographic-primitives/technology/image clarity sharpness_a9506b8e-9c3c-514f-a343-98e61ffe7e14.svg'
AUTHOR = 'gpt-6'

class HalfCircleWithBeamLines(Solo48):
    icon_id = 'half-circle-with-beam-lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('clarity', 'sharpness', 'image', 'beam', 'light', 'focus', 'display')

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
        arc('lens',(20,8),(20,40),16,sweep=False)
        line('edge',(20,40),(20,8));contour('half-disc','lens','edge',closed=True)
        for i,(y,end) in enumerate([(8,35),(18,42),(28,40),(40,34)]):line(f'beam-{i}',(29,y),(end,y))
