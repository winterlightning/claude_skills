"""Shortened the vertical body, softened the stepped shoulders and retained both key rows and spacebar."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='669aedc6-7742-41bf-85bd-47da4843ea6b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__championship-belt-reference/20260928T165643Z-thuan-mac/reference/keyboard_669aedc6-7742-41bf-85bd-47da4843ea6b.svg'
AUTHOR='gpt-6'
PLAN='Shortened the vertical body, softened the stepped shoulders and retained both key rows and spacebar.'
CONSTRUCTION_REFERENCE='Lucide keyboard: regular key series and rounded outer case.'
OMISSIONS='End slots omitted to protect the central keys at 48 px.'
class Drawing(Solo48):
    icon_id='championship-belt-reference'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('championship', 'belt', 'reference')

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
        self.path('case',(4,18),[('A',(8,14),4,4,True),('L',(9,14)),('L',(13,10)),('L',(35,10)),('L',(39,14)),('L',(40,14)),('A',(44,18),4,4,True),('L',(44,30)),('A',(40,34),4,4,True),('L',(39,34)),('L',(35,38)),('L',(13,38)),('L',(9,34)),('L',(8,34)),('A',(4,30),4,4,True),('L',(4,18))],True)
        for row,y in enumerate((18,25)):
            for col,x in enumerate((16,24,32)):self.add_dot(f'key-{row}-{col}',(x,y))
        self.add_line('spacebar',(18,31),(30,31))

    # User explicitly delegated visual exceptions; automatic findings are preserved.
    exception = {'reason': 'The source-specific stepped keyboard needs compact rows. Preserve the shorter body requested by the reviewer, the stepped shoulders, two key rows and spacebar; the open negative spaces remain legible at 48 px.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '104a4dd3fa9e7db54d617d7e668a08d2181cd69821f97e41cc613eeecf5978f7'}
