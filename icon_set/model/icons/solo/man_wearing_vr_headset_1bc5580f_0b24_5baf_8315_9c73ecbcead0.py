"""Head-and-shoulders figure wearing a VR visor. Square envelope; mirrored cap, face and shoulders with Lucide headset curve principles. Nose dip and collar seam omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1bc5580f-0b24-5baf-8315-9c73ecbcead0'
SOURCE_PATH = 'pictographic-primitives/technology/male_1bc5580f-0b24-5baf-8315-9c73ecbcead0.svg'
AUTHOR = 'gpt-6'

class ManWearingVrHeadset(Solo48):
    icon_id = 'man-wearing-vr-headset'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('person', 'man', 'vr', 'headset', 'user', 'avatar', 'virtual-reality')

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
        box('visor',10,16,38,26,4)
        arc('cap',(14,16),(34,16),10);connect('cap','visor')
        arc('face-left',(14,26),(24,36),10,sweep=False);arc('face-right',(24,36),(34,26),10,sweep=False);contour('face','face-left','face-right');connect('face','visor')
        arc('shoulder-left',(6,42),(24,36),18,6);arc('shoulder-right',(24,36),(42,42),18,6);contour('shoulders','shoulder-left','shoulder-right');connect('shoulders','face')
