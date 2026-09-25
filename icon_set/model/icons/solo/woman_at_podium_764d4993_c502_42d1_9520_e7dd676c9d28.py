"""A woman with a pointed fringe and long hair stands behind a lectern. Lucide user-round informs the head and shoulder arcs. The reference supplies the hair and splayed lectern legs; fingers and ears are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '764d4993-c502-42d1-9520-e7dd676c9d28'
SOURCE_PATH = 'pictographic-primitives/users/woman podium_764d4993-c502-42d1-9520-e7dd676c9d28.svg'
AUTHOR = 'gpt-6'


class WomanAtPodium(Solo48):
    icon_id = 'woman-at-podium'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    aliases = ()
    keywords = ('woman', 'podium', 'lectern', 'speaker', 'presentation', 'speech', 'female', 'talk')

    def circle(self,name,cx,cy,r):
        pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        ids=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(i);self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)


    def build(self) -> None:
        # Square centerline extremes (6,6)-(42,42), shared axis x=24.
        self.circle('head',24,13,7)
        self.add_polyline('fringe',(17,13),(24,12),(31,13))
        self.relate('connect','head','fringe')
        for side,d in (('left',-1),('right',1)):
            self.add_line('hair-'+side,(24+d*7,13),(24+d*9,23))
            self.relate('connect','head','hair-'+side)
        self.add_arc('shoulder-left',(15,36),(24,29),radius_x=9,radius_y=7)
        self.add_arc('shoulder-right',(24,29),(33,36),radius_x=9,radius_y=7)
        self.add_contour('shoulders','shoulder-left','shoulder-right')
        self.add_polyline('lectern',(6,36),(15,36),(33,36),(42,36))
        self.add_line('leg-left',(15,36),(12,42))
        self.add_line('leg-right',(33,36),(36,42))
        self.relate('connect','shoulders','lectern')
        for name in ('leg-left','leg-right'):
            self.relate('connect','lectern',name)
            self.relate('connect','shoulders',name)
