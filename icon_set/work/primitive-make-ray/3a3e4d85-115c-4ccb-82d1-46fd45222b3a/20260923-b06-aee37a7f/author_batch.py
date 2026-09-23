"""Standalone batch-06 authoring, exports remain beside each input metadata file."""
from pathlib import Path
import importlib.util
import json
import io
import traceback
import cairosvg
from PIL import Image, ImageDraw

AUTHOR = "gpt-6"
ENTRIES = json.loads(Path(__file__).with_name("batch-inputs.json").read_text())
SOURCE_ICON_ID = tuple(e["source_uuid"] for e in ENTRIES)
SOURCE_PATH = tuple(e["reference_path"] for e in ENTRIES)

HELPERS = '''
    def path(self, name, start, commands, closed=False):
        members = []
        point = start
        for i, command in enumerate(commands):
            member = f"{name}-{i}"
            target = command[1]
            if command[0] == "L":
                self.add_line(member, point, target)
            else:
                self.add_arc(member, point, target, radius_x=command[2],
                             radius_y=command[3], sweep=command[4])
            members.append(member)
            point = target
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), [("A",(x+r,y),r,r,True),
                                  ("A",(x-r,y),r,r,True)], True)

    def browser(self):
        # VRECT_L gives the enclosed marks a taller content area.
        self.path("browser-top", (8,12), [("L",(8,8)),
            ("A",(12,4),4,4,True),("L",(36,4)),
            ("A",(40,8),4,4,True),("L",(40,12))])
        self.path("browser-right", (40,12), [("L",(40,40)),
            ("A",(36,44),4,4,True)])
        self.add_line("browser-bottom",(36,44),(12,44))
        self.path("browser-left", (12,44), [
            ("A",(8,40),4,4,True),("L",(8,12))])
        self.add_line("header",(8,12),(40,12))
        for name in ("browser-right","browser-left"):
            self.relate("connect",name,"browser-bottom")
            self.relate("connect",name,"browser-top")
        for name in ("browser-top","browser-right","browser-left"):
            self.relate("connect", name, "header")

    def calendar(self, header=True, three=False):
        # Repeated bindings terminate at the top rim; retain exact 8-unit header.
        rings = (14,24,34) if three else (14,34)
        top = [("L",(x,10)) for x in rings] + [("L",(38,10)),
            ("A",(42,14),4,4,True),("L",(42,18))]
        self.path("calendar-top",(6,18),[("L",(6,14)),
            ("A",(10,10),4,4,True)]+top)
        self.path("calendar-body",(42,18),[("L",(42,38)),
            ("A",(38,42),4,4,True),("L",(10,42)),
            ("A",(6,38),4,4,True),("L",(6,18))])
        self.relate("connect","calendar-top","calendar-body")
        for x in rings:
            name=f"binding-{x}"
            self.add_line(name,(x,6),(x,10))
            self.relate("connect",name,"calendar-top")
        if header:
            self.add_line("header",(6,18),(42,18))
            for name in ("calendar-top","calendar-body"):
                self.relate("connect",name,"header")
'''

SPECS = [
dict(key="VRECT_L", refs=["panels-top-left", "human_ref/user.svg"],
     description="A browser window containing a circular user head and open shoulder bust.",
     omissions=["Two tiny browser title-bar marks omitted to preserve the 8-unit header band."],
     plan="Upright browser encloses a detached user bust; mirrored shoulders about x=24. Head bottom y=26, shoulder top y=34 gives exactly 4 ink units.",
     body='''
        self.browser()
        # Shared human_ref/user.svg: circular head, smooth broad open shoulders.
        self.circle("head",24,23,3)
        self.path("shoulders",(17,36),[("A",(24,34),7,2,True),
            ("A",(31,36),7,2,True)])
'''),
dict(key="VRECT_L", refs=["panels-top-left","pound-sterling"],
     description="A browser with a pound sterling sign aligned to the lower right.",
     omissions=["Tiny browser title-bar marks omitted."],
     plan="Browser enclosure plus a right-aligned pound with rounded hook, horizontal crossbar and foot. Right alignment is intentional.",
     body='''
        self.browser()
        x=23
        self.path("pound-stem",(x+8,24),[("A",(x,24),4,4,False),
            ("L",(x,27)),("L",(x,35))])
        self.add_polyline("pound-foot",(x-4,35),(x,35),(x+8,35))
        self.add_polyline("pound-bar",(x-4,27),(x,27),(x+4,27))
        self.relate("connect","pound-stem","pound-foot")
        self.relate("connect","pound-stem","pound-bar")
'''),
dict(key="VRECT_L", refs=["panels-top-left","pound-sterling"],
     description="A browser with a centered pound sterling sign.",
     omissions=["Tiny browser title-bar marks omitted."],
     plan="Browser enclosure plus centered pound hook, stem, crossbar and foot; curve and stem have vertical tangent continuity.",
     body='''
        self.browser()
        x=22
        self.path("pound-stem",(x+8,24),[("A",(x,24),4,4,False),
            ("L",(x,27)),("L",(x,35))])
        self.add_polyline("pound-foot",(x-4,35),(x,35),(x+8,35))
        self.add_polyline("pound-bar",(x-4,27),(x,27),(x+4,27))
        self.relate("connect","pound-stem","pound-foot")
        self.relate("connect","pound-stem","pound-bar")
'''),
dict(key="SQUARE", refs=["calendar"],
     description="A two-binding calendar-like browser displaying 18+ as in the source.",
     omissions=["Binding tails inside the header omitted; the two bindings remain."],
     plan="Calendar enclosure contains hand-authored 1, two circular lobes of 8 and plus; all three characters retained.",
     body='''
        self.calendar()
        self.add_polyline("one",(13,26),(16,24),(16,35))
        self.circle("eight-top",24,26,2)
        self.circle("eight-bottom",24,32,4)
        self.relate("connect","eight-top","eight-bottom")
        self.add_polyline("plus-horizontal",(32,30),(35,30),(38,30))
        self.add_polyline("plus-vertical",(35,27),(35,30),(35,33))
        self.relate("connect","plus-horizontal","plus-vertical")
'''),
dict(key="VRECT_L", refs=["panels-top-left","japanese-yen"],
     description="A browser containing a right-aligned yuan sign with one crossbar.",
     omissions=["Tiny browser title-bar marks omitted."],
     plan="Upright browser frame and one-bar yuan. Repeated arm endpoints mirror about x=26; symbol placement intentionally right-aligned.",
     body='''
        self.browser()
        x=26
        self.add_polyline("yuan-fork",(x-5,21),(x,27),(x+5,21))
        self.add_polyline("yuan-stem",(x,27),(x,30),(x,35))
        self.add_polyline("yuan-bar",(x-4,30),(x,30),(x+4,30))
        self.relate("connect","yuan-fork","yuan-stem")
        self.relate("connect","yuan-stem","yuan-bar")
'''),
dict(key="VRECT_L", refs=["panels-top-left","japanese-yen"],
     description="A browser containing a centered yuan sign with one crossbar.",
     omissions=["Tiny browser title-bar marks omitted."],
     plan="Browser frame and one-bar yuan mirrored about x=24; one crossbar follows the source rather than Lucide's two.",
     body='''
        self.browser()
        x=24
        self.add_polyline("yuan-fork",(x-6,21),(x,27),(x+6,21))
        self.add_polyline("yuan-stem",(x,27),(x,30),(x,35))
        self.add_polyline("yuan-bar",(x-4,30),(x,30),(x+4,30))
        self.relate("connect","yuan-fork","yuan-stem")
        self.relate("connect","yuan-stem","yuan-bar")
'''),
dict(key="SQUARE", refs=["message-square"],
     description="An oval message bubble with a lower-left tail and PM lettering.",
     omissions=[],
     plan="One coherent oval-and-tail contour surrounds a round-bow P and angular M. Tail asymmetry follows the reference.",
     body='''
        self.path("bubble",(6,22),[("A",(24,6),18,16,True),
            ("A",(42,22),18,16,True),("A",(24,38),18,16,True),
            ("L",(18,37)),("L",(8,42)),("L",(11,32)),
            ("A",(6,22),18,16,True)],True)
        self.add_polyline("p-stem",(14,29),(14,22),(14,16))
        self.path("p-bow",(14,16),[("L",(17,16)),
            ("A",(17,22),3,3,True),("L",(14,22))])
        self.relate("connect","p-stem","p-bow")
        self.add_polyline("m",(25,29),(28,16),(31,25),(34,16),(37,29))
'''),
dict(key="VRECT_L", refs=["cup-soda","heart"],
     description="A tapered bubble-tea cup with straw, horizontal lid and heart motif.",
     omissions=["Secondary lid seam omitted; single lid retains the cup construction."],
     plan="Cup and centered straw on x=24, mirrored cup walls and heart lobes. VRECT_L gives the upright straw room, extremes 8,4,40,44.",
     body='''
        self.add_polyline("lid",(8,12),(24,12),(40,12))
        self.add_line("straw",(24,4),(24,12))
        self.relate("connect","straw","lid")
        self.path("cup",(8,12),[("L",(10,40)),
            ("A",(14,44),4,4,False),("L",(34,44)),
            ("A",(38,40),4,4,False),("L",(40,12))])
        self.relate("connect","cup","lid")
        self.path("heart",(24,25),[("A",(18,25),3,3,False),
            ("A",(19,29),6,6,False),("L",(24,35)),
            ("L",(29,29)),("A",(30,25),6,6,False),
            ("A",(24,25),3,3,False)],True)
'''),
dict(key="SQUARE", refs=["calendar"],
     description="A three-binding calendar showing the arithmetic expression 2+1.",
     omissions=["Binding tails inside the calendar omitted."],
     plan="Three evenly repeated bindings with no header divider, matching the source. Hand-authored 2, plus and 1 remain in source order.",
     body='''
        self.calendar(header=False,three=True)
        self.path("two",(12,23),[("A",(20,23),4,4,True),
            ("A",(18,27),5,5,True),("L",(12,34)),("L",(20,34))])
        self.add_polyline("plus-horizontal",(24,27),(28,27),(32,27))
        self.add_polyline("plus-vertical",(28,23),(28,27),(28,31))
        self.relate("connect","plus-horizontal","plus-vertical")
        self.add_polyline("one",(34,22),(37,20),(37,34))
'''),
dict(key="SQUARE", refs=["calendar"],
     description="A two-binding calendar displaying a single numeral seven.",
     omissions=["Binding tails inside the header omitted."],
     plan="Calendar with an 8-unit header and seven centered in the lower panel; right-slanted seven preserves intentional directional asymmetry.",
     body='''
        self.calendar()
        self.add_polyline("seven",(20,26),(30,26),(25,33))
'''),
dict(key="SQUARE", refs=["calendar"],
     description="A calendar containing a diagonal telephone handset.",
     omissions=["Binding tails inside the header omitted."],
     plan="Calendar plus continuous handset silhouette; diagonal receiver preserves the source's lower-left to upper-right bends.",
     body='''
        self.calendar()
        self.path("handset",(16,25),[("A",(20,24),3,3,True),
            ("L",(23,27)),("L",(20,30)),("L",(26,35)),
            ("L",(29,32)),("L",(33,35)),
            ("A",(31,39),3,3,True),("A",(14,27),20,20,True),
            ("L",(16,25))],True)
'''),
dict(key="SQUARE", refs=["calendar"],
     description="A three-binding calendar containing a three-sector pie chart.",
     omissions=["Binding tails inside the calendar omitted."],
     plan="Calendar without header and centered circular pie. Radial dividers share one center and actual circle endpoints; unequal sectors preserve the source.",
     body='''
        self.calendar(header=False,three=True)
        self.path("pie",(24,18),[("A",(34,28),10,10,True),
            ("A",(18,36),10,10,True),("A",(24,18),10,10,True)],True)
        for name,end in [("pie-up",(24,18)),("pie-right",(34,28)),("pie-diagonal",(18,36))]:
            self.add_line(name,(24,28),end)
            self.relate("connect",name,"pie")
        for a,b in [("pie-up","pie-right"),("pie-up","pie-diagonal"),("pie-right","pie-diagonal")]:
            self.relate("connect",a,b)
'''),
dict(key="SQUARE", refs=["file-video-camera"],
     description="An upright document with clipped upper-right corner and a camera symbol.",
     omissions=[],
     plan="SQUARE document contour with clipped corner gives the enclosed camera more width; camera retains raised prism and lens point. Asymmetric page corner follows source.",
     body='''
        self.path("document-upper",(10,6),[("L",(34,6)),("L",(42,14)),
            ("L",(42,38)),("A",(38,42),4,4,True)])
        self.add_line("document-bottom",(38,42),(10,42))
        self.path("document-left",(10,42),[("A",(6,38),4,4,True),
            ("L",(6,10)),("A",(10,6),4,4,True)])
        self.relate("connect","document-upper","document-left")
        self.relate("connect","document-upper","document-bottom")
        self.relate("connect","document-left","document-bottom")
        self.path("camera",(17,18),[("L",(20,18)),("L",(22,15)),
            ("L",(26,15)),("L",(28,18)),("L",(31,18)),
            ("A",(33,20),2,2,True),("L",(33,32)),
            ("A",(31,34),2,2,True),("L",(17,34)),
            ("A",(15,32),2,2,True),("L",(15,20)),
            ("A",(17,18),2,2,True)],True)
        self.add_dot("lens",(24,25))
'''),
]

def run():
    for entry, spec in zip(ENTRIES, SPECS):
        d=Path(entry['dir'])
        if (d/'result.json').exists():
            continue
        stem=entry['icon_id'].replace('-','_')+'_'+entry['source_uuid'].replace('-','_')
        source='\n'.join([
            '"""'+spec['description']+'\nPlan: '+spec['plan']+'"""',
            'from icon_set.model.keyshapes import Keyshape',
            'from icon_set.model.icons.solo._base import Solo48',
            f'SOURCE_ICON_ID = {entry["source_uuid"]!r}',
            f'SOURCE_PATH = {entry["reference_path"]!r}',
            f'AUTHOR = {AUTHOR!r}',
            f'CONSTRUCTION_REFERENCES = {spec["refs"]!r}',
            'class Drawing(Solo48):',
            f'    icon_id = {entry["icon_id"]!r}',
            f'    keyshape = Keyshape.{spec["key"]}',
            '    semantic_role = "MAIN"', '    semantic_kind = "noun"',
            '    category = "objects/media"','    aliases = ()',
            f'    keywords = {tuple(entry["concept"].split())!r}',
            HELPERS, '    def build(self):', spec['body'],
        ])
        path=d/(stem+'.py');path.write_text(source)
        record=dict(**entry,**{k:v for k,v in spec.items() if k!='body'},python=path.name)
        try:
            loader=importlib.util.spec_from_file_location(stem,path)
            module=importlib.util.module_from_spec(loader);loader.loader.exec_module(module)
            icon=module.Drawing(); report=icon.validate_icon()
            (d/'validation.txt').write_text(report.describe())
            record['validation_status']=report.status
            record['validation_findings']=report.describe()
            svg=icon.to_svg(); (d/(entry['icon_id']+'.svg')).write_text(svg)
            for size in (48,192):
                # Render the unmodified model SVG. Theme is a raster foreground/background presentation.
                raw=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size))).convert('RGBA')
                alpha=raw.getchannel('A')
                for theme,bg,fg in [('light','white','#111111'),('dark','#15191f','#f5f5f5')]:
                    im=Image.new('RGB',(size,size),bg); im.paste(Image.new('RGB',(size,size),fg),(0,0),alpha)
                    im.save(d/f'{theme}-{size}.png')
            record['svg']=entry['icon_id']+'.svg'
        except Exception:
            record['validation_status']='error'
            record['error']=traceback.format_exc()
            (d/'error.txt').write_text(record['error'])
        # Draft findings: final result is written only after visual inspection.
        (d/'attempt-findings.json').write_text(json.dumps(record,indent=2))
        print(entry['concept'],record['validation_status'],flush=True)
    sheet=Image.new('RGB',(800,240*len(ENTRIES)),'#c6cbd0');draw=ImageDraw.Draw(sheet)
    for i,e in enumerate(ENTRIES):
        d=Path(e['dir']);y=i*240
        for x,name in [(0,'reference-192.png'),(200,'light-192.png'),(400,'dark-192.png'),(610,'light-48.png'),(680,'dark-48.png')]:
            if (d/name).exists():sheet.paste(Image.open(d/name),(x,y))
        draw.text((5,y+200),str(i+1)+'. '+e['concept'],fill='black')
    sheet.save(Path(__file__).with_name('comparison.png'))

if __name__=='__main__':
    run()
