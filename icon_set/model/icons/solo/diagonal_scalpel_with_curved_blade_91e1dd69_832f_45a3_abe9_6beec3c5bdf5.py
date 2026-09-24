"""Bad-stroke revision. Lucide pen informed rounded handle cap and diagonal shoulder construction.
Omissions: Redundant narrow collar line omitted; curved blade and handle seam retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '91e1dd69-832f-45a3-abe9-6beec3c5bdf5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/razor cut_91e1dd69-832f-45a3-abe9-6beec3c5bdf5.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'diagonal-scalpel-with-curved-blade'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('razor', 'cut')
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

        # One continuous tool contour; curved lower blade meets a broad handle.
        path('tool',(14,26),[('L',(30,10)),('C',(34,6),(32,8),(32,6)),('A',(42,14),8,8,True),('C',(38,22),(42,18),(40,20)),('L',(24,36)),('C',(6,42),(20,40),(12,40)),('L',(14,26))],True)
        line('blade-seam',(14,26),(24,36));join('tool','blade-seam')
