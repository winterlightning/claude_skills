"""Radio tower connected to two network nodes. Square envelope, centerline extremes 6/6/42/42. Lucide radio-tower beacon and tapered mast; paired waves reduced to one per side while retaining the bottom network bar."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6528c96f-6dff-48bf-b666-e223df6fdfa3'
SOURCE_PATH = 'pictographic-primitives/technology/signal tower node 5g_6528c96f-6dff-48bf-b666-e223df6fdfa3.svg'
AUTHOR = 'gpt-6'

class RadioTowerNode(Solo48):
    icon_id = 'radio-tower-node'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('tower', 'antenna', 'radio', 'signal', 'node', '5g', 'network')

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
        circle('beacon',24,12,4)
        poly('tower',(24,16),(32,30),(24,30),(16,30),closed=True);connect('tower','beacon')
        arc('left-top',(10,6),(6,14),4,8,sweep=False);arc('left-bottom',(6,14),(10,22),4,8,sweep=False);contour('left-wave','left-top','left-bottom')
        arc('right-top',(38,6),(42,14),4,8);arc('right-bottom',(42,14),(38,22),4,8);contour('right-wave','right-top','right-bottom')
        line('stem',(24,30),(24,40));connect('stem','tower')
        circle('left-node',10,40,2);circle('right-node',38,40,2)
        poly('network',(12,40),(24,40),(36,40));connect('network','stem');connect('network','left-node');connect('network','right-node')
