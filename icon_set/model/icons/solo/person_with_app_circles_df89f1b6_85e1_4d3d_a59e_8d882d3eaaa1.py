"""Person beneath five floating app circles. Square extremes 6/6/42/42. Preserve all five launcher positions; tiny internal dots omitted. Lucide person-standing head hierarchy inspected earlier informs the listener."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'df89f1b6-85e1-4d3d-a59e-8d882d3eaaa1'
SOURCE_PATH = 'pictographic-primitives/technology/vr os homepage_df89f1b6-85e1-4d3d-a59e-8d882d3eaaa1.svg'
AUTHOR = 'gpt-6'

class PersonWithAppCircles(Solo48):
    icon_id = 'person-with-app-circles'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('vr', 'os', 'homepage', 'apps', 'person', 'launcher', 'interface')

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
        for n,x,y in [('top',24,8),('tl',10,12),('tr',38,12),('left',8,26),('right',40,26)]:circle(n,x,y,2)
        circle('head',24,25,4)
        arc('shoulders',(14,42),(34,42),10,4)
