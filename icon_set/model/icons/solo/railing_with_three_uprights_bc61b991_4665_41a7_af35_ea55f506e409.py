'Railing with Three Uprights.\nSymbol plan: A short railing has broad horizontal top and bottom rails with rounded ends. Three straight vertical supports join the rails, evenly dividing the open space between them into adjoining bays.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape HRECT_M: ink extremes (2, 8, 46, 40).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bc61b991-4665-41a7-af35-ea55f506e409'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/railing_bc61b991-4665-41a7-af35-ea55f506e409.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'railing-with-three-uprights'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('railing', 'rail', 'fence', 'balustrade', 'barrier', 'upright')
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
        rect('top',4,10,40,8,2);rect('bottom',4,30,40,8,2)
        for i,x in enumerate((12,24,36)):
         line('post'+str(i),(x,18),(x,30));self.relate('connect','post'+str(i),'top');self.relate('connect','post'+str(i),'bottom')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
