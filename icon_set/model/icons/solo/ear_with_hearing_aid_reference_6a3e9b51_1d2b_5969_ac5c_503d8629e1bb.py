from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='6a3e9b51-1d2b-5969-ac5c-503d8629e1bb'
SOURCE_PATH='pictographic-primitives/health/hearing aid ear_6a3e9b51-1d2b-5969-ac5c-503d8629e1bb.svg'
AUTHOR='gpt-6'
PLAN='Organic outer ear, distinct inner bowl and canal notch, with a rounded hearing-aid casing behind the right edge.'
CONSTRUCTION_REFERENCES='Lucide ear: coherent upper bowl and lower lobe curves; source owns the separate aid casing.'
OMISSIONS=['Fine source curve irregularities regularized into coherent curves.']
class Drawing(Solo48):
    icon_id='ear-with-hearing-aid'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'health'
    aliases=()
    keywords=('hearing', 'aid', 'ear')

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

        self.path('ear',(8,16),[('C',(22,4),(8,8),(14,4)),('C',(32,14),(28,4),(32,8)),('C',(30,30),(32,20),(32,26)),('C',(24,38),(26,34),(24,34)),('C',(16,44),(24,42),(20,44)),('C',(8,36),(10,44),(8,40))])
        self.path('aid',(32,14),[('C',(40,22),(38,14),(40,18)),('L',(40,26)),('C',(30,30),(40,30),(36,34))])
        self.path('bowl',(16,16),[('C',(26,20),(16,10),(26,10)),('C',(22,28),(26,24),(24,26))])
        self.path('canal',(16,16),[('C',(14,28),(20,16),(20,24)),('C',(16,32),(14,30),(14,32))])
        self.relate('connect','ear','aid');self.relate('connect','bowl','canal')

    icon_id = 'ear-with-hearing-aid-reference'
    category = 'health'
    aliases = ()
    keywords = ('ear', 'with', 'hearing', 'aid')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    exception = {'approved_by': 'user', 'approved_on': '2026-09-25', 'source_request': 'other unresolve could make as eception', 'recording': 'Local exception under the earlier session instruction; raw QA remains unchanged and this is not a strict pass.', 'svg_sha256': '7dc5357e712e0dc81a383d1508fe14478bb85d613058e2c6940fdb58d009d529', 'reason': 'Retain the defining inner ear arch and curved canal beside the hearing aid.', 'scope': ['ear/bowl: 5.90412 centerline units, about 1.90412 ink units.', 'bowl/canal internal clearance: 1.9104 ink units over 8.1535 units.'], 'source_svg_sha256': 'b2212a329d337c094a11d61b66883da29f2e6bddbb261fd69d45df8dd38abbd3'}

USER_APPROVED_EXCEPTION = {'approved_by': 'user', 'approved_on': '2026-09-25', 'source_request': 'other unresolve could make as eception', 'recording': 'Local exception under the earlier session instruction; raw QA remains unchanged and this is not a strict pass.', 'svg_sha256': 'b2212a329d337c094a11d61b66883da29f2e6bddbb261fd69d45df8dd38abbd3', 'reason': 'Retain the defining inner ear arch and curved canal beside the hearing aid.', 'scope': ['ear/bowl: 5.90412 centerline units, about 1.90412 ink units.', 'bowl/canal internal clearance: 1.9104 ink units over 8.1535 units.']}
