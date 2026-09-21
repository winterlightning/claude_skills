"""Three equal five-point outlined stars in a horizontal row. Lucide star supplies outline; source supplies equal repeats. Shared local point definition at x10,24,38; circle keyshape avoids stretched stars. Required holes and inter-star spaces cannot be discarded."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cf0d9970-8b38-5723-b109-a3be9696acdb'
SOURCE_PATH = 'work/drawn-unpublished-2026-09-21/batch-04/05-three-star-rating/reference.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-star-rating-row-v2'
    variant_of = 'three-star-rating-row'
    variant_label = 'Distilled reconstruction'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('three', 'star', 'rating', 'row', 'v2')

    def build(self):
        def circle(name, x, y, r):
            self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        def path(name, start, commands, closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                part=f'{name}-{i}'
                if kind=='L': self.add_line(part,here,end)
                elif kind=='A': self.add_arc(part,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                else: self.add_bezier(part,here,(args[0],args[1],end))
                here=end; members.append(part)
            self.add_contour(name,*members,closed=closed)
        for i,cx in enumerate((8,24,40)):
            self.add_polyline(f'star-{i}',(cx,20),(cx+1,24),(cx+4,24),(cx+2,26),(cx+3,29),(cx,27),(cx-3,29),(cx-2,26),(cx-4,24),(cx-1,24),closed=True)
