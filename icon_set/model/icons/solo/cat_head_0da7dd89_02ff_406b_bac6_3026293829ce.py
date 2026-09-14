'Cat face: matched ears, curved cheeks, symmetric eyes and a small connected muzzle. Lucide cat informs the expressive silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0da7dd89-02ff-406b-bac6-3026293829ce'
SOURCE_PATH = 'icons-json/pets/cat head_0da7dd89-02ff-406b-bac6-3026293829ce.json'
AUTHOR = 'gpt-6'

class CatHead(Solo48):
    icon_id = 'cat-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('cat', 'head', 'pets')

    def build(self) -> None:
        # Square envelope. Ear tips are deliberate corners; cheeks and chin stay smooth.
        self.add_bezier('forehead',(18,13),((22,11),(26,11),(30,13)))
        self.add_bezier('ear-right',(30,13),((34,9),(37,6),(40,6)),((42,10),(41,17),(40,20)))
        self.add_bezier('cheek-right',(40,20),((41,22),(42,24),(42,27)),((42,36),(34,42),(24,42)))
        self.add_bezier('cheek-left',(24,42),((14,42),(6,36),(6,27)),((6,24),(7,22),(8,20)))
        self.add_bezier('ear-left',(8,20),((7,17),(6,10),(8,6)),((11,6),(14,9),(18,13)))
        self.add_contour('head','forehead','ear-right','cheek-right','cheek-left','ear-left',closed=True)
        for x in (16,32): self.add_dot('eye-'+str(x),(x,22))
        self.add_arc('mouth-left',(18,30),(24,30),radius_x=3,radius_y=2,sweep=False)
        self.add_arc('mouth-right',(24,30),(30,30),radius_x=3,radius_y=2,sweep=False)
        self.add_contour('mouth','mouth-left','mouth-right')
        self.add_line('nose',(24,28),(24,30))
        self.relate('connect','nose','mouth')
