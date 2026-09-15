"""Heart-Eyes Face; rebuilt from the supplied visual reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '947547ca-2668-5370-8ab0-93b823725d21'
SOURCE_PATH = 'pictographic-primitives/smileys/in love_947547ca-2668-5370-8ab0-93b823725d21.svg'
AUTHOR = 'gpt-6'


class HeartEyesFace(Solo48):
    icon_id = 'heart-eyes-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('love', 'heart', 'smile', 'adoring', 'face', 'emoji')

    def build(self) -> None:

        # Open cheek sectors leave the two actual heart apertures readable.
        self.add_arc("crown",(12,8),(36,8),radius_x=20)
        self.add_arc("chin",(40,36),(8,36),radius_x=20)
        for side,sign in (("left",1),("right",-1)):
            def p(x,y): return (24+sign*(x-24),y)
            self.add_arc(f"heart-{side}-a",p(14,17),p(9,20),radius_x=3,sweep=sign<0)
            self.add_line(f"heart-{side}-b",p(9,20),p(14,26))
            self.add_line(f"heart-{side}-c",p(14,26),p(19,20))
            self.add_arc(f"heart-{side}-d",p(19,20),p(14,17),radius_x=3,sweep=sign<0)
            self.add_contour(f"heart-{side}",*(f"heart-{side}-{c}" for c in "abcd"),closed=True)
        self.add_arc("smile",(20,33),(28,33),radius_x=5,sweep=False)
