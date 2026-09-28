"""Okra Vegetable Pod.
Symbol plan: Diagonal tapered pod with a short upper-right stem. Bounds (6,6)-(42,42).
Construction reference: Supplied okra; Lucide bean smooth continuous vegetable outline.
Reduction: The narrow interior ridges would create pinched holes at 48; direction, taper and pointed tip are retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '84924c4f-7965-41fe-a352-1d342cc1460a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__okra-vegetable-pod/20260927T133654Z-thuan-mac-1/reference/okra_84924c4f-7965-41fe-a352-1d342cc1460a.svg'
AUTHOR = 'gpt-6'

class OkraVegetablePod(Solo48):
    icon_id = 'okra-vegetable-pod'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('okra', 'vegetable', 'pod')

    def build(self):
        # The source's long asymmetrical taper and short hooked stem distinguish
        # this pod. Its hairline interior rib would create a pinched hole at 48.
        self.path('pod',(6,42),[((7,27),(18,13),(36,10)),
                                ((42,17),(34,31),(6,42))],True)
        self.add_line('stem',(36,10),(42,6))
        self.relate('connect','stem','pod')

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
