"""Top-view head with nose, ear bumps and divergent sight rays. Square diagram; no useful exact Lucide match; one clear dash per ray."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9441b8ec-57df-4f5b-8f53-e4bc68bdb94e'
SOURCE_PATH = 'pictographic-primitives/technology/field of view fov top_9441b8ec-57df-4f5b-8f53-e4bc68bdb94e.svg'
AUTHOR = 'gpt-6'

class HeadFieldOfViewTop(Solo48):
    icon_id = 'head-field-of-view-top'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('field-of-view', 'fov', 'head', 'top-view', 'vision', 'sight', 'perspective')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
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
        arc('head-right',(27,19),(37,29),12)
        arc('lower',(37,29),(11,29),13)
        arc('head-left',(11,29),(21,19),12)
        line('nose-1',(21,19),(24,17));line('nose-2',(24,17),(27,19))
        contour('head','head-right','lower','head-left','nose-1','nose-2',closed=True)
        line('ear-left',(11,29),(9,29));connect('ear-left','head')
        line('ear-right',(37,29),(39,29));connect('ear-right','head')
        line('ray-left',(6,6),(12,12))
        line('ray-right',(42,6),(36,12))
