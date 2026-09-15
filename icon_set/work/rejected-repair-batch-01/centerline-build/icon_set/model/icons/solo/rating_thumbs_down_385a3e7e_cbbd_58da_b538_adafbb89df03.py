"""A downward thumb with a broad back and stacked fingers. Lucide thumbs-down informs the connected hand silhouette and rounded corners; preserve the source’s rightward fingers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '385a3e7e-cbbd-58da-b538-adafbb89df03'
SOURCE_PATH = 'pictographic-primitives/rating/dislike_385a3e7e-cbbd-58da-b538-adafbb89df03.svg'
AUTHOR = 'gpt-6'

class RatingThumbsDown(Solo48):
    icon_id = 'rating-thumbs-down'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/rating"
    aliases = ()
    keywords = ('dislike', 'thumbs-down', 'hand', 'disapprove', 'negative', 'feedback', 'rating', 'vote')

    def circle(self,name,cx,cy,r):
        points=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        for i in range(4):self.add_arc(name+'-'+str(i),points[i],points[i+1],radius_x=r)
        self.add_contour(name,*(name+'-'+str(i) for i in range(4)),closed=True)

    def build(self) -> None:
        # Centerline envelope (8,4)-(40,44).
        self.add_line('back',(14,4),(34,4))
        self.add_arc('top-right',(34,4),(40,10),radius_x=6)
        self.add_polyline('finger-edge',(40,10),(40,13),(40,21),(40,24))
        self.add_arc('lower-right',(40,24),(34,30),radius_x=6)
        self.add_line('palm',(34,30),(26,30))
        self.add_line('thumb-inner',(26,30),(29,39))
        self.add_arc('thumb-tip-right',(29,39),(24,44),radius_x=5)
        self.add_arc('thumb-tip-left',(24,44),(20,40),radius_x=4)
        self.add_line('thumb-outer',(20,40),(14,28))
        self.add_arc('lower-left',(14,28),(8,22),radius_x=6)
        self.add_line('wrist',(8,22),(8,10))
        self.add_arc('top-left',(8,10),(14,4),radius_x=6)
        self.add_contour('hand','lower-right','palm','thumb-inner','thumb-tip-right','thumb-tip-left','thumb-outer','lower-left','wrist','top-left','back','top-right')
        self.relate('connect','hand','finger-edge')
        for y in (13,21):
         self.add_line('finger-'+str(y),(32,y),(40,y));self.relate('connect','finger-'+str(y),'finger-edge')
