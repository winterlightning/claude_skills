from pathlib import Path
import json,re,ast,shutil,textwrap
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='fix-batch-20260924T172356/claims.json'
ROOT=Path('icon_set/work/primitive-make-ray');BATCH=ROOT/'fix-batch-20260924T172356'
tree=ast.parse((ROOT/'fix-batch-20260924/author.py').read_text())
HELPERS=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='HELPERS' for t in n.targets))
HELPERS=HELPERS.replace("self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)","self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)")
cases={}
def case(i,k,refs,plan,body,omissions='None'):cases[i]=(k,refs,plan,textwrap.dedent(body),omissions)
case(0,'SQUARE',['sliders-vertical'],'Two evenly constructed sliders beside a Bitcoin B, with round bowls and two currency stems.', '''
for n,x,y in [('low',10,32),('high',22,14)]:
    self.path(n,(x,y-4),[('L',(x+4,y-4)),('L',(x+4,y+4)),('L',(x,y+4)),('L',(x-4,y+4)),('L',(x-4,y-4)),('L',(x,y-4))],True)
    self.add_line(n+'-up',(x,6),(x,y-4));self.add_line(n+'-down',(x,y+4),(x,42))
    self.relate('connect',n,n+'-up');self.relate('connect',n,n+'-down')
self.path('bitcoin',(34,8),[('L',(35,8)),('A',(35,24),7,8,True),('A',(35,40),7,8,True),('L',(34,40)),('L',(34,24)),('L',(34,8))],True)
self.add_line('divider',(34,24),(35,24));self.relate('connect','divider','bitcoin')
for y,z in [(6,8),(40,42)]:
    self.add_line('currency-'+str(y),(34,y),(34,z));self.relate('connect','bitcoin','currency-'+str(y))
''','Second Bitcoin stem reduced to one at 48px.')
case(1,'VRECT_L',['calendar'],'Calendar with identical rounded corners and bindings; phone receiver is one coherent flowing contour.', '''
self.path('frame',(12,8),[('L',(16,8)),('L',(32,8)),('L',(36,8)),('A',(40,12),4,4,True),('L',(40,17)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,17)),('L',(8,12)),('A',(12,8),4,4,True)],True)
self.add_line('header',(8,17),(40,17));self.relate('connect','header','frame')
for x in (16,32):
    self.add_line('binding-'+str(x),(x,4),(x,8));self.relate('connect','binding-'+str(x),'frame')
self.path('phone',(20,26),[('L',(17,29)),('C',(27,36),(19,33),(23,36)),('L',(31,32)),('L',(28,29))])
''','Handset pads rendered as short ends instead of tiny enclosed pads.')
case(2,'HRECT_L',['ticket','plane'],'Boarding ticket with matching rounded corners and semicircular notches, enclosing a clean diagonal plane mark.', '''
self.path('ticket',(8,8),[('L',(40,8)),('A',(44,12),4,4,True),('L',(44,20)),('A',(44,28),4,4,False),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,28)),('A',(4,20),4,4,False),('L',(4,12)),('A',(8,8),4,4,True)],True)
self.add_polyline('plane',(16,27),(20,31),(27,24),(33,18))
self.add_line('wing',(20,17),(27,24));self.relate('connect','plane','wing')
''','Ticket divider and plane outline reduced to readable wing, fuselage and tail strokes.')
case(3,'VRECT_L',['network'],'Molecule with three round outer nodes and a round central node, joined by three straight bonds.', '''
for n,x,y,r in [('top',13,9,5),('bottom',13,39,5),('center',25,25,5),('right',35,15,5)]:self.circle(n,x,y,r)
for n,a,b,left,right in [('top-link',(16,13),(22,21),'top','center'),('bottom-link',(16,35),(22,29),'bottom','center'),('right-link',(28,21),(32,19),'center','right')]:
    self.add_line(n,a,b);self.relate('connect',n,left);self.relate('connect',n,right)
''')
case(4,'SQUARE',['soup'],'A smooth semicircular grill bowl on matching splayed legs under three gentle smoke curves.', '''
self.path('bowl',(6,22),[('L',(42,22)),('C',(33,32),(42,27),(38,31)),('C',(24,34),(30,34),(27,34)),('C',(15,32),(21,34),(18,34)),('C',(6,22),(10,31),(6,27))],True)
for n,x,z in [('left',15,10),('right',33,38)]:
    self.add_line('leg-'+n,(x,32),(z,42));self.relate('connect','leg-'+n,'bowl')
for j,x in enumerate((14,24,34)):
    self.path('smoke-'+str(j),(x,6),[('C',(x,13),(x-3,8),(x+3,11))])
''','Lower leg brace omitted to preserve open space.')
case(5,'CIRCLE',[],'Question mark has a smooth round hook, short vertical return and distinct dot centered within a true circle.', '''
self.circle('ring',24,24,20)
self.path('question',(18,19),[('A',(30,19),6,6,True),('C',(24,27),(30,23),(24,23)),('L',(24,28))])
self.add_dot('dot',(24,36))
''')
case(6,'HRECT_M',[],'Sun visor with a mirrored domed band and smoothly scalloped brim; paired curves share horizontal and vertical tangents.', '''
self.path('visor',(4,30),[('L',(6,20)),('C',(24,10),(6,14),(14,10)),('C',(42,20),(34,10),(42,14)),('L',(44,30)),('C',(37,38),(44,35),(41,38)),('C',(24,34),(33,38),(30,34)),('C',(11,38),(18,34),(15,38)),('C',(4,30),(7,38),(4,35))],True)
self.path('band',(4,30),[('C',(24,22),(10,25),(17,22)),('C',(44,30),(31,22),(38,25))])
self.relate('connect','band','visor')
''')
case(7,'CIRCLE',['globe','network'],'Three circular nodes form a smooth triangular network inside a circular globe.', '''
self.circle('globe',24,24,20)
for n,x,y in [('a',24,15),('b',14,27),('c',33,29)]:self.circle(n,x,y,3)
self.path('ab',(21,15),[('C',(14,24),(18,16),(14,20))]);self.relate('connect','ab','a');self.relate('connect','ab','b')
self.path('ac',(27,15),[('C',(33,26),(31,17),(33,21))]);self.relate('connect','ac','a');self.relate('connect','ac','c')
self.path('bc',(17,27),[('C',(30,29),(21,27),(27,28))]);self.relate('connect','bc','b');self.relate('connect','bc','c')
''','Meridian extension to outer circle omitted to preserve node spacing.')
case(8,'SQUARE',[],'Tilting hand truck with a round wheel, bent handle, and a square load derived from perpendicular integer vectors.', '''
self.path('handle',(6,6),[('L',(9,6)),('C',(13,10),(12,6),(12,7)),('L',(17,30))])
self.circle('wheel',17,36,6);self.relate('connect','handle','wheel')
self.add_polyline('load',(21,18),(35,14),(39,28),(25,32),closed=True)
self.add_polyline('platform',(23,36),(25,32),(39,28),(42,27))
self.relate('connect','wheel','platform');self.relate('connect','load','platform')
''','Small trailing wheel omitted; primary wheel and tilting load retained.')
case(9,'SQUARE',[],'Tooth with mirrored flowing crown and roots, beside a dental pick with a round bent tip.', '''
self.path('tooth',(30,9),[('C',(24,6),(27,9),(27,6)),('C',(18,14),(20,6),(18,10)),('C',(21,25),(18,19),(21,21)),('C',(24,35),(21,30),(21,35)),('C',(30,25),(27,35),(27,25)),('C',(36,35),(33,25),(33,35)),('C',(39,25),(39,35),(39,30)),('C',(42,14),(39,21),(42,19)),('C',(36,6),(42,10),(40,6)),('C',(30,9),(33,6),(33,9))],True)
self.path('pick',(11,12),[('L',(8,15)),('C',(6,20),(6,17),(6,18)),('C',(9,26),(6,22),(7,24)),('L',(19,42))])
''','Double wall of dental pick reduced to a consistent single centerline.')
case(10,'SQUARE',[],'A diagonal toothpaste tube over a horizontal toothbrush; matching nozzle and brush curves.', '''
self.add_polyline('tube',(26,6),(42,18),(28,30),(20,24),closed=True)
self.add_line('nozzle',(20,24),(16,28));self.relate('connect','tube','nozzle')
self.path('brush',(6,42),[('L',(14,42)),('L',(24,42)),('C',(34,38),(29,42),(29,38)),('L',(42,38))])
for x in (6,14):
    self.add_line('bristle-'+str(x),(x,34),(x,42));self.relate('connect','bristle-'+str(x),'brush')
''','Detached toothpaste dollop and fine bristle subdivisions omitted due to clearance.')
case(11,'HRECT_L',['hand'],'Two matching upright fingertips under a smooth leftward motion arrow, with a clearly open arrowhead.', '''
for i,x in enumerate((9,29)):
    self.path('finger-'+str(i),(x,40),[('L',(x,29)),('A',(x+10,29),5,5,True),('L',(x+10,40))])
self.path('swipe',(44,16),[('C',(24,8),(38,11),(31,8)),('C',(4,16),(17,8),(10,11))])
self.add_polyline('head',(10,8),(4,16),(14,16));self.relate('connect','swipe','head')
''')
case(12,'HRECT_L',['hand'],'Horizontal paired fingers beside a single smooth descending gesture arrow.', '''
self.path('upper',(4,14),[('L',(26,14)),('A',(26,22),4,4,True),('L',(4,22))])
self.add_line('lower',(4,32),(21,32))
self.path('swipe',(36,8),[('C',(44,23),(41,12),(44,17)),('C',(34,40),(44,29),(40,35))])
self.add_polyline('head',(31,31),(34,40),(43,37));self.relate('connect','head','swipe')
''','Second finger kept as a single open lower edge as in the reference.')
case(13,'HRECT_L',['hand'],'Two matching finger arches below a gently curved rightward swipe arrow.', '''
for i,x in enumerate((4,30)):
    self.path('finger-'+str(i),(x,40),[('L',(x,31)),('A',(x+14,31),7,7,True),('L',(x+14,40))])
self.path('swipe',(20,8),[('C',(42,16),(29,8),(36,12))])
self.add_polyline('head',(36,8),(42,16),(32,16));self.relate('connect','head','swipe')
''')
case(14,'SQUARE',['pen-tool'],'Diagonal pen nib with straight symmetric flanks, clean slit and square cap, beside a plus sign.', '''
self.add_polyline('nib',(6,42),(16,22),(27,17),(37,27),(32,38),(6,42),closed=True)
self.path('cap',(27,17),[('L',(36,8)),('C',(39,8),(37,6),(38,6)),('L',(42,11)),('L',(37,27))])
self.relate('connect','nib','cap')
self.add_line('slit',(6,42),(22,26));self.relate('connect','slit','nib')
self.add_polyline('plus-h',(6,12),(12,12),(18,12));self.add_polyline('plus-v',(12,6),(12,12),(12,18));self.relate('connect','plus-h','plus-v')
''')
case(15,'HRECT_L',['hand'],'Horizontal finger with rounded nail and a smoothly bowed downward motion arrow.', '''
self.path('finger',(4,12),[('L',(18,12)),('A',(18,36),12,12,True),('L',(4,36))])
self.path('nail',(12,20),[('L',(17,20)),('A',(17,28),4,4,True),('L',(12,28)),('L',(12,20))],True)
self.path('swipe',(38,8),[('C',(44,24),(42,13),(44,18)),('C',(36,40),(44,30),(40,36))])
self.add_polyline('head',(35,31),(36,40),(44,38));self.relate('connect','head','swipe')
''')
case(16,'CIRCLE',['clock'],'A pair of true circular counterclockwise arrows surrounds an orthogonal pair of clock hands.', '''
for n,flip in [('top',False),('bottom',True)]:
    def p(x,y):return (48-x,48-y) if flip else (x,y)
    self.add_arc(n,p(40,12),p(4,24),radius_x=20,sweep=False)
    self.add_polyline(n+'-head',p(4,14),p(4,24),p(14,24));self.relate('connect',n,n+'-head')
self.add_polyline('hands',(24,15),(24,27),(30,27))
''')
case(17,'HRECT_L',['banknote'],'Wavy banknote with repeated smooth top/bottom contours and a readable dollar S with exposed stems.', '''
self.path('bill',(4,12),[('C',(14,8),(7,9),(10,8)),('C',(34,12),(21,8),(27,12)),('C',(44,8),(38,12),(41,11)),('L',(44,36)),('C',(34,40),(41,39),(38,40)),('C',(14,36),(27,40),(21,36)),('C',(4,40),(10,36),(7,37)),('L',(4,12))],True)
self.path('dollar',(28,18),[('C',(24,17),(27,17),(25,17)),('C',(24,24),(17,17),(17,23)),('C',(24,31),(31,25),(31,31)),('C',(20,30),(22,31),(21,31))])
for n,a,b in [('top',(24,15),(24,17)),('bottom',(24,31),(24,33))]:
    self.add_line(n,a,b);self.relate('connect',n,'dollar')
''')
for i,closed in [(18,False),(19,True)]:
 case(i,'VRECT_L',['user-round'],'Woman portrait with circular jaw, smooth center-parted hair and broad curved shoulders. Shared human reference user.svg informs jaw and shoulder proportions; touching bust construction.',f'''
self.path('hair',(8,28),[('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,28))])
self.path('face',(16,18),[('C',(24,12),(19,16),(22,14)),('C',(32,18),(26,14),(29,16)),('L',(32,21)),('A',(16,21),8,8,True),('L',(16,18))],True)
self.path('shoulders',(8,44),[('A',(24,33),16,11,True),('A',(40,44),16,11,True)]{',True' if False else ''})
self.relate('connect','face','shoulders')
{'' if not closed else "self.add_line('base',(8,44),(40,44));self.relate('connect','base','shoulders')"}
''','Hairline is reduced to one symmetric part; facial details omitted.')
manifest=[]
for i,s in enumerate(json.loads((BATCH/'claims.json').read_text())):
 fix=Path(s);item=json.loads((fix/'claim.json').read_text())['item'];ref=next((fix/'reference').glob('*.svg'));concept,uuid=re.search(r'(.+)_([a-f0-9-]{36})$',ref.stem).groups();key,refs,plan,body,omissions=cases[i]
 run=ROOT/uuid/'20260924T172356-clean-centerlines-thuan-mac';run.mkdir(parents=True,exist_ok=False)
 meta={'index':i,'concept':concept,'source_uuid':uuid,'reference_path':str(ref),'icon_id':item['icon_id'],'author':AUTHOR,'plan':plan,'construction_references':refs,'omissions':omissions,'keyshape':key,'fix_dir':str(fix),'run':str(run)}
 (run/(item['icon_id']+'.metadata.json')).write_text(json.dumps(meta,indent=2))
 shutil.copy(fix/'reference.png',run/'reference.png')
 module=run/(item['icon_id'].replace('-','_')+'_'+uuid.replace('-','_')+'.py');meta['module']=str(module)
 header=f'"""{plan}\nOmissions: {omissions}\nLucide: {refs or "no useful match"}.\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID={uuid!r}\nSOURCE_PATH={str(ref)!r}\nAUTHOR={AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id={item["icon_id"]!r}\n    keyshape=Keyshape.{key}\n    semantic_role="MAIN"\n    semantic_kind="noun"\n    category="objects"\n    aliases=()\n    keywords={tuple(concept.split())!r}\n'
 if i>=18:header+='    human_construction="bust"\n'
 module.write_text(header+HELPERS+'\n    def build(self):\n'+textwrap.indent(body.strip()+'\n','        '));manifest.append(meta)
(BATCH/'manifest.json').write_text(json.dumps(manifest,indent=2))
# Reuse the local-only validation/render harness for this batch.
script=(ROOT/'fix-batch-20260924/check.py').read_text().replace('fix-batch-20260924\'','fix-batch-20260924T172356\'')
(BATCH/'check.py').write_text(script)
