from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e4b8631c-5185-5ace-a823-05b73325753b'
SOURCE_PATH = 'icon_set/work/todo-references/pen tools_e4b8631c-5185-5ace-a823-05b73325753b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A pen nib beneath vector curve control handles.
    Plan: Symmetric nib, central hole, repeated control nodes and a broad curve.
    Reference: pen-tool: nib, slit and circular hole; source adds curve handles.
    """
    icon_id = 'pen-tools'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('pen', 'tools')

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

        self.circle('left-node',8,8,2);self.circle('right-node',40,8,2)
        self.add_polyline('control-square',(20,6),(28,6),(28,14),(20,14),closed=True)
        self.add_line('left-control',(10,8),(20,8));self.relate('connect','left-control','left-node');self.relate('connect','left-control','control-square')
        self.add_line('right-control',(28,8),(38,8));self.relate('connect','right-control','right-node');self.relate('connect','right-control','control-square')
        self.add_arc('curve-left',(8,24),(20,10),radius_x=16,radius_y=16)
        self.add_arc('curve-right',(28,10),(40,24),radius_x=16,radius_y=16)
        self.relate('connect','curve-left','control-square');self.relate('connect','curve-right','control-square')
        self.add_polyline('nib',(24,18),(14,30),(18,34),(30,34),(34,30),closed=True)
        self.circle('nib-hole',24,28,2)
        self.add_line('slit',(24,18),(24,26));self.relate('connect','slit','nib');self.relate('connect','slit','nib-hole')
        self.add_polyline('base',(16,34),(32,34),(32,42),(16,42),closed=True);self.relate('connect','base','nib')
