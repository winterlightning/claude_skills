from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c2caf72a-e028-4b0f-9d4f-ea1a841b97bb'
SOURCE_PATH = 'icon_set/work/todo-references/paragraph image right_c2caf72a-e028-4b0f-9d4f-ea1a841b97bb.svg'
AUTHOR = 'gpt-6'
PLAN = 'Text document with a small image aligned at the upper right.'
OMISSIONS = 'Four text rows reduced to three.'
LUCIDE_REFERENCE = 'image'

class Drawing(Solo48):
    icon_id = 'paragraph-image-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('paragraph', 'image', 'right')
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
        # Symbol plan: Text document with a small image aligned at the upper right.

        self.box('frame',6,6,36,36,4)
        self.box('image',25,15,8,9,2)
        self.add_line('short',(15,20),(17,20))
        self.add_line('row',(15,33),(33,33))

