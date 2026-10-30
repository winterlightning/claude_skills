import sqlite3,json,hashlib,pathlib
import sys
root=pathlib.Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True)
repo=pathlib.Path(__file__).resolve().parents[4]
db=sqlite3.connect(':memory:')
for p in sorted((repo/'cloud/worker/migrations').glob('*.sql')):db.executescript(p.read_text())
def svg(n,body):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n} {n}" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
main=svg(64,'<circle cx="32" cy="32" r="28"/>')
sub=svg(32,'<path d="M16 28 A12 12 0 1 1 28 16 M22 12 L28 16 L30 10"/>')
old=svg(64,'<circle cx="32" cy="32" r="28"/><path d="M32 40 A8 8 0 1 1 40 32 M36 29 L40 32 L42 28"/>')
def add(k,art,name):
 sha=hashlib.sha256(art.encode()).hexdigest();family=k.split('/')[0];url='/api/icon-artwork/svg?icon='+k+'&v='+sha
 record={'key':k,'icon_id':k.split('/')[1],'family':family,'name':name,'svg_sha256':sha,'preview_url':url,'canvas_size':64 if family!='symbol' else 32,'build_failed':False}
 db.execute('INSERT INTO icons(key,icon_id,name,family,canvas_size,svg_sha256,preview_url,record,pushed_at,card,search,sort_name,version_group,version,variant) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(k,k.split('/')[1],name,family,record['canvas_size'],sha,url,json.dumps(record),'now',json.dumps(record),name.lower(),name,k,1,0))
 db.execute('INSERT INTO revisions VALUES(?,?,?,?,?)',(sha,k,art,'artwork','now'))
 db.execute("INSERT INTO reviews(icon,svg_sha256,status,updated_at,updated_by) VALUES(?,?,'approve','now','fixture')",(k,sha))
 return sha
m=add('container/test-circle',main,'Test circle');s=add('symbol/test-refresh',sub,'Test refresh arrow')
for rid in ['demo-arrow','api-regression','plain-control']:
 k='container_combination64/'+rid;h=add(k,old+'\n'*len(rid),'Circular Refresh Arrow — '+rid)
 db.execute('INSERT INTO "references"(reference_id,kind,concept,source) VALUES(?,?,?,?)',(rid,'combination','Circular Refresh Arrow — '+rid,'synthetic fixture'))
 for role,key,sha,box in [('container','container/test-circle',m,{'x':4,'y':4,'w':56,'h':56}),('symbol','symbol/test-refresh',s,{'x':18,'y':18,'w':28,'h':28,'scope':'pair'})]:
  db.execute('INSERT INTO reference_parts(reference_id,role,part_reference_id,icon,layout,built_sha,updated_at,updated_by) VALUES(?,?,?,?,?,?,?,?)',(rid,role,'fixture-'+role,key,json.dumps([box]),sha,'now','fixture'))
 db.execute('INSERT INTO icon_references VALUES(?,?)',(k,rid))
 if rid!='plain-control':
  doc={'schema':'pictographic.icon-artwork.v1','icon':k,'source_mode':'use_upload','source_svg_sha256':'fixture-baseline','selected_svg_sha256':h,'revision':2,'selected_upload':{'svg':old+'\n'*len(rid),'svg_sha256':h,'name':'old-small-arrow.svg'},'uploaded':{'svg':old+'\n'*len(rid),'svg_sha256':h,'name':'old-small-arrow.svg'}}
  db.execute('INSERT INTO store_documents VALUES(?,?,?,?,?)',('icon-artwork',k,json.dumps(doc),'now','fixture'))
# Materialized state for initial fixture only; all subsequent writes use the real Worker.
cols='decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked'
db.execute(f'UPDATE icons SET ({cols})=(SELECT {cols} FROM icon_state v WHERE v.key=icons.key)')
# seed search through the standard FTS schema
for row in db.execute('SELECT key,search FROM icons').fetchall():
 db.execute('INSERT INTO icon_search(key,search) VALUES(?,?)',row)
tables=['references','icons','reference_parts','icon_references','reviews','revisions','store_documents']
dump=list(db.iterdump())
text='\n'.join(line for t in tables for line in dump if line.startswith('INSERT INTO "'+t+'"'))
# FTS shadow tables are not imported; explicit virtual-table inserts instead.
text+='\n'+'\n'.join("INSERT INTO icon_search(key,search) VALUES("+','.join("'"+v.replace("'","''")+"'" for v in row)+');' for row in db.execute('SELECT key,search FROM icons'))
text+='\nINSERT INTO icon_search_keys(key,search_rowid) SELECT key,rowid FROM icon_search;\n'
text+="INSERT INTO icon_counts(family,side_role,style,state,category,built_failed,n) SELECT COALESCE(family,''),COALESCE(side_role,''),COALESCE(style,'normal'),COALESCE(state,''),COALESCE(category,''),build_failed,count(*) FROM icons GROUP BY 1,2,3,4,5,6;\n"
(root/'seed.sql').write_text(text)
