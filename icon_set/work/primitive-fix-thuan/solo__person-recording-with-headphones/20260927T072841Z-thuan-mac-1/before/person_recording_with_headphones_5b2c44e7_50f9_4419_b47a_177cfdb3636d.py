'person-recording-with-headphones: Restore a profile wearing a headphone band and ear cup beside a broad studio microphone on a stand. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '5b2c44e7-50f9-4419-b47a-177cfdb3636d'
SOURCE_PATH = 'pictographic-primitives/audio/microphone podcast person_5b2c44e7-50f9-4419-b47a-177cfdb3636d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-recording-with-headphones'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('person', 'recording', 'with', 'headphones')

    def build(self):
        # Symbol plan: Restore a profile wearing a headphone band and ear cup beside a broad studio microphone on a stand.

        def path(name,start,commands,closed=False):
            members=[];here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): ellipse(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('head',(38,44),[('L',(46,44)),('L',(46,18)),('A',(22,18),12,14,False),('L',(18,28)),('L',(22,28)),('L',(22,36)),('L',(30,36)),('L',(30,44)),('L',(38,44))],True)
        line('band',(35,4),(35,20));circle('earcup',35,23,3);join('band','head');join('band','earcup')
        rounded('microphone',2,12,10,30,4)
        line('mic-stand',(6,30),(6,42));line('mic-base',(2,42),(10,42));join('microphone','mic-stand');join('mic-stand','mic-base')
