"""outdoors dog house: standalone SOLO48 repair.
Plan: Dog in side profile under an open sloping shelter.
Keyshape: SQUARE; shared dimensions and nodes own repeated elements.
Reduction: Rebalanced the roof, head and muzzle; retained two open leg strokes. Belly, far legs, tiny eye and tail omitted.
Lucide originals and atomic-debug construction reference: house.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '176149f5-709e-4aea-827c-9e372966aa1a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_29/outdoors dog house_176149f5-709e-4aea-827c-9e372966aa1a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'outdoors-dog-house'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('outdoors', 'dog', 'house')

    def circle(self, n, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(n+'-a', (x-r,y), (x+r,y), radius_x=r, radius_y=ry)
        self.add_arc(n+'-b', (x+r,y), (x-r,y), radius_x=r, radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=3):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for j,a in enumerate(points):
            b=points[(j+1)%8];name=f'{n}-{j}';names.append(name)
            if j%2: self.add_arc(name,a,b,radius_x=r)
            else: self.add_line(name,a,b)
        self.add_contour(n,*names,closed=True)

    def p(self,n,x,y,w,h):
        # Open P stem and a tangent semicircular bowl share the upper node.
        self.add_line(n+'-stem-1',(x,y+h),(x,y))
        self.add_line(n+'-stem-2',(x,y),(x+w//2,y))
        self.add_arc(n+'-bowl',(x+w//2,y),(x+w//2,y+h//2),radius_x=w//2,radius_y=h//4)
        self.add_line(n+'-return',(x+w//2,y+h//2),(x,y+h//2))
        self.add_contour(n,n+'-stem-1',n+'-stem-2',n+'-bowl',n+'-return')

    def build(self):
        # Symbol plan: Dog standing under an open sloped kennel roof; intentional side profile.

        self.add_polyline('kennel',(42,6),(6,12),(6,42),(42,42))
        self.add_polyline('dog',(14,34),(14,25),(18,22),(26,22),(32,16),(34,18),(42,20),(38,28),(30,28),(28,34))
        # Open lower silhouette retains the two leg ends.

