'Pet ID tag: round attachment loop above a smoothly rounded plate with exact VRECT_L dimensions.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a91a1f35-2f2e-50ff-b821-7d588f9492dc'
SOURCE_PATH = 'pictographic-primitives/animals/dog tag_a91a1f35-2f2e-50ff-b821-7d588f9492dc.svg'
AUTHOR = 'gpt-6'


class PetIdTag(Solo48):
    icon_id = 'pet-id-tag'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/pets'
    aliases = ()
    keywords = ('dog tag', 'pet', 'id', 'tag', 'collar', 'identification', 'label', 'name')

    def build(self) -> None:
        self.add_arc('loop-top', (19,9), (29,9), radius_x=5, radius_y=5)
        self.add_arc('loop-bottom', (29,9), (19,9), radius_x=5, radius_y=5)
        self.add_contour('loop', 'loop-top', 'loop-bottom', closed=True)

        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 8, 14, 40, 44, 7
        self.add_line('plate-top', (left+radius,top), (right-radius,top))
        self.add_arc('plate-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('plate-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('plate-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('plate-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('plate-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('plate-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('plate-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('plate', *('plate-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)
        self.relate('connect','plate','loop')
