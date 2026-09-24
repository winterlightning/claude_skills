from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='707a74f4-f696-4ab1-aaf2-6be7de8a3c1a'
SOURCE_PATH='pictographic-primitives/_uncategorized_32/read world_707a74f4-f696-4ab1-aaf2-6be7de8a3c1a.svg'
AUTHOR='gpt-6'
PLAN='Open book below globe dome. Drop page text and latitude to keep globe/open-book arrangement readable; one central meridian.'
CONSTRUCTION_REFERENCE='Lucide book-open paired curved pages and shared spine'
class Drawing(Solo48):
    icon_id='read-world'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('read', 'world')
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,k=4):
        ps=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        ns=[]
        for j,a in enumerate(ps):
            z=ps[(j+1)%8]
            if a==z: continue
            m=f'{n}-{j}'; ns.append(m)
            if j%2:self.add_arc(m,a,z,radius_x=k)
            else:self.add_line(m,a,z)
        self.add_contour(n,*ns,closed=True)
    def cross(self,n,x,y,r):
        ns=[]
        for j,p in enumerate([(x-r,y),(x+r,y),(x,y-r),(x,y+r)]):
            m=f'{n}-{j}';ns.append(m);self.add_line(m,(x,y),p)
        self.relate('connect',*ns)
    def build(self):
        # Symmetric globe hemisphere, open book, shared spine.
        self.add_arc('dome-left',(10,18),(24,4),radius_x=14)
        self.add_arc('dome-right',(24,4),(38,18),radius_x=14)
        self.add_contour('globe','dome-left','dome-right')
        self.add_line('meridian',(24,4),(24,18));self.relate('connect','meridian','globe')
        self.add_bezier('book-top',(8,27),((16,27),(20,28),(24,31)),((28,28),(32,27),(40,27)))
        self.add_line('book-right',(40,27),(40,40))
        self.add_bezier('book-bottom',(40,40),((32,40),(28,41),(24,44)),((20,41),(16,40),(8,40)))
        self.add_line('book-left',(8,40),(8,27))
        self.add_contour('book','book-top','book-right','book-bottom','book-left',closed=True)
        self.add_line('spine',(24,31),(24,44));self.relate('connect','spine','book')
