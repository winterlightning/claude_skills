"""Face with Tears of Joy; rebuilt from the supplied visual reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ebca36dd-6917-4471-8aaa-e054027cccaa'
SOURCE_PATH = 'pictographic-primitives/smileys/lol_ebca36dd-6917-4471-8aaa-e054027cccaa.svg'
AUTHOR = 'gpt-6'


class FaceWithTearsOfJoy(Solo48):
    icon_id = 'face-with-tears-of-joy'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('joy', 'laughing', 'tears', 'happy', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE with intentional gaps where rounded tear strokes descend.
        self.add_arc("head-top",(8,12),(40,12),radius_x=20)
        self.add_arc("head-bottom",(36,40),(12,40),radius_x=20)
        for side,sign in (("left",1),("right",-1)):
            def p(x,y): return (24+sign*(x-24),y)
            self.add_arc(f"eye-{side}",p(16,17),p(19,17),radius_x=2,sweep=sign>0)
            self.add_arc(f"tear-{side}",p(7,22),p(7,30),radius_x=6,sweep=sign<0)
        self.add_line("mouth-top",(17,27),(31,27))
        self.add_arc("mouth-bottom",(31,27),(17,27),radius_x=7,radius_y=8)
        self.add_contour("mouth","mouth-top","mouth-bottom",closed=True)
