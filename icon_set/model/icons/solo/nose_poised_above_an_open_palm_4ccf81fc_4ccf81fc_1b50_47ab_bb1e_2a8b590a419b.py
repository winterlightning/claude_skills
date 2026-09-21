'Nose Poised Above an Open Palm.\nSymbol plan: A large nose appears in side profile above an upward-facing hand. The hand extends from a rectangular cuff on the left, with a curved palm and raised fingertip pointing right.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Omit tiny finger and nostril details while retaining the nose and upturned palm.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4ccf81fc-1b50-47ab-bb1e-2a8b590a419b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baby family slime play dough 2_4ccf81fc-1b50-47ab-bb1e-2a8b590a419b.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'nose-poised-above-an-open-palm-4ccf81fc'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('nose', 'hand', 'palm', 'smell', 'scent', 'profile', 'senses')
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
        poly('nose',(24,6),(18,18),(24,20),(30,18))
        rect('cuff',6,30,8,12)
        bez('palm',(14,40),((28,44),(34,42),(42,30)),((39,27),(32,32),(28,32)))
        line('hand',(14,30),(28,32));self.relate('connect','palm','cuff');self.relate('connect','hand','cuff')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
