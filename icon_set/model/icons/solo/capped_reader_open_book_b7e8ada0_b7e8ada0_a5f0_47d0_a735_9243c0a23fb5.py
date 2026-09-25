'Capped Reader with Open Book.\nSymbol plan: A front-facing reader wears a rounded cap and a plain garment with a short central neckline. An open book spreads across the chest, its curved upper edges meeting at a central fold.\nConstruction: human_ref/user.svg and Lucide book-open: circular face, broad shoulders and central book spine.\nReduction: Book occupies the lower bust; reduce small cap details.\nKeyshape VRECT_L: ink extremes (6, 2, 42, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b7e8ada0-a5f0-47d0-a735-9243c0a23fb5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/muslim reading quraan 3_b7e8ada0-a5f0-47d0-a735-9243c0a23fb5.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'capped-reader-open-book-b7e8ada0'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = "Uncategorized"
    aliases = ()
    keywords = ('reader', 'cap', 'book', 'person', 'reading', 'garment')
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
        circle('head',24,12,8)
        arc('shoulder-left',(8,32),(24,24),16,8)
        arc('shoulder-right',(24,24),(40,32),16,8)
        poly('book',(8,32),(24,36),(40,32),(40,44),(24,44),(8,44),(8,32))
        line('spine',(24,36),(24,44))
        line('cap',(16,12),(32,12))
        self.relate('connect','cap','head');self.relate('connect','head','shoulder-left');self.relate('connect','head','shoulder-right')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
