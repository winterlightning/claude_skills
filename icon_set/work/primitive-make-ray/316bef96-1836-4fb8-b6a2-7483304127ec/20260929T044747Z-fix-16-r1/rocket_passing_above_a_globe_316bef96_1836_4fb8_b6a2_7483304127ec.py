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
        self.path('rocket',(15,23),[('L',(27,10)),('C',(42,6),(33,7),(38,6)),('C',(38,20),(42,11),(40,17)),('L',(25,32)),('L',(15,23))],True)
        self.add_polyline('fin-left',(19,19),(12,19),(7,24),(15,27));self.add_polyline('fin-right',(29,29),(29,36),(24,41),(21,33))
        self.add_line('nose-seam',(30,9),(39,18));self.relate('connect','rocket','fin-left','fin-right','nose-seam')
        self.path('globe',(35,30),[('C',(42,36),(40,30),(42,33)),('C',(31,44),(42,42),(36,44)),('C',(25,38),(27,44),(25,41))])
        self.path('continent',(42,36),[('L',(36,37)),('C',(35,43),(33,38),(37,40))]);self.relate('connect','globe','continent')
        self.add_line('exhaust-a',(12,31),(6,37));self.add_line('exhaust-b',(16,35),(12,39))
