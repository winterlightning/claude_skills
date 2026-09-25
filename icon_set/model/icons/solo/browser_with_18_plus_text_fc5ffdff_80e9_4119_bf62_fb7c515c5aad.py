from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='fc5ffdff-80e9-4119-bf62-fb7c515c5aad'
SOURCE_PATH='pictographic-primitives/other/browser with 18+ text_fc5ffdff-80e9-4119-bf62-fb7c515c5aad.svg'
AUTHOR="gpt-6"
USER_HEADER_SPACING={"approved_by":"user","visible_gap":4,"scope":"calendar top rim to divider"}
PARENT_RESULT='icon_set/work/primitive-make-ray/fc5ffdff-80e9-4119-bf62-fb7c515c5aad/20260925-text-resize-d586e92a/result.json'
TYPEFACE_GLYPHS=[{'icon_id': 'digit-1', 'character': '1', 'kind': 'digit', 'preferred': True, 'body_top': 2, 'baseline': 17.0, 'body_height': 15.0, 'bounds': [6.0, 2.0, 14.0, 17.0], 'measurement': 'source-body-band', 'paths': ['M 10.0,17.0 L 10.0,2.38816 C 10.0,2.17379 9.82621,2.0 9.61184,2.0 L 6.0,2.0', 'M 10.0,17.0 L 6.0,17.0', 'M 10.0,17.0 L 14.0,17.0'], 'preview_box': [0.0, 0.0, 19.0, 19.0], 'svg_sha256': '504797ca0474536f949b1e4a7e33af00572c82263f08bddb8584593733a1799a', 'source_path': 'Letters/new/1.svg', 'source_sha256': '420e5680b90624d1a1abc967bf3683ff85135508018e2a2abefa492c371207b9', 'author': 'user-supplied', 'geometry_policy': 'source-native-20', 'construction': 'source centerlines and native canvas used unchanged', 'stroke_width': 4, 'ink_width': 12.0, 'ink_height': 19.0, 'ink_left': 4.0, 'ink_top': 0.0, 'centerline_width': 8.0, 'centerline_height': 15.0, 'canvas_width': 19.0, 'canvas_height': 19.0, 'centerline_band_height': 15.0}, {'icon_id': 'digit-8', 'character': '8', 'kind': 'digit', 'preferred': True, 'body_top': 2, 'baseline': 17.0, 'body_height': 15.0, 'bounds': [4.999999999999998, 2.0, 15.0, 17.0], 'measurement': 'source-body-band', 'paths': ['M 5.55556,5.53814 C 5.55556,3.58408 7.094,2.0 8.99177,2.0 L 11.0288,2.0 C 12.9266,2.0 14.465,3.58408 14.465,5.53814 C 14.465,7.49219 12.9266,9.07627 11.0288,9.07627 L 8.99177,9.07627 C 7.094,9.07627 5.55556,7.49219 5.55556,5.53814', 'M 5.0,13.0381 C 5.0,10.8501 6.72269,9.07627 8.84774,9.07627 L 11.1523,9.07627 C 13.2773,9.07627 15.0,10.8501 15.0,13.0381 C 15.0,15.2262 13.2773,17.0 11.1523,17.0 L 8.84774,17.0 C 6.72269,17.0 5.0,15.2262 5.0,13.0381'], 'preview_box': [0.0, 0.0, 19.0, 19.0], 'svg_sha256': '6b669fcdeec43402129b44cc804ce4317dec1c359fb07dd6e8ab175cc808b339', 'source_path': 'Letters/new/8.svg', 'source_sha256': '7b077320062db9973ff03e77c4e7ead35412d57cc9c8d7c5b257d063eed05ea3', 'author': 'user-supplied', 'geometry_policy': 'source-native-20', 'construction': 'source centerlines and native canvas used unchanged', 'stroke_width': 4, 'ink_width': 14.000000000000002, 'ink_height': 19.0, 'ink_left': 2.9999999999999982, 'ink_top': 0.0, 'centerline_width': 10.000000000000002, 'centerline_height': 15.0, 'canvas_width': 19.0, 'canvas_height': 19.0, 'centerline_band_height': 15.0}]
class Drawing(Solo48):
    icon_id='browser-with-18-plus-text'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,rad=3):
        points=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        for i,a in enumerate(points):
            z=points[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,z,radius_x=rad)
            else:self.add_line(n+str(i),a,z)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)
    def glyph(self,n,char,dx,dy,scale=0.6):
        from svgpathtools import parse_path,Line as SvgLine,CubicBezier
        from icon_set.model.primitives import Bezier,Point
        data=next(g for g in TYPEFACE_GLYPHS if g['character']==char and g['preferred'])
        xy=lambda z:(z.real*scale+dx,z.imag*scale+dy)
        for j,d in enumerate(data['paths']):
            members=[]
            for k,s in enumerate(parse_path(d)):
                eid=f'{n}-{j}-{k}';members.append(eid)
                if isinstance(s,SvgLine):self.add_line(eid,xy(s.start),xy(s.end))
                elif isinstance(s,CubicBezier):self.primitives.append(Bezier(eid,Point(*xy(s.start)),Point(*xy(s.end)),((xy(s.control1),xy(s.control2),xy(s.end)),)))
                else:raise ValueError('Unexpected v2 segment')
            self.add_contour(f'{n}-{j}',*members,closed=parse_path(d).isclosed())
    def build(self):
        # User-approved compact header: rim y=10, divider y=18 (4 visible units).
        # Typeface-v2 digit outlines at 60% geometry size; all strokes remain 4 units; no replacement glyphs.
        self.add_polyline('calendar',(4,18),(4,10),(14,10),(34,10),(44,10),(44,18),(44,40),(4,40),closed=True)
        self.add_line('header',(4,18),(44,18));self.relate('connect','calendar','header')
        for x in (14,34):
            self.add_line('binding-'+str(x),(x,8),(x,10));self.relate('connect','calendar','binding-'+str(x))
        self.glyph('one','1',7.6,24.8)
        self.glyph('eight','8',18.4,24.8)
        self.add_polyline('plus-h',(32.8,30.5),(34.8,30.5),(36.8,30.5))
        self.add_polyline('plus-v',(34.8,28.5),(34.8,30.5),(34.8,32.5));self.relate('connect','plus-h','plus-v')

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': 'cb120d38dfe6227ba73d3ebee27ca18bd8775d4e8a990bbba244b896c4d0ccf7', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': 'fc5ffdff-80e9-4119-bf62-fb7c515c5aad'}
