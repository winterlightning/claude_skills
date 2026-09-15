"""An eight-point contrast sun with a left-facing half disc. Square envelope reaches the eight-point silhouette. Lucide contrast informs the semicircle and vertical diameter. Centre reduced for clearance; its half-disc identity and deliberate left/right asymmetry remain."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5243c60-cfbb-42ad-8319-7d11d5997e34'
SOURCE_PATH = 'pictographic-primitives/photography/light mode bright dark 1_e5243c60-cfbb-42ad-8319-7d11d5997e34.svg'
AUTHOR = 'gpt-6'

class ContrastStarBadge(Solo48):
    icon_id = 'contrast-star-badge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('contrast', 'brightness', 'dark mode', 'light mode', 'badge', 'display', 'setting', 'half')

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

        poly('sunburst',(24,6),(32,10),(38,10),(38,16),(42,24),(38,32),(38,38),(32,38),(24,42),(16,38),(10,38),(10,32),(6,24),(10,16),(10,10),(16,10),closed=True)
        arc('half-disc',(27,17),(27,31),7,sweep=False)
        line('diameter',(27,31),(27,17));contour('contrast','half-disc','diameter',closed=True)
