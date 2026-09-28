"""Ski jumper leaning forward above a diagonal ski. Lucide accessibility informs the detached head and bent pose; one long ski with upturned tip retained.

SOLO48 VRECT_L; live visible envelope (6, 2, 42, 46).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2ad6ecb9-65ae-41f6-a0c3-fd3e57b60034'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ski-jumping/20260927T092933Z-thuan-mac-1/reference/snow jumping_2ad6ecb9-65ae-41f6-a0c3-fd3e57b60034.svg'
AUTHOR = "gpt-6"


class SkiJumping(Solo48):
    icon_id = 'ski-jumping'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('ski-jumping', 'skiing', 'winter', 'sport', 'jump', 'snow', 'flight', 'olympics')

    def build(self) -> None:
        cx,cy,r=24,9,5

        self.add_arc('head-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc('head-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour('head','head-top','head-bottom',closed=True)

        self.add_line('body-rise',(24,22),(12,26))
        self.mark_human_figure('person',head='head',torso='body-rise',torso_junction='start')
        self.add_arc('body-turn-upper',(12,26),(8,30),radius_x=4,sweep=False)
        self.add_arc('body-turn-lower',(8,30),(12,34),radius_x=4,sweep=False)
        self.add_contour('body','body-rise','body-turn-upper','body-turn-lower')
        self.add_polyline('ski',(16,44),(36,24),(40,20),(40,14))
