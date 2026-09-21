'Diagonal Open-End Spanner.\nSymbol plan: An open-end spanner extends diagonally from a rounded handle at lower left to a broad crescent-shaped jaw at upper right. The forked head has a deep angled opening between its two tips.\nConstruction: Lucide wrench: integrated jaw, diagonal handle and circular heel.\nReduction: \nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '41bd81cf-2446-4283-b6f3-90c7dde89ad1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/socket wrench_41bd81cf-2446-4283-b6f3-90c7dde89ad1.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'diagonal-open-end-spanner'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('spanner', 'wrench', 'tool', 'jaw', 'handle', 'repair')
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
        bez('heel',(6,36),((6,42),(10,42),(14,42)))
        line('handle-right',(14,42),(30,26))
        bez('jaw-right',(30,26),((42,28),(42,18),(42,12)))
        poly('mouth',(42,12),(32,20),(24,12),(32,6))
        bez('jaw-left',(32,6),((20,6),(14,12),(16,22)))
        line('handle-left',(16,22),(6,36))
        con('wrench','heel','handle-right','jaw-right','mouth-1','mouth-2','mouth-3','jaw-left','handle-left',closed=True)
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
