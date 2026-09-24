"""Surgical scissors with two circular grips and a rotated female symbol.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: Blade seam replaced by two coherent strokes.
Construction: Lucide venus: ring and cross; shared round contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='852044c0-c346-4658-9c9c-035df8dc7b7b'
SOURCE_PATH='pictographic-primitives/_uncategorized_36/stablization operation female_852044c0-c346-4658-9c9c-035df8dc7b7b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='stablization-operation-female'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('stablization', 'operation', 'female')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.circle('handle-left',9,39,3)
        self.circle('handle-right',25,39,3)
        self.add_polyline('blade-left',(12,39),(18,24),(18,6))
        self.add_polyline('blade-right',(22,39),(18,24),(22,8))
        self.relate('connect','blade-left','handle-left');self.relate('connect','blade-right','handle-right');self.relate('connect','blade-left','blade-right')
        self.add_arc('female-bowl',(30,16),(34,32),radius_x=9)
        self.add_polyline('female-stem',(36,18),(39,12),(42,6))
        self.add_polyline('female-cross',(34,9),(39,12),(42,14))
        self.relate('connect','female-stem','female-cross')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
    def path(self,n,start,ops,closed=False):
        p=start;members=[]
        for i,op in enumerate(ops):
            name=f'{n}-{i}';end=op[1]
            if op[0]=='L':self.add_line(name,p,end)
            elif op[0]=='A':self.add_arc(name,p,end,radius_x=op[2],radius_y=op[3],sweep=op[4])
            elif op[0]=='B':self.add_bezier(name,p,(op[2],op[3],end))
            members.append(name);p=end
        if closed and p!=start:
            self.add_line(n+'-close',p,start);members.append(n+'-close')
        self.add_contour(n,*members,closed=closed)
