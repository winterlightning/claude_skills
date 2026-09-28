"""Person beneath inward-curving side panels. Square extremes 6/6/42/42. Shared arch center and mirrored shoulder geometry; panel thickness reduced to outer curves and lower folded corners. Lucide person-standing hierarchy inspected earlier."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '97ee4b15-7f44-488f-9abe-6e5d660fe265'
SOURCE_PATH = 'pictographic-primitives/technology/window workspace_97ee4b15-7f44-488f-9abe-6e5d660fe265.svg'
AUTHOR = 'gpt-6'

class PersonInsideArchedPanels(Solo48):
    icon_id = 'person-inside-arched-panels'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('workspace', 'window', 'person', 'panels', 'immersive', 'spatial', 'arch')

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
            chain(n+'r',(r,t+rad),(r,(t+b)//2),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            chain(n+'l',(l,b-rad),(l,(t+b)//2),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r-1','r-2','br','b','bl','l-1','l-2','tl')],closed=True)
        chain('left-panel',(12,32),(6,36),(6,24))
        arc('arch-left',(6,24),(24,6),18);arc('arch-right',(24,6),(42,24),18)
        chain('right-panel',(42,24),(42,36),(36,32))
        contour('panels','left-panel-1','left-panel-2','arch-left','arch-right','right-panel-1','right-panel-2')
        circle('head',24,24,4)
        arc('shoulders',(16,42),(32,42),8,4)
