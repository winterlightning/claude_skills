"""Rejected orbital band is a thick diagonal slash. Restore a complete steeply tilted elliptical loop with visible front and rear lobes around the globe."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='a55f45de-c7d1-4563-93a4-39142d00a866'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__ringed-planet-with-a-steep-tilt/20260929T044747Z-thuan-mac/reference/astronomy planet saturn 2_a55f45de-c7d1-4563-93a4-39142d00a866.svg'
AUTHOR='gpt-6'
PLAN='Rejected orbital band is a thick diagonal slash. Restore a complete steeply tilted elliptical loop with visible front and rear lobes around the globe.'
CONSTRUCTION_REFERENCE='Lucide orbit: simple circle and smooth orbital arcs; original establishes steep ellipse.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='ringed-planet-with-a-steep-tilt'
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
        self.circle('planet',24,24,15)
        self.path('orbit',(42,6),[('C',(29,29),(45,9),(39,19)),('C',(6,42),(19,39),(9,45)),('C',(19,19),(3,39),(9,29)),('C',(42,6),(29,9),(39,3))],True)
        self.relate('connect','planet','orbit')
