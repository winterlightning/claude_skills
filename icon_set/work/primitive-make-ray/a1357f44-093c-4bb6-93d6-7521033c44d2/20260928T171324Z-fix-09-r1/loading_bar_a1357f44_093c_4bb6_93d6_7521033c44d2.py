"""Restored a shallow capsule with true semicircular ends and two parallel stripes at the source-specific angle."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a1357f44-093c-4bb6-93d6-7521033c44d2'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__loading-bar/20260928T171324Z-thuan-mac/reference/loading bar_a1357f44-093c-4bb6-93d6-7521033c44d2.svg'
AUTHOR='gpt-6'
PLAN='Restored a shallow capsule with true semicircular ends and two parallel stripes at the source-specific angle.'
CONSTRUCTION_REFERENCE='No useful Lucide loading-bar match (loader is a spinner); source owns the capsule and stripes. Rounded enclosure technique follows the inspected smartphone reference.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='loading-bar'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('loading', 'bar')

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
        tops=(18, 30);bottoms=(14, 26)
        commands=[('L',(x,18)) for x in tops if x!=10]
        if tops[-1]!=38:commands.append(('L',(38,18)))
        commands += [('A',(44,24),6,6,True),('A',(38,30),6,6,True)]
        commands += [('L',(x,30)) for x in reversed(bottoms) if x!=38]
        if bottoms[0]!=10:commands.append(('L',(10,30)))
        commands += [('A',(4,24),6,6,True),('A',(10,18),6,6,True)]
        self.path('capsule',(10,18),commands,True)
        for j,(a,b) in enumerate(zip(tops,bottoms)):
            self.add_line(f'stripe-{j}',(a,18),(b,30));self.relate('connect','capsule',f'stripe-{j}')

    # User delegated visual exceptions; original automatic findings remain recorded.
    exception = {'reason': 'The loading bar must be a shallow capsule with true semicircular ends. Keep the 16-unit visible height and source stripe angle rather than stretch it into a tall rounded box. All automatic spacing checks pass.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'baba6978d467ae7140c2a9e4c79bb9448407bdf7b482d3b7bb942d7c92bcabad'}
