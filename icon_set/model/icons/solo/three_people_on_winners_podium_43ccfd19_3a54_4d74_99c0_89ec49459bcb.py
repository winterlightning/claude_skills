'Three People on Winners Podium.\nSymbol plan: Three simplified people stand behind a stepped winners podium, with the central figure raised highest. Each has a rounded head and curved shoulders, while the podium has a wide base and a tall middle step.\nConstruction: Human full_body_ref.png: three circular heads with exact 8u torso gaps.\nReduction: Simple narrow body strokes keep all three ranked figures visible.\nKeyshape HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '43ccfd19-3a54-4d74-99c0-89ec49459bcb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/ranking people first_43ccfd19-3a54-4d74-99c0-89ec49459bcb.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'three-people-on-winners-podium'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('podium', 'people', 'winner', 'ranking', 'competition', 'award')
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
        for i,(x,y) in enumerate(((7,17),(24,11),(41,17))):
         circle('head'+str(i),x,y,3);line('torso'+str(i),(x,y+11),(x,32 if i!=1 else 26));self.mark_human_figure('person'+str(i),head='head'+str(i),torso='torso'+str(i),torso_junction='start')
        poly('podium',(4,32),(17,32),(17,26),(31,26),(31,32),(44,32),(44,40),(4,40),closed=True)
        for i in range(3):self.relate('connect','torso'+str(i),'podium')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
