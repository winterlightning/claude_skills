"""A long-haired woman under an elliptical halo. Keep halo, hair and blank face; drop garment folds to preserve open spaces."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51d30682-39f9-5a08-95aa-4743470a5b0c'
SOURCE_PATH = 'pictographic-primitives/religion/female_51d30682-39f9-5a08-95aa-4743470a5b0c.svg'
AUTHOR = 'gpt-6'


class WomanWithHalo(Solo48):
    icon_id = 'woman-with-halo'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    categories = ("primitives", "religion")
    aliases = ()
    keywords = ('woman', 'halo', 'portrait', 'hair', 'holy', 'figure')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Shared axis x=24, live VRECT centerline box (8,4)-(40,44).
        self.oval('halo',24,8,16,4)
        self.add_arc('face',(17,21),(31,21),radius_x=7,radius_y=10,sweep=False)
        self.add_line('fringe',(17,21),(31,21))
        self.relate('connect','face','fringe')
        for side in (-1,1):
            self.add_line('hair-'+str(side),(24+side*16,21),(24+side*16,31))
        self.add_arc('shoulders',(8,44),(40,44),radius_x=16,radius_y=4)
