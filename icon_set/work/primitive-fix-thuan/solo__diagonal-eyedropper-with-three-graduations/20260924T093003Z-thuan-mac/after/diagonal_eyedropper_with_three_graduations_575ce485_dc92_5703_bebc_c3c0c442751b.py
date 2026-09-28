"""Bad-stroke revision. Lucide pipette: round bulb and coherent tube; evenly repeated graduation ticks.
Omissions: No graduation removed; tiny nozzle transition simplified.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '575ce485-dc92-5703-bebc-c3c0c442751b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-eyedropper-with-three-graduations/20260924T093003Z-thuan-mac/reference/picker_575ce485-dc92-5703-bebc-c3c0c442751b.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'diagonal-eyedropper-with-three-graduations'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('picker',)
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

        # Three repeated ticks use step(6,-6); a broad diagonal tube owns the series.
        path('pipette',(28,12),[('L',(32,8)),('C',(38,6),(34,6),(36,6)),('C',(42,12),(42,6),(42,10)),('C',(38,22),(42,16),(40,20)),('L',(20,40)),('C',(10,42),(18,42),(14,38)),('L',(6,42)),('L',(6,38)),('C',(10,30),(10,34),(8,32)),('L',(16,24)),('L',(22,18)),('L',(28,12))],True)
        poly('flange',(24,8),(28,12),(38,22),(42,26));join('flange','pipette')
        for i in range(3):
            x,y=10+6*i,30-6*i
            line(f'tick-{i}',(x,y),(x+3,y+3));join('pipette',f'tick-{i}')
