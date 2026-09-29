"""Rejected planet uses one slash and a solid X. Restore an elliptical orbit around a round planet and a pointed four-way sparkle."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='74539cee-3f62-4324-b3c6-99b6a90c985e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__ringed-planet-beside-small-star/20260929T044747Z-thuan-mac/reference/mars_74539cee-3f62-4324-b3c6-99b6a90c985e.svg'
AUTHOR='gpt-6'
PLAN='Rejected planet uses one slash and a solid X. Restore an elliptical orbit around a round planet and a pointed four-way sparkle.'
CONSTRUCTION_REFERENCE='Lucide orbit original/atomic-debug: clean circular planet; supplied reference owns elliptical ring and star.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='ringed-planet-beside-small-star'
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
        self.circle('planet',21,28,14)
        self.path('ring',(8,27),[('C',(4,36),(0,32),(2,37)),('C',(43,22),(15,41),(48,24)),('C',(34,20),(46,16),(39,18))])
        self.path('star',(38,5),[('C',(43,10),(38,8),(40,10)),('C',(38,15),(40,10),(38,12)),('C',(33,10),(38,12),(36,10)),('C',(38,5),(36,10),(38,8))],True)
        self.relate('connect','planet','ring')
