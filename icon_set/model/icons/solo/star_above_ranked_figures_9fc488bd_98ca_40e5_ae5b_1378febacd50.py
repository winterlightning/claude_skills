"""Three ranked figures with a star above the tallest center block. Preserve the star and unequal side-figure heights; reduce side bodies to upright strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9fc488bd-98ca-40e5-ae5b-1378febacd50'
SOURCE_PATH = 'pictographic-primitives/rating/ranking star top_9fc488bd-98ca-40e5-ae5b-1378febacd50.svg'
AUTHOR = 'gpt-6'

class StarAboveRankedFigures(Solo48):
    icon_id = 'star-above-ranked-figures'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "rating"
    aliases = ()
    keywords = ('ranking', 'star', 'top', 'winner', 'people', 'leaderboard', 'best', 'competition')

    def circle(self,name,cx,cy,r):
        points=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        for i in range(4):self.add_arc(name+'-'+str(i),points[i],points[i+1],radius_x=r)
        self.add_contour(name,*(name+'-'+str(i) for i in range(4)),closed=True)

    def build(self) -> None:
        # Centerline envelope (8,4)-(40,44).
        self.add_polyline('star',(24,4),(27,10),(32,11),(28,15),(29,20),(24,17),(19,20),(20,15),(16,11),(21,10),closed=True)
        self.add_line('center-body',(24,29),(24,44))
        for name,x,y in [('left',11,30),('right',37,34)]:
         self.circle('head-'+name,x,y,3)
         self.add_line('body-'+name,(x,y+3),(x,44))
         self.relate('connect','head-'+name,'body-'+name)
