from pathlib import Path
import json,importlib.util,cairosvg
from PIL import Image,ImageDraw
SOURCE_ICON_ID='0005e7b2-b6eb-47bb-9376-770c2522288d'
SOURCE_PATH='pictographic-primitives/computers/batch-06/monitor upload_0005e7b2-b6eb-47bb-9376-770c2522288d.svg'
AUTHOR='gpt-6'
BASE=Path(__file__).parent
entries=json.loads((BASE/'batch-inputs.json').read_text())
HELPERS='''
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,b,radius_x=r)
            else:self.add_line(n+str(i),a,b)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)
    def monitor(self):
        self.box('screen',6,6,36,28,3)
        self.add_line('stand',(24,34),(24,42))
        self.add_polyline('foot',(16,42),(24,42),(32,42))
        self.relate('connect','screen','stand');self.relate('connect','stand','foot')
    def person(self,x,y,r):
        # human_ref/user.svg: head and broad shoulders. Exact 8 centerline / 4 ink gap.
        self.circle('head',x,y,r)
        top=y+r+8
        self.add_arc('shoulders',(x-5,top+5),(x+5,top+5),radius_x=5)
    def play(self,x,y,w,h):
        self.add_polyline('play',(x,y),(x+w,y+h//2),(x,y+h),closed=True)
'''
DESIGNS=[
('SQUARE','Monitor with an upward upload arrow.','Lucide monitor: rounded screen, central stem and foot.','No omissions.',"""
self.monitor()
self.add_polyline('arrowhead',(18,20),(24,14),(30,20))
self.add_line('shaft',(24,14),(24,26));self.relate('connect','arrowhead','shaft')
"""),
('CIRCLE','Sperm cell inside a slashed prohibition circle.','No useful Lucide match for the organic cell.','Slash interrupted around the cell as in the reference.',"""
self.add_arc('ring-a',(12,40),(36,8),radius_x=20)
self.add_arc('ring-b',(36,8),(12,40),radius_x=20)
self.add_contour('ring','ring-a','ring-b',closed=True)
self.add_line('slash-low',(12,40),(18,34));self.relate('connect','ring','slash-low')
self.add_line('slash-high',(30,14),(36,8));self.relate('connect','ring','slash-high')
self.add_bezier('cell',(14,11),((10,11),(12,23),(16,23)),((20,23),(24,18),(22,15)),((20,12),(17,11),(14,11)))
self.add_bezier('tail',(20,21),((30,25),(29,29),(25,32)),((21,35),(25,39),(30,38)))
self.relate('connect','cell','tail')
"""),
('SQUARE','Numbered list with rows one, two and three.','Lucide list-ordered: numeral column and repeated rules.','Compact monoline numerals.',"""
self.add_polyline('one',(6,8),(9,6),(9,12))
self.add_arc('two-top',(6,22),(12,22),radius_x=3)
self.add_polyline('two-base',(12,22),(6,27),(12,27));self.relate('connect','two-top','two-base')
self.add_bezier('three',(6,34),((14,32),(14,38),(9,38)),((15,38),(14,44),(6,42)))
for i,y in enumerate((9,24,39)):self.add_line('row-'+str(i),(22,y),(42,y))
"""),
('SQUARE','Payment monitor with dollar sign and two menu rules.','Lucide monitor: screen and stand.','Compact currency glyph; no semantic omissions.',"""
self.monitor()
self.add_bezier('dollar',(22,15),((20,14),(14,13),(14,17)),((14,20),(22,20),(22,23)),((22,27),(16,26),(14,25)))
self.add_polyline('currency-stem',(18,14),(18,20),(18,26));self.relate('connect','dollar','currency-stem')
for i,y in enumerate((16,24)):self.add_line('menu-'+str(i),(31,y),(33,y))
"""),
('HRECT_L','Business card with portrait and two text rules.','Lucide id-card: enclosure and text; human_ref/user.svg for portrait.','Open shoulders replace the closed shirt outline.',"""
self.box('card',4,8,40,32,3)
self.person(16,19,3)
for i,y in enumerate((19,27)):self.add_line('text-'+str(i),(29,y),(35,y))
"""),
('SQUARE','Square speech bubble containing a question mark.','Lucide monitor enclosure principle; question and tail authored directly.','No omissions.',"""
self.add_polyline('bubble',(9,6),(39,6),(42,9),(42,31),(39,34),(24,34),(16,42),(16,34),(9,34),(6,31),(6,9),closed=True)
self.add_arc('question-top',(19,16),(29,16),radius_x=5)
self.add_bezier('question-hook',(29,16),((29,20),(24,20),(24,23)))
self.add_contour('question','question-top','question-hook')
self.add_dot('question-dot',(24,31))
"""),
('HRECT_L','Rounded video player with central play triangle.','Lucide monitor: tangent rounded enclosure.','No omissions.',"""
self.box('player',4,8,40,32,6)
self.play(19,17,12,14)
"""),
('VRECT_L','Protection shield with a check mark.','Lucide shield: mirrored shoulders and lower bowl.','No omissions.',"""
self.add_bezier('shield',(24,4),((19,8),(13,10),(8,10)),((8,26),(7,35),(24,44)),((41,35),(40,26),(40,10)),((35,10),(29,8),(24,4)))
self.add_polyline('check',(17,24),(22,29),(31,20))
"""),
('SQUARE','Movie player with top and bottom rails and play triangle.','Lucide monitor: rounded frame.','No omissions.',"""
self.box('player',6,6,36,36,3)
for i,y in enumerate((14,34)):
    self.add_line('rail-'+str(i),(6,y),(42,y));self.relate('connect','player','rail-'+str(i))
self.play(20,22,9,8)
"""),
('VRECT_L','Award medal with inset star and notched ribbon.','Lucide star: alternating points and shared mirror axis.','No omissions.',"""
self.circle('medal',24,20,16)
self.add_polyline('star',(24,11),(27,17),(33,18),(28,23),(29,29),(24,26),(19,29),(20,23),(15,18),(21,17),closed=True)
self.add_polyline('ribbon',(12,31),(12,44),(24,38),(36,44),(36,31))
self.relate('connect','medal','ribbon')
"""),
('HRECT_L','Ranking banner crowned with star and folded ribbon ends.','Lucide star: alternating points and shared mirror axis.','Simplified side-tail folds.',"""
self.add_polyline('star',(24,8),(27,16),(35,16),(29,22),(32,30),(24,25),(16,30),(19,22),(13,16),(21,16),closed=True)
self.add_bezier('banner-top',(4,26),((4,22),(12,21),(18,20)))
self.add_bezier('banner-top-right',(30,20),((36,21),(44,22),(44,26)))
self.add_polyline('banner-left',(4,26),(4,34),(13,31))
self.add_polyline('banner-right',(44,26),(44,34),(35,31))
self.add_bezier('banner-bottom',(4,34),((15,29),(33,29),(44,34)))
self.add_polyline('tail-left',(13,31),(13,36),(6,40),(6,36),(4,35),(4,34))
self.add_polyline('tail-right',(35,31),(35,36),(42,40),(42,36),(44,35),(44,34))
for a,b in [('star','banner-top'),('star','banner-top-right'),('banner-top','banner-left'),('banner-top-right','banner-right'),('banner-left','banner-bottom'),('banner-right','banner-bottom'),('banner-left','tail-left'),('banner-right','tail-right'),('banner-bottom','tail-left'),('banner-bottom','tail-right')]:self.relate('connect',a,b)
"""),
('SQUARE','Monitor showing next-track triangle and vertical bar.','Lucide monitor: screen and stand.','No omissions.',"""
self.monitor()
self.play(15,15,9,10)
self.add_line('next-bar',(33,15),(33,25))
"""),
('VRECT_L','Passport booklet with globe and rear-cover reveal.','Lucide monitor rounded enclosure principle; symmetric globe construction.','Rear-cover reveal simplified.',"""
self.box('cover',8,4,32,40,3)
self.circle('globe',24,25,9)
self.add_arc('meridian-left',(24,16),(24,34),radius_x=4,radius_y=9,sweep=False)
self.add_arc('meridian-right',(24,16),(24,34),radius_x=4,radius_y=9)
self.add_polyline('equator',(15,25),(24,25),(33,25))
for a,b in [('globe','meridian-left'),('globe','meridian-right'),('globe','equator'),('meridian-left','meridian-right'),('meridian-left','equator'),('meridian-right','equator')]:self.relate('connect',a,b)
self.add_polyline('rear-cover',(14,4),(36,4),(40,8));self.relate('connect','cover','rear-cover')
"""),
('VRECT_L','Uppercase A with rounded apex and horizontal crossbar.','No useful Lucide letter match; monoline letter authored directly.','No omissions.',"""
self.add_polyline('left-leg',(8,44),(14,29),(22,9))
self.add_arc('apex',(22,9),(26,9),radius_x=2)
self.add_polyline('right-leg',(26,9),(34,29),(40,44))
self.add_contour('letter','left-leg-1','left-leg-2','apex','right-leg-1','right-leg-2')
self.add_line('crossbar',(14,29),(34,29));self.relate('connect','letter','crossbar')
"""),
('VRECT_M','UV level panel with low circular indicator and stem.','Lucide monitor: rounded rectangle enclosure.','No omissions.',"""
self.box('panel',10,4,28,40,3)
self.circle('indicator',24,31,5)
self.add_line('stem',(24,18),(24,26));self.relate('connect','indicator','stem')
"""),
('SQUARE','Movie player with one header rail and play triangle.','Lucide monitor: rounded rectangle frame.','No omissions.',"""
self.box('player',6,6,36,36,3)
self.add_line('header',(6,14),(42,14));self.relate('connect','player','header')
self.play(19,23,12,10)
"""),
('SQUARE','Social profile webpage with header marks, portrait and text.','Lucide id-card: portrait and text; human_ref/user.svg for head and shoulders.','Header dashes become dots; no semantic components omitted.',"""
self.box('page',6,6,36,36,3)
self.add_line('header',(6,16),(42,16));self.relate('connect','page','header')
for i,x in enumerate((14,22,30)):self.add_dot('header-dot-'+str(i),(x,11))
self.person(17,25,3)
for i,y in enumerate((27,35)):self.add_line('text-'+str(i),(30,y),(34,y))
"""),
]
def author():
 for e,(key,plan,refs,omissions,body) in zip(entries,DESIGNS):
    d=Path(e['result_dir']);filename=e['icon_id'].replace('-','_')+'_'+e['source_uuid'].replace('-','_')+'.py'
    text='from icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\n'
    for name,value in [('SOURCE_ICON_ID',e['source_uuid']),('SOURCE_PATH',e['reference_path']),('AUTHOR',AUTHOR),('PLAN',plan),('CONSTRUCTION_REFERENCES',refs),('OMISSIONS',omissions)]:text+=f'{name} = {value!r}\n'
    text+=f'\nclass Drawing(Solo48):\n    icon_id = {e["icon_id"]!r}\n    keyshape = Keyshape.{key}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects/general"\n    aliases = ()\n    keywords = {tuple(e["concept"].lower().split())!r}\n'+HELPERS+'\n    def build(self):\n'+''.join('        '+line+'\n' for line in body.strip().splitlines())
    (d/filename).write_text(text)
def export():
 for i,e in enumerate(entries,1):
    d=Path(e['result_dir']);p=d/(e['icon_id'].replace('-','_')+'_'+e['source_uuid'].replace('-','_')+'.py')
    spec=importlib.util.spec_from_file_location('drawing'+str(i),p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    icon=m.Drawing();r=icon.validate_icon();(d/'validation.txt').write_text(r.describe());svg=icon.to_svg();(d/(e['icon_id']+'.svg')).write_text(svg)
    for theme,bg in [('light','#ffffff'),('dark','#ffffff')]:
      for sz in [48,240]:
        out=d/f'{theme}-{sz}.png';cairosvg.svg2png(bytestring=svg.encode(),write_to=str(out),output_width=sz,output_height=sz,background_color=bg)
        if theme=='dark':
          from PIL import ImageOps
          ImageOps.invert(Image.open(out).convert('RGB')).save(out)
    data=dict(e,author=AUTHOR,module=p.name,keyshape=icon.keyshape.name,subject_and_plan=m.PLAN,construction_references=m.CONSTRUCTION_REFERENCES,omissions=m.OMISSIONS,validation_status=r.status,validation_findings=r.describe(),validation_errors=len(r.errors),validation_warnings=len(r.warnings),svg=e['icon_id']+'.svg')
    (d/'review-draft.json').write_text(json.dumps(data,indent=2));print(i,e['concept'],r.describe(),flush=True)
def sheet():
 s=Image.new('RGB',(1200,1100),'#eeeeee');dr=ImageDraw.Draw(s)
 for i,e in enumerate(entries):
    d=Path(e['result_dir']);x=i%4*300;y=i//4*220
    for j,theme in enumerate(['light','dark']):
      im=Image.open(d/f'{theme}-240.png').convert('RGB').resize((140,140));s.paste(im,(x+j*150,y+20));s.paste(Image.open(d/f'{theme}-48.png').convert('RGB'),(x+j*150+46,y+163))
    dr.text((x+3,y+3),f'{i+1} {e["concept"][:34]}',fill='black')
 s.save(BASE/'review-sheet.png')
if __name__=='__main__':
 import sys
 # Final authored modules are authoritative; do not regenerate initial drafts.
 export();sheet()
