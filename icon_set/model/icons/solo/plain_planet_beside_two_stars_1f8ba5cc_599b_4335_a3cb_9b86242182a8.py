"Planet and Sparkling Stars.\nSymbol plan: Two open sparkle crosses replace the closed diamond star; globe remains dominant.\nConstruction: Lucide original and atomic-debug: bath, truck, notebook, piano, orbit, sprout and pill-bottle; coherent arcs, shared joins and repeated dimensions.\nKeyshape HRECT_L: exact SOLO48 contract envelope, selected for this subject's proportions.\nSource UUID and original reference preserved."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1f8ba5cc-599b-4335-a3cb-9b86242182a8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/astronomy planet ring star_1f8ba5cc-599b-4335-a3cb-9b86242182a8.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'plain-planet-beside-two-stars'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('planet', 'stars', 'space', 'sparkle', 'astronomy', 'circle', 'sky')
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
        circle('planet',16,24,12)
        poly('star-top',(40,8),(40,16));line('cross',(36,12),(44,12));self.relate('connect','star-top','cross')
        line('star-bottom',(40,32),(40,40));line('cross2',(36,36),(44,36));self.relate('connect','star-bottom','cross2')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
