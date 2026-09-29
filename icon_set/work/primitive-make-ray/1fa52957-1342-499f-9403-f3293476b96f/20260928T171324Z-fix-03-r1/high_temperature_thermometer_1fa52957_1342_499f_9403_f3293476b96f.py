"""Slimmed the stem, restored a small outlined mercury bulb and differentiated long and short scale ticks."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1fa52957-1342-499f-9403-f3293476b96f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__high-temperature-thermometer/20260928T171324Z-thuan-mac/reference/temperature thermometer high_1fa52957-1342-499f-9403-f3293476b96f.svg'
AUTHOR='gpt-6'
PLAN='Slimmed the stem, restored a small outlined mercury bulb and differentiated long and short scale ticks.'
CONSTRUCTION_REFERENCE='Lucide thermometer: rounded connected stem and bulb; source: high mercury and three alternating-length ticks.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='high-temperature-thermometer'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('high', 'temperature', 'thermometer')

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
        self.path('outline',(14,10),[('A',(26,10),6,6,True),('L',(26,26)),('C',(30,35),(29,29),(30,32)),('A',(20,44),10,9,True),('A',(10,35),10,9,True),('C',(14,26),(10,32),(11,29)),('L',(14,10))],True)
        self.circle('mercury-bulb',20,34,3)
        self.add_line('mercury',(20,12),(20,31));self.relate('connect','mercury','mercury-bulb')
        for j,(x,y) in enumerate(((34,8),(36,17),(34,26))):self.add_line(f'tick-{j}',(x,y),(38,y))

    # User delegated visual exceptions; original automatic findings remain recorded.
    exception = {'reason': 'A recognizable slender thermometer needs a narrow stem and mercury column. Their 2-unit visible gap, small outlined bulb and nearby three scale ticks remain clear at 48 px; widening the stem would recreate the rejected bulky silhouette.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '22df8d09b690dc3d60a477b55385adc6fc5a42ed7ba03049a5bdef4e2fe55819'}
