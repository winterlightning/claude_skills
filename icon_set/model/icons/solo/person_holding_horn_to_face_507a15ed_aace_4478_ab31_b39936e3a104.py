'Person Holding Horn to Face.\nSymbol plan: A person kneels with one leg raised while holding a flared horn toward the upper left. The rounded head sits behind a bent arm that supports the narrow mouthpiece.\nConstruction: Human full_body_ref.png: circular heads, coherent torso/limbs, exact 8u centerline / 4u ink head-to-neck clearance. Lucide megaphone: flared mouth and narrow end.\nReduction: Keep flared horn, bent arm and kneeling legs.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '507a15ed-aace-4478-ab31-b39936e3a104'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blow instrument_507a15ed-aace-4478-ab31-b39936e3a104.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'person-holding-horn-to-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('person', 'horn', 'megaphone', 'kneeling', 'announcement', 'figure', 'calling')
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
        circle('head',36,12,6);line('torso',(36,26),(36,34));poly('legs',(36,42),(36,34),(20,34),(20,42),(10,42))
        poly('arm',(36,26),(20,26),(16,18))
        poly('horn',(6,6),(20,12),(18,20),(6,18),closed=True)
        self.relate('connect','arm','horn');self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
