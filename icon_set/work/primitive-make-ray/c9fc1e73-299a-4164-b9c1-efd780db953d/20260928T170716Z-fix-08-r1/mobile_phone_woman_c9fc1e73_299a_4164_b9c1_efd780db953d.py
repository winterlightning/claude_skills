'The current phone omitted the lower bezel and reduced the woman to a small floating head. Restored bezel, larger circular face, long hair and fuller shoulders.\nSymbol plan: enclosure owns content; shared dimensions, radii, repetition and actual attachment nodes.\nConstruction: local Lucide smartphone original and atomic-debug. Human busts use human_ref/user.svg.\nKeyshape VRECT_M: intended proportional envelope; any departure is separately recorded as a drawing-bound exception.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c9fc1e73-299a-4164-b9c1-efd780db953d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mobile-phone-woman/20260928T170716Z-thuan-mac/reference/mobile phone woman_c9fc1e73-299a-4164-b9c1-efd780db953d.svg'
AUTHOR = 'gpt-6'
PARENT_MODULE = 'icon_set/work/primitive-fix-thuan/solo__mobile-phone-woman/20260928T170716Z-thuan-mac/before/mobile_phone_woman_c9fc1e73_299a_4164_b9c1_efd780db953d.py'
class Drawing(Solo48):
    icon_id = 'mobile-phone-woman'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('mobile', 'phone', 'woman')

    def path(self,n,p,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            k=f'{n}-{i}';q=c[1]
            if c[0]=='L':self.add_line(k,p,q)
            elif c[0]=='A':self.add_arc(k,p,q,radius_x=c[2],radius_y=c[3],sweep=c[4])
            elif c[0]=='C':self.add_bezier(k,p,(c[2],c[3],q))
            ids.append(k);p=q
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=4,split=None):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        commands=[]
        for i in range(8):
            q=pts[(i+1)%8]
            if i%2:commands.append(('A',q,rad,rad,True))
            else:
                for p in (split or {}).get(i,[]):commands.append(('L',p))
                commands.append(('L',q))
        self.path(n,pts[0],commands,True)
    def phone(self,l=10,r=38,t=4,b=44,footer=36):
        self.box('phone',l,t,r,b,4,{2:[(r,footer)],6:[(l,footer)]})
        self.add_line('bezel',(l,footer),(r,footer));self.relate('connect','phone','bezel')
    def monitor(self):
        self.box('screen',4,4,44,34,4,{4:[(24,34)]})
        self.add_line('stand',(24,34),(24,44))
        self.add_polyline('base',(16,44),(24,44),(32,44))
        self.relate('connect','screen','stand');self.relate('connect','stand','base')
    def dollar(self,cx=24,top=13):
        # Tangent semicircular bowls; centered currency ticks attach at split nodes.
        y=top
        self.path('dollar',(cx+4,y),[('L',(cx,y)),('L',(cx-1,y)),('A',(cx-1,y+8),4,4,False),('L',(cx+1,y+8)),('A',(cx+1,y+16),4,4,True),('L',(cx,y+16)),('L',(cx-4,y+16))])
        self.add_line('currency-top',(cx,y-3),(cx,y));self.add_line('currency-bottom',(cx,y+16),(cx,y+19))
        self.relate('connect','dollar','currency-top');self.relate('connect','dollar','currency-bottom')

    def build(self):
        self.phone()
        # Circular face and long hair; shoulders maintain exact 4u detached ink gap.
        self.circle('face',24,18,5)
        self.path('hair-left',(19,18),[('C',(17,26),(19,22),(19,24))])
        self.path('hair-right',(29,18),[('C',(31,26),(29,22),(29,24))])
        self.relate('connect','face','hair-left');self.relate('connect','face','hair-right')
        self.path('shoulders',(16,36),[('A',(24,31),8,5,True),('A',(32,36),8,5,True)])
        self.relate('connect','shoulders','bezel')
