"Person Sprinting Fast.\nSymbol plan: One motion stroke replaces the pair; vertical upper neck bends into the forward-running torso.\nConstruction: human_ref/full_body_ref.png: circular heads and coherent limbs; Lucide object construction where relevant.\nKeyshape SQUARE: exact SOLO48 contract envelope, selected for this subject's proportions.\nSource UUID and original reference preserved."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '28c92329-3d76-4a8d-b49a-3e58b083b7b0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/athletics running_28c92329-3d76-4a8d-b49a-3e58b083b7b0.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'sprinter-with-trailing-motion-marks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('runner', 'sprinter', 'athlete', 'running', 'motion', 'sport', 'person')
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
        circle('head',31,11,5)
        line('torso',(31,24),(31,27));line('back',(31,27),(22,34))
        poly('arm',(31,24),(40,28),(42,24));poly('reararm',(31,24),(18,24),(12,18))
        poly('frontleg',(22,34),(33,37),(29,42));poly('rearleg',(22,34),(15,42),(6,42))
        line('motion',(6,30),(9,30))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
