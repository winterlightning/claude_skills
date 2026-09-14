"""A front-facing woman with a center-parted fringe, a defined neck, and open sloping shoulders. Lucide user-round informs the portrait hierarchy; the reference supplies the hair and open base. Tiny facial details are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '502e497c-5b3c-40a4-a052-442908922554'
SOURCE_PATH = 'pictographic-primitives/users/woman actions_502e497c-5b3c-40a4-a052-442908922554.svg'
AUTHOR = 'gpt-6'


class WomanBust(Solo48):
    icon_id = 'woman-bust'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/users"
    aliases = ()
    keywords = ('woman', 'female', 'bust', 'user', 'avatar', 'profile', 'person', 'account')


    def woman_bust(self,closed):
        # Landscape centerline extremes (6,8)-(42,40), shared vertical axis x=24.
        self.add_line('shoulder-left',(6,40),(18,30))
        self.add_line('neck-left',(18,30),(18,28))
        self.add_arc('jaw-left',(18,28),(14,20),radius_x=10)
        if closed:
            self.add_arc('fringe-left',(14,20),(26,18),radius_x=20)
            self.add_line('fringe-right',(26,18),(34,20))
        else:
            self.add_line('fringe-left',(14,20),(24,17))
            self.add_line('fringe-right',(24,17),(34,20))
        self.add_arc('jaw-right',(34,20),(30,28),radius_x=10)
        self.add_line('neck-right',(30,28),(30,30))
        self.add_line('shoulder-right',(30,30),(42,40))
        members=['shoulder-left','neck-left','jaw-left','fringe-left','fringe-right','jaw-right','neck-right','shoulder-right']
        if closed:
            self.add_line('base',(42,40),(6,40));members.append('base')
        self.add_contour('face-and-bust',*members,closed=closed)
        self.add_arc('chin',(18,28),(30,28),radius_x=10,sweep=False)
        self.relate('connect','face-and-bust','chin')
        hair_end=30 if closed else 28
        self.add_line('hair-left',(4,hair_end),(6,20))
        self.add_arc('crown-left',(6,20),(24,8),radius_x=20,radius_y=12)
        self.add_arc('crown-right',(24,8),(42,20),radius_x=20,radius_y=12)
        self.add_line('hair-right',(42,20),(44,hair_end))
        self.add_contour('hair','hair-left','crown-left','crown-right','hair-right')

    def build(self) -> None:
        self.woman_bust(closed=False)
