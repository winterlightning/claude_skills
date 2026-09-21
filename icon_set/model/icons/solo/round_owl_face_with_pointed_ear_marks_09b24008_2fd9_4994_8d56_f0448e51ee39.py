'Round Owl Face with Pointed Ear Marks.\nSymbol plan: A circular owl face contains two large round eyes with small pupils and a pointed beak between them. Two short triangular ear marks sit above the eyes inside the head outline.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Merge the ear marks into the head outline and omit fine pupils, retaining the owl’s pointed ears, paired eyes, and beak.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '09b24008-2fd9-4994-8d56-f0448e51ee39'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/askfm logo_09b24008-2fd9-4994-8d56-f0448e51ee39.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'round-owl-face-with-pointed-ear-marks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('owl', 'face', 'eyes', 'beak', 'bird', 'ears', 'round')
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
        poly('crown',(6,24),(6,6),(18,10),(30,10),(42,6),(42,24))
        arc('jaw',(42,24),(6,24),18)
        con('head',*(f'crown-{i}' for i in range(1,6)),'jaw',closed=True)
        circle('left-eye',17,22,2);circle('right-eye',31,22,2)
        poly('beak',(22,31),(24,33),(26,31))
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
