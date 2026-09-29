"""Rejected rocket loses its fins and the globe becomes a semicircular cross. Restore a diagonal finned rocket and a round lower globe with a continent contour."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='316bef96-1836-4fb8-b6a2-7483304127ec'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rocket-passing-above-a-globe/20260929T044747Z-thuan-mac/reference/rocket attack global_316bef96-1836-4fb8-b6a2-7483304127ec.svg'
AUTHOR='gpt-6'
PLAN='Rejected rocket loses its fins and the globe becomes a semicircular cross. Restore a diagonal finned rocket and a round lower globe with a continent contour.'
CONSTRUCTION_REFERENCE='Lucide rocket original and atomic-debug: pointed body and attached fins; original defines globe placement.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='rocket-passing-above-a-globe'
    keyshape=Keyshape.SQUARE
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
        self.path('rocket',(14,20),[('L',(29,7)),('C',(40,4),(34,5),(38,4)),('C',(36,16),(40,8),(38,13)),('L',(23,28)),('L',(14,20))],True)
        self.add_polyline('fin-left',(20,15),(13,15),(8,20),(15,23))
        self.add_polyline('fin-right',(29,22),(29,27),(25,31),(23,28))
        self.add_line('nose-seam',(30,7),(37,14));self.relate('connect','rocket','fin-left','fin-right','nose-seam')
        self.circle('globe',35,37,7)
        self.path('continent',(35,30),[('C',(35,37),(29,33),(41,34)),('C',(34,44),(31,40),(36,42))]);self.relate('connect','globe','continent')
        self.add_line('exhaust-a',(12,28),(6,34));self.add_line('exhaust-b',(17,33),(12,38))
