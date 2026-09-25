"""A blank skull with a domed cranium and two divisions in its lower teeth.

VRECT_L extrema (8,4)-(40,44). The cranium mirrors about x=24 and narrows
to a rounded jaw. The source leaves the face blank. Human user.svg informed
the centered head width; Lucide skull informed cheek-to-jaw transitions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "30707083-b1bf-4737-b77c-8195d26ecdb5"
SOURCE_PATH = "pictographic-primitives/_uncategorized_13/crime tools drugs powder_30707083-b1bf-4737-b77c-8195d26ecdb5.svg"
AUTHOR = "gpt-6"


class HumanSkullSymbol(Solo48):
    icon_id = "human-skull-symbol"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("blank skull", "divided teeth skull")
    keywords = ("cranium", "jaw", "bone", "teeth")

    def build(self) -> None:
        self.add_arc("crown-left",(8,20),(24,4),radius_x=16,radius_y=16,sweep=True)
        self.add_arc("crown-right",(24,4),(40,20),radius_x=16,radius_y=16,sweep=True)
        self.add_line("temple-right",(40,20),(40,30))
        self.add_arc("cheek-right",(40,30),(36,34),radius_x=4,radius_y=4,sweep=True)
        self.add_line("jaw-right",(36,34),(36,40))
        self.add_arc("jaw-se",(36,40),(32,44),radius_x=4,radius_y=4,sweep=True)
        self.add_line("teeth-bottom-right",(32,44),(28,44))
        self.add_line("teeth-bottom-middle",(28,44),(20,44))
        self.add_line("teeth-bottom-left",(20,44),(16,44))
        self.add_arc("jaw-sw",(16,44),(12,40),radius_x=4,radius_y=4,sweep=True)
        self.add_line("jaw-left",(12,40),(12,34))
        self.add_arc("cheek-left",(12,34),(8,30),radius_x=4,radius_y=4,sweep=True)
        self.add_line("temple-left",(8,30),(8,20))
        self.add_contour("skull","crown-left","crown-right","temple-right","cheek-right","jaw-right","jaw-se","teeth-bottom-right","teeth-bottom-middle","teeth-bottom-left","jaw-sw","jaw-left","cheek-left","temple-left",closed=True)
        for x in (20,28):
            name=f"tooth-divider-{x}"
            self.add_line(name,(x,34),(x,44))
            self.relate("connect",name,"skull")
