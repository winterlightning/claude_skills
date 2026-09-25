"""A person bust with round head and a flat-bottom torso. Vertical envelope preserves portrait proportions. Lucide user-round informs head and matching shoulder arcs. No facial features added; clear separation remains between head and torso."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b077f4c4-b7ab-598a-91af-1bfe79067043'
SOURCE_PATH = 'pictographic-primitives/photography/man_b077f4c4-b7ab-598a-91af-1bfe79067043.svg'
AUTHOR = 'gpt-6'

class PersonBust(Solo48):
    icon_id = 'person-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    aliases = ()
    keywords = ('person', 'user', 'man', 'avatar', 'profile', 'account', 'portrait', 'bust')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'-top',(x-r,y),(x+r,y),r)
            arc(n+'-bottom',(x+r,y),(x-r,y),r)
            contour(n,n+'-top',n+'-bottom',closed=True)
        def box(n,l,t,r,b,rad=4):
            pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
            for j,a in enumerate(pts):
                z=pts[(j+1)%8]
                if j%2:arc(n+str(j),a,z,rad)
                else:line(n+str(j),a,z)
            contour(n,*[n+str(j) for j in range(8)],closed=True)

        circle('head',24,11,7)
        arc('shoulder-left',(8,38),(18,28),10)
        line('shoulder-top',(18,28),(30,28))
        arc('shoulder-right',(30,28),(40,38),10)
        poly('lower',(40,38),(40,44),(8,44),(8,38))
        connect('shoulder-left','shoulder-top');connect('shoulder-right','shoulder-top');connect('lower','shoulder-left');connect('lower','shoulder-right')
