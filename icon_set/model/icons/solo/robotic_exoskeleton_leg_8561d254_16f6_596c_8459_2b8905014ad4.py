"""Side-view mechanical leg with thigh plate, circular knee, angled shin and flat foot. Portrait envelope reaches 8/40 and 4/44. Preserve rightward stepping asymmetry; narrow paired shin struts reduced to one."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8561d254-16f6-596c-8459-2b8905014ad4'
SOURCE_PATH = 'pictographic-primitives/technology/robot exo skeleton leg_8561d254-16f6-596c-8459-2b8905014ad4.svg'
AUTHOR = 'gpt-6'

class RoboticExoskeletonLeg(Solo48):
    icon_id = 'robotic-exoskeleton-leg'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('exoskeleton', 'leg', 'robotic', 'prosthetic', 'joint', 'wearable', 'mobility')

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
        poly('thigh',(8,4),(20,4),(28,20),(24,20),(16,20),closed=True)
        circle('knee',24,24,4);connect('knee','thigh')
        poly('shin',(24,28),(18,36),(18,44),(40,44),(30,36),(18,36));connect('shin','knee')
