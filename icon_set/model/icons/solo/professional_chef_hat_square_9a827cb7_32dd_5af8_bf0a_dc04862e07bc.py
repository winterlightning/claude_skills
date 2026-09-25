"""Professional Chef Hat.
Symbol plan: Broad three-lobed crown, curling side lobes and square base band. Bounds (6,6)-(42,42).
Construction reference: Supplied square-based toque; Lucide chef-hat crown lobes and flat band.
Reduction: No small fabric folds; inward side curls and square base retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a827cb7-32dd-5af8-bf0a-dc04862e07bc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chef gear hat_9a827cb7-32dd-5af8-bf0a-dc04862e07bc.svg'
AUTHOR = 'gpt-6'

class ProfessionalChefHatSquare(Solo48):
    icon_id = 'professional-chef-hat-square'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('professional', 'chef', 'hat', 'square')

    def build(self):
        axis=24
        self.path('hat',(axis,6),[((18,6),(16,8),(16,12)),((10,10),(6,13),(6,19)),((6,24),(9,26),(12,26)),(12,33),(12,42),(36,42),(36,33),(36,26),((39,26),(42,24),(42,19)),((42,13),(38,10),(32,12)),((32,8),(30,6),(axis,6))],True)
        self.add_line('band',(12,33),(36,33));self.relate('connect','band','hat')
        for j,(a,b) in enumerate([((12,26),(16,24)),((36,26),(32,24))]):self.add_line('curl-'+str(j),a,b);self.relate('connect','curl-'+str(j),'hat')

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
