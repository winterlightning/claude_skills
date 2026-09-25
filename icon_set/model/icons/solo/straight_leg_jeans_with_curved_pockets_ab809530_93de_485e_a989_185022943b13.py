'Straight Leg Jeans with Curved Pockets.\nSymbol plan: A pair of jeans faces forward beneath a wide horizontal waistband. Curved pocket openings sit at either hip, with a central fly above two straight legs separated by a tapered gap.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Omit narrow fly seam; retain both curved pockets.\nKeyshape VRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ab809530-93de-485e-a989-185022943b13'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/denim_ab809530-93de-485e-a989-185022943b13.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'straight-leg-jeans-with-curved-pockets'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('jeans', 'denim', 'trousers', 'pants', 'pockets', 'clothing', 'waistband')
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
        poly('pants',(12,4),(36,4),(40,44),(28,44),(24,24),(20,44),(8,44),closed=True)
        line('waist',(11,12),(37,12))
        arc('pocket-left',(20,12),(11,21),9);arc('pocket-right',(37,21),(28,12),9)
        self.relate('connect','waist','pants');self.relate('connect','pocket-left','waist');self.relate('connect','pocket-left','pants');self.relate('connect','pocket-right','waist');self.relate('connect','pocket-right','pants')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
