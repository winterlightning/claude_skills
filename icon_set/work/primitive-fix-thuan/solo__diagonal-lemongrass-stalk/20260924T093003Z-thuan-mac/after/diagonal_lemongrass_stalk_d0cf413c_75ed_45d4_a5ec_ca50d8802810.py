"""Bad-stroke revision. No useful exact Lucide match; coherent tapering curves and shared leaf junctions.
Omissions: Fine root hairs, internal vein and one crowded leaf tip omitted; bulb and two branching blades preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd0cf413c-75ed-45d4-a5ec-ca50d8802810'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-lemongrass-stalk/20260924T093003Z-thuan-mac/reference/lemongrass_d0cf413c-75ed-45d4-a5ec-ca50d8802810.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'diagonal-lemongrass-stalk'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('lemongrass',)
    def build(self):

        # Typed continuous paths own their junctions. Repeated parts share parameters.
        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i, (kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                ids.append(ident);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        # Bulb and tapering sheath flow into a fork of two long leaves.
        path('stalk',(10,42),[('C',(6,34),(6,42),(6,38)),('C',(16,24),(6,30),(12,27)),('C',(30,6),(23,17),(27,11)),('L',(27,20)),('L',(42,6)),('C',(20,36),(34,21),(26,29)),('C',(10,42),(17,41),(14,42))],True)
