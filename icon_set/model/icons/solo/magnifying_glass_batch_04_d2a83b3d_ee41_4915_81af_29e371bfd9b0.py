"""Independent round magnifier extracted as requested by the component brief. Lucide search supplies circular lens and attached handle. Circle radius15 has integer 9,12 diagonal attachment; lens receiver split at attachment. Plus is a separate sub component."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd2a83b3d-ee41-4915-81af-29e371bfd9b0'
SOURCE_PATH = 'work/drawn-unpublished-2026-09-21/batch-04/08-zoom-in-magnifying-glass/reference.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'magnifying-glass-batch-04'
    variant_of = 'zoom-in-magnifying-glass-batch-033'
    variant_label = 'Distilled reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('magnifying', 'glass', 'batch', '04')

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
        self.add_arc('lens-a',(30,33),(6,21),radius_x=15,large_arc=False)
        self.add_arc('lens-b',(6,21),(30,33),radius_x=15,large_arc=True)
        self.add_contour('lens','lens-a','lens-b',closed=True)
        self.add_line('handle',(30,33),(42,42))
        self.relate('connect','lens','handle')
