from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3af64961-f052-4e8f-8f05-82873eb08c7f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty hearing_3af64961-f052-4e8f-8f05-82873eb08c7f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ear-with-sound-rays'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ()
    keywords = ('ear', 'with', 'sound', 'rays')

    def build(self):
        # Plan: Ear and three radiating sound strokes; bounds (6,6)-(42,42). Lucide ear guides upper arch and lobe. Inner fold simplified; rays shared radial definition.
        self.path('ear',(6,18),[((6,10),(12,6),(18,6)),((25,6),(28,12),(28,20)),((28,28),(18,30),(18,36)),((18,40),(15,42),(12,42)),((8,42),(6,39),(6,34))])
        self.path('fold',(16,15),[((19,15),(19,22),(16,22))])
        for name,a,z in [('top',(37,12),(42,9)),('middle',(38,24),(42,24)),('bottom',(35,35),(42,39))]:self.add_line(name,a,z)

    def path(self, name, start, commands, closed=False):
        members=[]
        for i, command in enumerate(commands):
            tag=f"{name}-{i}"
            if len(command)==2:
                self.add_line(tag,start,command); start=command
            else:
                self.add_bezier(tag,start,command); start=command[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
