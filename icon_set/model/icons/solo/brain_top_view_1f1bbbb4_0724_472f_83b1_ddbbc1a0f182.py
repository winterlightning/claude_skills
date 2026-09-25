"""Brain with two lobed hemispheres and central divide. Square extremes 6/6/42/42. Lucide brain informs coherent lobes and folds attached to the divide. Four small folds reduced to one mirrored pair."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1f1bbbb4-0724-472f-83b1-ddbbc1a0f182'
SOURCE_PATH = 'pictographic-primitives/technology/study brain_1f1bbbb4-0724-472f-83b1-ddbbc1a0f182.svg'
AUTHOR = 'gpt-6'

class BrainTopView(Solo48):
    icon_id = 'brain-top-view'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('brain', 'study', 'mind', 'hemispheres', 'thinking', 'learning', 'intelligence')

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
        arc('upper-left',(24,12),(12,12),6,sweep=False)
        arc('side-left-top',(12,12),(6,24),6,12,sweep=False)
        arc('side-left-bottom',(6,24),(12,36),6,12,sweep=False)
        arc('lower-left',(12,36),(24,36),6,sweep=False)
        arc('lower-right',(24,36),(36,36),6,sweep=False)
        arc('side-right-bottom',(36,36),(42,24),6,12,sweep=False)
        arc('side-right-top',(42,24),(36,12),6,12,sweep=False)
        arc('upper-right',(36,12),(24,12),6,sweep=False)
        contour('outline','upper-left','side-left-top','side-left-bottom','lower-left','lower-right','side-right-bottom','side-right-top','upper-right',closed=True)
        poly('divide',(24,12),(24,24),(24,36));connect('divide','outline')
        arc('fold-left',(24,24),(15,28),9,4);arc('fold-right',(24,24),(33,28),9,4,sweep=False)
        connect('fold-left','divide');connect('fold-right','divide');connect('fold-left','fold-right')
