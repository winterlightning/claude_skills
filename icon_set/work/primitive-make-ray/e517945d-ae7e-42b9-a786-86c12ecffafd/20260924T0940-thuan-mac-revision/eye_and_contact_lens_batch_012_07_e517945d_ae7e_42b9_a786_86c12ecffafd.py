"""Almond eye with circular iris and separate round contact lens.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide: dog (rounded animal contours), pipette (coherent diagonal tool construction).
Human parts: human_ref/full_body_ref.png; no detached human head in these subjects.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e517945d-ae7e-42b9-a786-86c12ecffafd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__eye-and-contact-lens-batch-012-07/20260924T093128Z-thuan-mac/reference/ophthalmic contact lens_e517945d-ae7e-42b9-a786-86c12ecffafd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='eye-and-contact-lens-batch-012-07'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('ophthalmic contact lens',)
    def build(self):
        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                k,end,*args=c; name=f'{n}-{j}'
                if k=='L': self.add_line(name,here,end)
                elif k=='A': self.add_arc(name,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif k=='C': self.add_bezier(name,here,(args[0],args[1],end))
                here=end; members.append(name)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('eye',(18,14),[('C',(30,6),(22,8),(26,6)),('C',(42,18),(36,6),(40,12)),('C',(32,28),(38,26),(36,28))])
        circle('iris',30,17,2)
        circle('lens',15,33,9)
