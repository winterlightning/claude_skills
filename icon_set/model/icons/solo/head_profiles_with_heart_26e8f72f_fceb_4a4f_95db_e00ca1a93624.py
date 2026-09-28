"""Opposing head profiles share a heart between them. No useful exact Lucide match; coherent crown arcs and a symmetric heart retain the source relationship. Small facial steps are reduced."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26e8f72f-fceb-4a4f-95db-e00ca1a93624'
SOURCE_PATH = 'pictographic-primitives/users/empathy authentication heart intersect_26e8f72f-fceb-4a4f-95db-e00ca1a93624.svg'
AUTHOR = 'gpt-6'


class HeadProfilesWithHeart(Solo48):
    icon_id = 'head-profiles-with-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    categories = ("users", "primitives")
    aliases = ()
    keywords = ('empathy', 'heads', 'profile', 'heart', 'compassion', 'people', 'care', 'understanding')

    def build(self) -> None:
        # Square extremes (6,6)-(42,42); unequal heads leave room for a shared heart.
        self.add_arc('rear-crown-a',(18,10),(26,6),radius_x=10)
        self.add_arc('rear-crown-b',(26,6),(38,18),radius_x=12)
        self.add_line('rear-face-1',(38,18),(42,26))
        self.add_line('rear-face-2',(42,26),(38,28))
        self.add_line('rear-face-3',(38,28),(38,35))
        self.add_line('rear-face-4',(38,35),(31,35))
        self.add_line('rear-face-5',(31,35),(31,42))
        self.add_contour('rear','rear-crown-a','rear-crown-b','rear-face-1','rear-face-2','rear-face-3','rear-face-4','rear-face-5')
        self.add_arc('front-crown',(11,16),(9,24),radius_x=12,sweep=False)
        self.add_line('front-face-1',(9,24),(6,31))
        self.add_line('front-face-2',(6,31),(11,33))
        self.add_line('front-face-3',(11,33),(11,37))
        self.add_line('front-face-4',(11,37),(17,38))
        self.add_line('front-face-5',(17,38),(17,42))
        self.add_contour('front','front-crown','front-face-1','front-face-2','front-face-3','front-face-4','front-face-5')
        self.add_arc('heart-left',(24,20),(18,23),radius_x=4,sweep=False)
        self.add_line('heart-left-tip',(18,23),(24,29))
        self.add_line('heart-right-tip',(24,29),(30,23))
        self.add_arc('heart-right',(30,23),(24,20),radius_x=4,sweep=False)
        self.add_contour('heart','heart-left','heart-left-tip','heart-right-tip','heart-right',closed=True)
