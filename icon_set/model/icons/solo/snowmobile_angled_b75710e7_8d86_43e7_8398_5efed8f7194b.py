"""Angled right-facing snowmobile with handlebars, track and front ski. No exact local Lucide match. Shared front ski geometry preserves the differing body and track silhouettes.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b75710e7-8d86-43e7-8398-5efed8f7194b'
SOURCE_PATH = 'pictographic-primitives/symbol/snow scooter_b75710e7-8d86-43e7-8398-5efed8f7194b.svg'
AUTHOR = 'gpt-6'


class SnowmobileAngled(Solo48):
    icon_id = 'snowmobile-angled'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('snowmobile', 'snow', 'scooter', 'winter', 'vehicle', 'sled', 'ride', 'mountain')

    def build(self) -> None:

        self.add_polyline('handlebar',(20,8),(22,8),(28,14))

        pts=[(4,30),(6,22),(18,21),(23,14),(28,14),(34,20)]
        for j,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line('upper-'+str(j),a,b)
        top=['upper-'+str(j) for j in range(1,6)]

        self.add_arc('nose',(34,20),(34,30),radius_x=4,radius_y=5)
        pts=[(34,30),(32,30),(24,30),(20,30),(8,30),(4,30)]
        for j,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line('bottom-'+str(j),a,b)
        self.add_contour('body',*top,'nose',*['bottom-'+str(j) for j in range(1,6)],closed=True)
        self.relate('connect','handlebar','body')
        self.add_line('ski-post',(32,30),(32,40))
        self.add_polyline('ski-flat',(26,40),(32,40),(38,40))
        self.add_arc('ski-curl',(38,40),(44,34),radius_x=6,sweep=False)
        self.relate('connect','ski-post','body')
        self.relate('connect','ski-post','ski-flat')
        self.relate('connect','ski-flat','ski-curl')

        self.add_arc('track-front-turn',(8,30),(4,36),radius_x=4,radius_y=6,sweep=False)
        self.add_arc('track-bottom-turn',(4,36),(8,40),radius_x=4,sweep=False)
        self.add_line('track-run-1',(8,40),(14,40))
        self.add_line('track-run-2',(14,40),(24,30))
        self.add_contour('track','track-front-turn','track-bottom-turn','track-run-1','track-run-2')
        self.relate('connect','track','body')
