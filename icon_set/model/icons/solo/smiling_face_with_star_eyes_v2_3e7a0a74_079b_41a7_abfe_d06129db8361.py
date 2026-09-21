"""Circular smiling face with two matched five-point star eyes. Shared x=24 symmetry; star holes remain mandatory. Lucide star supplies five-tip contour; supplied reference owns expression."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3e7a0a74-079b-41a7-abfe-d06129db8361'
SOURCE_PATH = 'work/drawn-unpublished-2026-09-21/batch-04/01-star-struck-face/reference.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-face-with-star-eyes-v2'
    variant_of = 'smiling-face-with-star-eyes'
    variant_label = 'Distilled reconstruction'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('smiling', 'face', 'with', 'star', 'eyes', 'v2')

    def build(self):
        def circle(name, x, y, r):
            self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        def path(name, start, commands, closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                part=f'{name}-{i}'
                if kind=='L': self.add_line(part,here,end)
                elif kind=='A': self.add_arc(part,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                else: self.add_bezier(part,here,(args[0],args[1],end))
                here=end; members.append(part)
            self.add_contour(name,*members,closed=closed)
        circle('face',24,24,20)
        for i,cx in enumerate((17,31)):
            self.add_polyline(f'star-{i}',(cx,15),(cx+1,18),(cx+3,18),(cx+2,20),(cx+2,23),(cx,21),(cx-2,23),(cx-2,20),(cx-3,18),(cx-1,18),closed=True)
        path('smile',(16,32),[('C',(32,32),(20,37),(28,37))])
