"""Eye with a half iris and horizontal strain marks. HRECT_L centerline extremes 4/8/44/40. Lucide eye informs coherent outline and iris; two rays replace three and the outer eye is gently rounded to preserve clear interior space."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ddd19dd6-b9d8-4f43-9403-4673a5541cd4'
SOURCE_PATH = 'pictographic-primitives/technology/vision comfort eye strain_ddd19dd6-b9d8-4f43-9403-4673a5541cd4.svg'
AUTHOR = 'gpt-6'

class EyeStrain(Solo48):
    icon_id = 'eye-strain'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('eye', 'strain', 'vision', 'comfort', 'sight', 'fatigue', 'display')

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
        arc('eye-top',(4,24),(44,24),20,16);arc('eye-bottom',(44,24),(4,24),20,16);contour('eye','eye-top','eye-bottom',closed=True)
        arc('iris',(24,17),(24,31),7,sweep=False)
        chain('flat',(24,31),(24,29),(24,19),(24,17));contour('iris-outline','iris','flat-1','flat-2','flat-3',closed=True)
        line('ray-top',(24,19),(32,19));line('ray-bottom',(24,29),(32,29));connect('ray-top','iris-outline');connect('ray-bottom','iris-outline')
