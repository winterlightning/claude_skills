"""tv: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dfe4f7a-b750-45e7-ad95-2237e3f60595'
SOURCE_PATH = 'pictographic-primitives/tv/tv_8dfe4f7a-b750-45e7-ad95-2237e3f60595.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class Tv(Solo48):
    icon_id = 'tv'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tv'
    categories = ('tv', 'primitives')
    aliases = ()
    keywords = ('tv',)

    def build(self):
        # VRECT_L (8,4)-(40,44); same corner radius and mirrored feet.
        # Construction reference: Lucide tv: rounded screen and paired antenna
        def rounded_box(name, left, top, right, bottom, radius):
            points=[(left+radius,top),(right-radius,top),(right,top+radius),(right,bottom-radius),(right-radius,bottom),(left+radius,bottom),(left,bottom-radius),(left,top+radius)]
            members=[]
            for i,start in enumerate(points):
                end=points[(i+1)%8]; member=f'{name}-{i}';members.append(member)
                if i%2: self.add_arc(member,start,end,radius_x=radius)
                else: self.add_line(member,start,end)
            self.add_contour(name,*members,closed=True)

        rounded_box('screen',8,12,40,38,5)
        self.add_polyline('antenna',(16,4),(24,12),(32,4))
        self.add_line('left-foot',(16,38),(13,44))
        self.add_line('right-foot',(32,38),(35,44))
        for member in ['antenna','left-foot','right-foot']:self.relate('connect','screen',member)
