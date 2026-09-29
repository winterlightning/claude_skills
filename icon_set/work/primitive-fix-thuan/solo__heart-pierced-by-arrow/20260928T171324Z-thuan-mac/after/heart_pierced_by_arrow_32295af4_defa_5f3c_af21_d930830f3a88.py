"""Rebuilt a balanced heart with paired smooth lobes and a clean lower point; retained the piercing diagonal arrow."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='32295af4-defa-5f3c-af21-d930830f3a88'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__heart-pierced-by-arrow/20260928T171324Z-thuan-mac/reference/love heart arrow_32295af4-defa-5f3c-af21-d930830f3a88.svg'
AUTHOR='gpt-6'
PLAN='Rebuilt a balanced heart with paired smooth lobes and a clean lower point; retained the piercing diagonal arrow.'
CONSTRUCTION_REFERENCE='Lucide heart: paired lobes flowing into tapered sides; source: diagonal arrow.'
OMISSIONS='Fine closed feather panels replaced by two clear fletching strokes.'
class Drawing(Solo48):
    icon_id='heart-pierced-by-arrow'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('heart', 'pierced', 'by', 'arrow')

    def path(self,n,start,commands,closed=False):
        here=start; ids=[]
        for i,(kind,end,*a) in enumerate(commands):
            ident=f'{n}-{i}';ids.append(ident)
            if kind=='L': self.add_line(ident,here,end)
            elif kind=='A': self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C': self.add_bezier(ident,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
    def phone(self,band=True):
        # Shared outline owns width, corner radius and band attachment nodes.
        l,r,t,b,k,y=10,38,4,44,4,36
        self.path('phone',(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,y)),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,y)),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        if band:
            self.add_line('band',(l,y),(r,y));self.relate('connect','phone','band')

    def build(self):
        # Heart owns shared arrow contact nodes (35,14) and (14,34).
        self.path('heart',(21,15),[('C',(13,10),(18,12),(16,10)),('C',(6,20),(8,10),(6,14)),('C',(14,34),(6,26),(10,30)),('L',(21,40)),('C',(36,20),(29,33),(36,26)),('C',(35,14),(36,18),(36,16)),('C',(29,10),(34,11),(31,10)),('C',(21,15),(26,10),(23,12))],True)
        self.add_polyline('arrow-front',(28,22),(35,14),(42,6))
        self.add_polyline('arrow-head',(34,6),(42,6),(42,14))
        self.relate('connect','heart','arrow-front');self.relate('connect','arrow-front','arrow-head')
        self.add_polyline('arrow-tail',(6,42),(12,36),(14,34))
        self.add_polyline('feather',(6,36),(12,36),(12,42))
        self.relate('connect','heart','arrow-tail');self.relate('connect','arrow-tail','feather')

    # User delegated visual exceptions; original automatic findings remain recorded.
    exception = {'reason': 'The piercing arrow creates intentional short narrow regions near its real heart crossing. Retain the complete smooth heart, arrow shaft and arrowhead; both are clearly distinguishable in native light/dark previews.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '39e6bafeee71f15ff04093c1cefb4f140fb11146f0cf404028f6e67a1551181e'}
