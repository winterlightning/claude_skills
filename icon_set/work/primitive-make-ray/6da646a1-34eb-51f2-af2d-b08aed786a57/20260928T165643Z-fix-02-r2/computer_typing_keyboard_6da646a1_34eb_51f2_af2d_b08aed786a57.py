"""Made the keyboard proportionally wider, with longer key dashes and a centered spacebar."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6da646a1-34eb-51f2-af2d-b08aed786a57'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__computer-typing-keyboard/20260928T165643Z-thuan-mac/reference/keyboard_6da646a1-34eb-51f2-af2d-b08aed786a57.svg'
AUTHOR='gpt-6'
PLAN='Made the keyboard proportionally wider, with longer key dashes and a centered spacebar.'
CONSTRUCTION_REFERENCE='Lucide keyboard: shared key spacing and quarter-circle case corners.'
OMISSIONS='Four source keys per row reduced to three; two rows preserved.'
class Drawing(Solo48):
    icon_id='computer-typing-keyboard'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('computer', 'typing', 'keyboard')

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
        self.box('case',4,10,44,38,4)
        for row,y in enumerate((17,24)):
            for col,x in enumerate((14,24,34)):self.add_line(f'key-{row}-{col}',(x-1,y),(x+1,y))
        self.add_line('spacebar',(14,31),(34,31))

    # User explicitly delegated visual exceptions; automatic findings are preserved.
    exception = {'reason': 'A wider keyboard proportion needs three interior rows in HRECT_M. Retain uniform 7-unit centerline spacing (3-unit visible gaps), both rows and the spacebar instead of returning to the rejected squat proportions.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '587d8fa368aa403cd0e7300bc13ce4b2ec2fa60cd45a1e7a6ef35c64768f6dc7'}
