'Mimosa Branch with Berries and Pointed Leaves.\nSymbol plan: A branching mimosa sprig carries several round berries on the left and pointed leaves on the right. Thin angled stems join the fruit and leaves to a long central branch.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Reduce to three berries and two leaves, retaining the asymmetric sprig.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8e40565d-c7b2-4420-8d5b-1b493254eb23'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mimosa_8e40565d-c7b2-4420-8d5b-1b493254eb23.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'mimosa-branch-with-berries-and-pointed-leaves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('mimosa', 'branch', 'berries', 'leaves', 'plant', 'sprig', 'botanical')
    def build(self):



        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry,sweep=s)
        def bez(n,a,*s): self.add_bezier(n,a,*s)
        def con(n,*p,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members)&set(p)]
            self.add_contour(n,*p,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            con(n,n+'a',n+'b',closed=True)
        def rect(n,x,y,w,h,r=0):
            if not r: poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True);return
            ps=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for j in range(8):
                if j%2: arc(n+str(j),ps[j],ps[(j+1)%8],r)
                else: line(n+str(j),ps[j],ps[(j+1)%8])
            con(n,*(n+str(j) for j in range(8)),closed=True)
        poly('stem',(24,42),(20,36),(20,8))
        for i,y in enumerate((8,24,40)):
         circle('berry'+str(i),8,y,2)
         line('twig'+str(i),(10,y),(20,y if i!=2 else 36));self.relate('connect','twig'+str(i),'berry'+str(i));self.relate('connect','twig'+str(i),'stem')
        bez('leaf-top',(30,20),((30,8),(36,6),(42,6)),((42,18),(38,20),(30,20)))
        bez('leaf-bottom',(30,40),((30,30),(36,28),(42,28)),((42,40),(38,42),(30,40)))
        line('top-branch',(20,20),(30,20));line('bottom-branch',(20,36),(30,40))
        self.relate('connect','top-branch','stem');self.relate('connect','bottom-branch','stem')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
