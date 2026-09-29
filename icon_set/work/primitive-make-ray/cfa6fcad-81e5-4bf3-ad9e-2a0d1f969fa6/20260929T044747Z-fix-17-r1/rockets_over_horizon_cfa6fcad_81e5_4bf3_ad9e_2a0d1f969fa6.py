"""Rejected descending objects become angular shield-like symbols. Restore two rounded downward rockets with side fins, falling trails and a curved planetary horizon."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='cfa6fcad-81e5-4bf3-ad9e-2a0d1f969fa6'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rockets-over-horizon/20260929T044747Z-thuan-mac/reference/network firewall rocket_cfa6fcad-81e5-4bf3-ad9e-2a0d1f969fa6.svg'
AUTHOR='gpt-6'
PLAN='Rejected descending objects become angular shield-like symbols. Restore two rounded downward rockets with side fins, falling trails and a curved planetary horizon.'
CONSTRUCTION_REFERENCE='No useful Lucide subject match; original reference establishes silhouette and arrangement.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='rockets-over-horizon'
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
        for n,x,y in [('left',14,19),('right',34,15)]:
         self.path(n+'-body',(x-4,y),[('A',(x+4,y),4,4,True),('L',(x+4,y+10)),('C',(x,y+15),(x+4,y+12),(x+2,y+14)),('C',(x-4,y+10),(x-2,y+14),(x-4,y+12)),('L',(x-4,y))],True)
         self.path(n+'-left-fin',(x-4,y),[('L',(x-10,y-3)),('L',(x-10,y+2)),('C',(x-4,y+6),(x-10,y+5),(x-7,y+6))])
         self.path(n+'-right-fin',(x+4,y),[('L',(x+10,y-3)),('L',(x+10,y+2)),('C',(x+4,y+6),(x+10,y+5),(x+7,y+6))])
         self.relate('connect',n+'-body',n+'-left-fin',n+'-right-fin')
        self.add_line('trail-left',(14,8),(14,11));self.add_line('trail-right',(34,4),(34,7))
        self.add_bezier('horizon',(4,44),((17,39),(31,39),(44,44)))
