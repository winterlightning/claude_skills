"""Locomotive front grille; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1261a1dd-5b20-41fe-b8ee-3a27dbda4a58'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad train_1261a1dd-5b20-41fe-b8ee-3a27dbda4a58.svg'
AUTHOR = 'gpt-6'

class LocomotiveFrontGrille(Solo48):
    icon_id = 'locomotive-front-grille'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('locomotive', 'train', 'front', 'railway', 'diesel', 'rail', 'engine', 'transport')

    def build(self) -> None:
        # VRECT_L (8,6)-(40,42). Split windscreen and a central divided grille arch.
        self.add_line('roof-left',(12,6),(24,6))
        self.add_line('roof-right',(24,6),(36,6))
        self.add_arc('top-right',(36,6),(40,8),radius_x=4)
        self.add_line('right-upper',(40,8),(40,18))
        self.add_line('right-middle',(40,18),(40,26))
        self.add_line('right-lower',(40,26),(40,34))
        self.add_arc('bottom-right',(40,34),(36,38),radius_x=4)
        floor=[(36,38),(34,38),(32,38),(24,38),(16,38),(14,38),(12,38)]
        for j,(a,b) in enumerate(zip(floor,floor[1:])):self.add_line('floor-'+str(j),a,b)
        self.add_arc('bottom-left',(12,38),(8,34),radius_x=4)
        self.add_line('left-lower',(8,34),(8,26))
        self.add_line('left-middle',(8,26),(8,18))
        self.add_line('left-upper',(8,18),(8,8))
        self.add_arc('top-left',(8,8),(12,6),radius_x=4)
        self.add_contour('body','roof-left','roof-right','top-right','right-upper','right-middle','right-lower','bottom-right',*[f'floor-{j}' for j in range(6)],'bottom-left','left-lower','left-middle','left-upper','top-left',closed=True)
        self.add_polyline('divider',(8,18),(24,18),(40,18))
        self.add_line('window-post',(24,6),(24,18))
        self.relate('connect','divider','body')
        self.relate('connect','window-post','body')
        self.relate('connect','window-post','divider')
        for name,x,end in [('left',14,8),('right',34,40)]:
            self.add_line(name+'-rail',(x,38),(end,44))
            self.relate('connect',name+'-rail','body')
        self.add_line('left-lamp',(8,26),(10,26))
        self.add_line('right-lamp',(38,26),(40,26))
        self.relate('connect','left-lamp','body')
        self.relate('connect','right-lamp','body')
        self.add_line('grille-left',(16,38),(16,35))
        self.add_arc('grille-upper-left',(16,35),(24,27),radius_x=8)
        self.add_arc('grille-upper-right',(24,27),(32,35),radius_x=8)
        self.add_line('grille-right',(32,35),(32,38))
        self.add_contour('grille','grille-left','grille-upper-left','grille-upper-right','grille-right')
        self.add_line('grille-slat',(24,27),(24,38))
        self.relate('connect','grille','body')
        self.relate('connect','grille-slat','body')
        self.relate('connect','grille-slat','grille')
