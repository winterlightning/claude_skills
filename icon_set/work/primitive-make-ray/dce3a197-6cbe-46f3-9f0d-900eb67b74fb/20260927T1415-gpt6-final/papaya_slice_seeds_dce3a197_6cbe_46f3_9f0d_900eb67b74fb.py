"""Papaya Slice with Seeds.
Symbol plan: Elongated asymmetric papaya half with three central seeds. Bounds (8,4)-(40,44).
Construction reference: Supplied papaya; Lucide bean for organic tapered outline.
Reduction: A single cavity arc and two seeds preserve the cut fruit while keeping the flesh band clear at 48 pixels.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'dce3a197-6cbe-46f3-9f0d-900eb67b74fb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__papaya-slice-seeds/20260927T133654Z-thuan-mac-1/reference/papaya slice_dce3a197-6cbe-46f3-9f0d-900eb67b74fb.svg'
AUTHOR = "gpt-6"

class PapayaSliceSeeds(Solo48):
    icon_id = 'papaya-slice-seeds'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('papaya', 'slice', 'seeds')

    def build(self):
        # Broaden the cut fruit so a cavity and seeds have real 4-unit ink
        # clearance instead of collapsing into a bean-shaped silhouette.
        self.path('fruit',(27,4),[((36,4),(40,10),(40,20)),
                                 ((40,32),(30,44),(20,44)),
                                 ((11,44),(8,36),(8,28)),
                                 ((8,16),(18,4),(27,4))],True)
        self.add_bezier('cavity',(24,16),((31,18),(31,27),(26,32)))
        for j,p in enumerate([(17,24),(17,32)]):self.add_dot('seed-'+str(j),p)

    def path(self, name, start, commands, closed=False):
        members=[]
        for j,c in enumerate(commands):
            tag=f'{name}-{j}'
            if len(c)==2:self.add_line(tag,start,c);start=c
            else:self.add_bezier(tag,start,c);start=c[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def loop(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-r',(x,y-ry),(x,y+ry),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-l',(x,y+ry),(x,y-ry),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-r',name+'-l',closed=True)

    def steam(self,x,top,bottom,name):
        mid=(top+bottom)//2
        self.add_bezier(name,(x+1,top),((x-2,top+2),(x-2,mid),(x,mid)),((x+2,mid),(x+2,bottom-2),(x-1,bottom)))
