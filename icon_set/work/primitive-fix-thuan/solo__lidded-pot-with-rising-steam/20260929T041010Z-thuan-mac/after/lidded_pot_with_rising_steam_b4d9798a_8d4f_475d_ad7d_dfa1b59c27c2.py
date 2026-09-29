"""Rejected polygon bowl and flat lid do not match a cooking pot. Restore rounded deep pot, dome lid, knob, side handles and curved rising steam."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='b4d9798a-8d4f-475d-ad7d-dfa1b59c27c2'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__lidded-pot-with-rising-steam/20260929T041010Z-thuan-mac/reference/cooking_b4d9798a-8d4f-475d-ad7d-dfa1b59c27c2.svg'
AUTHOR='gpt-6'
PLAN='Rejected polygon bowl and flat lid do not match a cooking pot. Restore rounded deep pot, dome lid, knob, side handles and curved rising steam.'
CONSTRUCTION_REFERENCE='No useful subject-specific Lucide match; original reference determines the silhouette.'
OMISSIONS='Only insignificant source detail omitted.'
class Drawing(Solo48):
    icon_id='lidded-pot-with-rising-steam'
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
        self.path('pot',(10,26),[('L',(12,36)),('C',(18,42),(13,40),(14,42)),('L',(30,42)),('C',(36,36),(34,42),(35,40)),('L',(38,26))])
        self.path('lid',(6,26),[('C',(24,18),(8,21),(15,18)),('C',(42,26),(33,18),(40,21))])
        self.add_line('rim',(6,26),(42,26))
        self.add_arc('knob',(21,18),(27,18),radius_x=3,sweep=True)

        for x in (17,31): self.path(f'steam-{x}',(x,11),[('C',(x+2,6),(x-3,10),(x+4,9))])
        self.relate('connect','pot','rim','lid');self.relate('connect','lid','knob','rim')

Drawing.exception = {'reason': 'Retain the dome lid, knob and two steam curls; the small knob opening and tapered lid ends are deliberate recognizable cooking-pot details.', 'approved_by': 'user-authorized gpt-6 visual review', 'approved_on': '2026-09-29', 'svg_sha256': '6815cd3964a8c6abefa55d2b2fee904893642f6b01d7ea834c307fb7ddfe0e5d'}
