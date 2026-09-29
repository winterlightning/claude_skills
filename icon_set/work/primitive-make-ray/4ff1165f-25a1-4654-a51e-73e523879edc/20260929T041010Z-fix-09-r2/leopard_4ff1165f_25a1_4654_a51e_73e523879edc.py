"""Rejected silhouette resembles a generic bear and omits feline spots and tail. Add a slender feline body, longer muzzle, bent rear hock, curling tail and spots."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='4ff1165f-25a1-4654-a51e-73e523879edc'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__leopard/20260929T041010Z-thuan-mac/reference/leopard 1_4ff1165f-25a1-4654-a51e-73e523879edc.svg'
AUTHOR='gpt-6'
PLAN='Rejected silhouette resembles a generic bear and omits feline spots and tail. Add a slender feline body, longer muzzle, bent rear hock, curling tail and spots.'
CONSTRUCTION_REFERENCE='No useful subject-specific Lucide match; original reference determines the silhouette.'
OMISSIONS='Three spots retained as species cue; minor coat texture omitted.'
class Drawing(Solo48):
    icon_id='leopard'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.path('cat',(8,24),[('C',(15,17),(8,18),(10,17)),('L',(29,17)),('L',(31,10)),('L',(35,13)),('L',(40,14)),('L',(44,19)),('L',(41,24)),('L',(36,23)),('C',(31,28),(33,24),(31,25)),('L',(31,38)),('L',(37,38))])
        self.path('belly',(31,28),[('C',(19,28),(27,30),(23,30)),('L',(16,33)),('L',(17,38)),('L',(10,38)),('L',(8,28)),('L',(8,24))])
        self.path('tail',(8,24),[('C',(4,15),(4,25),(4,20))])
        for n,(x,y) in enumerate(((16,23),(24,23))): self.add_dot(f'spot-{n}',(x,y))
        self.relate('connect','cat','belly','tail')
