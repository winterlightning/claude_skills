"""An upright clipped document with horizontal and vertical dimension markers. Caps share equal spans and axes; document and two measured edges remain distinct. Lucide files informed the page contour; measurement geometry comes from the source.
Hosting probes using plus-sign-state-131, heart-state-63, check-mark: valid, review, valid. Full content occupies the slot; see batch hosting report.
Whole subject explicitly authorized by user; preserve saved family.
Keyshape: SQUARE; fine source details simplified only for native readability.
"""
from ._base import Container64
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '8524400e-0564-4340-8a90-4cd3a0d75a88'
SOURCE_PATH = 'pictographic-primitives/files/paper sizes one document measure_8524400e-0564-4340-8a90-4cd3a0d75a88.svg'
AUTHOR = "gpt-6"

def page(icon, prefix, left, top, right, bottom, cut=10, radius=3):
    pts=[(left+radius,top),(right-cut,top),(right,top+cut),(right,bottom-radius)]
    for j,(a,b) in enumerate(zip(pts,pts[1:]),1):
        icon.add_line(prefix+"-upper-"+str(j),a,b)
    icon.add_arc(prefix+"-br",pts[-1],(right-radius,bottom),radius_x=radius)
    icon.add_line(prefix+"-bottom",(right-radius,bottom),(left+radius,bottom))
    icon.add_arc(prefix+"-bl",(left+radius,bottom),(left,bottom-radius),radius_x=radius)
    icon.add_line(prefix+"-left",(left,bottom-radius),(left,top+radius))
    icon.add_arc(prefix+"-tl",(left,top+radius),pts[0],radius_x=radius)
    icon.add_contour(prefix,prefix+"-upper-1",prefix+"-upper-2",prefix+"-upper-3",prefix+"-br",prefix+"-bottom",prefix+"-bl",prefix+"-left",prefix+"-tl",closed=True)

class Icon(Container64):
    icon_id = 'document-size-measurement'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'files'
    categories = ('files', 'primitives')
    aliases = ('Document Size Measurement',)
    keywords = ('document', 'size', 'measurement')
    def build(self):
        page(self,"page",2,2,46,46,cut=12,radius=3)
        for name,start,end in (("horizontal",(2,58),(46,58)),("vertical",(58,2),(58,46))):
            self.add_line(name,start,end)
            for j,p in enumerate((start,end)):
                x,y=p
                a,b=((x,y-4),(x,y+4)) if name=="horizontal" else ((x-4,y),(x+4,y))
                self.add_line(name+"-cap-"+str(j)+"-a",a,p)
                self.add_line(name+"-cap-"+str(j)+"-b",p,b)
                self.relate("connect",name,name+"-cap-"+str(j)+"-a",name+"-cap-"+str(j)+"-b")
