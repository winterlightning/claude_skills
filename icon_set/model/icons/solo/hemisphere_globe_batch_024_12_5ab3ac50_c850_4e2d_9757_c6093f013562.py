from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='5ab3ac50-c850-4e2d-9757-c6093f013562'
SOURCE_PATH='pictographic-primitives/other/half globe_5ab3ac50-c850-4e2d-9757-c6093f013562.svg'
AUTHOR='gpt-6'
PLAN='True semicircular half globe, flat right cut, equator and curved meridian. Preserve the source half-circle aspect rather than the previous widened half ellipse.'
CONSTRUCTION_REFERENCES='Lucide globe: circular graticule; supplied half-globe silhouette owns the vertical cut.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='hemisphere-globe-grid'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('half', 'globe')

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
        self.path('outer',(34,4),[('A',(14,24),20,20,False),('A',(34,44),20,20,False),('L',(34,24)),('L',(34,4))],True)
        self.path('meridian',(34,4),[('A',(26,24),8,20,False),('A',(34,44),8,20,False)])
        self.add_polyline('equator',(14,24),(26,24),(34,24))
        for a,b in [('outer','meridian'),('outer','equator'),('meridian','equator')]:self.relate('connect',a,b)

    icon_id = 'hemisphere-globe-batch-024-12'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hemisphere', 'globe')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    exception = {'approved_by': 'user', 'approved_on': '2026-09-25', 'source_request': 'other unresolve could make as eception', 'reason': 'Preserve the true semicircular half-globe instead of stretching it into a half ellipse.', 'scope': ['Exact VRECT_M horizontal envelope only: actual ink (12,2,36,46), required (8,2,40,46).'], 'svg_sha256': '0a1fc542ae20007033507b7625cd7a44f893b1771a7402b9bceadff9aee0c6cc', 'recording': 'Local SOLO48 exception under the earlier session instruction; automatic QA remains fail. This is not a strict validation pass.', 'source_svg_sha256': '8a90f84047895966f0f86006b17eccf7af2f2a3d34a9404e00cbdeb01db53f9a'}

USER_APPROVED_EXCEPTION = {'approved_by': 'user', 'approved_on': '2026-09-25', 'source_request': 'other unresolve could make as eception', 'reason': 'Preserve the true semicircular half-globe instead of stretching it into a half ellipse.', 'scope': ['Exact VRECT_M horizontal envelope only: actual ink (12,2,36,46), required (8,2,40,46).'], 'svg_sha256': '8a90f84047895966f0f86006b17eccf7af2f2a3d34a9404e00cbdeb01db53f9a', 'recording': 'Local SOLO48 exception under the earlier session instruction; automatic QA remains fail. This is not a strict validation pass.'}
