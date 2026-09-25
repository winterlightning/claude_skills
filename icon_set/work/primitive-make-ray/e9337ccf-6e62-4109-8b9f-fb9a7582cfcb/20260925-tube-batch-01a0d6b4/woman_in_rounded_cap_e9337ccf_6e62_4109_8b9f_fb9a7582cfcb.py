from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='e9337ccf-6e62-4109-8b9f-fb9a7582cfcb'
SOURCE_PATH='pictographic-primitives/avatars/detective woman_e9337ccf-6e62-4109-8b9f-fb9a7582cfcb.svg'
AUTHOR='gpt-6'
PLAN='Restore the reference rounded cap and curved visor, circular lower face, flipped bob hair and V-neck shoulders.'
CONSTRUCTION_REFERENCES='Lucide hat-glasses: separate crown and brim construction; human_ref/user.svg owns round jaw and shoulder vocabulary.'
OMISSIONS=['Upper visor seam omitted; small closed hair wedges reduced to open curved flips.']
class Drawing(Solo48):
    icon_id='woman-in-rounded-cap'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('detective', 'woman')

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
    def ellipse(self,n,x,y,rx,ry):
        self.path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
    def box(self,n,l,t,r,b,k=4,split=False):
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        ids=[]
        for i,a in enumerate(pts):
            ident=f'{n}-{i}';ids.append(ident);z=pts[(i+1)%8]
            if i%2:self.add_arc(ident,a,z,radius_x=k)
            else:self.add_line(ident,a,z)
        if split:
            for i in range(8):self.relate('connect',ids[i],ids[(i+1)%8])
        else:self.add_contour(n,*ids,closed=True)

    def build(self):
        # Jaw circle center (24,18), r12. Collar endpoints (12,34)/(36,34)
        # are exactly 20 from its center: 12-16-20 triangle, 8 centerline/4 ink gap.
        self.path('crown',(12,16),[('A',(24,4),12,12,True),('A',(36,16),12,12,True)])
        self.path('visor',(12,16),[('C',(36,16),(18,20),(30,20))])
        self.path('jaw',(12,16),[('L',(12,18)),('A',(24,30),12,12,False),('A',(36,18),12,12,False),('L',(36,16))])
        for side in (-1,1):
            p=lambda x,y:(x,y) if side==-1 else (48-x,y)
            n='hair'+str(side)
            self.path(n,p(12,18),[('C',p(8,26),p(12,22),p(10,26))])
            self.relate('connect',n,'jaw')
        self.path('left-shoulder',(8,44),[('C',(12,34),(8,38),(8,34))])
        self.add_polyline('collar',(12,34),(24,44),(36,34))
        self.path('right-shoulder',(36,34),[('C',(40,44),(40,34),(40,38))])
        self.relate('connect','left-shoulder','collar');self.relate('connect','right-shoulder','collar')
        self.relate('connect','crown','visor');self.relate('connect','visor','jaw');self.relate('connect','crown','jaw')

HUMAN_CONSTRUCTION_REVIEW = {'reference': 'icon_set/references/human_ref/user.svg', 'jaw_center': [24, 18], 'jaw_radius': 12, 'body_nearest_points': [[12, 34], [36, 34]], 'head_to_body_ink_gap': 4, 'proof': 'sqrt(12^2+16^2)-12-4=4. Nearest jaw points are (16.8,27.6) and (31.2,27.6). Shoulder curves approach these endpoints from outside the offset circle; each collar line moves away from it. The checker reports review for the curved pair, not a strict pass.'}

USER_APPROVED_EXCEPTION = {'approved_by': 'user', 'approved_on': '2026-09-25', 'source_request': 'other unresolve could make as eception', 'recording': 'Local exception under the earlier session instruction; raw QA remains unchanged and this is not a strict pass.', 'svg_sha256': '36ccb648c1a80e29a38e56bf3d603e601fb7649b1286c0fe64a215905eede11a', 'reason': 'The exact four-unit head/body ink gap is proved analytically, but the checker cannot certify the diagonal arc/shoulder minimum.', 'scope': ['jaw/left-shoulder curved-distance review; reported 8.00043 centerline distance.'], 'analytical_proof': {'reference': 'icon_set/references/human_ref/user.svg', 'jaw_center': [24, 18], 'jaw_radius': 12, 'body_nearest_points': [[12, 34], [36, 34]], 'head_to_body_ink_gap': 4, 'proof': 'sqrt(12^2+16^2)-12-4=4. Nearest jaw points are (16.8,27.6) and (31.2,27.6). Shoulder curves approach these endpoints from outside the offset circle; each collar line moves away from it. The checker reports review for the curved pair, not a strict pass.'}}
