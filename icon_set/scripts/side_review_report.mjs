#!/usr/bin/env node
// Local report of the side combination review (/side-layout-adjust): every prepared pair's stored layout, what the
// 2026-10-12 canvas keyshape snap did to it, its flags, the keyshape check, the earlier (superseded) review and the
// new review once recorded. Read-only; rerun to refresh as reviews come in.
//
//   node icon_set/scripts/side_review_report.mjs            (64)
//   node icon_set/scripts/side_review_report.mjs --watch [60]   rebuild every 60 s while reviews run (the page reloads
//                                                               itself); stop with Ctrl-C
//   SIDE_SIZE=72 node icon_set/scripts/side_review_report.mjs
//
// Writes icon_set/work/<side-layout-adjust | side-layout-adjust-72>-report/index.html (pictures linked from the work
// folders, nothing copied).
import {existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync} from 'node:fs';
import path from 'node:path';
import {SIZE, WORK_NAME} from './side_compose.mjs';
import {FRAMES, keyshapeCheck} from './side_keyshape_check.mjs';

const HERE = path.dirname(new URL(import.meta.url).pathname);
// SIDE_REPORT_WORK / SIDE_REPORT_OUT: another folder of work folders (a test copy) and where to write its report.
const WORK = process.env.SIDE_REPORT_WORK || path.resolve(HERE, '../work', WORK_NAME);
const OUT = process.env.SIDE_REPORT_OUT || path.resolve(HERE, '../work', WORK_NAME + '-report');
const read = f => { try { return JSON.parse(readFileSync(f, 'utf8')); } catch { return null; } };
// A part's painted box (its groups' centerline box + 2 for the stroke), and the keyshape picture data of a layout:
// the canvas keyshape it sits in (name + painted box) and the main / sub painted boxes, for the card overlay.
const r2 = v => Math.round(v * 100) / 100;
const painted = groups => { if (!groups?.length) return null;
  const b = [Math.min(...groups.map(g => g.x)), Math.min(...groups.map(g => g.y)), Math.max(...groups.map(g => g.x + g.w)), Math.max(...groups.map(g => g.y + g.h))];
  return [b[0] - 2, b[1] - 2, b[2] + 2, b[3] + 2].map(r2); };
const frameBox = name => FRAMES.find(f => f.name === name)?.box || null;
function overlay(dir, layout) {
  if (!layout) return null;
  let ks = null;
  try { ks = keyshapeCheck(dir, layout); } catch { return null; }
  const problems = [...(ks.canvas && !ks.canvas.ok ? [ks.canvas.problem] : []), ...Object.values(ks.roles).filter(x => !x.ok).map(x => x.problem)];
  return {ok: ks.ok, canvas: ks.canvas?.keyshape || null, frame: frameBox(ks.canvas?.keyshape), main: painted(layout.main), sub: painted(layout.sub),
          parts: Object.fromEntries(Object.entries(ks.roles).map(([k, x]) => [k, x.ok ? (x.preset || x.note) + (x.moved ? ' (moved)' : '') : 'off ' + x.box])),
          problems};
}
// The boxes a review recorded ([x, y, w, h] per part) as layout groups.
const recorded = rec => rec?.main ? {position: rec.position, main: [{x: rec.main[0], y: rec.main[1], w: rec.main[2], h: rec.main[3]}],
                                     sub: rec.sub ? [{x: rec.sub[0], y: rec.sub[1], w: rec.sub[2], h: rec.sub[3]}] : []} : null;

const watchIdx = process.argv.indexOf('--watch');
const WATCH = watchIdx >= 0 ? Math.max(15, Number(process.argv[watchIdx + 1]) || 60) : 0;

function build() {
const rows = [];
for (const id of readdirSync(WORK).sort()) {
  const dir = path.join(WORK, id), f = read(path.join(dir, 'fetch.json'));
  if (!f) continue;
  const base = read(path.join(dir, 'base-layout.json'));
  let ks = null;
  try { ks = base ? keyshapeCheck(dir, base) : null; } catch { ks = null; }
  const review = read(path.join(dir, 'review.json'));
  const history = read(path.join(dir, 'review-history.json')) || [];
  const prev = [...history].reverse().find(h => h.superseded) || history[history.length - 1] || null;
  const s = f.snap || {};
  rows.push({
    id, n: f.concept || id, pos: base?.position || '', main: f.main, sub: f.sub, hand: !!(f.hand_layout?.main || f.hand_layout?.sub),
    flags: f.overlap?.flags || [], pen: f.overlap?.penalty ?? 0, erased: f.overlap?.erased_pct ?? 0, reach: f.overlap?.reach ?? null,
    lost: f.overlap?.parts?.lost || [],
    snap: s.class || '-', ks: s.keyshape || '-', together: !!s.move?.together, move: s.move?.total ?? null,
    newFlags: s.new_flags || [], cBefore: s.contact_before || '', cAfter: s.contact_after || '',
    swapped: (s.swapped || []).map(x => `${x.role} ${x.from} → ${x.to}`), reset: s.layout_reset || [],
    system: !ks ? 'unknown' : ks.ok ? 'on' : ks.canvas && !ks.canvas.ok ? 'canvas off' : 'part off preset',
    canvas: ks?.canvas?.keyshape || (ks?.canvas ? 'OFF' : 'text'),
    prev: prev ? {v: prev.verdict, note: (prev.note || '').slice(0, 220), at: prev.reviewed_at || ''} : null,
    rev: review ? {v: review.verdict, user: !!review.user_marked, note: (review.note || '').slice(0, 260), at: review.reviewed_at || '', pushed: review.result === 'pushed',
                   proposed: existsSync(path.join(dir, 'proposed@4x.png'))} : null,
    // Keyshape picture of the stored layout, and of the recorded fix (the boxes the review recorded).
    ksStored: overlay(dir, base),
    ksFix: review?.verdict === 'fix' ? overlay(dir, recorded(review.after)) : null,
  });
}

const count = (list, key) => list.reduce((m, r) => { const k = typeof key === 'function' ? key(r) : r[key]; m[k] = (m[k] || 0) + 1; return m; }, {});
const flagCount = {};
for (const r of rows) for (const fl of r.flags) flagCount[fl] = (flagCount[fl] || 0) + 1;
const summary = {
  size: SIZE, pairs: rows.length, generated: new Date().toISOString(),
  reviewed: rows.filter(r => r.rev).length, verdicts: count(rows.filter(r => r.rev), r => r.rev.v),
  pushed: rows.filter(r => r.rev?.pushed).length,
  snap: count(rows, 'snap'), canvas: count(rows, 'canvas'), system: count(rows, 'system'),
  flagged: rows.filter(r => r.flags.length).length, flags: flagCount,
  prevVerdicts: count(rows.filter(r => r.prev), r => r.prev.v),
  fixSystem: count(rows.filter(r => r.ksFix), r => r.ksFix.ok ? 'fix on the system' : 'fix OFF the system'),
  userMarked: rows.filter(r => r.rev?.user).length,
};
// Progress: reviews per hour over the last two hours of recorded reviews, time left at that pace, the last reviews,
// and reviews per hour for the timeline.
const times = rows.filter(r => r.rev?.at).map(r => ({t: Date.parse(r.rev.at), r})).filter(x => Number.isFinite(x.t)).sort((a, b) => b.t - a.t);
const now = Date.now(), window2h = times.filter(x => now - x.t <= 2 * 3600e3);
const span = window2h.length > 1 ? Math.max(0.25, (window2h[0].t - window2h[window2h.length - 1].t) / 3600e3) : 0;
summary.ratePerHour = span ? Math.round(window2h.length / span) : 0;
summary.lastHour = times.filter(x => now - x.t <= 3600e3).length;
const left = summary.pairs - summary.reviewed;
summary.etaText = !left ? 'done' : summary.ratePerHour ? `about ${Math.ceil(left / summary.ratePerHour)} h left at this pace` : 'no reviews in the last 2 h';
summary.lastAt = times[0] ? new Date(times[0].t).toISOString() : null;
summary.recent = times.slice(0, 12).map(x => ({id: x.r.id, n: x.r.n, v: x.r.rev.v, at: new Date(x.t).toISOString(), note: x.r.rev.note.slice(0, 120)}));
const perHour = {};
for (const x of times) { const h = new Date(x.t).toISOString().slice(0, 13); perHour[h] = (perHour[h] || 0) + 1; }
summary.timeline = Object.entries(perHour).sort().slice(-24);
summary.watch = WATCH;
mkdirSync(OUT, {recursive: true});
writeFileSync(path.join(OUT, 'summary.json'), JSON.stringify(summary, null, 2) + '\n');

const IMG = process.env.SIDE_REPORT_WORK ? `file://${WORK}/` : `../${WORK_NAME}/`;
const esc = s => JSON.stringify(s).replace(/</g, '\\u003c');
const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Side ${SIZE} review</title>
<style>
:root{--bg:#f6f6f4;--fg:#1b1b1b;--muted:#77756f;--card:#fff;--line:#e2e0da;--ok:#1a7f37;--warn:#c26a00;--bad:#c62828;--accent:#2f6fde;--chip:#efeee9}
@media (prefers-color-scheme:dark){:root{--bg:#131313;--fg:#ececea;--muted:#9a9890;--card:#1d1d1c;--line:#323230;--chip:#262624}}
*{box-sizing:border-box}body{margin:0;padding:20px 16px;background:var(--bg);color:var(--fg);font:14px/1.45 system-ui,-apple-system,sans-serif}
main{max-width:1280px;margin:0 auto}h1{font-size:22px;margin:0 0 2px}h2{font-size:15px;margin:22px 0 8px}.sub{color:var(--muted);margin:0 0 16px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}
.stat{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px}.stat b{display:block;font-size:26px;font-variant-numeric:tabular-nums}
.stat span{color:var(--muted);font-size:12px}.stat ul{list-style:none;margin:6px 0 0;padding:0;font-size:12px}.stat li{display:flex;justify-content:space-between;gap:8px}
.stat li em{font-style:normal;font-variant-numeric:tabular-nums;color:var(--muted)}
.bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:14px 0}
select,input{background:var(--card);color:var(--fg);border:1px solid var(--line);border-radius:6px;padding:5px 8px;font:inherit}
#grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:8px;display:flex;flex-direction:column;gap:6px}
.imgs{display:flex;gap:4px}.pic{position:relative;flex:1;min-width:0}.pic img{display:block;width:100%;aspect-ratio:1;border:1px solid var(--line);border-radius:4px;background:#fff}
.pic svg{position:absolute;left:1px;top:1px;width:calc(100% - 2px);aspect-ratio:1;pointer-events:none}.pic .lab{display:block;font-size:10px;color:var(--muted);margin-top:2px;line-height:1.25;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.group{margin:18px 0 6px;padding:10px 12px;background:var(--card);border:1px solid var(--line);border-radius:10px;display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.group img{width:56px;height:56px;border:1px solid var(--line);border-radius:6px;background:#fff}.group .gt{font-weight:650}.group .gm{font-size:12px;color:var(--muted)}
.group button{margin-left:auto;font-size:12px}.ggrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px}
.pager{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin:12px 0}.pager button{padding:4px 10px;min-width:34px}
.pager button.cur{background:var(--fg);color:var(--bg);border-color:var(--fg)}.pager button:disabled{opacity:.4;cursor:default}.pager .gap{color:var(--muted)}
.pager select{margin-left:auto}
.markbtn{font-size:12px;padding:4px 10px}.markbtn.on{background:var(--ok);color:#fff;border-color:var(--ok)}
.card.marked{outline:2px solid var(--ok);outline-offset:-2px}.pic.clickable{cursor:pointer}
.flagrow{display:flex;gap:6px;flex-wrap:wrap}.flagrow button{font-size:12px;padding:3px 9px}
.flagrow button.on{background:var(--fg);color:var(--bg);border-color:var(--fg)}.flagnote{font-size:11px;color:var(--muted)}
.legend{font-size:12px;color:var(--muted);margin:-4px 0 10px}.legend i{display:inline-block;width:14px;height:0;border-top:2px dashed;vertical-align:middle;margin:0 4px 0 10px}
.t{font-weight:600;font-size:13px}.m{font-size:12px;color:var(--muted);word-break:break-word}
.chips{display:flex;flex-wrap:wrap;gap:4px}.chip{font-size:11px;padding:1px 7px;border-radius:10px;background:var(--chip)}
.c-ok{color:var(--ok)}.c-warn{color:var(--warn)}.c-bad{color:var(--bad)}
code{font-size:11px}button{border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:6px;padding:6px 14px;cursor:pointer}
.note{font-size:12px;border-left:3px solid var(--line);padding-left:6px}
.progress{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px;margin-bottom:12px}
.track{height:10px;background:var(--line);border-radius:5px;overflow:hidden;margin:8px 0}.fill{height:100%;background:var(--accent)}
.prow{display:flex;flex-wrap:wrap;gap:6px 22px;font-size:13px}.prow b{font-variant-numeric:tabular-nums}
.tl{display:flex;align-items:flex-end;gap:3px;height:48px;margin-top:10px}.tl div{flex:1;background:var(--accent);opacity:.75;border-radius:2px 2px 0 0;min-height:1px}
.recent{list-style:none;padding:0;margin:10px 0 0;font-size:12px;display:grid;gap:3px}.recent li{display:flex;gap:8px}.recent time{color:var(--muted);font-variant-numeric:tabular-nums}
</style></head><body><main>
<h1>Side ${SIZE} combinations: layout review</h1>
<p class="sub">${summary.pairs.toLocaleString()} prepared pairs (approved parts) · stored layouts snapped into canvas keyshapes on 2026-10-12 · generated ${summary.generated.slice(0, 16).replace('T', ' ')} UTC · local only</p>
<div class="progress" id="progress"></div>
<div class="stats" id="stats"></div>
<h2>Pairs</h2>
<p class="legend">Overlay on each picture:<i style="color:#e5484d"></i>canvas keyshape the layout sits in<i style="color:#d97706"></i>main box<i style="color:#2f6fde"></i>sub box (painted ink boxes). Left: stored layout · right: the recorded fix (or the overlap picture until reviewed).</p>
<p class="legend" id="markstat"></p>
<p class="legend" id="flagstat"></p>
<div class="bar">
 <input id="q" type="search" placeholder="Search concept or id" size="26">
 <select id="fRev"><option value="">Review: all</option><option value="none">Not reviewed</option><option value="user">Marked good by you</option><option value="ai">Reviewed by the AI</option><option value="ok">ok</option><option value="fix">fix</option><option value="redraw">redraw</option></select>
 <select id="fSnap"><option value="">Snap: all</option></select>
 <select id="fCanvas"><option value="">Canvas keyshape: all</option></select>
 <select id="fSys"><option value="">Keyshape check: all</option></select>
 <select id="fFlag"><option value="">Flags: all</option><option value="any">Any flag</option><option value="none">No flag</option></select>
 <select id="fPrev"><option value="">Earlier review: all</option></select>
 <select id="fGroup"><option value="main">Group by main icon</option><option value="">No grouping</option></select>
 <select id="fHuman"><option value="">Human review: all</option><option value="yes">Reviewed by you</option><option value="no">Not reviewed by you</option></select>
 <select id="fUser"><option value="">Your flag: all</option><option value="stored-better">Stored is better</option><option value="fix-good">Fix is good</option><option value="unflagged">Fix not flagged yet</option></select>
 <select id="fFixKs"><option value="">Fix keyshape: all</option><option value="on">Fix on the system</option><option value="off">Fix OFF the system</option></select>
 <span id="shown" class="m"></span>
</div>
<div class="pager" id="pagerTop"></div>
<div id="grid"></div>
<div class="pager" id="pagerBottom"></div>
</main>
<script>
const S=${esc(summary)}, D=${esc(rows)}, IMG=${esc(IMG)};
const el=(t,c,x)=>{const e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e};
function stat(title,big,sub,obj){const s=el('div','stat');s.append(el('span',null,title),el('b',null,big));if(sub)s.append(el('span',null,sub));
 if(obj){const ul=el('ul');Object.entries(obj).sort((a,b)=>b[1]-a[1]).forEach(([k,v])=>{const li=el('li');li.append(el('span',null,k),el('em',null,v.toLocaleString()));ul.append(li)});s.append(ul)}return s}
(()=>{const p=document.getElementById('progress'),pct=S.pairs?100*S.reviewed/S.pairs:0;
 p.append(el('div','t','Progress'+(S.watch?' · updates every '+S.watch+' s':' · run with --watch to keep this current')));
 const tr=el('div','track'),fi=el('div','fill');fi.style.width=pct.toFixed(1)+'%';tr.append(fi);p.append(tr);
 const row=el('div','prow');[['Reviewed',S.reviewed.toLocaleString()+' / '+S.pairs.toLocaleString()+' ('+pct.toFixed(1)+'%)'],['Left',(S.pairs-S.reviewed).toLocaleString()],
  ['Last hour',S.lastHour],['Pace',S.ratePerHour+' / h'],['Time left',S.etaText],['Last review',S.lastAt?new Date(S.lastAt).toLocaleTimeString():'none yet']]
  .forEach(([k,v])=>{const s=el('span');s.append(el('span','m',k+' '),el('b',null,String(v)));row.append(s)});p.append(row);
 if(S.timeline.length){const tl=el('div','tl'),max=Math.max(...S.timeline.map(x=>x[1]));S.timeline.forEach(([h,n])=>{const b=el('div');b.style.height=(100*n/max)+'%';b.title=h.replace('T',' ')+':00 UTC · '+n+' reviews';tl.append(b)});p.append(tl)}
 if(S.recent.length){const ul=el('ul','recent');S.recent.forEach(r=>{const li=el('li');li.append(el('time',null,new Date(r.at).toLocaleTimeString()),el('span',r.v==='ok'?'c-ok':r.v==='fix'?'c-warn':'c-bad',r.v),el('span',null,r.n));ul.append(li)});p.append(ul)}})();
const st=document.getElementById('stats');
st.append(stat('Reviewed (new rule)',S.reviewed.toLocaleString()+' / '+S.pairs.toLocaleString(),S.pushed?S.pushed+' pushed':'none pushed yet',S.verdicts),
 stat('Snap (2026-10-12)',(S.snap['snapped-flagged']||0).toLocaleString(),'snapped but flagged',S.snap),
 stat('Canvas keyshape of the stored layout',(S.canvas.SQUARE||0).toLocaleString(),'in SQUARE',S.canvas),
 stat('Keyshape check (stored)',(S.system.on||0).toLocaleString(),'on the system',S.system),
 stat('Stored layouts with flags',S.flagged.toLocaleString(),'overlap flags now',S.flags),
 stat('Marked good by you',(S.userMarked||0).toLocaleString(),'no AI review needed',null),
 stat('Recorded fixes: keyshape check',Object.values(S.fixSystem).reduce((a,b)=>a+b,0).toLocaleString(),'fixes recorded',S.fixSystem),
 stat('Earlier reviews (superseded)',Object.values(S.prevVerdicts).reduce((a,b)=>a+b,0).toLocaleString(),'judged the old layouts',S.prevVerdicts));
const opts=(id,key)=>{const sel=document.getElementById(id);const c={};D.forEach(r=>{const k=key(r);c[k]=(c[k]||0)+1});Object.entries(c).sort((a,b)=>b[1]-a[1]).forEach(([k,v])=>{const o=el('option',null,k+' ('+v+')');o.value=k;sel.append(o)})};
opts('fSnap',r=>r.snap);opts('fCanvas',r=>r.canvas);opts('fSys',r=>r.system);opts('fPrev',r=>r.prev?r.prev.v:'none');
const $=id=>document.getElementById(id);let page=1,perPage=96;
// ?ids=a,b,c in the address: only those pairs (a list handed over to look at), on top of the other filters.
const ONLY_IDS=(()=>{try{const v=new URLSearchParams(location.search).get('ids');return v?new Set(v.split(',').map(x=>x.trim()).filter(Boolean)):null}catch{return null}})();
function list(){const q=$('q').value.trim().toLowerCase();return D.filter(r=>(!ONLY_IDS||ONLY_IDS.has(r.id))&&(!q||(r.n+' '+r.id).toLowerCase().includes(q))
 &&(!$('fRev').value||($('fRev').value==='none'?!r.rev:$('fRev').value==='user'?r.rev&&r.rev.user:$('fRev').value==='ai'?r.rev&&!r.rev.user:r.rev&&r.rev.v===$('fRev').value))
 &&(!$('fSnap').value||r.snap===$('fSnap').value)&&(!$('fCanvas').value||r.canvas===$('fCanvas').value)&&(!$('fSys').value||r.system===$('fSys').value)
 &&(!$('fFlag').value||($('fFlag').value==='any'?r.flags.length:!r.flags.length))&&(!$('fPrev').value||(r.prev?r.prev.v:'none')===$('fPrev').value)
 &&(!$('fFixKs').value||(r.ksFix&&(r.ksFix.ok?'on':'off')===$('fFixKs').value))
 &&(!$('fHuman').value||(humanReviewed(r)?'yes':'no')===$('fHuman').value)
 &&(!$('fUser').value||($('fUser').value==='unflagged'?(r.rev&&r.rev.v==='fix'&&!flagOf(r)):(flagOf(r)||{}).kind===$('fUser').value)))}
// Your flags (the flag server, icon_set/work/side-layout-flags/server.py on :8771, writes flags.json / flags-72.json):
// a flag counts only for the review it was given on (a later review of the pair starts unflagged).
const FLAG_API='http://127.0.0.1:8771';let FLAGS={},flagServer=null;
const flagOf=r=>{const f=FLAGS[r.id];return f&&r.rev&&f.review_reviewed_at===r.rev.at?f:null};
async function loadFlags(){try{const res=await fetch(FLAG_API+'/api/flags?size='+S.size,{cache:'no-store'});FLAGS=(await res.json()).flags||{};flagServer=true}catch{flagServer=false}}
async function setFlag(r,kind){try{const res=await fetch(FLAG_API+'/api/flag',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id:r.id,kind,size:S.size})});
 const d=await res.json();if(!res.ok)throw Error(d.error||res.status);FLAGS=d.flags||FLAGS;return true}catch(e){alert('Flag not saved: '+e.message+'. Start the flag server: /opt/homebrew/bin/python3 icon_set/work/side-layout-flags/server.py');return false}}
function flagButtons(r){const row=el('div','flagrow'),f=flagOf(r);
 const btn=(kind,label)=>{const b=el('button',f&&f.kind===kind?'on':'',label);b.title=kind==='stored-better'?'I like the stored layout better than this AI fix':'The AI fix is good';
  b.onclick=async()=>{const next=f&&f.kind===kind?null:kind;if(await setFlag(r,next)){row.replaceWith(flagButtons(r));updateFlagStat();updateMarkStat()}};return b};
 row.append(btn('stored-better','Stored is better'),btn('fix-good','Fix is good'));
 if(f)row.append(el('span','flagnote','flagged '+new Date(f.flagged_at).toLocaleString()));
 if(flagServer===false)row.append(el('span','flagnote','flag server not running'));return row}
function updateFlagStat(){const e=document.getElementById('flagstat');if(!e)return;const c={};D.forEach(r=>{const f=flagOf(r);if(f)c[f.kind]=(c[f.kind]||0)+1});
 const fixes=D.filter(r=>r.rev&&r.rev.v==='fix').length;e.textContent='Your flags: '+(c['stored-better']||0)+' stored is better · '+(c['fix-good']||0)+' fix is good · '+(fixes-(c['stored-better']||0)-(c['fix-good']||0))+' fixes not flagged';}
// Your "good as stored" marks before the AI review: POST /api/mark writes the pair's review (verdict ok, user_marked), so
// the AI review skips it; clicking again removes it. Click the stored picture or the button.
async function setMark(r,good){try{const res=await fetch(FLAG_API+'/api/mark',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id:r.id,size:S.size,good})});
 const d=await res.json();if(!res.ok)throw Error(d.error||res.status);
 r.rev=good?{v:'ok',user:true,note:'Marked good by you: no AI review needed.',at:new Date().toISOString(),pushed:false,proposed:false}:null;touched();return true}
 catch(e){alert('Not saved: '+e.message+(String(e.message).includes('fetch')?'. Start the flag server: /opt/homebrew/bin/python3 icon_set/work/side-layout-flags/server.py':''));return false}}
function markable(r){return !r.rev||r.rev.user}
// Reviewed by a person: marked good by you, or an AI fix you flagged (stored is better / fix is good).
const humanReviewed=r=>!!(r.rev&&(r.rev.user||flagOf(r)));
async function toggleMark(r,card){if(!markable(r))return;if(await setMark(r,!(r.rev&&r.rev.user))){card.replaceWith(cardOf(r));updateMarkStat()}}
function updateMarkStat(){const e=document.getElementById('markstat');if(!e)return;const n=D.filter(r=>r.rev&&r.rev.user).length,left=D.filter(r=>!r.rev).length,h=D.filter(humanReviewed).length;
 e.textContent='Reviewed by you: '+h.toLocaleString()+' of '+D.length.toLocaleString()+' · marked good '+n.toLocaleString()+' (no AI review) · '+left.toLocaleString()+' left for the AI review'}
// Watch mode: reload for fresh data only after 2 minutes without clicks or scrolling, keeping filters and scroll position.
let lastTouch=Date.now();const touched=()=>{lastTouch=Date.now()};['scroll','click','input','keydown'].forEach(ev=>addEventListener(ev,touched,{passive:true}));
const STATE_KEY='side-report-'+S.size;
function saveState(){try{sessionStorage.setItem(STATE_KEY,JSON.stringify({y:scrollY,page,perPage,f:['q','fRev','fSnap','fCanvas','fSys','fFlag','fPrev','fFixKs','fUser','fHuman','fGroup'].map(id=>[id,$(id).value])}))}catch{}}
if(S.watch)setInterval(()=>{if(Date.now()-lastTouch>120000){saveState();location.reload()}},S.watch*1000);
const NS='http://www.w3.org/2000/svg';
function ksSvg(k){const svg=document.createElementNS(NS,'svg');svg.setAttribute('viewBox','0 0 ${SIZE} ${SIZE}');
 const rect=(b,color,dash,w)=>{if(!b)return;const r=document.createElementNS(NS,'rect');r.setAttribute('x',b[0]);r.setAttribute('y',b[1]);r.setAttribute('width',b[2]-b[0]);r.setAttribute('height',b[3]-b[1]);
  r.setAttribute('fill','none');r.setAttribute('stroke',color);r.setAttribute('stroke-width',w);r.setAttribute('stroke-dasharray',dash);svg.append(r)};
 rect(k.main,'#d97706','1 .8',.35);rect(k.sub,'#2f6fde','1 .8',.35);rect(k.frame,'#e5484d','1.6 .9',.5);return svg}
function pic(f,a,k,label){const p=el('div','pic'),i=el('img');i.loading='lazy';i.src=IMG+cur+'/'+f;i.alt=a;i.title=a;p.append(i);
 if(k){p.append(ksSvg(k));p.append(el('span','lab',label||((k.canvas||'no canvas keyshape')+(k.ok?'':' · OFF'))))}else p.append(el('span','lab',a));return p}
let cur='';
function cardOf(r){return card(r)}
function card(r){const c=el('div','card'+(r.rev&&r.rev.user?' marked':'')),imgs=el('div','imgs');cur=r.id;
 const stored=pic('current@4x.png','stored layout'+(markable(r)?' (click: mark good, no review)':''),r.ksStored,'stored · '+((r.ksStored&&r.ksStored.canvas)||'—')+(r.ksStored&&!r.ksStored.ok?' · OFF':''));
 if(markable(r)){stored.classList.add('clickable');stored.onclick=()=>toggleMark(r,c)}
 imgs.append(stored);
 if(r.rev&&r.rev.proposed&&r.ksFix)imgs.append(pic('proposed@4x.png','recorded fix',r.ksFix,'fix · '+(r.ksFix.canvas||'no canvas keyshape')+(r.ksFix.ok?' · on the system':' · OFF')));
 else if(r.rev&&r.rev.proposed)imgs.append(pic('proposed@4x.png','proposed',null));
 else imgs.append(pic('overlap-current.png','overlap: erased red, sub blue',null));
 c.append(imgs,el('div','t',r.n));
 const ch=el('div','chips');const chip=(t,cl)=>ch.append(el('span','chip '+(cl||''),t));
 chip(r.pos);chip(r.canvas);chip(r.snap,r.snap==='snapped-flagged'?'c-warn':r.snap==='snapped-ok'||r.snap==='already-fits'?'c-ok':'c-bad');
 if(r.system!=='on')chip(r.system,'c-bad');
 if(r.ksStored&&r.ksStored.parts)Object.entries(r.ksStored.parts).forEach(([role,t])=>{if(String(t).includes('in-between'))chip(role+' '+String(t).split(' ')[0]+' · in-between size','c-ok')});r.flags.forEach(f=>chip(f,'c-warn'));if(r.hand)chip('hand layout');
 if(r.rev&&r.rev.user)chip('marked good by you','c-ok');else if(r.rev)chip('AI review: '+r.rev.v+(r.rev.pushed?' · pushed':''),r.rev.v==='ok'?'c-ok':r.rev.v==='fix'?'c-warn':'c-bad');else chip('not reviewed');
 c.append(ch);
 const m=[];if(r.move!=null)m.push((r.together?'moved together ':'parts moved ')+r.move);if(r.cBefore||r.cAfter)m.push('contact '+r.cBefore+' → '+r.cAfter);
 if(r.newFlags.length)m.push('snap added '+r.newFlags.join(', '));if(r.lost.length)m.push('lost part '+r.lost.join(', '));m.push('erased '+r.erased+'%');
 c.append(el('div','m',m.join(' · ')));
 if(r.ksFix)c.append(el('div','m '+(r.ksFix.ok?'c-ok':'c-bad'),'fix keyshape: '+(r.ksFix.ok?'on the system · ':'OFF · ')+(r.ksFix.canvas||'no canvas keyshape')+' · main '+(r.ksFix.parts.main||'-')+' · sub '+(r.ksFix.parts.sub||'-')+(r.ksFix.problems.length?' · '+r.ksFix.problems.join('; '):'')));
 if(r.swapped.length)c.append(el('div','m','re-picked: '+r.swapped.join('; ')));if(r.reset.length)c.append(el('div','m','placed automatically: '+r.reset.join(', ')));
 if(markable(r)){const b=el('button','markbtn'+(r.rev&&r.rev.user?' on':''),r.rev&&r.rev.user?'✓ Marked good — click to undo':'Good — no review');b.onclick=()=>toggleMark(r,c);c.append(b)}
 if(r.rev&&r.rev.v==='fix')c.append(flagButtons(r));
 if(r.rev&&r.rev.note)c.append(el('div','note',r.rev.v+': '+r.rev.note));else if(r.prev)c.append(el('div','note m','earlier '+r.prev.v+': '+r.prev.note));
 const id=el('div','m');id.append(el('code',null,r.id));c.append(id);return c}
// Pages instead of endless scrolling: page numbers and previous / next at the top and the bottom.
function pagerInto(el,total,pages){el.innerHTML='';
 const go=p=>{page=Math.max(1,Math.min(pages,p));draw();scrollTo(0,$('pagerTop').offsetTop-8)};
 const btn=(label,p,opts={})=>{const b=el2('button',opts.cur?'cur':'',label);b.disabled=!!opts.disabled;if(!opts.disabled&&!opts.cur)b.onclick=()=>go(p);el.append(b)};
 btn('‹ Prev',page-1,{disabled:page<=1});
 const nums=new Set([1,2,pages-1,pages,page-2,page-1,page,page+1,page+2].filter(p=>p>=1&&p<=pages));let last=0;
 [...nums].sort((a,b)=>a-b).forEach(p=>{if(p-last>1)el.append(el2('span','gap','…'));btn(String(p),p,{cur:p===page});last=p});
 btn('Next ›',page+1,{disabled:page>=pages});
 el.append(el2('span','m','Page '+page+' of '+pages+' · '+total.toLocaleString()+' pairs'));
 const sel=el2('select');[48,96,192].forEach(n=>{const o=el2('option',null,n+' per page');o.value=n;if(n===perPage)o.selected=true;sel.append(o)});
 sel.onchange=()=>{perPage=Number(sel.value);page=1;draw()};el.append(sel)}
const el2=(t,c,x)=>{const e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e};
// The view in the address bar (?rev=none&sys=part+off+preset&page=2&per=96…), so a filtered page can be bookmarked,
// reloaded or shared; an empty filter is left out.
const URL_KEYS={fGroup:'group',q:'q',fRev:'rev',fSnap:'snap',fCanvas:'canvas',fSys:'sys',fFlag:'flags',fPrev:'earlier',fFixKs:'fixks',fUser:'flag',fHuman:'human'};
function writeURL(){try{const u=new URLSearchParams();Object.entries(URL_KEYS).forEach(([id,k])=>{const v=$(id).value;if(id==='fGroup'){if(v!=='main')u.set(k,v||'none')}else if(v)u.set(k,v)});
 if(ONLY_IDS)u.set('ids',[...ONLY_IDS].join(','));if(page>1)u.set('page',page);if(perPage!==96)u.set('per',perPage);const q=u.toString();history.replaceState(null,'',location.pathname+(q?'?'+q:''))}catch{}}
function readURL(){const u=new URLSearchParams(location.search);let any=false;
 Object.entries(URL_KEYS).forEach(([id,k])=>{if(u.has(k)){$(id).value=(id==='fGroup'&&u.get(k)==='none')?'':u.get(k);any=true}});
 if(u.has('per'))perPage=Number(u.get('per'))||perPage;if(u.has('page'))page=Number(u.get('page'))||1;return any||u.has('page')}
// Grouped by main icon: pairs of one main together under a header (its picture, counts, mark-all); a page holds whole
// groups, about perPage pairs. Ungrouped: perPage pairs a page.
const mainName=k=>String(k||'').split('/').pop();
function groupsOf(l){const m=new Map();l.forEach(r=>{const k=r.main||'?';if(!m.has(k))m.set(k,[]);m.get(k).push(r)});
 return [...m.entries()].sort((a,b)=>b[1].length-a[1].length||mainName(a[0]).localeCompare(mainName(b[0])))}
function groupPages(groups){const pages=[];let cur=[],n=0;groups.forEach(g=>{if(n&&n+g[1].length>perPage){pages.push(cur);cur=[];n=0}cur.push(g);n+=g[1].length});if(cur.length)pages.push(cur);return pages.length?pages:[[]]}
async function markGroup(rows,btn){const todo=rows.filter(r=>!r.rev);if(!todo.length)return;
 if(!confirm('Mark '+todo.length+' not-reviewed pairs with this main icon as good (no AI review)?'))return;
 btn.disabled=true;let done=0;for(const r of todo){if(await setMark(r,true))done++;btn.textContent='Marking '+done+' / '+todo.length+'…'}
 const y=scrollY;draw();scrollTo(0,y);updateMarkStat()}
function groupHeader(key,rows){const h=el('div','group'),img=el('img');img.loading='lazy';img.src=IMG+rows[0].id+'/main@4x.png';img.alt=key;
 const t=el('div');t.append(el('div','gt',mainName(key)));
 const left=rows.filter(r=>!r.rev).length,mine=rows.filter(r=>r.rev&&r.rev.user).length,ai=rows.filter(r=>r.rev&&!r.rev.user).length;
 t.append(el('div','gm',rows.length+' pairs · '+left+' not reviewed · '+mine+' marked good by you · '+ai+' reviewed by the AI'));h.append(img,t);
 if(left){const b=el('button',null,'Mark all '+left+' not-reviewed good');b.onclick=()=>markGroup(rows,b);h.append(b)}return h}
function draw(){const g=$('grid'),l=list();g.innerHTML='';let pages,total=l.length;
 if($('fGroup').value==='main'){const gp=groupPages(groupsOf(l));pages=gp.length;page=Math.max(1,Math.min(page,pages));writeURL();
  gp[page-1].forEach(([key,rows])=>{g.append(groupHeader(key,rows));const gg=el('div','ggrid');rows.forEach(r=>gg.append(card(r)));g.append(gg)});
  $('shown').textContent=total.toLocaleString()+' pairs · '+groupsOf(l).length.toLocaleString()+' main icons'}
 else{pages=Math.max(1,Math.ceil(total/perPage));page=Math.max(1,Math.min(page,pages));writeURL();
  l.slice((page-1)*perPage,page*perPage).forEach(r=>g.append(card(r)));$('shown').textContent=total.toLocaleString()+' pairs'}
 g.style.display=$('fGroup').value==='main'?'block':'grid';
 pagerInto($('pagerTop'),total,pages);pagerInto($('pagerBottom'),total,pages)}
function render(reset){if(reset)page=1;draw()}
['q','fRev','fSnap','fCanvas','fSys','fFlag','fPrev','fFixKs','fUser','fHuman','fGroup'].forEach(id=>$(id).addEventListener('input',()=>render(true)));
(()=>{try{const st=JSON.parse(sessionStorage.getItem(STATE_KEY)||'null');if(!st&&readURL()){draw();return}if(st){st.f.forEach(([id,v])=>{if($(id))$(id).value=v});sessionStorage.removeItem(STATE_KEY);
 perPage=st.perPage||perPage;page=st.page||1;draw();setTimeout(()=>scrollTo(0,st.y),50)}else render(true)}catch{render(true)}})();
updateMarkStat();loadFlags().then(()=>{const y=scrollY;draw();scrollTo(0,y);updateFlagStat();updateMarkStat()});
</script></body></html>
`;
writeFileSync(path.join(OUT, 'index.html'), html);
return summary;
}

const first = build();
console.log(JSON.stringify({report: path.join(OUT, 'index.html'), ...first, generated: undefined, recent: undefined, timeline: undefined}, null, 1));
if (WATCH) {
  console.error(`watching: rebuilding every ${WATCH} s (Ctrl-C to stop)`);
  setInterval(() => { try { const s = build(); process.stderr.write(`\r${new Date().toLocaleTimeString()} reviewed ${s.reviewed} of ${s.pairs} · ${s.ratePerHour}/h · ${s.etaText}   `); } catch (e) { console.error(e.message); } }, WATCH * 1000);
}
