"""Bicycle with two equal wheels, a mounted rear box, step-through frame and straight forward handlebar."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='697554f1-3afd-5c1d-87a3-50b358ece127'
SOURCE_PATH='pictographic-primitives/transportation/bike cargo back_697554f1-3afd-5c1d-87a3-50b358ece127.svg'
AUTHOR='gpt-6'
PLAN='Bicycle with two equal wheels, a mounted rear box, step-through frame and straight forward handlebar.'
CONSTRUCTION_REFERENCE='bike original: balanced equal wheels; supplied reference owns the rear carrier and step-through frame.'
OMISSIONS='Lower hub-level frame, internal wheel spokes and fine pedal detail omitted to retain clear wheel openings; shallow step-through connection retained.'
class Drawing(Solo48):
    icon_id='rear-cargo-bicycle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('bike', 'cargo', 'back')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,start,commands,closed=False):
        ids=[];here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid);here=end
        self.add_contour(n,*ids,closed=closed)

    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def file(self,l=8,t=4,r=40,b=44):
        self.path('page',(l+4,t),[('L',(r-10,t)),('L',(r,t+10)),('L',(r,b-4)),('A',(r-4,b),4,4,True),('L',(l+4,b)),('A',(l,b-4),4,4,True),('L',(l,t+4)),('A',(l+4,t),4,4,True)],True)

    def build(self):
        for n,x in [('rear',13),('front',35)]:self.circle(n+'-wheel',x,35,7)
        self.box('cargo',6,6,18,19,3)
        self.add_line('rack',(13,19),(13,28));self.relate('connect','rack','cargo');self.relate('connect','rack','rear-wheel')
        self.add_polyline('fork',(35,28),(31,19),(29,11),(29,6),(35,6));self.relate('connect','fork','front-wheel')
        self.add_polyline('frame',(18,19),(26,22),(31,19));self.relate('connect','frame','cargo');self.relate('connect','frame','fork')

# Keyshape rationale: SQUARE balances equal wheels below the rear cargo and handlebar.
# Visual review: Rear cargo, two equal wheels and forward handlebar read at native size. Frame simplified to a shallow step-through; wheel spokes and lower hub-level frame omitted to prevent crowding.
