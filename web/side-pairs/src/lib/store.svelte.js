// The Side pairs page's data and actions (the old grid's globals and loaders): every pair of the chosen size from D1
// through side-pairs-data.js (window.SideData), the components and their status per source, reviews, statuses, and
// the combined icons composed in this browser for pairs not built yet. Svelte reads `version` to redraw after a change.
import {SvelteMap} from 'svelte/reactivity';
import {usable} from './rules.js';

const data = () => window.SideData;

export class SideStore {
  version = $state(0);
  // Bumped when the list of pairs changes (a load, a pair read again): the review buttons get the pairs then.
  pairsVersion = $state(0);
  loading = $state(false);
  error = $state('');
  status = $state('');
  ready = $state(false);
  size = $state(64);
  // Build all / Rebuild stale progress: {status: 'idle' | 'running' | 'error', message}
  combine = $state({status: 'idle', message: ''});

  pairs = new Map();
  previews = {};
  components = null;
  componentStatus = {main: new Map(), sub: new Map()};
  reviews = {};
  statuses = {};
  run = null;
  catalog = {rows: [], references: {}};
  // Previews composed here, read only by the figures that show them: a finished one redraws its figure, not the list.
  rendered = new SvelteMap();
  #queue = [];
  #active = 0;

  constructor(size) { this.size = data().setSize(size); }
  touch() { this.version++; }
  sizes() { return data().sizes(); }
  item(id) { return data().item(id); }
  flagged = item => !!window.SideRepairFlags?.flagged(item);

  async setSize(size) {
    this.size = data().setSize(size);
    this.ready = false;this.pairs = new Map();this.previews = {};this.rendered.clear();
    this.componentStatus = {main: new Map(), sub: new Map()};
    await this.load();
  }

  async load() {
    if (this.loading) return;
    this.loading = true;
    try {
      const got = await data().load();
      this.catalog = got.catalog;this.pairs = got.pairs;this.previews = got.previews;this.error = '';
      this.components = got.components;this.reviews = got.reviews;this.run = got.run;this.statuses = got.statuses;
      if (Object.keys(this.reviews).length) window.SideRepairFlags?.setReviews(this.reviews);
      this.componentStatus = {main: new Map(), sub: new Map()};
      for (const item of [...this.components.mains, ...this.components.subs]) {
        item.status = item.drawings.some(d => usable(this, d)) ? 'done' : item.drawings.length ? 'failing' : 'missing';
      }
      for (const [role, list] of [['main', this.components.mains], ['sub', this.components.subs]]) {
        for (const item of list) for (const id of item.source_ids) this.componentStatus[role].set(id, item.status);
      }
      this.madeStatuses();
      this.ready = true;this.pairsVersion++;
    } catch (error) { this.error = error.message; }
    finally { this.loading = false;this.touch(); }
  }
  // A pair whose main / sub has no catalog drawing (picked by key, or made here): its status is the picked drawing's.
  madeStatuses() {
    for (const pair of this.pairs.values()) for (const role of ['main', 'sub']) {
      const id = pair[role + '_id'], item = pair[role + 's'][0];
      if (!id || !item || this.componentStatus[role].get(id) === 'done') continue;
      this.componentStatus[role].set(id, usable(this, {key: item.model_key, status: 'pass'}) ? 'done' : 'failing');
    }
  }
  // After a pair changed here (a build, a pick, a layout): read it again from D1 and redraw its row.
  async refresh(id) {
    // null: the pair is gone from D1; undefined: it could not be read (kept as it was).
    const got = await data().refresh(id).catch(error => { this.status = error.message;return undefined; });
    if (got) {
      this.pairs.set(id, got.pair);Object.assign(this.catalog.references, got.references);
      const rows = this.catalog.rows, at = rows.findIndex(r => r.id === id);
      if (at < 0) rows.unshift(got.row); else rows[at] = got.row;
      if (got.preview) this.previews[id] = got.preview; else delete this.previews[id];
      this.madeStatuses();
    } else if (got === null) {
      // Removed (a pair made here and taken back): it leaves the list.
      this.pairs.delete(id);delete this.previews[id];
      this.catalog.rows = this.catalog.rows.filter(r => r.id !== id);
    }
    if (got !== undefined) this.pairsVersion++;
    for (const k of [...this.rendered.keys()]) if (k.startsWith(id + '|')) this.rendered.delete(k);
    this.touch();
  }

  // The pair's stored combined icon (D1), else the one composed here from the current drawings.
  combined(pair, sub) {
    const prebuilt = this.previews[pair.id];
    if (prebuilt?.built) return prebuilt;
    return this.rendered.get(pair.id + '|' + sub.icon);
  }
  // Composes previews of pairs not built yet in the browser, two at a time.
  requestRender(pair, sub) {
    const k = pair.id + '|' + sub.icon;
    if (this.rendered.has(k) || this.#queue.some(q => q.k === k)) return;
    this.#queue.push({k, pair});this.#drain();
  }
  #drain() {
    while (this.#active < 2 && this.#queue.length) {
      const {k, pair} = this.#queue.shift();this.#active++;
      data().compose(pair.id)
        .then(c => this.rendered.set(k, {result: {...c.result, svg: c.svg}}))
        .catch(error => this.rendered.set(k, {error: error.message}))
        .finally(() => { this.#active--;this.#drain(); });
    }
  }

  buildState(id) { return data().item(id)?.state; }
  handLayout(id) { return data().handLayout(id); }
  staleRoles(id) { return data().staleRoles(id); }

  // Build all: every pair whose main and sub are drawn and that is not built yet or was built from older drawings,
  // each with its own saved layout, composed here and stored (50 a request).
  async buildPairs(ids, label) {
    this.combine = {status: 'running', message: `${label} 0 / ${ids.length}…`};
    try {
      const {results, skipped} = await data().buildPairs(ids, (n, total) => { this.combine = {status: 'running', message: `${label} ${n.toLocaleString()} / ${total.toLocaleString()}…`}; });
      const failed = results.filter(r => !r.ok), unchanged = results.filter(r => r.unchanged).length,
            waiting = results.filter(r => r.ok && !r.unchanged && r.build_failed).length;
      this.combine = {status: 'idle', message: ''};
      const done = results.filter(r => r.ok).length.toLocaleString();
      this.status = (label === 'Rebuilding' ? `Rebuilt ${done} stale side pairs.` : `Built ${done} side pairs.`)
        + (failed.length ? ` ${failed.length} refused (${failed[0].reference_id}: ${failed[0].error}).` : '')
        + (skipped.length ? ` ${skipped.length} could not be drawn (${skipped[0].reference_id}: ${skipped[0].error}).` : '')
        + (unchanged ? ` ${unchanged.toLocaleString()} came out the same as before (their Icon review status stays).` : '')
        + (waiting ? ` ${waiting.toLocaleString()} wait under Failed in Icon review until their main or sub is approved.` : '');
      this.ready = false;this.rendered.clear();
      await this.load();
    } catch (error) { this.combine = {status: 'error', message: error.message}; }
  }
}
