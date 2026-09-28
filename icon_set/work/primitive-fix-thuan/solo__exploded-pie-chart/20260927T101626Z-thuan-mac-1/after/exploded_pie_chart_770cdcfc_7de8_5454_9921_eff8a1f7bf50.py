"""Revision: Reduced the lower right wedge and increased its displacement to make the exploded chart read more like the reference."""
"""Three separated pie sectors form a chart. Lucide chart-pie informs radial wedge construction; the large left sector is elliptical and the two right wedges are equalized for clearance."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '770cdcfc-7de8-5454-9921-eff8a1f7bf50'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__exploded-pie-chart/20260927T101626Z-thuan-mac-1/reference/pie_770cdcfc-7de8-5454-9921-eff8a1f7bf50.svg'
AUTHOR = 'gpt-6'


class ExplodedPieChart(Solo48):
    icon_id = 'exploded-pie-chart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    categories = ("school-learning", "primitives")
    aliases = ()
    keywords = ('pie', 'chart', 'sector', 'data', 'statistics', 'diagram')

    def run(self, name, *points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(name+"-"+str(j),a,b)

    def circle(self, name, x, y, r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        ids=[]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(j)
            self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def build(self) -> None:
        # Current centerline bounds: SQUARE 6,6-42,42; HRECT 4,8-44,40; VRECT 8,4-40,44.

        self.add_arc('main-left',(18,6),(18,42),radius_x=12,radius_y=18,sweep=False)
        self.add_line('main-edge',(18,42),(18,6))
        self.add_contour('main-sector','main-left','main-edge',closed=True)
        self.add_arc('upper-curve',(29,6),(42,19),radius_x=13)
        self.run('upper-radii',(42,19),(29,19),(29,6))
        self.add_contour('upper-sector','upper-curve','upper-radii-1','upper-radii-2',closed=True)
        self.add_arc('lower-curve',(42,32),(32,42),radius_x=10)
        self.run('lower-radii',(32,42),(32,32),(42,32))
        self.add_contour('lower-sector','lower-curve','lower-radii-1','lower-radii-2',closed=True)
