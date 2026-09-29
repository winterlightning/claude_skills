"""Elongated the tapered pin, enlarged its circular opening and brought the ground line closer to its point."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='632bbd50-870e-4274-87d8-51bc5834f214'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__location-pin-ground/20260928T171406Z-thuan-mac/reference/location dot_632bbd50-870e-4274-87d8-51bc5834f214.svg'
AUTHOR='gpt-6'
PLAN='Elongated the tapered pin, enlarged its circular opening and brought the ground line closer to its point.'
CONSTRUCTION_REFERENCE='Lucide map-pin: round cap, circular opening and taper to a centered point.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='location-pin-ground'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('location', 'pin', 'ground')

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
        self.path('pin',(10,18),[('A',(38,18),14,14,True),('C',(24,38),(38,25),(29,34)),('C',(10,18),(19,34),(10,25))],True)
        self.circle('opening',24,18,6)
        self.add_line('ground',(16,44),(32,44))

    # User delegated visual exceptions; original automatic findings remain recorded.
    exception = {'reason': 'Restore the taller pin and larger circular opening while keeping the reference ground line close to its point. The intentional ground gap is 2 visible units; the circular opening remains distinct and unclipped.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'ba2bfb2f1b560587a80d0d5a8317f62d64fd177117dd0923bd0ea112c981b02a'}
