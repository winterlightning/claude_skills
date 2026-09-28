from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3a3e4d85-115c-4ccb-82d1-46fd45222b3a'
SOURCE_PATH = 'pictographic-primitives/other/browser person_3a3e4d85-115c-4ccb-82d1-46fd45222b3a.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    """A browser window containing a detached user bust."""
    icon_id = 'browser-user-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('web', 'browser', 'user', 'profile')

    def build(self):
        # Plan: rounded frame with header; centered detached circular head and broad shoulders.
        # Human construction: icon_set/references/human_ref/user.svg.
        # Head bottom 24, shoulders top 32: exactly 8 centerline / 4 ink units.
        # Centerline bounds (8,4)-(40,44).
        self.add_line('top',(12,4),(36,4))
        self.add_arc('tr',(36,4),(40,8),radius_x=4)
        self.add_line('ru',(40,8),(40,12))
        self.add_line('rl',(40,12),(40,40))
        self.add_arc('br',(40,40),(36,44),radius_x=4)
        self.add_line('bottom',(36,44),(12,44))
        self.add_arc('bl',(12,44),(8,40),radius_x=4)
        self.add_line('ll',(8,40),(8,12))
        self.add_line('lu',(8,12),(8,8))
        self.add_arc('tl',(8,8),(12,4),radius_x=4)
        self.add_contour('frame','top','tr','ru','rl','br','bottom','bl','ll','lu','tl',closed=True)
        self.add_line('header',(8,12),(40,12))
        self.relate('connect','frame','header')
        cx,cy,r = 24,22,2
        self.add_arc('head-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc('head-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_arc('shoulders',(17,35),(31,35),radius_x=7,radius_y=3)
