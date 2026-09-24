"""Grinning face with outlined star eyes.
Plan: CIRCLE retains the circular face. Star holes and eye clearance remain inadequate; not visually approved.
Reduction: Grin reduced to one smooth smile arc; stars retained.
Construction references: Original reference supplies the five-point star expression; no useful exact Lucide construction used.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3e7a0a74-079b-41a7-abfe-d06129db8361'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/face grin stars_3e7a0a74-079b-41a7-abfe-d06129db8361.svg'
AUTHOR = "gpt-6"

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
        for i,x in enumerate((17,31)):
            self.add_polyline(f'star-{i}',(x,13),(x+2,17),(x+4,17),(x+3,21),(x+4,25),(x,22),(x-4,25),(x-3,21),(x-4,17),(x-2,17),closed=True)
        self.add_arc('smile',(20,33),(28,33),radius_x=5,sweep=False)