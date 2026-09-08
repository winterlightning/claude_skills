"""A sitting penguin with a rounded upright body, flat beak and splayed feet."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6673357d-4cc5-548b-a630-59b4a3dcce8b'
SOURCE_PATH = 'pictographic-primitives/animals/tux_6673357d-4cc5-548b-a630-59b4a3dcce8b.svg'
AUTHOR = 'gpt-6'


class SittingPenguin(Solo48):
    icon_id = 'sitting-penguin'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('penguin', 'sitting', 'tux', 'linux', 'mascot', 'bird', 'flippers', 'antarctic')

    def build(self) -> None:
        # Visible keyshape extremes: (3, 0, 45, 48).
        self.add_arc("crown",(13,13),(35,13),radius_x=11)
        self.add_line("neck-right",(35,13),(35,20))
        self.add_arc("body-right",(35,20),(36,34),radius_x=30,sweep=False)
        self.add_arc("body-left",(12,34),(13,20),radius_x=30,sweep=False)
        self.add_line("neck-left",(13,20),(13,13))
        self.add_contour("body","body-left","neck-left","crown","neck-right","body-right")
        for side,x in (("left",12),("right",36)):
            self.add_arc(side+"-foot-top-right",(x,34),(x+7,40),radius_x=7,radius_y=6)
            self.add_arc(side+"-foot-bottom-right",(x+7,40),(x,46),radius_x=7,radius_y=6)
            self.add_arc(side+"-foot-bottom-left",(x,46),(x-7,40),radius_x=7,radius_y=6)
            self.add_arc(side+"-foot-top-left",(x-7,40),(x,34),radius_x=7,radius_y=6)
            self.add_contour(side+"-foot",side+"-foot-top-right",side+"-foot-bottom-right",side+"-foot-bottom-left",side+"-foot-top-left",closed=True)
            self.relate("connect","body",side+"-foot")
        self.add_line("belly",(19,40),(29,40))
        self.relate("connect","belly","left-foot")
        self.relate("connect","belly","right-foot")
        self.add_dot("eye-left",(21,13))
        self.add_dot("eye-right",(27,13))
        self.add_line("beak",(21,22),(27,22))
