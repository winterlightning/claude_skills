"""Rejected face is an open C-shaped notch with disconnected wind dots. Restore the forehead, nose, lips, chin and neck, plus two continuous outward breath curls."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='bc8b590c-4f02-4ec8-a8d5-4c92ef3b7c1d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__right-facing-head-with-curled-breath-lines/20260929T044747Z-thuan-mac/reference/spit_bc8b590c-4f02-4ec8-a8d5-4c92ef3b7c1d.svg'
AUTHOR='gpt-6'
PLAN='Rejected face is an open C-shaped notch with disconnected wind dots. Restore the forehead, nose, lips, chin and neck, plus two continuous outward breath curls.'
CONSTRUCTION_REFERENCE='No useful Lucide subject match; original reference establishes silhouette and arrangement.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='right-facing-head-with-curled-breath-lines'
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
        self.path('profile',(10,42),[('L',(10,35)),('C',(6,23),(10,31),(6,28)),('C',(19,6),(6,13),(10,6)),('C',(33,21),(28,6),(33,12)),('L',(34,25)),('L',(30,25)),('L',(30,29)),('L',(26,29)),('C',(26,34),(22,29),(22,34)),('L',(29,34)),('C',(22,39),(29,38),(26,39)),('L',(22,42))])
        self.path('breath-top',(34,31),[('L',(40,31)),('A',(40,25),3,3,False)])
        self.path('breath-bottom',(34,38),[('C',(40,42),(40,37),(43,40)),('L',(38,42))])
