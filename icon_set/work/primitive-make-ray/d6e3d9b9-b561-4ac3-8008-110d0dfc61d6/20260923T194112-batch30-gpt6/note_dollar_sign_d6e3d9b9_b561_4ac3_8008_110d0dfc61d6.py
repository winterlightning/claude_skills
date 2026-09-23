from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd6e3d9b9-b561-4ac3-8008-110d0dfc61d6'
SOURCE_PATH = 'icon_set/work/todo-references/note dollar sign_d6e3d9b9-b561-4ac3-8008-110d0dfc61d6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A clipboard displaying a dollar sign.

    Plan: U-shaped board with a centered capsule clip; dollar construction belongs to the board interior.
    Construction reference: notebook: coherent rounded enclosure; clip is reconstructed from the input.
    """
    icon_id = 'note-dollar-sign'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('note', 'dollar', 'sign')

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-a', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-b', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded(self, name, left, top, right, bottom, radius=4):
        r=radius
        pts=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
             (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        names=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8]; n=f'{name}-{i}'; names.append(n)
            if i%2: self.add_arc(n,a,b,radius_x=r)
            else: self.add_line(n,a,b)
        self.add_contour(name,*names,closed=True)

    def clipboard(self):
        # Clip and board share the two nodes (16,12), (32,12).
        self.add_polyline('board', (16,12),(8,12),(8,44),(40,44),(40,12),(32,12))
        self.rounded('clip',16,4,32,12,4)
        self.relate('connect','board','clip')

    def cross(self, name, cx, cy, radius):
        for suffix,end in [('l',(cx-radius,cy)),('r',(cx+radius,cy)),('t',(cx,cy-radius)),('b',(cx,cy+radius))]:
            self.add_line(name+'-'+suffix,(cx,cy),end)
        self.relate('connect',*(name+'-'+s for s in ['l','r','t','b']))

    def build(self):

        self.clipboard()
        # Coherent S with two tangent semicircular lobes and split currency stem.
        self.add_line('s-top',(29,21),(24,21))
        self.add_arc('s-left',(24,21),(24,29),radius_x=4,sweep=False)
        self.add_arc('s-right',(24,29),(24,37),radius_x=4)
        self.add_line('s-bottom',(24,37),(19,37))
        self.add_contour('dollar-s','s-top','s-left','s-right','s-bottom')
        self.add_line('dollar-top',(24,17),(24,21))
        self.add_line('dollar-bottom',(24,37),(24,40))
        self.relate('connect','dollar-top','dollar-s')
        self.relate('connect','dollar-bottom','dollar-s')
