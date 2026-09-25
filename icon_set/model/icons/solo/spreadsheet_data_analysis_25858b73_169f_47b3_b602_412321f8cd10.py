"""A spreadsheet with a lower-right rising chart.
Plan: SQUARE reserves a larger lower-right chart cutout.
Reduction: Grid reduced to two columns and two header bands; rising trend made shallower to clear baseline.
Construction: Source grid and Lucide-style orthogonal construction; trend uses one smooth Bezier.
Layout: Chart is intentionally offset to the lower right; grid junctions are shared."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25858b73-169f-47b3-b602-412321f8cd10'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_35/spreadsheet data analysis_25858b73-169f-47b3-b602-412321f8cd10.svg'
AUTHOR = "gpt-6"
# Plan: Spreadsheet grid with lower-right analytics chart cutout and a rising curve.
# References: Rounded grid construction; coherent chart axes and smooth S-shaped data trend.
# Reduction: Reduced grid to two columns and two rows; retained chart cutout.

class AuthoredIcon(Solo48):
    icon_id = 'spreadsheet-data-analysis'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('spreadsheet', 'data', 'analysis')

    def build(self):
        self.add_polyline('table',(6,42),(6,6),(42,6),(42,22),(20,22),(20,42),closed=True)
        self.add_line('header',(6,14),(42,14));self.add_line('row',(6,22),(20,22));self.add_line('column',(20,14),(20,22))
        for n in ('header','row','column'):self.relate('connect',n,'table')
        self.relate('connect','header','column');self.relate('connect','row','column')
        self.add_polyline('axes',(29,31),(29,34),(29,42),(42,42))
        self.add_bezier('curve',(29,34),((36,34),(35,31),(42,31)));self.relate('connect','axes','curve')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
