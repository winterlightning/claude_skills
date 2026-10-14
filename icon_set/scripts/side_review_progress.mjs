// Usage: node icon_set/scripts/side_review_progress.mjs [SINCE e.g. 2026-10-09T05:00]
// Progress of the side review run: reviews recorded since SINCE (default today), verdicts, rank, pairs left.
import fs from "fs"; import { execSync } from "child_process";
const repo = "/Applications/Workspaces/pictographic/claude_skills", d = `${repo}/icon_set/work/side-layout-adjust`;
const since = process.argv[2] || new Date().toISOString().slice(0, 10);
const rows = [];
for (const id of fs.readdirSync(d)) {
  const p = `${d}/${id}/review.json`; if (!fs.existsSync(p)) continue;
  const r = JSON.parse(fs.readFileSync(p)); if ((r.reviewed_at || "") < since) continue;
  const rank = (r.note || "").match(/rank\s*([123])/i)?.[1] || "-";
  const contact = (r.verdict === "fix" ? r.after?.contact : r.before?.contact) || "?";
  rows.push({ at: r.reviewed_at, id, verdict: r.verdict, rank, contact, concept: r.concept, note: r.note || "" });
}
rows.sort((a, b) => a.at.localeCompare(b.at));
const count = (k) => rows.reduce((m, r) => (m[r[k]] = (m[r[k]] || 0) + 1, m), {});
const left = execSync(`node icon_set/scripts/side_layout.mjs list --limit 5000 --unreviewed`, { cwd: repo, stdio: ["ignore", "pipe", "ignore"] })
  .toString().split("\n").filter((l) => l.split("\t").length > 3).length;
console.log(`since ${since}: ${rows.length} reviewed · ${left} unreviewed left`);
console.log("verdict", count("verdict"), " rank", count("rank"), " contact", count("contact"));
for (const r of rows.slice(-8)) console.log(`${r.at.slice(11, 16)}  ${r.verdict.padEnd(6)} r${r.rank} ${r.contact.padEnd(8)} ${r.concept}  — ${r.note.slice(0, 90)}`);
