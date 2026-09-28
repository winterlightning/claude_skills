'Right-Facing Head with Curled Breath Lines.\nSymbol plan: A plain head faces right with a projecting nose and a wide open mouth. Two curling breath lines extend outward from the mouth, while the neck descends below the rounded back of the head.\nConstruction: Human full_body_ref.png: circular heads, coherent torso/limbs, exact 8u centerline / 4u ink head-to-neck clearance. Continuous profile neck; no detached-head construction.\nReduction: Two broad breath marks replace tiny curling tips.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bc8b590c-4f02-4ec8-a8d5-4c92ef3b7c1d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/spit_bc8b590c-4f02-4ec8-a8d5-4c92ef3b7c1d.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'right-facing-head-with-curled-breath-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('head', 'breath', 'spit', 'mouth', 'profile', 'person')
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
        bez('head',(6,42),((6,34),(6,28),(6,24)),((6,6),(12,6),(18,6)),((28,6),(28,16),(28,20)))
        poly('nose',(28,20),(30,24),(24,24));bez('mouth',(24,24),((18,24),(18,34),(26,34)))
        line('neck',(20,34),(20,42))
        line('breath-a',(38,24),(42,24));line('breath-b',(36,36),(42,38))
        self.relate('connect','mouth','neck')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
