from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='ca0b86cd-f823-4251-8d27-7775eddb1f7a'
SOURCE_PATH='pictographic-primitives/other/lock person_ca0b86cd-f823-4251-8d27-7775eddb1f7a.svg'
AUTHOR='gpt-6'
PLAN='Restored a fully closed, rounded lock body and distinct broad shoulders. Circular head center(24,26), radius4; shoulders crest38 gives exactly4 ink clearance from head bottom30. Flat base and person symbol remain separately readable.'
CONSTRUCTION_REFERENCES='Lucide lock original and atomic-debug: rounded shackle. icon_set/references/human_ref/user.svg: circular head and broad symmetric shoulders.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='lock-person'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('lock', 'person')

    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=f'{n}-{i}';members.append(k)
            if kind=='L':self.add_line(k,here,end)
            elif kind=='A':self.add_arc(k,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C':self.add_bezier(k,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

    def build(self):
        # Closed lock; split actual top tangent nodes for exact clearance certification.
        self.add_polyline('top',(12,14),(14,14),(34,14),(36,14))
        self.path('body',(36,14),[('A',(40,18),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(32,44)),('L',(16,44)),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,18)),('A',(12,14),4,4,True)])
        self.relate('connect','top','body')
        self.add_arc('shackle',(14,14),(34,14),radius_x=10);self.relate('connect','shackle','top')
        self.circle('head',24,26,4)
        self.path('shoulders',(16,44),[('A',(24,38),8,6,True),('A',(32,44),8,6,True)])
        self.relate('connect','shoulders','body')
        # Human reference: head bottom30, shoulder crest38. Exact4-unit visible gap.

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': 'afe98f50992bd65c6c04226cc3c6e223097a4ed9a3c5f84dbd71c3a0a274a24c', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': 'ca0b86cd-f823-4251-8d27-7775eddb1f7a'}
