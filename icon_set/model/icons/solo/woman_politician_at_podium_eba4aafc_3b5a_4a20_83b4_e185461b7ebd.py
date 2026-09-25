"""Lucide user-round informs portrait and shoulder arcs; outward hair distinguishes the woman. Sash and fringe omitted for clearance; outward hair retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eba4aafc-3b5a-4a20-83b4-e185461b7ebd'
SOURCE_PATH = 'pictographic-primitives/school-learning/election politician podium woman_eba4aafc-3b5a-4a20-83b4-e185461b7ebd.svg'
AUTHOR = 'gpt-6'


class WomanPoliticianAtPodium(Solo48):
    icon_id = 'woman-politician-at-podium'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    aliases = ()
    keywords = ('woman', 'podium', 'politician', 'speech', 'sash', 'election')

    def circle(self, name, x, y, r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        ids=[]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(j)
            self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def bust(self, name, x, y, r=2, width=5):
        self.circle(name+'-head',x,y,r)
        self.add_arc(name+'-sl',(x-width,y+7),(x,y+r),radius_x=width,radius_y=7-r)
        self.add_arc(name+'-sr',(x,y+r),(x+width,y+7),radius_x=width,radius_y=7-r)
        self.add_contour(name+'-shoulders',name+'-sl',name+'-sr')
        self.relate('connect',name+'-head',name+'-shoulders')

    def build(self) -> None:
        # Bounds are derived from the live SOLO48 contract, not the stale skill table.

        self.circle('head',24,11,5)
        self.add_polyline('hair-left',(19,11),(18,16),(15,18))
        self.add_polyline('hair-right',(29,11),(30,16),(33,18))
        self.relate('connect','head','hair-left')
        self.relate('connect','head','hair-right')
        self.add_arc('shoulders',(12,34),(36,34),radius_x=12,radius_y=7)
        self.add_polyline('ledge',(6,34),(12,34),(36,34),(42,34))
        self.relate('connect','shoulders','ledge')
        for side,x,d in (('left',12,1),('right',36,-1)):
            self.add_line('leg-'+side,(x,34),(x+d*2,42))
            self.relate('connect','leg-'+side,'ledge')
            self.relate('connect','leg-'+side,'shoulders')
