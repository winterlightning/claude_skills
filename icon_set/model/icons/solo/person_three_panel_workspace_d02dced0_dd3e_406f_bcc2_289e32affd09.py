"""Person before three connected workspace panels. Square extremes 6/6/42/42. Two angled wings and bowed central edge retained; lower center edge omitted around the user. Lucide person-standing hierarchy and mirrored panel construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd02dced0-dd3e-406f-bcc2-289e32affd09'
SOURCE_PATH = 'pictographic-primitives/technology/window workspace_d02dced0-dd3e-406f-bcc2-289e32affd09.svg'
AUTHOR = 'gpt-6'

class PersonThreePanelWorkspace(Solo48):
    icon_id = 'person-three-panel-workspace'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('workspace', 'window', 'panels', 'person', 'multi-screen', 'spatial', 'immersive')

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
        poly('left-wing',(6,6),(14,8),(14,22),(6,26),closed=True)
        poly('right-wing',(42,6),(34,8),(34,22),(42,26),closed=True)
        arc('middle-left',(14,8),(24,10),10,2,sweep=False);arc('middle-right',(24,10),(34,8),10,2,sweep=False)
        contour('middle-top','middle-left','middle-right');connect('middle-top','left-wing');connect('middle-top','right-wing')
        circle('head',24,25,2)
        arc('shoulders',(16,42),(32,42),8,6)
