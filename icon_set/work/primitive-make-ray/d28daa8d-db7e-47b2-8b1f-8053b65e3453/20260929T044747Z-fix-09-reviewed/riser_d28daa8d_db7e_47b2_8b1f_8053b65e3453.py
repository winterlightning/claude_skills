"""Rejected arrow is short and heavy inside the square. Restore the reference tall shaft and wider upward arrow, balanced within a softly rounded square."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='d28daa8d-db7e-47b2-8b1f-8053b65e3453'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__riser/20260929T044747Z-thuan-mac/reference/riser_d28daa8d-db7e-47b2-8b1f-8053b65e3453.svg'
AUTHOR='gpt-6'
PLAN='Rejected arrow is short and heavy inside the square. Restore the reference tall shaft and wider upward arrow, balanced within a softly rounded square.'
CONSTRUCTION_REFERENCE='No useful Lucide subject match; original reference establishes silhouette and arrangement.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='riser'
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
        self.box('frame',6,6,42,42,5)
        self.add_polyline('arrow',(15,22),(24,15),(33,22))
        self.add_line('shaft',(24,15),(24,33));self.relate('connect','arrow','shaft')
