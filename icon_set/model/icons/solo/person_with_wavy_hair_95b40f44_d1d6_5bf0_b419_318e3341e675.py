from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='95b40f44-d1d6-5bf0-b419-318e3341e675'
SOURCE_PATH='pictographic-primitives/avatars/woman_95b40f44-d1d6-5bf0-b419-318e3341e675.svg'
AUTHOR='gpt-6'
PLAN = 'Long wavy hair rests on broad curved shoulders around a large centered circular face and smooth parted fringe.'
CONSTRUCTION_REFERENCES='icon-avatar and human_ref/user.svg: centered circular face, zero-gap touching shoulders; Lucide user-round: tangent curves.'
OMISSIONS = ['Fine hair ripples condensed into one broad wave per side; neckline omitted.']
class Drawing(Solo48):
    icon_id='woman-with-soft-wavy-hair'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases=()
    keywords=('woman',)
    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=('body-top' if i==2 else 'body-top-right') if n=='body' and i in (2,3) else f'{n}-{i}';members.append(k)
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

    def avatar_body(self,top=32):
        self.add_line('body-left-side',(8,44),(8,top+8))
        self.add_arc('body-left-shoulder',(8,top+8),(16,top),radius_x=8)
        self.add_line('body-top',(16,top),(24,top))
        self.add_line('body-top-right',(24,top),(32,top))
        self.add_arc('body-right-shoulder',(32,top),(40,top+8),radius_x=8)
        self.add_line('body-right-side',(40,top+8),(40,44))
        self.add_contour('body','body-left-side','body-left-shoulder','body-top','body-top-right','body-right-shoulder','body-right-side')
    def portrait_head(self):
        self.add_line('root-left',(14,18),(14,14))
        self.add_arc('crown',(14,14),(34,14),radius_x=10)
        self.add_line('root-right',(34,14),(34,18))
        self.add_arc('jaw',(34,18),(14,18),radius_x=10)
        self.add_contour('head','root-left','crown','root-right','jaw',closed=True)
        self.add_bezier('fringe',(14,18),((20,18),(22,13),(24,13)),((26,13),(28,18),(34,18)))
        self.relate('connect','head','fringe')
    def build(self):
        self.path('hair',(14,32),[('C',(8,28),(6,34),(6,30)),('C',(6,18),(7,26),(6,24)),('A',(24,6),18,12,True),('A',(42,18),18,12,True),('C',(40,28),(42,24),(41,26)),('C',(34,32),(42,30),(42,34))])
        self.add_bezier('fringe',(14,18),((19,18),(22,14),(24,14)),((26,14),(29,18),(34,18)))
        self.add_arc('jaw',(34,18),(14,18),radius_x=10)
        self.add_contour('face','fringe','jaw',closed=True)
        self.path('body',(6,42),[('L',(6,40)),('A',(14,32),8,8,True),('L',(24,32)),('L',(34,32)),('A',(42,40),8,8,True),('L',(42,42))])
        self.relate('connect','hair','body');self.relate('connect','face','body')

    icon_id = 'person-with-wavy-hair'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('person', 'with', 'wavy', 'hair')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'

HUMAN_CONSTRUCTION_REVIEW = {'head_bottoms': [28], 'shoulder_tops': [32], 'reference': 'icon_set/references/human_ref/user.svg', 'specialization': 'icon-avatar', 'centerline_gap': 4, 'visible_ink_gap': 0, 'proof': 'Each shoulder apex is four centerline units below its own circular head or jaw bottom. With stroke width four, the ink edges touch. Avatar specialization requested by user.'}
