"""Disconnected Electric Plug and Socket.
Symbol plan: Disconnected diagonal plug and socket use paired semicircular bodies and opposed cords.
Reference construction: unplug.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1324dd3f-6137-461d-894c-e4a5c0b512d1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/plug disconnected_1324dd3f-6137-461d-894c-e4a5c0b512d1.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'diagonal-disconnected-plug-and-socket-pair'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/electronics'
    aliases = ()
    keywords = ('plug', 'socket', 'disconnected', 'cable', 'power', 'connection', 'electric', 'electronics')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def contour(n,*parts,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members) & set(parts)]
            self.add_contour(n,*parts,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
        def rect(n,x,y,w,h,r=0):
            if not r:
                poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2: arc(n+str(i),a,b,r)
                else: line(n+str(i),a,b)
            contour(n,*(n+str(i) for i in range(8)),closed=True)
        line('socket-face',(8,26),(24,38))
        arc('socket-a',(24,38),(10,40),10)
        arc('socket-b',(10,40),(8,26),10)
        contour('socket','socket-face','socket-a','socket-b',closed=True)
        line('socket-cord',(10,40),(8,42))
        poly('plug-face',(24,10),(28,13),(36,19),(40,22))
        arc('plug-a',(40,22),(38,8),10,sweep=False)
        arc('plug-b',(38,8),(24,10),10,sweep=False)
        contour('plug','plug-face-1','plug-face-2','plug-face-3','plug-a','plug-b',closed=True)
        line('plug-cord',(38,8),(40,6))
        for i,(a,b) in enumerate((((28,13),(25,17)),((36,19),(33,23)))):line('prong'+str(i),a,b)
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
