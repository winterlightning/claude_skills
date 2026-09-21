'Long Jumper Above a Ground Line.\nSymbol plan: A round-headed athlete stretches into a leap with one leg extended forward and the other folded beneath the body. Two short motion marks trail behind above a separate horizontal ground line.\nConstruction: Human full_body_ref.png: circular heads, coherent torso/limbs, exact 8u centerline / 4u ink head-to-neck clearance.\nReduction: Omit motion ticks; bent rear leg, extended front leg and detached ground retain the jump.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f66d874-f536-41dd-bfae-be8151d586ac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/athletics long jumping_6f66d874-f536-41dd-bfae-be8151d586ac.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'long-jumper-above-a-ground-line'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('jumper', 'long jump', 'athlete', 'leap', 'sport', 'motion', 'person')
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
        circle('head',26,10,4);line('torso',(26,22),(26,24));line('lower-torso',(26,24),(22,30))
        line('arms',(8,22),(38,22));self.relate('connect','arms','torso')
        poly('legs',(22,30),(30,34),(38,34));poly('back-leg',(22,30),(18,34),(12,34));line('ground',(6,42),(42,42));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
