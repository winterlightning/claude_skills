"""A woman with hair past the chin, a swept parting, and a closed flat bust base. Lucide user-round informs the portrait hierarchy; the reference supplies long hair and the base. Tiny facial details are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '163a9d8d-9ccd-53b0-b145-c50822422f8c'
SOURCE_PATH = 'pictographic-primitives/users/woman half_163a9d8d-9ccd-53b0-b145-c50822422f8c.svg'
AUTHOR = 'gpt-6'


class WomanBustLongHair(Solo48):
    icon_id = 'woman-bust-long-hair'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/users"
    aliases = ()
    keywords = ('woman', 'female', 'bust', 'long hair', 'user', 'avatar', 'profile', 'person')


    def woman_bust(self,closed):
        # Landscape centerline extremes (6,8)-(40,40), shared vertical axis x=24.
        self.add_line('shoulder-left',(8,40),(18,32))
        self.add_line('neck-left',(18,32),(18,28))
        self.add_arc('jaw-left',(18,28),(15,21),radius_x=10)
        if closed:
            self.add_arc('fringe-left',(15,21),(26,18),radius_x=20)
            self.add_line('fringe-right',(26,18),(33,21))
        else:
            self.add_line('fringe-left',(15,21),(24,17))
            self.add_line('fringe-right',(24,17),(33,21))
        self.add_arc('jaw-right',(33,21),(30,28),radius_x=10)
        self.add_line('neck-right',(30,28),(30,32))
        self.add_line('shoulder-right',(30,32),(40,40))
        members=['shoulder-left','neck-left','jaw-left','fringe-left','fringe-right','jaw-right','neck-right','shoulder-right']
        if closed:
            self.add_line('base',(40,40),(8,40));members.append('base')
        self.add_contour('face-and-bust',*members,closed=closed)
        self.add_arc('chin',(18,28),(30,28),radius_x=10,sweep=False)
        self.relate('connect','face-and-bust','chin')
        hair_end=32 if closed else 28
        self.add_line('hair-left',(4,hair_end),(6,20))
        self.add_arc('crown-left',(6,20),(24,8),radius_x=20,radius_y=12)
        self.add_arc('crown-right',(24,8),(42,20),radius_x=20,radius_y=12)
        self.add_line('hair-right',(42,20),(44,hair_end))
        self.add_contour('hair','hair-left','crown-left','crown-right','hair-right')

    def build(self) -> None:
        self.woman_bust(closed=True)
