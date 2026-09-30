from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50c9d08d-facc-4f2d-8e34-dc7e97caef61'
SOURCE_PATH = 'icon_set/work/todo-references/person magnifying glass_50c9d08d-facc-4f2d-8e34-dc7e97caef61.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A magnifying glass framing a broad-shouldered person.
    Plan: Lens uses exact integer circle points for shoulder and handle joins; detached inner head.
    Reference: user-search: circular head and magnifier; source places the person inside the lens.
    """
    icon_id = 'person-magnifying-glass'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('person', 'magnifying', 'glass')

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
        # Circle radius 17 has exact integer points with offsets (8,15).
        points=[(15,8),(31,8),(38,15),(38,31),(31,38),(15,38),(8,31),(8,15)]
        for i,p in enumerate(points):self.add_arc(f'rim-{i}',p,points[(i+1)%8],radius_x=17)
        self.add_contour('lens',*(f'rim-{i}' for i in range(8)),closed=True)
        self.add_line('handle',(38,31),(42,42));self.relate('connect','handle','lens')
        self.circle('person-head',23,19,4)
        self.add_arc('person-shoulders',(15,38),(31,38),radius_x=8,radius_y=7)
        self.relate('connect','person-shoulders','lens')

# Final human spacing: Shared human_ref/user.svg inspected. Head (23,19), radius 4, bottom y=23. Shoulder apex (23,31): exact 8 centerline / 4 ink gap. Circular head and broad rounded shoulders retained. Shoulder endpoints (15,38), (31,38) lie exactly on radius-17 lens about (23,23).
