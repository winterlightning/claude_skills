"""rectangle like text: standalone batch 17 repair.
All four LIKE letters and the rectangular border retained. Enlarged E spacing, redistributed glyphs and compared three keyshapes. Blocked: frame/letter and letter/letter clearances remain six units; I/K parallel stems are also six units apart.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3d250c41-6017-4d1f-9278-42fadf1fc93d'
SOURCE_PATH = 'pictographic-primitives/other/rectangle like text_3d250c41-6017-4d1f-9278-42fadf1fc93d.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'rectangle-ellipsis'

class Drawing(Solo48):
    icon_id='rectangle-like-text'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('rectangle', 'like', 'text')


    def box(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for j,a in enumerate(pts):
            b=pts[(j+1)%8];name=f'{n}-{j}';names.append(name)
            if j%2:self.add_arc(name,a,b,radius_x=r)
            else:self.add_line(name,a,b)
        self.add_contour(n,*names,closed=True)


        # Exact detached gap: (y+r+8) - (y+r) = 8 centerline / 4 ink.

    def build(self):
        self.box('frame',4,8,40,32,3)
        self.add_polyline('l',(10,16),(10,32),(13,32))
        self.add_line('i',(19,16),(19,32))
        self.add_polyline('k-stem',(25,16),(25,24),(25,32))
        self.add_polyline('k-arms',(29,16),(25,24),(29,32))
        self.relate('connect','k-stem','k-arms')
        self.add_polyline('e',(38,16),(35,16),(35,24),(35,32),(38,32))
        self.add_line('e-middle',(35,24),(38,24))
        self.relate('connect','e','e-middle')

