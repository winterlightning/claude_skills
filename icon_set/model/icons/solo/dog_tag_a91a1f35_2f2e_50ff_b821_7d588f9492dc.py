"""Blank pet identification tag with suspension loop. Centerlines (11,2)-(37,46). Lucide tag supplies rounded corners; one legible ring replaces nested rings."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a91a1f35-2f2e-50ff-b821-7d588f9492dc'
SOURCE_PATH = 'pictographic-primitives/animals/dog tag_a91a1f35-2f2e-50ff-b821-7d588f9492dc.svg'
AUTHOR = 'gpt-6'


class PetIdTag(Solo48):
    icon_id = 'pet-id-tag'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/pets'
    aliases = ()
    keywords = ('dog tag', 'pet', 'id', 'tag', 'collar', 'identification', 'label', 'name')

    def build(self) -> None:
        self.add_arc('loop-left',(24,2),(18,8),radius_x=6,sweep=False)
        self.add_arc('loop-bottom',(18,8),(24,14),radius_x=6,sweep=False)
        self.add_arc('loop-right',(24,14),(30,8),radius_x=6,sweep=False)
        self.add_arc('loop-top',(30,8),(24,2),radius_x=6,sweep=False)
        self.add_contour('loop','loop-left','loop-bottom','loop-right','loop-top',closed=True)
        self.add_line('plate-top-left',(18,14),(24,14))
        self.add_line('plate-top-right',(24,14),(30,14))
        self.add_arc('plate-tr',(30,14),(37,21),radius_x=7)
        self.add_line('plate-right',(37,21),(37,39))
        self.add_arc('plate-br',(37,39),(30,46),radius_x=7)
        self.add_line('plate-bottom',(30,46),(18,46))
        self.add_arc('plate-bl',(18,46),(11,39),radius_x=7)
        self.add_line('plate-left',(11,39),(11,21))
        self.add_arc('plate-tl',(11,21),(18,14),radius_x=7)
        self.add_contour('plate','plate-top-left','plate-top-right','plate-tr','plate-right','plate-br','plate-bottom','plate-bl','plate-left','plate-tl',closed=True)
        self.relate('connect','plate','loop')
