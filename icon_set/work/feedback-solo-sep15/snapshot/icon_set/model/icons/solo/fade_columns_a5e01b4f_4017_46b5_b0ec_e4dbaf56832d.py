"""Three outlined columns, with two diagonal hatch lines in the left column. Wide envelope provides eight-unit openings and gaps for three columns. Lucide columns-3 informs repeated widths; corners use round stroke joins rather than curved caps to certify spacing. Extra hatching is omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5e01b4f-4017-46b5-b0ec-e4dbaf56832d'
SOURCE_PATH = 'pictographic-primitives/photography/photo fade_a5e01b4f-4017-46b5-b0ec-e4dbaf56832d.svg'
AUTHOR = 'gpt-6'

class FadeColumns(Solo48):
    icon_id = 'fade-columns'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('fade', 'columns', 'photo', 'filter', 'edit', 'effect', 'transition', 'opacity')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def segments(n,*p):
            for j,(a,b) in enumerate(zip(p,p[1:]),1):line(n+'-'+str(j),a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y)]
            for j,p in enumerate(pts):arc(n+'-'+str(j),p,pts[(j+1)%4],r)
            contour(n,*[n+'-'+str(j) for j in range(4)],closed=True)

        for j,x in enumerate((4,20,36)):
            poly('column-'+str(j),(x,8),(x+8,8),(x+8,12),(x+8,24),(x+8,40),(x,40),(x,32),(x,20),closed=True)
        for j,(a,b) in enumerate((((4,20),(12,12)),((4,32),(12,24)))):
            line('hatch-'+str(j),a,b);connect('hatch-'+str(j),'column-0')
