from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3e8bfa80-059e-487c-bda0-70b3d4ddf001'
SOURCE_PATH = 'icon_set/work/todo-references/roleplay game poisonous dagger knife_3e8bfa80-059e-487c-bda0-70b3d4ddf001.svg'
AUTHOR = 'gpt-6'
# Construction plan: Diagonal dagger with poison droplet and an open-neck vial at lower right.
# Reference reduction: Omitted blade bevel; preserved blade, guard, grip, droplet and vial.
# Construction references: ['wand-sparkles']

class AuthoredIcon(Solo48):
    icon_id = 'roleplay-game-poisonous-dagger-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('roleplay', 'game', 'poisonous', 'dagger', 'knife')

    def build(self):
        self.add_polyline('blade',(14,28),(36,6),(33,19),(22,34))
        self.add_line('guard',(10,24),(26,40))
        self.add_polyline('grip',(14,28),(6,36),(6,42),(12,42),(20,34))
        self.relate('connect','blade','guard');self.relate('connect','grip','guard');self.relate('connect','blade','grip')
        self.add_bezier('drop',(40,17),((36,22),(36,26),(40,26)),((44,26),(44,22),(40,17)))
        self.add_bezier('vial',(32,42),((32,39),(28,38),(28,34)),((28,27),(42,27),(42,34)),((42,38),(38,39),(38,42)))

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def box(self, name, l, t, r, b, radius=3):
        q=radius
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{name}-{k}'; ids.append(ident)
            a,z=pts[k],pts[(k+1)%8]
            if k%2: self.add_arc(ident,a,z,radius_x=q)
            else: self.add_line(ident,a,z)
        self.add_contour(name,*ids,closed=True)

    def heart(self, name, cx, top, half, bottom):
        # Mirrored lobes and tangent downward shoulders share one outline.
        l=cx-half; r=cx+half; y=top+half//2
        self.add_bezier(name,(cx,top+3),
            ((cx-half//2,top-3),(l,top),(l,y)),
            ((l,y+4),(cx-half//2,bottom-4),(cx,bottom)),
            ((cx+half//2,bottom-4),(r,y+4),(r,y)),
            ((r,top),(cx+half//2,top-3),(cx,top+3)))
