"""Face with Steam from Nose; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a739aba3-680e-4958-8ded-555dc6c3c98e'
SOURCE_PATH = 'pictographic-primitives/smileys/rage_a739aba3-680e-4958-8ded-555dc6c3c98e.svg'
AUTHOR = 'gpt-6'


class FaceWithSteamFromNose(Solo48):
    icon_id = 'face-with-steam-from-nose'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('rage', 'angry', 'steam', 'nose', 'face', 'emoji')

    def build(self) -> None:

        # SQUARE: open lower head leaves space for two mirrored jets and puffs.
        self.add_arc("head",(6,24),(42,24),radius_x=18)
        for side,sign in (("left",1),("right",-1)):
            def p(x,y):return (24+sign*(x-24),y)
            self.add_line(f"brow-{side}",p(18,17),p(20,18))
            self.add_line(f"jet-{side}",p(19,27),p(12,32))
            self.add_arc(f"puff-{side}-a",p(12,32),p(6,38),radius_x=6,sweep=sign<0)
            self.add_arc(f"puff-{side}-b",p(6,38),p(10,42),radius_x=4,sweep=sign<0)
            self.add_arc(f"puff-{side}-c",p(10,42),p(14,38),radius_x=4,sweep=sign<0)
            self.add_contour(f"steam-{side}",f"jet-{side}",*(f"puff-{side}-{c}" for c in "abc"))
