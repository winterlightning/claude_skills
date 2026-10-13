#!/usr/bin/env node
// The side pairs one page of a side-overlap review page shows, from its link (for /side-layout-adjust).
//
//   node icon_set/scripts/side_review_page.mjs 'file:///…/side-overlap-audit/<run>/review.html#p3&det=problem&sort=penalty'
//
// Prints the page's pair ids, one per line, in the order the page shows them; a summary goes to stderr. The page
// (review.py) writes review-pairs.json beside review.html and keeps its page number and filters in the link, so the
// filters and sort here mirror the page's render(). The "Your mark" filter lives in the viewer's browser and cannot
// be read here: such a link is refused (use the page's Copy for skill button instead).
import {existsSync, readFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const PER_PAGE = 10;
const DEFAULTS = {det: 'all', flag: 'all', mark: 'all', ai: 'all', day: 'all', sort: 'id', q: ''};
// The local calendar day a review was recorded, as the page's "Reviewed on" filter shows it.
const reviewDay = p => {
  const t = p.review?.reviewed_at && new Date(p.review.reviewed_at);
  return t && !isNaN(t) ? `${t.getFullYear()}-${String(t.getMonth() + 1).padStart(2, '0')}-${String(t.getDate()).padStart(2, '0')}` : '';
};

function fail(message) { console.error('error: ' + message); process.exit(1); }

const link = process.argv[2];
if (!link) fail('give the review page link, e.g. file:///…/review.html#p1');
const [where, hash = ''] = link.split('#');
const file = where.startsWith('file:') ? fileURLToPath(where) : path.resolve(where);
const data = path.join(path.dirname(file), 'review-pairs.json');
if (!existsSync(data)) fail(`no review-pairs.json beside ${file}; run review.py in that folder first.`);

const [head, ...rest] = hash.split('&');
const page = Number((head.match(/^p([0-9]+)$/) || [])[1] || 1);
const pairsData = JSON.parse(readFileSync(data, 'utf8'));
// Like the page, a link without day= means the latest review day (the current run); day=all means every day.
DEFAULTS.day = pairsData.map(reviewDay).filter(Boolean).sort().pop() || 'all';
const opts = {...DEFAULTS, ...Object.fromEntries(new URLSearchParams(rest.join('&')))};
if (opts.mark !== 'all') fail('this link filters by your marks, which only the page knows. Use its "Copy for skill" button instead.');

const problem = p => p.flags.length > 0;
const q = opts.q.trim().toLowerCase();
const list = pairsData.filter(p => {
  if (opts.det === 'problem' && !problem(p)) return false;
  if (opts.det === 'clean' && problem(p)) return false;
  if (opts.flag === 'subfix') { if (p.rebuild !== 'sub') return false; }
  else if (opts.flag === 'stale') { if (p.state !== 'stale') return false; }
  else if (opts.flag === 'outdated') { if (!p.outdated) return false; }
  else if (opts.flag !== 'all' && !p.flags.includes(opts.flag)) return false;
  if (opts.ai === 'none' && p.review) return false;
  if (opts.ai === 'reviewed' && !p.review) return false;
  if (!['all', 'none', 'reviewed'].includes(opts.ai) && p.review?.verdict !== opts.ai) return false;
  if (opts.day !== 'all' && reviewDay(p) !== opts.day) return false;
  if (q && !(p.concept + ' ' + p.main + ' ' + p.sub + ' ' + p.id).toLowerCase().includes(q)) return false;
  return true;
});
const by = {id: (a, b) => a.id.localeCompare(b.id), reach: (a, b) => (b.reach ?? -99) - (a.reach ?? -99),
            erased: (a, b) => b.erased - a.erased, m2s: (a, b) => (a.m2s ?? 99) - (b.m2s ?? 99), penalty: (a, b) => b.penalty - a.penalty};
if (!by[opts.sort]) fail(`unknown sort "${opts.sort}".`);
list.sort(by[opts.sort]);
const pages = Math.max(1, Math.ceil(list.length / PER_PAGE));
if (page < 1 || page > pages) fail(`page ${page} does not exist; these filters give ${pages} pages.`);
const slice = list.slice((page - 1) * PER_PAGE, page * PER_PAGE);
for (const p of slice) console.log(p.id);
console.error(`page ${page} of ${pages} (${list.length} pairs match): ${slice.map(p => p.concept + (p.flags.length ? ` [${p.flags.join(', ')}]` : '')).join('; ')}`);
