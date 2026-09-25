"""A clipped page encloses an upper-left sun and a two-peak mountain silhouette. Lower peak deliberately differs from higher right peak. Lucide file-image informed page and circular-sun construction, source supplies detached closed landscape.
Hosting probes using plus-sign-state-131, heart-state-63, check-mark: invalid, review, invalid. Full content occupies the slot; see batch hosting report.
Whole subject explicitly authorized by user; preserve saved family.
Keyshape: VRECT_XL; fine source details simplified only for native readability.
"""
from ._base import Container64
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '41f3ad63-cd17-441d-b26d-945da63c6f7c'
SOURCE_PATH = 'pictographic-primitives/files/image file_41f3ad63-cd17-441d-b26d-945da63c6f7c.svg'
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
    icon_id = 'landscape-picture-media-file'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'files'
    categories = ('files', 'other', 'primitives-generate')
    aliases = ('Landscape Picture Media File',)
    keywords = ('landscape', 'picture', 'media', 'file')
    def build(self):
        page(self,"page",6,2,58,62,cut=16,radius=3)
        self.add_arc("sun-top",(20,22),(30,22),radius_x=5)
        self.add_arc("sun-bottom",(30,22),(20,22),radius_x=5)
        self.add_contour("sun","sun-top","sun-bottom",closed=True)
        self.add_polyline("mountains",(16,52),(25,38),(31,44),(40,32),(49,52),closed=True)
