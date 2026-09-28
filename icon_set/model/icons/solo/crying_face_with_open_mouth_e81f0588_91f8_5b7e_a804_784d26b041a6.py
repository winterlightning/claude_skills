"""Crying Face with Open Mouth; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e81f0588-91f8-5b7e-a804-784d26b041a6'
SOURCE_PATH = 'pictographic-primitives/smileys/sad crying_e81f0588-91f8-5b7e-a804-784d26b041a6.svg'
AUTHOR = 'gpt-6'


class CryingFaceWithOpenMouth(Solo48):
    icon_id = 'crying-face-with-open-mouth'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('crying', 'tear', 'sad', 'distressed', 'face', 'emoji')

    def build(self) -> None:

        # CIRCLE with a right cheek gap for the physical tear.
        self.add_arc("head",(36,8),(36,40),radius_x=20,large_arc=True,sweep=False)
        for side,sign in (("left",1),("right",-1)):
            def p(x,y):return (24+sign*(x-24),y)
            self.add_arc(f"eye-{side}",p(16,18),p(19,18),radius_x=2,sweep=sign>0)
        self.add_arc("mouth-top",(17,32),(29,32),radius_x=6,radius_y=5)
        self.add_arc("mouth-bottom",(29,32),(17,32),radius_x=6,radius_y=3)
        self.add_contour("mouth","mouth-top","mouth-bottom",closed=True)
        self.add_arc("tear",(40,25),(40,31),radius_x=5,sweep=False)
