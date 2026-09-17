"""Japanese Dango Rice Dumplings Skewer.
Symbol plan: Three rounded diagonal dumplings with shared occlusion seams and skewer tip. Bounds (6,6)-(42,42).
Construction reference: Supplied dango; no useful direct Lucide food match.
Reduction: Overlapping contours become shared seams; no surface marks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1f111a2-448d-5b0c-a1a7-7f8feffca82b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/japanese sweets dango on stick_c1f111a2-448d-5b0c-a1a7-7f8feffca82b.svg'
AUTHOR = 'gpt-6'

class DangoRiceDumplingSkewer(Solo48):
    icon_id = 'dango-rice-dumpling-skewer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('dango', 'rice', 'dumpling', 'skewer')

    def build(self):
        self.path('lower',(16,24),[((10,24),(6,28),(6,34)),((6,39),(9,42),(14,42)),((19,42),(24,38),(24,32)),(16,24)],True)
        self.path('middle',(16,24),[((16,18),(20,14),(26,14)),(34,22),((34,28),(30,32),(24,32))]);self.relate('connect','middle','lower')
        self.path('upper',(26,14),[((26,9),(29,6),(34,6)),((36,6),(37,7),(38,8)),((40,10),(42,12),(42,15)),((42,20),(38,22),(34,22))]);self.relate('connect','upper','middle')
        self.add_line('stick',(38,8),(40,6));self.relate('connect','stick','upper')

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
