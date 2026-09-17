"""Pair of String Beans.
Symbol plan: Mirror-related curved pods with pointed tips and curled stems. Bounds (8,4)-(40,44).
Construction reference: Supplied string beans; Lucide bean smooth opposing sides and narrowed ends.
Reduction: No internal ridges; paired curved outlines and short curled stems retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8339c26-b8e4-5270-a72e-978c4d2f8b33'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/stringbean_d8339c26-b8e4-5270-a72e-978c4d2f8b33.svg'
AUTHOR = 'gpt-6'

class PairedStringBean(Solo48):
    icon_id = 'paired-string-bean'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('paired', 'string', 'bean')

    def build(self):
        axis=24
        for j,mirror in enumerate((False,True)):
         def pt(x,y):return (2*axis-x if mirror else x,y)
         self.path('pod-'+str(j),pt(14,12),[(pt(8,12),pt(8,18),pt(8,26)),pt(8,44),(pt(16,41),pt(19,35),pt(19,26)),pt(19,18),(pt(19,14),pt(18,12),pt(14,12))],True)
         self.add_bezier('stem-'+str(j),pt(14,12),(pt(14,8),pt(11,4),pt(8,4)));self.relate('connect','stem-'+str(j),'pod-'+str(j))

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
