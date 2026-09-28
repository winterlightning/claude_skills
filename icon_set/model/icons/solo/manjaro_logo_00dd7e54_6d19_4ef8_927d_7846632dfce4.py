"""Three rectangles stand side by side on a shared base, rising in height from a short left bar to a tall right bar.

Symbol plan: Three identical-width bars on one baseline, heights16,24,32; 16-unit series step. Extremes (4,8)-(44,40).
Review notes: All three source bars retained with eight-unit open separation. Lucide square informs coherent closed contours; heights deliberately ascend left to right.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00dd7e54-6d19-4ef8-927d-7846632dfce4'
SOURCE_PATH = 'pictographic-primitives/logos/manjaro logo_00dd7e54-6d19-4ef8-927d-7846632dfce4.svg'
AUTHOR = 'gpt-6'

class ManjaroLogo(Solo48):
    icon_id = 'manjaro-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('manjaro', 'linux', 'operating-system', 'bars', 'logo', 'brand', 'open-source')

    def build(self):

        def chain(name, *points):
            for i,(start,end) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{i}',start,end)
        def ring(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def rounded(name, left, top, right, bottom, r):
            points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for i,start in enumerate(points):
                end=points[(i+1)%8]; ident=f'{name}-{i}'
                if start==end: continue
                if i%2:self.add_arc(ident,start,end,radius_x=r)
                else:self.add_line(ident,start,end)
                members.append(ident)
            self.add_contour(name,*members,closed=True)
        left,step,width,baseline=4,16,8,40
        for i,height in enumerate((16,24,32)):
            x=left+i*step;top=baseline-height
            self.add_polyline(f'bar-{i}',(x,top),(x+width,top),(x+width,baseline),(x,baseline),closed=True)
