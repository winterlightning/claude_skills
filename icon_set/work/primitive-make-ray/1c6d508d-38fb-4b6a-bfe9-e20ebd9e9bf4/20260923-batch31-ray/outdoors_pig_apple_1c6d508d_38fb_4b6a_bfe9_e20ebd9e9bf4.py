from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4'
SOURCE_PATH = 'icon_set/work/todo-references/outdoors pig apple_1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4.svg'
AUTHOR = 'gpt-6'
PLAN = 'A pig snout reaches toward an apple poster; asymmetry preserves the scene.'
OMISSIONS = 'Eye and tiny ear folds omitted.'
LUCIDE_REFERENCE = None

class Drawing(Solo48):
    icon_id = 'outdoors-pig-apple'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('outdoors', 'pig', 'apple')
    # Pantyhose anatomy reference: icon_set/references/human_ref/full_body_ref.png; no detached head.

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
        # Symbol plan: A pig snout reaches toward an apple poster; asymmetry preserves the scene.

        self.add_polyline('poster',(24,17),(24,6),(42,6),(42,42),(24,42),(24,34))
        self.add_bezier('pig',(6,18),((6,11),(12,13),(14,21)),((18,22),(19,26),(24,26)),((27,26),(27,33),(22,33)),((15,34),(12,37),(8,42)))
        self.add_bezier('apple',(33,23),((23,16),(26,34),(33,32)),((40,34),(43,16),(33,23)))
        self.add_line('stem',(33,23),(35,17))
        self.relate('connect','stem','apple')

