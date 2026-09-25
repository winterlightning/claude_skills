'Person beside Two Ball Snowman.\nSymbol plan: A person stands to the right of a snowman formed from two stacked circles. One arm extends toward the snowman, whose left side carries a short angled stick arm.\nConstruction: Human full_body_ref.png: circular heads, coherent torso/limbs, exact 8u centerline / 4u ink head-to-neck clearance.\nReduction: Two broad joined snowballs retain a visible waist; omit its small stick arm.\nKeyshape HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '47428121-76fd-443d-8ee2-ab1ad5fe0dda'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/build snowman_47428121-76fd-443d-8ee2-ab1ad5fe0dda.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'person-beside-two-ball-snowman'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('snowman', 'person', 'winter', 'snow', 'building', 'play', 'scene')
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
        bez('neck-left',(10,22),((6,20),(6,18),(6,16)))
        arc('head-left',(6,16),(14,8),8);arc('head-right',(14,8),(22,16),8)
        bez('neck-right',(22,16),((22,18),(22,20),(18,22)))
        bez('body-right',(18,22),((22,24),(24,26),(24,30)),((24,36),(20,40),(14,40)))
        bez('body-left',(14,40),((8,40),(4,36),(4,30)),((4,26),(6,24),(10,22)))
        con('snowman','neck-left','head-left','head-right','neck-right','body-right','body-left',closed=True)
        circle('head',36,12,4);line('torso',(36,24),(36,32));poly('arms',(32,24),(36,24),(44,28));poly('legs',(30,40),(36,32),(42,40));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start');self.relate('connect','arms','torso')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
