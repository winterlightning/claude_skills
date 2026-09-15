"""Person with outstretched arms inside a panoramic screen. Square scene; shared figure axis and concave panel top. Lower panel edge omitted around the figure to preserve clear space."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cad6a2b3-29ca-425e-80db-7ffe5f2234d4'
SOURCE_PATH = 'pictographic-primitives/technology/pass full immersive_cad6a2b3-29ca-425e-80db-7ffe5f2234d4.svg'
AUTHOR = 'gpt-6'

class PersonInWraparoundScreen(Solo48):
    icon_id = 'person-in-wraparound-screen'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('immersive', 'person', 'panorama', 'screen', 'full-immersion', 'spatial', 'virtual-reality')

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
        line('left-side',(6,34),(6,6))
        arc('top-left',(6,6),(24,8),18,2,sweep=False);arc('top-right',(24,8),(42,6),18,2,sweep=False)
        line('right-side',(42,6),(42,34));contour('panel','left-side','top-left','top-right','right-side')
        circle('head',24,20,2)
        poly('arms',(15,31),(24,31),(33,31))
        poly('body',(24,31),(24,35),(20,42));connect('body','arms')
        line('leg',(24,35),(28,42));connect('leg','body')
