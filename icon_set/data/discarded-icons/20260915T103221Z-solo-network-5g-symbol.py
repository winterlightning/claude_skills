"""Standalone 5G network symbol. HRECT_L gives the letterforms clear counters; corner speed brackets omitted. No exact Lucide match; geometric monoline characters."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9dc361bf-d268-4878-852c-ebdc9f66c69b'
SOURCE_PATH = 'pictographic-primitives/technology/network 5g_9dc361bf-d268-4878-852c-ebdc9f66c69b.svg'
AUTHOR = 'gpt-6'

class Network5GSymbol(Solo48):
    icon_id = 'network-5g-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('5g', 'network', 'mobile', 'cellular', 'speed', 'wireless', 'signal')

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
        chain('five-top',(18,8),(4,8),(4,24),(12,24))
        arc('five-round',(12,24),(12,40),8)
        line('five-base',(12,40),(4,40));contour('five','five-top-1','five-top-2','five-top-3','five-round','five-base')
        arc('g-top',(44,15),(30,15),7,sweep=False)
        line('g-left',(30,15),(30,33));arc('g-bottom',(30,33),(44,33),7,sweep=False)
        chain('g-bar',(44,33),(44,25),(38,25));contour('g','g-top','g-left','g-bottom','g-bar-1','g-bar-2')
