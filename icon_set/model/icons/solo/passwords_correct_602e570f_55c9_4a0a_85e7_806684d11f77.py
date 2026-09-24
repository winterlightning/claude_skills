from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '602e570f-55c9-4a0a-85e7-806684d11f77'
SOURCE_PATH = 'pictographic-primitives/other/passwords correct_602e570f-55c9-4a0a-85e7-806684d11f77.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A password field displaying two X characters.
    Plan: Two identical diagonal crosses spaced on a common baseline inside a wide rectangle.
    Reference: No useful Lucide match; repeated crosses and field are reconstructed from the supplied reference.
    """
    icon_id = 'passwords-correct'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('passwords', 'correct')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def rounded(self,n,l,t,r,b,k=4):
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        members=[]
        for i,p in enumerate(pts):
            q=pts[(i+1)%8];name=f'{n}-{i}';members.append(name)
            if i%2:self.add_arc(name,p,q,radius_x=k)
            else:self.add_line(name,p,q)
        self.add_contour(n,*members,closed=True)

    def dollar(self):
        self.add_line('s-top',(29,16),(24,16))
        self.add_arc('s-left',(24,16),(24,24),radius_x=4,sweep=False)
        self.add_arc('s-right',(24,24),(24,32),radius_x=4)
        self.add_line('s-bottom',(24,32),(19,32))
        self.add_contour('dollar','s-top','s-left','s-right','s-bottom')
        self.add_line('stem-top',(24,12),(24,16));self.relate('connect','stem-top','dollar')
        self.add_line('stem-bottom',(24,32),(24,36));self.relate('connect','stem-bottom','dollar')

    def bust(self,n,x,y,r,width,body_y,body_ry):
        # Detached head bottom = y+r; shoulder apex = body_y-body_ry.
        # Author parameters require their difference to be exactly eight.
        self.circle(n+'-head',x,y,r)
        self.add_arc(n+'-shoulders',(x-width,body_y),(x+width,body_y),radius_x=width,radius_y=body_ry)

    def build(self):

        self.add_polyline('field',(4,10),(44,10),(44,38),(4,38),closed=True)
        for i,x in enumerate((16,32)):
            for j,(dx,dy) in enumerate(((-3,-3),(3,3),(-3,3),(3,-3))):self.add_line(f'x-{i}-{j}',(x,24),(x+dx,24+dy))
            self.relate('connect',*(f'x-{i}-{j}' for j in range(4)))
