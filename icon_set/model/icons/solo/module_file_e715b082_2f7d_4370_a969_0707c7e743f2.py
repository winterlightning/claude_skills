"""A document contains three square modules below a clipped corner.
Construction reference: none.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e715b082-2f7d-4370-a969-0707c7e743f2'
SOURCE_PATH = 'icon_set/work/todo-references/module file_e715b082-2f7d-4370-a969-0707c7e743f2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'module-file'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('module', 'file')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
    def rect(self,name,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,a in enumerate(pts):
            n=f'{name}-{i}';b=pts[(i+1)%8]
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def build(self):

        # Plan: document envelope; three equal square modules on a 12-unit grid.
        self.add_polyline('document',(8,4),(30,4),(40,14),(40,44),(8,44),closed=True)
        size=8
        for i,(x,y) in enumerate([(20,14),(14,28),(28,28)]):
            self.add_polyline('module-'+str(i),(x,y),(x+size,y),(x+size,y+size),(x,y+size),closed=True)
