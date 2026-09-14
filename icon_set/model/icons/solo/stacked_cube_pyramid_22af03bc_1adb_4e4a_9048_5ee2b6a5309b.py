"""Three isometric cubes in a pyramid; shared mesh inspired by Lucide boxes. HRECT_L spreads the lower pair; all three cube identities retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '22af03bc-1adb-4e4a-9048-5ee2b6a5309b'
SOURCE_PATH = 'pictographic-primitives/technology/element reallity kit_22af03bc-1adb-4e4a-9048-5ee2b6a5309b.svg'
AUTHOR = 'gpt-6'

class StackedCubePyramid(Solo48):
    icon_id = 'stacked-cube-pyramid'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('cubes', 'blocks', '3d', 'stack', 'objects', 'reality-kit', 'geometry')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
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
        # Three cubes share real edges; a single planar mesh avoids doubled seams.
        poly('outline',(24,8),(34,12),(34,22),(42,26),(42,36),(34,40),(24,36),(14,40),(6,36),(6,26),(14,22),(14,12),closed=True)
        poly('top-face',(14,12),(24,16),(34,12));connect('top-face','outline')
        poly('center',(24,16),(24,26),(24,36));connect('center','top-face');connect('center','outline')
        poly('middle',(14,22),(24,26),(34,22));connect('middle','outline');connect('middle','center')
        poly('left-face',(6,26),(14,30),(24,26));connect('left-face','outline');connect('left-face','center');connect('left-face','middle')
        line('left-edge',(14,30),(14,40));connect('left-edge','left-face');connect('left-edge','outline')
        poly('right-face',(24,26),(34,30),(42,26));connect('right-face','outline');connect('right-face','center');connect('right-face','middle');connect('right-face','left-face')
        line('right-edge',(34,30),(34,40));connect('right-edge','right-face');connect('right-edge','outline')
