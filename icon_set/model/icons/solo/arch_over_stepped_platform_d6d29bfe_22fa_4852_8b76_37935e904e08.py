"""Semicircular stadium arch above a flared platform. Square envelope; shared radial center and mirrored feet. The narrow internal step line is omitted to preserve the platform opening."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd6d29bfe-22fa-4852-8b76-37935e904e08'
SOURCE_PATH = 'pictographic-primitives/technology/indoor stadium_d6d29bfe-22fa-4852-8b76-37935e904e08.svg'
AUTHOR = 'gpt-6'

class ArchOverSteppedPlatform(Solo48):
    icon_id = 'arch-over-stepped-platform'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('stadium', 'arena', 'indoor', 'arch', 'dome', 'platform', 'venue')

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
        arc('arch-left',(6,24),(24,6),18)
        arc('arch-right',(24,6),(42,24),18)
        chain('foot-right',(42,24),(42,32),(34,24))
        arc('inner',(34,24),(14,24),10,sweep=False)
        chain('foot-left',(14,24),(6,32),(6,24))
        contour('arch','arch-left','arch-right','foot-right-1','foot-right-2','inner','foot-left-1','foot-left-2',closed=True)
        poly('platform',(20,32),(28,32),(36,42),(12,42),closed=True)
