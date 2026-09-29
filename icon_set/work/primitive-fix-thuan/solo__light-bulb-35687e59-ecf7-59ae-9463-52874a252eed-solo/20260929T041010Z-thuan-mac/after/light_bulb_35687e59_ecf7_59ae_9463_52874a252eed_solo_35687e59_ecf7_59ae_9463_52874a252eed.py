"""Rejected broad mushroom-shaped bulb loses the tall rounded glass and tapered neck. Restore a tall globe, smoothly tapered shoulders and rounded base."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='35687e59-ecf7-59ae-9463-52874a252eed'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__light-bulb-35687e59-ecf7-59ae-9463-52874a252eed-solo/20260929T041010Z-thuan-mac/reference/light bulb_35687e59-ecf7-59ae-9463-52874a252eed.svg'
AUTHOR='gpt-6'
PLAN='Rejected broad mushroom-shaped bulb loses the tall rounded glass and tapered neck. Restore a tall globe, smoothly tapered shoulders and rounded base.'
CONSTRUCTION_REFERENCE='No useful subject-specific Lucide match; original reference determines the silhouette.'
OMISSIONS='No defining silhouette omitted.'
class Drawing(Solo48):
    icon_id='light-bulb-35687e59-ecf7-59ae-9463-52874a252eed-solo'
    keyshape=Keyshape.VRECT_M
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
        self.path('glass',(17,35),[('C',(14,26),(17,31),(16,30)),('C',(10,18),(11,22),(10,20)),('A',(38,18),14,14,True),('C',(34,26),(38,20),(37,22)),('C',(31,35),(32,30),(31,31)),('L',(17,35))],True)
        self.path('base',(17,35),[('L',(17,38)),('A',(23,44),6,6,False),('L',(25,44)),('A',(31,38),6,6,False),('L',(31,35))])
        self.relate('connect','glass','base')
