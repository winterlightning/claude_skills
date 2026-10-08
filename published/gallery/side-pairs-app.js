var SidePairsApp = (function(exports) {
	Object.defineProperty(exports, Symbol.toStringTag, { value: "Module" });
	//#region node_modules/svelte/src/internal/shared/utils.js
	var is_array = Array.isArray;
	var index_of = Array.prototype.indexOf;
	var includes = Array.prototype.includes;
	var array_from = Array.from;
	var define_property = Object.defineProperty;
	var get_descriptor = Object.getOwnPropertyDescriptor;
	var get_descriptors = Object.getOwnPropertyDescriptors;
	var object_prototype = Object.prototype;
	var array_prototype = Array.prototype;
	var get_prototype_of = Object.getPrototypeOf;
	var is_extensible = Object.isExtensible;
	var noop = () => {};
	/** @param {Array<() => void>} arr */
	function run_all(arr) {
		for (var i = 0; i < arr.length; i++) arr[i]();
	}
	/**
	* TODO replace with Promise.withResolvers once supported widely enough
	* @template [T=void]
	*/
	function deferred() {
		/** @type {(value: T) => void} */
		var resolve;
		/** @type {(reason: any) => void} */
		var reject;
		return {
			promise: new Promise((res, rej) => {
				resolve = res;
				reject = rej;
			}),
			resolve,
			reject
		};
	}
	/**
	* When encountering a situation like `let [a, b, c] = $derived(blah())`,
	* we need to stash an intermediate value that `a`, `b`, and `c` derive
	* from, in case it's an iterable
	* @template T
	* @param {ArrayLike<T> | Iterable<T>} value
	* @param {number} [n]
	* @returns {Array<T>}
	*/
	function to_array(value, n) {
		if (Array.isArray(value)) return value;
		if (n === void 0 || !(Symbol.iterator in value)) return Array.from(value);
		/** @type {T[]} */
		const array = [];
		for (const element of value) {
			array.push(element);
			if (array.length === n) break;
		}
		return array;
	}
	var CLEAN = 1024;
	var DIRTY = 2048;
	var MAYBE_DIRTY = 4096;
	var INERT = 8192;
	var DESTROYED = 16384;
	/** Set once a reaction has run for the first time */
	var REACTION_RAN = 32768;
	/** Effect is in the process of getting destroyed. Can be observed in child teardown functions */
	var DESTROYING = 1 << 25;
	/**
	* 'Transparent' effects do not create a transition boundary.
	* This is on a block effect 99% of the time but may also be on a branch effect if its parent block effect was pruned
	*/
	var EFFECT_TRANSPARENT = 65536;
	var EFFECT_PRESERVED = 1 << 19;
	var USER_EFFECT = 1 << 20;
	var EFFECT_OFFSCREEN = 1 << 25;
	var REACTION_IS_UPDATING = 1 << 21;
	var ASYNC = 1 << 22;
	var ERROR_VALUE = 1 << 23;
	var STATE_SYMBOL = Symbol("$state");
	/** Marks component export objects, so that `proxy(...)` leaves them untouched */
	var COMPONENT_SYMBOL = Symbol("component");
	var LEGACY_PROPS = Symbol("legacy props");
	var LOADING_ATTR_SYMBOL = Symbol("");
	var ATTRIBUTES_CACHE = Symbol("attributes");
	var CLASS_CACHE = Symbol("class");
	var STYLE_CACHE = Symbol("style");
	var TEXT_CACHE = Symbol("text");
	var FORM_RESET_HANDLER = Symbol("form reset");
	/** allow users to ignore aborted signal errors if `reason.name === 'StaleReactionError` */
	var STALE_REACTION = new class StaleReactionError extends Error {
		name = "StaleReactionError";
		message = "The reaction that called `getAbortSignal()` was re-run or destroyed";
	}();
	var IS_XHTML = !!globalThis.document?.contentType && /* @__PURE__ */ globalThis.document.contentType.includes("xml");
	//#endregion
	//#region node_modules/svelte/src/constants.js
	var HYDRATION_ERROR = {};
	var UNINITIALIZED = Symbol("uninitialized");
	var NAMESPACE_HTML = "http://www.w3.org/1999/xhtml";
	/**
	* Reading a derived belonging to a now-destroyed effect may result in stale values
	*/
	function derived_inert() {
		console.warn(`https://svelte.dev/e/derived_inert`);
	}
	/**
	* Hydration failed because the initial UI does not match what was rendered on the server. The error occurred near %location%
	* @param {string | undefined | null} [location]
	*/
	function hydration_mismatch(location) {
		console.warn(`https://svelte.dev/e/hydration_mismatch`);
	}
	/**
	* The `value` property of a `<select multiple>` element should be an array, but it received a non-array value. The selection will be kept as is.
	*/
	function select_multiple_invalid_value() {
		console.warn(`https://svelte.dev/e/select_multiple_invalid_value`);
	}
	/**
	* A `<svelte:boundary>` `reset` function only resets the boundary the first time it is called
	*/
	function svelte_boundary_reset_noop() {
		console.warn(`https://svelte.dev/e/svelte_boundary_reset_noop`);
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/hydration.js
	/** @import { TemplateNode } from '#client' */
	/**
	* Use this variable to guard everything related to hydration code so it can be treeshaken out
	* if the user doesn't use the `hydrate` method and these code paths are therefore not needed.
	*/
	var hydrating = false;
	/** @param {boolean} value */
	function set_hydrating(value) {
		hydrating = value;
	}
	/**
	* The node that is currently being hydrated. This starts out as the first node inside the opening
	* <!--[--> comment, and updates each time a component calls `$.child(...)` or `$.sibling(...)`.
	* When entering a block (e.g. `{#if ...}`), `hydrate_node` is the block opening comment; by the
	* time we leave the block it is the closing comment, which serves as the block's anchor.
	* @type {TemplateNode}
	*/
	var hydrate_node;
	/** @param {TemplateNode | null} node */
	function set_hydrate_node(node) {
		if (node === null) {
			hydration_mismatch();
			throw HYDRATION_ERROR;
		}
		return hydrate_node = node;
	}
	function hydrate_next() {
		return set_hydrate_node(/* @__PURE__ */ get_next_sibling(hydrate_node));
	}
	/** @param {TemplateNode} node */
	function reset(node) {
		if (!hydrating) return;
		if (/* @__PURE__ */ get_next_sibling(hydrate_node) !== null) {
			hydration_mismatch();
			throw HYDRATION_ERROR;
		}
		hydrate_node = node;
	}
	function next(count = 1) {
		if (hydrating) {
			var i = count;
			var node = hydrate_node;
			while (i--) node = /* @__PURE__ */ get_next_sibling(node);
			hydrate_node = node;
		}
	}
	/**
	* Skips or removes (depending on {@link remove}) all nodes starting at `hydrate_node` up until the next hydration end comment
	* @param {boolean} remove
	*/
	function skip_nodes(remove = true) {
		var depth = 0;
		var node = hydrate_node;
		while (true) {
			if (node.nodeType === 8) {
				var data = node.data;
				if (data === "]") {
					if (depth === 0) return node;
					depth -= 1;
				} else if (data === "[" || data === "[!" || data[0] === "[" && !isNaN(Number(data.slice(1)))) depth += 1;
			}
			var next = /* @__PURE__ */ get_next_sibling(node);
			if (remove) node.remove();
			node = next;
		}
	}
	/**
	*
	* @param {TemplateNode} node
	*/
	function read_hydration_instruction(node) {
		if (!node || node.nodeType !== 8) {
			hydration_mismatch();
			throw HYDRATION_ERROR;
		}
		return node.data;
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/reactivity/equality.js
	/** @import { Equals } from '#client' */
	/** @type {Equals} */
	function equals(value) {
		return value === this.v;
	}
	/**
	* @param {unknown} a
	* @param {unknown} b
	* @returns {boolean}
	*/
	function safe_not_equal(a, b) {
		return a != a ? b == b : a !== b || a !== null && typeof a === "object" || typeof a === "function";
	}
	/** @type {Equals} */
	function safe_equals(value) {
		return !safe_not_equal(value, this.v);
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/errors.js
	/**
	* Cannot create a `$derived(...)` with an `await` expression outside of an effect tree
	* @returns {never}
	*/
	function async_derived_orphan() {
		throw new Error(`https://svelte.dev/e/async_derived_orphan`);
	}
	/**
	* Keyed each block has duplicate key `%value%` at indexes %a% and %b%
	* @param {string} a
	* @param {string} b
	* @param {string | undefined | null} [value]
	* @returns {never}
	*/
	function each_key_duplicate(a, b, value) {
		throw new Error(`https://svelte.dev/e/each_key_duplicate`);
	}
	/**
	* `%rune%` cannot be used inside an effect cleanup function
	* @param {string} rune
	* @returns {never}
	*/
	function effect_in_teardown(rune) {
		throw new Error(`https://svelte.dev/e/effect_in_teardown`);
	}
	/**
	* Effect cannot be created inside a `$derived` value that was not itself created inside an effect
	* @returns {never}
	*/
	function effect_in_unowned_derived() {
		throw new Error(`https://svelte.dev/e/effect_in_unowned_derived`);
	}
	/**
	* `%rune%` can only be used inside an effect (e.g. during component initialisation)
	* @param {string} rune
	* @returns {never}
	*/
	function effect_orphan(rune) {
		throw new Error(`https://svelte.dev/e/effect_orphan`);
	}
	/**
	* Maximum update depth exceeded. This typically indicates that an effect reads and writes the same piece of state
	* @returns {never}
	*/
	function effect_update_depth_exceeded() {
		throw new Error(`https://svelte.dev/e/effect_update_depth_exceeded`);
	}
	/**
	* Cannot do `bind:%key%={undefined}` when `%key%` has a fallback value
	* @param {string} key
	* @returns {never}
	*/
	function props_invalid_value(key) {
		throw new Error(`https://svelte.dev/e/props_invalid_value`);
	}
	/**
	* Property descriptors defined on `$state` objects must contain `value` and always be `enumerable`, `configurable` and `writable`.
	* @returns {never}
	*/
	function state_descriptors_fixed() {
		throw new Error(`https://svelte.dev/e/state_descriptors_fixed`);
	}
	/**
	* Cannot set prototype of `$state` object
	* @returns {never}
	*/
	function state_prototype_fixed() {
		throw new Error(`https://svelte.dev/e/state_prototype_fixed`);
	}
	/**
	* Updating state inside `$derived(...)`, `$inspect(...)` or a template expression is forbidden. If the value should not be reactive, declare it without `$state`
	* @returns {never}
	*/
	function state_unsafe_mutation() {
		throw new Error(`https://svelte.dev/e/state_unsafe_mutation`);
	}
	/**
	* A `<svelte:boundary>` `reset` function cannot be called while an error is still being handled
	* @returns {never}
	*/
	function svelte_boundary_reset_onerror() {
		throw new Error(`https://svelte.dev/e/svelte_boundary_reset_onerror`);
	}
	//#endregion
	//#region node_modules/svelte/src/internal/flags/index.js
	/** True if experimental.async=true */
	var async_mode_flag = false;
	/** True if we're not certain that we only have Svelte 5 code in the compilation */
	var legacy_mode_flag = false;
	//#endregion
	//#region node_modules/svelte/src/internal/client/context.js
	/** @import { ComponentContext, DevStackEntry, Effect } from '#client' */
	/** @type {ComponentContext | null} */
	var component_context = null;
	/** @param {ComponentContext | null} context */
	function set_component_context(context) {
		component_context = context;
	}
	/**
	* @param {Record<string, unknown>} props
	* @param {any} runes
	* @param {Function} [fn]
	* @returns {void}
	*/
	function push(props, runes = false, fn) {
		component_context = {
			p: component_context,
			i: false,
			c: null,
			e: null,
			s: props,
			x: null,
			r: active_effect,
			l: legacy_mode_flag && !runes ? {
				s: null,
				u: null,
				$: []
			} : null
		};
	}
	/**
	* @template {Record<string, any>} T
	* @param {T} [component]
	* @returns {T}
	*/
	function pop(component) {
		var context = component_context;
		var effects = context.e;
		if (effects !== null) {
			context.e = null;
			for (var fn of effects) create_user_effect(fn);
		}
		if (component !== void 0) context.x = component;
		context.i = true;
		component_context = context.p;
		return mark_as_component(component);
	}
	/**
	* Add a symbol to the object (or create one if undefined) to mark it as a component so it isn't proxified.
	* @param {any} component
	*/
	function mark_as_component(component = {}) {
		define_property(component, COMPONENT_SYMBOL, { value: true });
		return component;
	}
	/** @returns {boolean} */
	function is_runes() {
		return !legacy_mode_flag || component_context !== null && component_context.l === null;
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/task.js
	/** @type {Array<() => void>} */
	var micro_tasks = [];
	function run_micro_tasks() {
		var tasks = micro_tasks;
		micro_tasks = [];
		run_all(tasks);
	}
	/**
	* @param {() => void} fn
	*/
	function queue_micro_task(fn) {
		if (micro_tasks.length === 0 && !is_flushing_sync) {
			var tasks = micro_tasks;
			queueMicrotask(() => {
				if (tasks === micro_tasks) run_micro_tasks();
			});
		}
		micro_tasks.push(fn);
	}
	/**
	* Synchronously run any queued tasks.
	*/
	function flush_tasks() {
		while (micro_tasks.length > 0) run_micro_tasks();
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/reactivity/status.js
	/** @import { Derived, Signal } from '#client' */
	var STATUS_MASK = ~(DIRTY | MAYBE_DIRTY | CLEAN);
	/**
	* @param {Signal} signal
	* @param {number} status
	*/
	function set_signal_status(signal, status) {
		signal.f = signal.f & STATUS_MASK | status;
	}
	/**
	* Set a derived's status to CLEAN or MAYBE_DIRTY based on its connection state.
	* @param {Derived} derived
	*/
	function update_derived_status(derived) {
		if ((derived.f & 512) !== 0 || derived.deps === null) set_signal_status(derived, CLEAN);
		else set_signal_status(derived, MAYBE_DIRTY);
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/reactivity/utils.js
	/** @import { Effect } from '#client' */
	/**
	* @param {Effect} effect
	* @param {Set<Effect>} dirty_effects
	* @param {Set<Effect>} maybe_dirty_effects
	*/
	function defer_effect(effect, dirty_effects, maybe_dirty_effects) {
		if ((effect.f & 2048) !== 0) dirty_effects.add(effect);
		else if ((effect.f & 4096) !== 0) maybe_dirty_effects.add(effect);
		set_signal_status(effect, CLEAN);
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/elements/misc.js
	var listening_to_form_reset = false;
	function add_form_reset_listener() {
		if (!listening_to_form_reset) {
			listening_to_form_reset = true;
			document.addEventListener("reset", (evt) => {
				Promise.resolve().then(() => {
					if (!evt.defaultPrevented) for (const e of evt.target.elements)
 /** @type {any} */ e[FORM_RESET_HANDLER]?.();
				});
			}, { capture: true });
		}
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/elements/bindings/shared.js
	/**
	* @template T
	* @param {() => T} fn
	*/
	function without_reactive_context(fn) {
		var previous_reaction = active_reaction;
		var previous_effect = active_effect;
		set_active_reaction(null);
		set_active_effect(null);
		try {
			return fn();
		} finally {
			set_active_reaction(previous_reaction);
			set_active_effect(previous_effect);
		}
	}
	/**
	* Listen to the given event, and then instantiate a global form reset listener if not already done,
	* to notify all bindings when the form is reset
	* @param {HTMLElement} element
	* @param {string} event
	* @param {(is_reset?: true) => void} handler
	* @param {(is_reset?: true) => void} [on_reset]
	*/
	function listen_to_event_and_reset_event(element, event, handler, on_reset = handler) {
		element.addEventListener(event, () => without_reactive_context(handler));
		const prev = element[FORM_RESET_HANDLER];
		if (prev)
 /** @type {any} */ element[FORM_RESET_HANDLER] = () => {
			prev();
			on_reset(true);
		};
		else
 /** @type {any} */ element[FORM_RESET_HANDLER] = () => on_reset(true);
		add_form_reset_listener();
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/reactivity/async.js
	/** @import { Blocker, Effect, Source, Value } from '#client' */
	/**
	* @param {Blocker[]} blockers
	* @param {Array<() => any>} sync
	* @param {Array<() => Promise<any>>} async
	* @param {(values: Value[]) => any} fn
	*/
	function flatten(blockers, sync, async, fn) {
		const d = is_runes() ? derived : derived_safe_equal;
		var pending = blockers.filter((b) => !b.settled);
		var deriveds = sync.map(d);
		if (async.length === 0 && pending.length === 0) {
			fn(deriveds);
			return;
		}
		var parent = active_effect;
		var restore = capture();
		var blocker_promise = pending.length === 1 ? pending[0].promise : pending.length > 1 ? Promise.all(pending.map((b) => b.promise)) : null;
		/**
		* @param {Source[]} async
		*/
		function finish(async) {
			if ((parent.f & 16384) !== 0) return;
			restore();
			try {
				fn([...deriveds, ...async]);
			} catch (error) {
				invoke_error_boundary(error, parent);
			}
			unset_context();
		}
		var decrement_pending = increment_pending();
		if (async.length === 0) {
			/** @type {Promise<any>} */ blocker_promise.then(() => finish([])).finally(decrement_pending);
			return;
		}
		function run() {
			Promise.all(async.map((expression) => /* @__PURE__ */ async_derived(expression))).then(finish).catch((error) => invoke_error_boundary(error, parent)).finally(decrement_pending);
		}
		if (blocker_promise) blocker_promise.then(() => {
			restore();
			run();
			unset_context();
		});
		else run();
	}
	/**
	* Captures the current effect context so that we can restore it after
	* some asynchronous work has happened (so that e.g. `await a + b`
	* causes `b` to be registered as a dependency).
	*/
	function capture() {
		var previous_effect = active_effect;
		var previous_reaction = active_reaction;
		var previous_component_context = component_context;
		var previous_batch = current_batch;
		return function restore(activate_batch = true) {
			set_active_effect(previous_effect);
			set_active_reaction(previous_reaction);
			set_component_context(previous_component_context);
			if (activate_batch && (previous_effect.f & 16384) === 0) {
				previous_batch?.activate();
				previous_batch?.apply();
			}
		};
	}
	function unset_context(deactivate_batch = true) {
		set_active_effect(null);
		set_active_reaction(null);
		set_component_context(null);
		if (deactivate_batch) current_batch?.deactivate();
	}
	/**
	* @returns {(skip?: boolean) => void}
	*/
	function increment_pending() {
		var effect = active_effect;
		var boundary = effect.b;
		var batch = current_batch;
		var blocking = !!boundary?.is_rendered();
		boundary?.update_pending_count(1, batch);
		batch.increment(blocking, effect);
		return () => {
			boundary?.update_pending_count(-1, batch);
			batch.decrement(blocking, effect);
		};
	}
	/**
	* @template V
	* @param {() => V} fn
	* @returns {Derived<V>}
	*/
	/*#__NO_SIDE_EFFECTS__*/
	function derived(fn) {
		var flags = 2 | DIRTY;
		if (active_effect !== null) active_effect.f |= EFFECT_PRESERVED;
		return {
			ctx: component_context,
			deps: null,
			effects: null,
			equals,
			f: flags,
			fn,
			reactions: null,
			rv: 0,
			v: UNINITIALIZED,
			wv: 0,
			parent: active_effect,
			ac: null
		};
	}
	var OBSOLETE = Symbol("obsolete");
	/**
	* @template V
	* @param {() => V | Promise<V>} fn
	* @param {string} [label]
	* @param {string} [location] If provided, print a warning if the value is not read immediately after update
	* @returns {Promise<Source<V>>}
	*/
	/*#__NO_SIDE_EFFECTS__*/
	function async_derived(fn, label, location) {
		let parent = active_effect;
		if (parent === null) async_derived_orphan();
		var promise = void 0;
		var signal = source(UNINITIALIZED);
		var should_suspend = !active_reaction;
		/** @type {Set<ReturnType<typeof deferred<V>>>} */
		var deferreds = /* @__PURE__ */ new Set();
		async_effect(() => {
			var effect = active_effect;
			/** @type {ReturnType<typeof deferred<V>>} */
			var d = deferred();
			promise = d.promise;
			try {
				Promise.resolve(fn()).then(d.resolve, (e) => {
					if (e !== STALE_REACTION) d.reject(e);
				}).finally(unset_context);
			} catch (error) {
				d.reject(error);
				unset_context();
			}
			var batch = current_batch;
			if (should_suspend) {
				if ((effect.f & 32768) !== 0) var decrement_pending = increment_pending();
				if (parent.b?.is_rendered()) batch.async_deriveds.get(effect)?.reject(OBSOLETE);
				else for (const d of deferreds.values()) d.reject(OBSOLETE);
				deferreds.add(d);
				batch.async_deriveds.set(effect, d);
			}
			/**
			* @param {any} value
			* @param {unknown} error
			*/
			const handler = (value, error = void 0) => {
				decrement_pending?.();
				deferreds.delete(d);
				if (error === OBSOLETE) return;
				batch.activate();
				if (error) {
					signal.f |= ERROR_VALUE;
					internal_set(signal, error);
				} else {
					if ((signal.f & 8388608) !== 0) signal.f ^= ERROR_VALUE;
					internal_set(signal, value);
				}
				batch.deactivate();
			};
			d.promise.then(handler, (e) => handler(null, e || "unknown"));
		});
		teardown(() => {
			for (const d of deferreds) d.reject(OBSOLETE);
		});
		return new Promise((fulfil) => {
			/** @param {Promise<V>} p */
			function next(p) {
				function go() {
					if (p === promise) fulfil(signal);
					else next(promise);
				}
				p.then(go, go);
			}
			next(promise);
		});
	}
	/**
	* @template V
	* @param {() => V} fn
	* @returns {Derived<V>}
	*/
	/*#__NO_SIDE_EFFECTS__*/
	function user_derived(fn) {
		const d = /* @__PURE__ */ derived(fn);
		if (!async_mode_flag) push_reaction_value(d);
		return d;
	}
	/**
	* @template V
	* @param {() => V} fn
	* @returns {Derived<V>}
	*/
	/*#__NO_SIDE_EFFECTS__*/
	function derived_safe_equal(fn) {
		const signal = /* @__PURE__ */ derived(fn);
		signal.equals = safe_equals;
		return signal;
	}
	/**
	* @param {Derived} derived
	* @returns {void}
	*/
	function destroy_derived_effects(derived) {
		var effects = derived.effects;
		if (effects !== null) {
			derived.effects = null;
			for (var i = 0; i < effects.length; i += 1) destroy_effect(effects[i]);
		}
	}
	/**
	* @template T
	* @param {Derived} derived
	* @returns {T}
	*/
	function execute_derived(derived) {
		var value;
		var prev_active_effect = active_effect;
		var parent = derived.parent;
		if (!is_destroying_effect && parent !== null && derived.v !== UNINITIALIZED && (parent.f & 24576) !== 0) {
			derived_inert();
			return derived.v;
		}
		set_active_effect(parent);
		try {
			destroy_derived_effects(derived);
			value = update_reaction(derived);
		} finally {
			set_active_effect(prev_active_effect);
		}
		return value;
	}
	/**
	* @param {Derived} derived
	* @returns {void}
	*/
	function update_derived(derived) {
		var value = execute_derived(derived);
		if (!derived.equals(value)) {
			derived.wv = increment_write_version();
			if (!current_batch?.is_fork || derived.deps === null) {
				if (current_batch !== null) {
					current_batch.capture(derived, value, true);
					previous_batch?.capture(derived, value, true);
				} else derived.v = value;
				if (derived.deps === null) {
					set_signal_status(derived, CLEAN);
					return;
				}
			}
		}
		if (is_destroying_effect) return;
		if (batch_values !== null) {
			if (effect_tracking() || current_batch?.is_fork) batch_values.set(derived, value);
		} else update_derived_status(derived);
	}
	/**
	* @param {Derived} derived
	*/
	function freeze_derived_effects(derived) {
		if (derived.effects === null) return;
		for (const e of derived.effects) if (e.teardown || e.ac) {
			e.teardown?.();
			if (e.ac !== null) without_reactive_context(() => {
				/** @type {AbortController} */ e.ac.abort(STALE_REACTION);
				e.ac = null;
			});
			if (e.fn !== null) e.teardown = noop;
			remove_reactions(e, 0);
			destroy_effect_children(e);
		}
	}
	/**
	* @param {Derived} derived
	*/
	function unfreeze_derived_effects(derived) {
		if (derived.effects === null) return;
		for (const e of derived.effects) if (e.teardown && e.fn !== null) update_effect(e);
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/reactivity/batch.js
	/** @import { Fork } from 'svelte' */
	/** @import { Derived, Effect, Reaction, Source, Value } from '#client' */
	/** @type {Batch | null} */
	var first_batch = null;
	/** @type {Batch | null} */
	var last_batch = null;
	/** @type {Batch | null} */
	var current_batch = null;
	/**
	* This is needed to avoid overwriting inputs
	* @type {Batch | null}
	*/
	var previous_batch = null;
	/**
	* When time travelling (i.e. working in one batch, while other batches
	* still have ongoing work), we ignore the real values of affected
	* signals in favour of their values within the batch
	* @type {Map<Value, any> | null}
	*/
	var batch_values = null;
	/** @type {Effect | null} */
	var last_scheduled_effect = null;
	var is_flushing_sync = false;
	var is_processing = false;
	/**
	* During traversal, this is an array. Newly created effects are (if not immediately
	* executed) pushed to this array, rather than going through the scheduling
	* rigamarole that would cause another turn of the flush loop.
	* @type {Effect[] | null}
	*/
	var collected_effects = null;
	/**
	* An array of effects that are marked during traversal as a result of a `set`
	* (not `internal_set`) call. These will be added to the next batch and
	* trigger another `batch.process()`
	* @type {Effect[] | null}
	* @deprecated when we get rid of legacy mode and stores, we can get rid of this
	*/
	var legacy_updates = null;
	var flush_count = 0;
	var uid = 1;
	var Batch = class Batch {
		id = uid++;
		/** True as soon as `#process` was called */
		#started = false;
		linked = true;
		/** @type {Batch | null} */
		#prev = null;
		/** @type {Batch | null} */
		#next = null;
		/** @type {Map<Effect, ReturnType<typeof deferred<any>>>} */
		async_deriveds = /* @__PURE__ */ new Map();
		/**
		* The current values of any signals that are updated in this batch.
		* Tuple format: [value, is_derived] (note: is_derived is false for deriveds, too, if they were overridden via assignment)
		* They keys of this map are identical to `this.#previous`
		* @type {Map<Value, [any, boolean]>}
		*/
		current = /* @__PURE__ */ new Map();
		/**
		* The values of any signals (sources and deriveds) that are updated in this batch _before_ those updates took place.
		* They keys of this map are identical to `this.#current`
		* @type {Map<Value, any>}
		*/
		previous = /* @__PURE__ */ new Map();
		/**
		* When the batch is committed (and the DOM is updated), we need to remove old branches
		* and append new ones by calling the functions added inside (if/each/key/etc) blocks
		* @type {Set<(batch: Batch) => void>}
		*/
		#commit_callbacks = /* @__PURE__ */ new Set();
		/**
		* If a fork is discarded, we need to destroy any effects that are no longer needed
		* @type {Set<(batch: Batch) => void>}
		*/
		#discard_callbacks = /* @__PURE__ */ new Set();
		/**
		* The number of async effects that are currently in flight
		*/
		#pending = 0;
		/**
		* Async effects that are currently in flight, _not_ inside a pending boundary
		* @type {Map<Effect, number>}
		*/
		#blocking_pending = /* @__PURE__ */ new Map();
		/**
		* A deferred that resolves when the batch is committed, used with `settled()`
		* TODO replace with Promise.withResolvers once supported widely enough
		* @type {{ promise: Promise<void>, resolve: (value?: any) => void, reject: (reason: unknown) => void } | null}
		*/
		#deferred = null;
		/**
		* Effects that were scheduled in this batch but not yet 'resolved' into the
		* root effects that need to be flushed. Resolving — the upwards traversal that
		* marks the path to each effect on the shared effect tree (see #resolve) — is
		* deferred until the batch is processed, so that the markers are created and
		* consumed within a single traversal. Scheduling into other batches (which can
		* happen concurrently, e.g. while a batch is committed) can therefore never
		* observe (and be confused by) this batch's markers.
		* May contain duplicates — deduplication happens during resolving
		* @type {Effect[]}
		*/
		#scheduled = [];
		/**
		* Effects created while this batch was active.
		* @type {Effect[]}
		*/
		#new_effects = [];
		/**
		* Deferred effects (which run after async work has completed) that are DIRTY
		* @type {Set<Effect>}
		*/
		#dirty_effects = /* @__PURE__ */ new Set();
		/**
		* Deferred effects that are MAYBE_DIRTY
		* @type {Set<Effect>}
		*/
		#maybe_dirty_effects = /* @__PURE__ */ new Set();
		/**
		* A map of branches that still exist, but will be destroyed when this batch
		* is committed — we skip over these during `process`.
		* The value contains child effects that were dirty/maybe_dirty before being reset,
		* so they can be rescheduled if the branch survives.
		* @type {Map<Effect, { d: Effect[], m: Effect[] }>}
		*/
		#skipped_branches = /* @__PURE__ */ new Map();
		/**
		* Inverse of #skipped_branches which we need to tell prior batches to unskip them when committing
		* @type {Set<Effect>}
		*/
		#unskipped_branches = /* @__PURE__ */ new Set();
		is_fork = false;
		#decrement_queued = false;
		constructor() {
			if (last_batch === null) first_batch = last_batch = this;
			else {
				last_batch.#next = this;
				this.#prev = last_batch;
			}
			last_batch = this;
		}
		#is_deferred() {
			if (this.is_fork) return true;
			for (const effect of this.#blocking_pending.keys()) {
				var e = effect;
				var skipped = false;
				while (e.parent !== null) {
					if (this.#skipped_branches.has(e)) {
						skipped = true;
						break;
					}
					e = e.parent;
				}
				if (!skipped) return true;
			}
			return false;
		}
		/**
		* Add an effect to the #skipped_branches map and reset its children
		* @param {Effect} effect
		*/
		skip_effect(effect) {
			if (!this.#skipped_branches.has(effect)) this.#skipped_branches.set(effect, {
				d: [],
				m: []
			});
			this.#unskipped_branches.delete(effect);
		}
		/**
		* Remove an effect from the #skipped_branches map and reschedule
		* any tracked dirty/maybe_dirty child effects
		* @param {Effect} effect
		* @param {(e: Effect) => void} callback
		*/
		unskip_effect(effect, callback = (e) => this.schedule(e)) {
			var tracked = this.#skipped_branches.get(effect);
			if (tracked) {
				this.#skipped_branches.delete(effect);
				for (var e of tracked.d) {
					set_signal_status(e, DIRTY);
					callback(e);
				}
				for (e of tracked.m) {
					set_signal_status(e, MAYBE_DIRTY);
					callback(e);
				}
			}
			this.#unskipped_branches.add(effect);
		}
		/**
		* Convert the effects that were scheduled in this batch into the root effects
		* that need to be traversed, marking the path to each effect (by clearing the
		* `CLEAN` flag on ancestor branches) so that the traversal can find them.
		* This happens right before traversal rather than at scheduling time, so that
		* the markers left on the (shared) effect tree are created and consumed within
		* a single traversal — scheduling into other batches can never observe them
		* @returns {Effect[]}
		*/
		#resolve() {
			/** @type {Effect[]} */
			var roots = [];
			for (const effect of this.#scheduled) {
				if ((effect.f & 16384) !== 0 || (effect.f & 6144) === 0) continue;
				var e = effect;
				var covered = false;
				while (e.parent !== null) {
					e = e.parent;
					var flags = e.f;
					if ((flags & 96) !== 0) {
						if ((flags & 1024) === 0) {
							covered = true;
							break;
						}
						e.f ^= CLEAN;
					}
				}
				if (!covered) roots.push(e);
			}
			this.#scheduled = [];
			return roots;
		}
		#process() {
			this.#started = true;
			for (const e of this.#dirty_effects) {
				this.#maybe_dirty_effects.delete(e);
				set_signal_status(e, DIRTY);
				this.schedule(e);
			}
			for (const e of this.#maybe_dirty_effects) {
				set_signal_status(e, MAYBE_DIRTY);
				this.schedule(e);
			}
			this.apply();
			/** @type {Effect[]} */
			var effects = collected_effects = [];
			/** @type {Effect[]} */
			var render_effects = [];
			/**
			* @type {Effect[]}
			* @deprecated when we get rid of legacy mode and stores, we can get rid of this
			*/
			var updates = legacy_updates = [];
			while (this.#scheduled.length > 0) {
				if (flush_count++ > 1e3) {
					this.#unlink();
					infinite_loop_guard();
				}
				for (const root of this.#resolve()) try {
					this.#traverse(root, effects, render_effects);
				} catch (e) {
					reset_all(root);
					if (!this.#is_deferred()) this.discard();
					throw e;
				}
			}
			current_batch = null;
			if (updates.length > 0) {
				var batch = Batch.ensure();
				for (const e of updates) batch.schedule(e);
			}
			collected_effects = null;
			legacy_updates = null;
			if (this.#is_deferred()) {
				this.#defer_effects(render_effects);
				this.#defer_effects(effects);
				for (const [e, t] of this.#skipped_branches) reset_branch(e, t);
				if (updates.length > 0)
 /** @type {Batch} */ current_batch.#process();
				return;
			}
			const earlier_batch = this.#find_earlier_batch();
			if (earlier_batch) {
				this.#defer_effects(render_effects);
				this.#defer_effects(effects);
				earlier_batch.#merge(this);
				return;
			}
			this.#dirty_effects.clear();
			this.#maybe_dirty_effects.clear();
			for (const fn of this.#commit_callbacks) fn(this);
			this.#commit_callbacks.clear();
			previous_batch = this;
			flush_queued_effects(render_effects);
			flush_queued_effects(effects);
			previous_batch = null;
			this.#deferred?.resolve();
			var next_batch = current_batch;
			if (this.#pending === 0 && (this.#scheduled.length === 0 || next_batch !== null)) {
				this.#unlink();
				if (async_mode_flag) {
					this.#commit();
					current_batch = next_batch;
				}
			}
			if (this.#scheduled.length > 0) {
				if (next_batch !== null) {
					for (const e of this.#scheduled) next_batch.#scheduled.push(e);
					this.#scheduled = [];
				} else next_batch = this;
			}
			if (next_batch !== null) {
				old_values.clear();
				next_batch.#process();
			}
		}
		/**
		* Traverse the effect tree, executing effects or stashing
		* them for later execution as appropriate
		* @param {Effect} root
		* @param {Effect[]} effects
		* @param {Effect[]} render_effects
		*/
		#traverse(root, effects, render_effects) {
			root.f ^= CLEAN;
			var effect = root.first;
			while (effect !== null) {
				var flags = effect.f;
				var is_branch = (flags & 96) !== 0;
				if (!(is_branch && (flags & 1024) !== 0 || (flags & 8192) !== 0 || this.#skipped_branches.has(effect)) && effect.fn !== null) {
					if (is_branch) effect.f ^= CLEAN;
					else if ((flags & 4) !== 0) effects.push(effect);
					else if (async_mode_flag && (flags & 16777224) !== 0) render_effects.push(effect);
					else if (is_dirty(effect)) {
						if ((flags & 16) !== 0) this.#maybe_dirty_effects.add(effect);
						update_effect(effect);
					}
					var child = effect.first;
					if (child !== null) {
						effect = child;
						continue;
					}
				}
				while (effect !== null) {
					var next = effect.next;
					if (next !== null) {
						effect = next;
						break;
					}
					effect = effect.parent;
				}
			}
		}
		#find_earlier_batch() {
			var batch = this.#prev;
			while (batch !== null) {
				if (!batch.is_fork) {
					for (const [value, [, is_derived]] of this.current) if (batch.current.has(value) && !is_derived) return batch;
				}
				batch = batch.#prev;
			}
			return null;
		}
		/**
		* @param {Batch} batch
		*/
		#merge(batch) {
			for (const [source, value] of batch.current) {
				if (!this.previous.has(source) && batch.previous.has(source)) this.previous.set(source, batch.previous.get(source));
				this.current.set(source, value);
			}
			for (const [effect, deferred] of batch.async_deriveds) {
				const d = this.async_deriveds.get(effect);
				if (d) deferred.promise.then(d.resolve).catch(d.reject);
			}
			batch.async_deriveds.clear();
			this.transfer_effects(batch.#dirty_effects, batch.#maybe_dirty_effects);
			/**
			* mark all effects that depend on `batch.current`, except the
			* async effects that we just resolved (TODO unless they depend
			* on values in this batch that are NOT in the later batch?).
			* Through this we also will populate the correct #skipped_branches,
			* oncommit callbacks etc, so we don't need to merge them separately.
			* @param {Value} value
			*/
			const mark = (value) => {
				var reactions = value.reactions;
				if (reactions === null) return;
				if ((value.f & 2) !== 0 && (value.f & 6144) === 0) return;
				for (const reaction of reactions) {
					var flags = reaction.f;
					if ((flags & 2) !== 0) mark(reaction);
					else {
						var effect = reaction;
						if (flags & 4194320 && !this.async_deriveds.has(effect)) {
							this.#maybe_dirty_effects.delete(effect);
							set_signal_status(effect, DIRTY);
							this.schedule(effect);
						}
					}
				}
			};
			for (const source of this.current.keys()) mark(source);
			this.oncommit(() => batch.discard());
			batch.#unlink();
			current_batch = this;
			this.#process();
		}
		/**
		* @param {Effect[]} effects
		*/
		#defer_effects(effects) {
			for (var i = 0; i < effects.length; i += 1) defer_effect(effects[i], this.#dirty_effects, this.#maybe_dirty_effects);
		}
		/**
		* Associate a change to a given source with the current
		* batch, noting its previous and current values
		* @param {Value} source
		* @param {any} value
		* @param {boolean} [is_derived]
		*/
		capture(source, value, is_derived = false) {
			if (source.v !== UNINITIALIZED && !this.previous.has(source)) this.previous.set(source, source.v);
			if ((source.f & 8388608) === 0) {
				this.current.set(source, [value, is_derived]);
				batch_values?.set(source, value);
			}
			if (!this.is_fork) source.v = value;
		}
		activate() {
			current_batch = this;
		}
		deactivate() {
			current_batch = null;
			batch_values = null;
		}
		flush() {
			try {
				is_processing = true;
				current_batch = this;
				this.#process();
			} finally {
				flush_count = 0;
				last_scheduled_effect = null;
				collected_effects = null;
				legacy_updates = null;
				is_processing = false;
				current_batch = null;
				batch_values = null;
				old_values.clear();
			}
		}
		discard() {
			for (const fn of this.#discard_callbacks) fn(this);
			this.#discard_callbacks.clear();
			for (const deferred of this.async_deriveds.values()) deferred.reject(OBSOLETE);
			this.#unlink();
			this.#deferred?.resolve();
		}
		/**
		* @param {Effect} effect
		*/
		register_created_effect(effect) {
			this.#new_effects.push(effect);
		}
		#commit() {
			for (let batch = first_batch; batch !== null; batch = batch.#next) {
				var is_earlier = batch.id < this.id;
				/** @type {Source[]} */
				var sources = [];
				for (const [source, [value, is_derived]] of this.current) {
					if (batch.current.has(source)) {
						var batch_value = batch.current.get(source)[0];
						if (is_earlier && value !== batch_value) batch.current.set(source, [value, is_derived]);
						else continue;
					}
					sources.push(source);
				}
				if (is_earlier) for (const [effect, deferred] of this.async_deriveds) {
					const d = batch.async_deriveds.get(effect);
					if (d) deferred.promise.then(d.resolve).catch(d.reject);
				}
				var current = [...batch.current.keys()].filter((source) => !batch.current.get(source)[1]);
				if (!batch.#started || current.length === 0) continue;
				var others = current.filter((source) => !this.current.has(source));
				if (others.length === 0) {
					if (is_earlier) batch.discard();
				} else if (sources.length > 0) {
					if (is_earlier) for (const unskipped of this.#unskipped_branches) batch.unskip_effect(unskipped, (e) => {
						if ((e.f & 4194320) !== 0) batch.schedule(e);
						else batch.#defer_effects([e]);
					});
					batch.activate();
					/** @type {Set<Value>} */
					var marked = /* @__PURE__ */ new Set();
					/** @type {Map<Reaction, boolean>} */
					var checked = /* @__PURE__ */ new Map();
					for (var source of sources) mark_effects(source, others, marked, checked);
					checked = /* @__PURE__ */ new Map();
					var current_unequal = [...batch.current].filter(([c, v1]) => {
						const v2 = this.current.get(c);
						if (!v2) return true;
						return v2[0] !== v1[0] || v2[1] !== v1[1];
					}).map(([c]) => c);
					if (current_unequal.length > 0) {
						for (const effect of this.#new_effects) if ((effect.f & 155648) === 0 && depends_on(effect, current_unequal, checked)) {
							if ((effect.f & 4194320) !== 0) {
								set_signal_status(effect, DIRTY);
								batch.schedule(effect);
							} else batch.#dirty_effects.add(effect);
						}
					}
					if (batch.#scheduled.length > 0 && !batch.#decrement_queued) {
						batch.apply();
						for (var root of batch.#resolve()) batch.#traverse(root, [], []);
					}
					batch.deactivate();
				}
			}
		}
		/**
		* @param {boolean} blocking
		* @param {Effect} effect
		*/
		increment(blocking, effect) {
			this.#pending += 1;
			if (blocking) {
				let blocking_pending_count = this.#blocking_pending.get(effect) ?? 0;
				this.#blocking_pending.set(effect, blocking_pending_count + 1);
			}
		}
		/**
		* @param {boolean} blocking
		* @param {Effect} effect
		*/
		decrement(blocking, effect) {
			this.#pending -= 1;
			if (blocking) {
				let blocking_pending_count = this.#blocking_pending.get(effect) ?? 0;
				if (blocking_pending_count === 1) this.#blocking_pending.delete(effect);
				else this.#blocking_pending.set(effect, blocking_pending_count - 1);
			}
			if (this.#decrement_queued) return;
			this.#decrement_queued = true;
			queue_micro_task(() => {
				this.#decrement_queued = false;
				if (this.linked) this.flush();
			});
		}
		/**
		* @param {Set<Effect>} dirty_effects
		* @param {Set<Effect>} maybe_dirty_effects
		*/
		transfer_effects(dirty_effects, maybe_dirty_effects) {
			for (const e of dirty_effects) this.#dirty_effects.add(e);
			for (const e of maybe_dirty_effects) this.#maybe_dirty_effects.add(e);
			dirty_effects.clear();
			maybe_dirty_effects.clear();
		}
		/** @param {(batch: Batch) => void} fn */
		oncommit(fn) {
			this.#commit_callbacks.add(fn);
		}
		/** @param {(batch: Batch) => void} fn */
		ondiscard(fn) {
			this.#discard_callbacks.add(fn);
		}
		settled() {
			return (this.#deferred ??= deferred()).promise;
		}
		static ensure() {
			if (current_batch === null) {
				const batch = current_batch = new Batch();
				if (!is_processing && !is_flushing_sync) queue_micro_task(() => {
					if (!batch.#started) batch.flush();
				});
			}
			return current_batch;
		}
		apply() {
			if (!async_mode_flag || !this.is_fork && this.#prev === null && this.#next === null) {
				batch_values = null;
				return;
			}
			batch_values = /* @__PURE__ */ new Map();
			for (const [source, [value]] of this.current) batch_values.set(source, value);
			for (let batch = first_batch; batch !== null; batch = batch.#next) {
				if (batch === this || batch.is_fork) continue;
				var intersects = false;
				if (batch.id < this.id) for (const [source, [, is_derived]] of batch.current) {
					if (is_derived) continue;
					if (this.current.has(source)) {
						intersects = true;
						break;
					}
				}
				if (!intersects) {
					for (const [source, previous] of batch.previous) if (!batch_values.has(source)) batch_values.set(source, previous);
				}
			}
		}
		/**
		*
		* @param {Effect} effect
		*/
		schedule(effect) {
			last_scheduled_effect = effect;
			if (effect.b?.is_pending && (effect.f & 16777228) !== 0 && (effect.f & 32768) === 0) {
				effect.b.defer_effect(effect);
				return;
			}
			this.#scheduled.push(effect);
		}
		#unlink() {
			if (!this.linked) return;
			var prev = this.#prev;
			var next = this.#next;
			if (prev === null) first_batch = next;
			else prev.#next = next;
			if (next === null) last_batch = prev;
			else next.#prev = prev;
			this.linked = false;
		}
	};
	/**
	* Synchronously flush any pending updates.
	* Returns void if no callback is provided, otherwise returns the result of calling the callback.
	* @template [T=void]
	* @param {(() => T) | undefined} [fn]
	* @returns {T}
	*/
	function flushSync(fn) {
		var was_flushing_sync = is_flushing_sync;
		is_flushing_sync = true;
		try {
			var result;
			if (fn) {
				if (current_batch !== null && !current_batch.is_fork) current_batch.flush();
				result = fn();
			}
			while (true) {
				flush_tasks();
				if (current_batch === null) return result;
				current_batch.flush();
			}
		} finally {
			is_flushing_sync = was_flushing_sync;
		}
	}
	function infinite_loop_guard() {
		try {
			effect_update_depth_exceeded();
		} catch (error) {
			invoke_error_boundary(error, last_scheduled_effect);
		}
	}
	/** @type {Set<Effect> | null} */
	var eager_block_effects = null;
	/**
	* @param {Array<Effect>} effects
	* @returns {void}
	*/
	function flush_queued_effects(effects) {
		var length = effects.length;
		if (length === 0) return;
		var i = 0;
		while (i < length) {
			var effect = effects[i++];
			if ((effect.f & 24576) === 0 && is_dirty(effect)) {
				eager_block_effects = /* @__PURE__ */ new Set();
				update_effect(effect);
				if (effect.deps === null && effect.first === null && effect.nodes === null && effect.teardown === null && effect.ac === null) unlink_effect(effect);
				if (eager_block_effects?.size > 0) {
					old_values.clear();
					for (const e of eager_block_effects) {
						if ((e.f & 24576) !== 0) continue;
						/** @type {Effect[]} */
						const ordered_effects = [e];
						let ancestor = e.parent;
						while (ancestor !== null) {
							if (eager_block_effects.has(ancestor)) {
								eager_block_effects.delete(ancestor);
								ordered_effects.push(ancestor);
							}
							ancestor = ancestor.parent;
						}
						for (let j = ordered_effects.length - 1; j >= 0; j--) {
							const e = ordered_effects[j];
							if ((e.f & 24576) !== 0) continue;
							update_effect(e);
						}
					}
					eager_block_effects.clear();
				}
			}
		}
		eager_block_effects = null;
	}
	/**
	* This is similar to `mark_reactions`, but it only marks async/block effects
	* depending on `value` and at least one of the other `sources`, so that
	* these effects can re-run after another batch has been committed
	* @param {Value} value
	* @param {Source[]} sources
	* @param {Set<Value>} marked
	* @param {Map<Reaction, boolean>} checked
	*/
	function mark_effects(value, sources, marked, checked) {
		if (marked.has(value)) return;
		marked.add(value);
		if (value.reactions !== null) for (const reaction of value.reactions) {
			const flags = reaction.f;
			if ((flags & 2) !== 0) mark_effects(reaction, sources, marked, checked);
			else if ((flags & 4194320) !== 0 && (flags & 2048) === 0 && depends_on(reaction, sources, checked)) {
				set_signal_status(reaction, DIRTY);
				schedule_effect(reaction);
			}
		}
	}
	/**
	* @param {Reaction} reaction
	* @param {Source[]} sources
	* @param {Map<Reaction, boolean>} checked
	*/
	function depends_on(reaction, sources, checked) {
		const depends = checked.get(reaction);
		if (depends !== void 0) return depends;
		if (reaction.deps !== null) for (const dep of reaction.deps) {
			if (includes.call(sources, dep)) return true;
			if ((dep.f & 2) !== 0 && depends_on(dep, sources, checked)) {
				checked.set(dep, true);
				return true;
			}
		}
		checked.set(reaction, false);
		return false;
	}
	/**
	* @param {Effect} effect
	* @returns {void}
	*/
	function schedule_effect(effect) {
		/** @type {Batch} */ current_batch.schedule(effect);
	}
	/**
	* Mark all the effects inside a skipped branch CLEAN, so that
	* they can be correctly rescheduled later. Tracks dirty and maybe_dirty
	* effects so they can be rescheduled if the branch survives.
	* @param {Effect} effect
	* @param {{ d: Effect[], m: Effect[] }} tracked
	*/
	function reset_branch(effect, tracked) {
		if ((effect.f & 32) !== 0 && (effect.f & 1024) !== 0) return;
		if ((effect.f & 2048) !== 0) tracked.d.push(effect);
		else if ((effect.f & 4096) !== 0) tracked.m.push(effect);
		set_signal_status(effect, CLEAN);
		var e = effect.first;
		while (e !== null) {
			reset_branch(e, tracked);
			e = e.next;
		}
	}
	/**
	* Mark an entire effect tree clean following an error
	* @param {Effect} effect
	*/
	function reset_all(effect) {
		set_signal_status(effect, CLEAN);
		var e = effect.first;
		while (e !== null) {
			reset_all(e);
			e = e.next;
		}
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/reactivity/sources.js
	/** @import { Derived, Effect, Source, Value } from '#client' */
	/** @type {Set<Effect>} */
	var eager_effects = /* @__PURE__ */ new Set();
	/** @type {Map<Source, any>} */
	var old_values = /* @__PURE__ */ new Map();
	var eager_effects_deferred = false;
	/**
	* @template V
	* @param {V} v
	* @param {Error | null} [stack]
	* @returns {Source<V>}
	*/
	function source(v, stack) {
		return {
			f: 0,
			v,
			reactions: null,
			equals,
			rv: 0,
			wv: 0
		};
	}
	/**
	* @template V
	* @param {V} v
	* @param {Error | null} [stack]
	*/
	/*#__NO_SIDE_EFFECTS__*/
	function state$1(v, stack) {
		const s = source(v, stack);
		push_reaction_value(s);
		return s;
	}
	/**
	* @template V
	* @param {V} initial_value
	* @param {boolean} [immutable]
	* @returns {Source<V>}
	*/
	/*#__NO_SIDE_EFFECTS__*/
	function mutable_source(initial_value, immutable = false, trackable = true) {
		const s = source(initial_value);
		if (!immutable) s.equals = safe_equals;
		if (legacy_mode_flag && trackable && component_context !== null && component_context.l !== null) (component_context.l.s ??= []).push(s);
		return s;
	}
	/**
	* @template V
	* @param {Source<V>} source
	* @param {V} value
	* @param {boolean} [should_proxy]
	* @returns {V}
	*/
	function set(source, value, should_proxy = false) {
		if (active_reaction !== null && (!untracking || (active_reaction.f & 131072) !== 0) && is_runes() && (active_reaction.f & 4325394) !== 0 && (current_sources === null || !current_sources.has(source))) state_unsafe_mutation();
		return internal_set(source, should_proxy ? proxy(value) : value, legacy_updates);
	}
	/**
	* A set of signals we have already seen while traversing in mark_reactions.
	* Not always set to balance the common case of sources only having a couple
	* of (transitive) dependencies (where always creating a Set would be bad for perf)
	* with the edge case of extremely deep or wide dependency arrays with cycles.
	* @type {Set<any> | null}
	*/
	var seen = null;
	/** Number of transitive dependencies, see {@link seen} for more info */
	var count_deps = 0;
	/**
	* @template V
	* @param {Source<V>} source
	* @param {V} value
	* @param {Effect[] | null} [updated_during_traversal]
	* @returns {V}
	*/
	function internal_set(source, value, updated_during_traversal = null) {
		if (!source.equals(value)) {
			if (is_destroying_effect) old_values.set(source, value);
			else if (!old_values.has(source)) old_values.set(source, source.v);
			var batch = Batch.ensure();
			batch.capture(source, value);
			if ((source.f & 2) !== 0) {
				const derived = source;
				if ((source.f & 2048) !== 0) execute_derived(derived);
				if (batch_values === null) update_derived_status(derived);
			}
			source.wv = increment_write_version();
			seen = null;
			count_deps = 0;
			mark_reactions(source, DIRTY, updated_during_traversal);
			seen = null;
			if (is_runes() && active_effect !== null && (active_effect.f & 1024) !== 0 && (active_effect.f & 96) === 0) {
				if (untracked_writes === null) set_untracked_writes([source]);
				else untracked_writes.push(source);
			}
			if (!batch.is_fork && eager_effects.size > 0 && !eager_effects_deferred) flush_eager_effects();
		}
		return value;
	}
	function flush_eager_effects() {
		eager_effects_deferred = false;
		for (const effect of eager_effects) {
			if ((effect.f & 1024) !== 0) set_signal_status(effect, MAYBE_DIRTY);
			let dirty;
			try {
				dirty = is_dirty(effect);
			} catch {
				dirty = true;
			}
			if (dirty) update_effect(effect);
		}
		eager_effects.clear();
	}
	/**
	* Silently (without using `get`) increment a source
	* @param {Source<number>} source
	*/
	function increment(source) {
		set(source, source.v + 1);
	}
	/**
	* @param {Value} signal
	* @param {number} status should be DIRTY or MAYBE_DIRTY
	* @param {Effect[] | null} updated_during_traversal
	* @returns {void}
	*/
	function mark_reactions(signal, status, updated_during_traversal) {
		var reactions = signal.reactions;
		if (reactions === null) return;
		var runes = is_runes();
		var length = reactions.length;
		count_deps += length;
		if (count_deps > 1e5 && seen === null) seen = /* @__PURE__ */ new Set();
		if (seen !== null) {
			if (seen.has(signal)) return;
			seen.add(signal);
		}
		for (var i = 0; i < length; i++) {
			var reaction = reactions[i];
			var flags = reaction.f;
			if (!runes && reaction === active_effect) continue;
			var not_dirty = (flags & DIRTY) === 0;
			if (not_dirty) set_signal_status(reaction, status);
			if ((flags & 131072) !== 0) eager_effects.add(reaction);
			else if ((flags & 2) !== 0) {
				var derived = reaction;
				batch_values?.delete(derived);
				mark_reactions(derived, MAYBE_DIRTY, updated_during_traversal);
			} else if (not_dirty) {
				var effect = reaction;
				if ((flags & 16) !== 0 && eager_block_effects !== null) eager_block_effects.add(effect);
				if (updated_during_traversal !== null) updated_during_traversal.push(effect);
				else schedule_effect(effect);
			}
		}
	}
	/**
	* @template T
	* @param {T} value
	* @returns {T}
	*/
	function proxy(value) {
		if (typeof value !== "object" || value === null || STATE_SYMBOL in value || COMPONENT_SYMBOL in value) return value;
		const prototype = get_prototype_of(value);
		if (prototype !== object_prototype && prototype !== array_prototype) return value;
		/** @type {Map<any, Source<any>>} */
		var sources = /* @__PURE__ */ new Map();
		var is_proxied_array = is_array(value);
		var version = /* @__PURE__ */ state$1(0);
		var stack = null;
		var parent_version = update_version;
		/**
		* Executes the proxy in the context of the reaction it was originally created in, if any
		* @template T
		* @param {() => T} fn
		*/
		var with_parent = (fn) => {
			if (update_version === parent_version) return fn();
			var reaction = active_reaction;
			var version = update_version;
			set_active_reaction(null);
			set_update_version(parent_version);
			var result = fn();
			set_active_reaction(reaction);
			set_update_version(version);
			return result;
		};
		if (is_proxied_array) sources.set("length", /* @__PURE__ */ state$1(
			/** @type {any[]} */
			value.length,
			stack
		));
		return new Proxy(value, {
			defineProperty(_, prop, descriptor) {
				if (!("value" in descriptor) || descriptor.configurable === false || descriptor.enumerable === false || descriptor.writable === false) state_descriptors_fixed();
				var s = sources.get(prop);
				if (s === void 0) with_parent(() => {
					var s = /* @__PURE__ */ state$1(descriptor.value, stack);
					sources.set(prop, s);
					return s;
				});
				else set(s, descriptor.value, true);
				return true;
			},
			deleteProperty(target, prop) {
				var s = sources.get(prop);
				if (s === void 0) {
					if (prop in target) {
						const s = with_parent(() => /* @__PURE__ */ state$1(UNINITIALIZED, stack));
						sources.set(prop, s);
						increment(version);
					}
				} else {
					set(s, UNINITIALIZED);
					increment(version);
				}
				return true;
			},
			get(target, prop, receiver) {
				if (prop === STATE_SYMBOL) return value;
				var s = sources.get(prop);
				var exists = prop in target;
				if (s === void 0 && (!exists || get_descriptor(target, prop)?.writable)) {
					s = with_parent(() => {
						return /* @__PURE__ */ state$1(proxy(exists ? target[prop] : UNINITIALIZED), stack);
					});
					sources.set(prop, s);
				}
				if (s !== void 0) {
					var v = get(s);
					return v === UNINITIALIZED ? void 0 : v;
				}
				return Reflect.get(target, prop, receiver);
			},
			getOwnPropertyDescriptor(target, prop) {
				this.has?.(target, prop);
				var descriptor = Reflect.getOwnPropertyDescriptor(target, prop);
				var s = sources.get(prop);
				if (s !== void 0) {
					var value = get(s);
					if (value === UNINITIALIZED) return;
					if (descriptor && "value" in descriptor) descriptor.value = value;
					else return {
						enumerable: true,
						configurable: true,
						value,
						writable: true
					};
				}
				return descriptor;
			},
			has(target, prop) {
				if (prop === STATE_SYMBOL) return true;
				var s = sources.get(prop);
				var has = s !== void 0 && s.v !== UNINITIALIZED || Reflect.has(target, prop);
				if (s !== void 0 || active_effect !== null && (!has || get_descriptor(target, prop)?.writable)) {
					if (s === void 0) {
						s = with_parent(() => {
							return /* @__PURE__ */ state$1(has ? proxy(target[prop]) : UNINITIALIZED, stack);
						});
						sources.set(prop, s);
					}
					if (get(s) === UNINITIALIZED) return false;
				}
				return has;
			},
			set(target, prop, value, receiver) {
				var s = sources.get(prop);
				var has = prop in target;
				if (is_proxied_array && prop === "length") for (var i = value; i < s.v; i += 1) {
					var other_s = sources.get(i + "");
					if (other_s !== void 0) set(other_s, UNINITIALIZED);
					else if (i in target) {
						other_s = with_parent(() => /* @__PURE__ */ state$1(UNINITIALIZED, stack));
						sources.set(i + "", other_s);
					}
				}
				if (s === void 0) {
					if (!has || get_descriptor(target, prop)?.writable) {
						s = with_parent(() => /* @__PURE__ */ state$1(void 0, stack));
						set(s, proxy(value));
						sources.set(prop, s);
					}
				} else {
					has = s.v !== UNINITIALIZED;
					var p = with_parent(() => proxy(value));
					set(s, p);
				}
				var descriptor = Reflect.getOwnPropertyDescriptor(target, prop);
				if (descriptor?.set) descriptor.set.call(receiver, value);
				if (!has) {
					if (is_proxied_array && typeof prop === "string") {
						var ls = sources.get("length");
						var n = Number(prop);
						if (Number.isInteger(n) && n >= ls.v) set(ls, n + 1);
					}
					increment(version);
				}
				return true;
			},
			ownKeys(target) {
				get(version);
				var own_keys = Reflect.ownKeys(target).filter((key) => {
					var source = sources.get(key);
					return source === void 0 || source.v !== UNINITIALIZED;
				});
				for (var [key, source] of sources) if (source.v !== UNINITIALIZED && !(key in target)) own_keys.push(key);
				return own_keys;
			},
			setPrototypeOf() {
				state_prototype_fixed();
			}
		});
	}
	/**
	* @param {any} value
	*/
	function get_proxied_value(value) {
		try {
			if (value !== null && typeof value === "object" && STATE_SYMBOL in value) return value[STATE_SYMBOL];
		} catch {}
		return value;
	}
	/**
	* @param {any} a
	* @param {any} b
	*/
	function is(a, b) {
		return Object.is(get_proxied_value(a), get_proxied_value(b));
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/operations.js
	/** @import { Effect, TemplateNode } from '#client' */
	/** @type {Window} */
	var $window;
	/** @type {boolean} */
	var is_firefox;
	/** @type {() => Node | null} */
	var first_child_getter;
	/** @type {() => Node | null} */
	var next_sibling_getter;
	/**
	* Initialize these lazily to avoid issues when using the runtime in a server context
	* where these globals are not available while avoiding a separate server entry point
	*/
	function init_operations() {
		if ($window !== void 0) return;
		$window = window;
		is_firefox = /Firefox/.test(navigator.userAgent);
		var element_prototype = Element.prototype;
		var node_prototype = Node.prototype;
		var text_prototype = Text.prototype;
		first_child_getter = get_descriptor(node_prototype, "firstChild").get;
		next_sibling_getter = get_descriptor(node_prototype, "nextSibling").get;
		if (is_extensible(element_prototype)) {
			/** @type {any} */ element_prototype[CLASS_CACHE] = void 0;
			/** @type {any} */ element_prototype[ATTRIBUTES_CACHE] = null;
			/** @type {any} */ element_prototype[STYLE_CACHE] = void 0;
			element_prototype.__e = void 0;
		}
		if (is_extensible(text_prototype))
 /** @type {any} */ text_prototype[TEXT_CACHE] = void 0;
	}
	/**
	* @param {string} value
	* @returns {Text}
	*/
	function create_text(value = "") {
		return document.createTextNode(value);
	}
	/**
	* @template {Node} N
	* @param {N} node
	*/
	/*@__NO_SIDE_EFFECTS__*/
	function get_first_child(node) {
		return first_child_getter.call(node);
	}
	/**
	* @template {Node} N
	* @param {N} node
	*/
	/*@__NO_SIDE_EFFECTS__*/
	function get_next_sibling(node) {
		return next_sibling_getter.call(node);
	}
	/**
	* Don't mark this as side-effect-free, hydration needs to walk all nodes
	* @template {Node} N
	* @param {N} node
	* @param {boolean} is_text
	* @returns {TemplateNode | null}
	*/
	function child(node, is_text) {
		if (!hydrating) return /* @__PURE__ */ get_first_child(node);
		var child = /* @__PURE__ */ get_first_child(hydrate_node);
		if (child === null) child = hydrate_node.appendChild(create_text());
		else if (is_text && child.nodeType !== 3) {
			var text = create_text();
			child?.before(text);
			set_hydrate_node(text);
			return text;
		}
		if (is_text) merge_text_nodes(child);
		set_hydrate_node(child);
		return child;
	}
	/**
	* Don't mark this as side-effect-free, hydration needs to walk all nodes
	* @param {TemplateNode} node
	* @param {boolean} [is_text]
	* @returns {TemplateNode | null}
	*/
	function first_child(node, is_text = false) {
		if (!hydrating) {
			var first = /* @__PURE__ */ get_first_child(node);
			if (first instanceof Comment && first.data === "") return /* @__PURE__ */ get_next_sibling(first);
			return first;
		}
		if (is_text) {
			if (hydrate_node?.nodeType !== 3) {
				var text = create_text();
				hydrate_node?.before(text);
				set_hydrate_node(text);
				return text;
			}
			merge_text_nodes(hydrate_node);
		}
		return hydrate_node;
	}
	/**
	* `child`, for the very common case of an element with exactly one child. Resetting the
	* hydration cursor is part of the same step, so the compiler doesn't have to emit a
	* separate `reset` call for every `<p>{text}</p>` in an app.
	* Don't mark this as side-effect-free, hydration needs to walk all nodes
	* @param {TemplateNode} node
	* @param {boolean} [is_text]
	* @returns {TemplateNode | null}
	*/
	function only_child(node, is_text = false) {
		if (!hydrating) return /* @__PURE__ */ get_first_child(node);
		var first = child(node, is_text);
		reset(node);
		return first;
	}
	/**
	* Don't mark this as side-effect-free, hydration needs to walk all nodes
	* @param {TemplateNode} node
	* @param {number} count
	* @param {boolean} is_text
	* @returns {TemplateNode | null}
	*/
	function sibling(node, count = 1, is_text = false) {
		let next_sibling = hydrating ? hydrate_node : node;
		var last_sibling;
		while (count--) {
			last_sibling = next_sibling;
			next_sibling = /* @__PURE__ */ get_next_sibling(next_sibling);
		}
		if (!hydrating) return next_sibling;
		if (is_text) {
			if (next_sibling?.nodeType !== 3) {
				var text = create_text();
				if (next_sibling === null) last_sibling?.after(text);
				else next_sibling.before(text);
				set_hydrate_node(text);
				return text;
			}
			merge_text_nodes(next_sibling);
		}
		set_hydrate_node(next_sibling);
		return next_sibling;
	}
	/**
	* @template {Node} N
	* @param {N} node
	* @returns {void}
	*/
	function clear_text_content(node) {
		node.textContent = "";
	}
	/**
	* Returns `true` if we're updating the current block, for example `condition` in
	* an `{#if condition}` block just changed. In this case, the branch should be
	* appended (or removed) at the same time as other updates within the
	* current `<svelte:boundary>`
	*/
	function should_defer_append() {
		if (!async_mode_flag) return false;
		if (eager_block_effects !== null) return false;
		return (active_effect.f & REACTION_RAN) !== 0;
	}
	/**
	* Branching here is intentional and load-bearing for perf. `createElement(tag)`
	* hits a fast path in Blink that `createElementNS(NAMESPACE_HTML, tag)` doesn't,
	* and passing an explicit `undefined` as the trailing options arg measurably
	* slows both APIs. Funnelling every case through a single `createElementNS(ns,
	* tag, options)` call would be smaller but slower on the HTML path.
	*
	* @template {keyof HTMLElementTagNameMap | string} T
	* @param {T} tag
	* @param {string} [namespace]
	* @param {string} [is]
	* @returns {T extends keyof HTMLElementTagNameMap ? HTMLElementTagNameMap[T] : Element}
	*/
	function create_element(tag, namespace, is) {
		if (namespace == null || namespace === "http://www.w3.org/1999/xhtml") return is ? document.createElement(tag, { is }) : document.createElement(tag);
		return is ? document.createElementNS(namespace, tag, { is }) : document.createElementNS(namespace, tag);
	}
	/**
	* Browsers split text nodes larger than 65536 bytes when parsing.
	* For hydration to succeed, we need to stitch them back together
	* @param {Text} text
	*/
	function merge_text_nodes(text) {
		if (text.nodeValue.length < 65536) return;
		let next = text.nextSibling;
		while (next !== null && next.nodeType === 3) {
			next.remove();
			/** @type {string} */ text.nodeValue += next.nodeValue;
			next = text.nextSibling;
		}
	}
	/**
	* @param {unknown} error
	*/
	function handle_error(error) {
		var effect = active_effect;
		if (effect === null) {
			/** @type {Derived} */ active_reaction.f |= ERROR_VALUE;
			return error;
		}
		if ((effect.f & 32768) === 0 && (effect.f & 4) === 0) throw error;
		invoke_error_boundary(error, effect);
	}
	/**
	* @param {unknown} error
	* @param {Effect | null} effect
	*/
	function invoke_error_boundary(error, effect) {
		if (effect !== null && (effect.f & 16384) !== 0) return;
		while (effect !== null) {
			if ((effect.f & 128) !== 0 && (effect.f & 33570816) === 0) {
				if ((effect.f & 32768) === 0) throw error;
				try {
					/** @type {Boundary} */ effect.b.error(error);
					return;
				} catch (e) {
					error = e;
				}
			}
			effect = effect.parent;
		}
		throw error;
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/reactivity/effects.js
	/** @import { Blocker, ComponentContext, ComponentContextLegacy, Derived, Effect, TemplateNode, TransitionManager } from '#client' */
	/**
	* @param {'$effect' | '$effect.pre' | '$inspect'} rune
	*/
	function validate_effect(rune) {
		if (active_effect === null) {
			if (active_reaction === null) effect_orphan(rune);
			effect_in_unowned_derived();
		}
		if (is_destroying_effect) effect_in_teardown(rune);
	}
	/**
	* @param {Effect} effect
	* @param {Effect} parent_effect
	*/
	function push_effect(effect, parent_effect) {
		var parent_last = parent_effect.last;
		if (parent_last === null) parent_effect.last = parent_effect.first = effect;
		else {
			parent_last.next = effect;
			effect.prev = parent_last;
			parent_effect.last = effect;
		}
	}
	/**
	* @param {number} type
	* @param {null | (() => void | (() => void))} fn
	* @returns {Effect}
	*/
	function create_effect(type, fn) {
		var parent = active_effect;
		if (parent !== null && (parent.f & 8192) !== 0) type |= INERT;
		/** @type {Effect} */
		var effect = {
			ctx: component_context,
			deps: null,
			nodes: null,
			f: type | DIRTY | 512,
			first: null,
			fn,
			last: null,
			next: null,
			parent,
			b: parent && parent.b,
			prev: null,
			teardown: null,
			wv: 0,
			ac: null
		};
		current_batch?.register_created_effect(effect);
		/** @type {Effect | null} */
		var e = effect;
		if ((type & 4) !== 0) {
			if (collected_effects !== null) collected_effects.push(effect);
			else Batch.ensure().schedule(effect);
		} else if (fn !== null) {
			try {
				update_effect(effect);
			} catch (e) {
				destroy_effect(effect);
				throw e;
			}
			if (e.deps === null && e.teardown === null && e.nodes === null && e.first === e.last && (e.f & 524288) === 0) {
				e = e.first;
				if ((type & 16) !== 0 && (type & 65536) !== 0 && e !== null) e.f |= EFFECT_TRANSPARENT;
			}
		}
		if (e !== null) {
			e.parent = parent;
			if (parent !== null) push_effect(e, parent);
			if (active_reaction !== null && (active_reaction.f & 2) !== 0 && (type & 64) === 0) {
				var derived = active_reaction;
				(derived.effects ??= []).push(e);
			}
		}
		return effect;
	}
	/**
	* Internal representation of `$effect.tracking()`
	* @returns {boolean}
	*/
	function effect_tracking() {
		return active_reaction !== null && !untracking;
	}
	/**
	* @param {() => void} fn
	*/
	function teardown(fn) {
		const effect = create_effect(8, null);
		set_signal_status(effect, CLEAN);
		effect.teardown = fn;
		return effect;
	}
	/**
	* Internal representation of `$effect(...)`
	* @param {() => void | (() => void)} fn
	*/
	function user_effect(fn) {
		validate_effect("$effect");
		var flags = active_effect.f;
		if (!active_reaction && (flags & 32) !== 0 && component_context !== null && !component_context.i) {
			var context = component_context;
			(context.e ??= []).push(fn);
		} else return create_user_effect(fn);
	}
	/**
	* @param {() => void | (() => void)} fn
	*/
	function create_user_effect(fn) {
		return create_effect(4 | USER_EFFECT, fn);
	}
	/**
	* An effect root whose children can transition out
	* @param {() => void} fn
	* @returns {(options?: { outro?: boolean }) => Promise<void>}
	*/
	function component_root(fn) {
		Batch.ensure();
		const effect = create_effect(64 | EFFECT_PRESERVED, fn);
		return (options = {}) => {
			return new Promise((fulfil) => {
				if (options.outro) pause_effect(effect, () => {
					destroy_effect(effect);
					fulfil(void 0);
				});
				else {
					destroy_effect(effect);
					fulfil(void 0);
				}
			});
		};
	}
	/**
	* @param {() => void | (() => void)} fn
	* @returns {Effect}
	*/
	function effect(fn) {
		return create_effect(4, fn);
	}
	/**
	* @param {() => void | (() => void)} fn
	* @returns {Effect}
	*/
	function async_effect(fn) {
		return create_effect(ASYNC | EFFECT_PRESERVED, fn);
	}
	/**
	* @param {() => void | (() => void)} fn
	* @returns {Effect}
	*/
	function render_effect(fn, flags = 0) {
		return create_effect(8 | flags, fn);
	}
	/**
	* @param {(...expressions: any) => void | (() => void)} fn
	* @param {Array<() => any>} sync
	* @param {Array<() => Promise<any>>} async
	* @param {Blocker[]} blockers
	*/
	function template_effect(fn, sync = [], async = [], blockers = []) {
		flatten(blockers, sync, async, (values) => {
			create_effect(8, () => {
				fn(...values.map(get));
			});
		});
	}
	/**
	* @param {(() => void)} fn
	* @param {number} flags
	*/
	function block(fn, flags = 0) {
		return create_effect(16 | flags, fn);
	}
	/**
	* @param {(() => void)} fn
	*/
	function branch(fn) {
		return create_effect(32 | EFFECT_PRESERVED, fn);
	}
	/**
	* @param {Effect} effect
	*/
	function execute_effect_teardown(effect) {
		var teardown = effect.teardown;
		if (teardown !== null) {
			const previously_destroying_effect = is_destroying_effect;
			const previous_reaction = active_reaction;
			set_is_destroying_effect(true);
			set_active_reaction(null);
			try {
				teardown.call(null);
			} catch (error) {
				invoke_error_boundary(error, effect.parent);
			} finally {
				set_is_destroying_effect(previously_destroying_effect);
				set_active_reaction(previous_reaction);
			}
		}
	}
	/**
	* @param {Effect} signal
	* @param {boolean} remove_dom
	* @returns {void}
	*/
	function destroy_effect_children(signal, remove_dom = false) {
		var effect = signal.first;
		signal.first = signal.last = null;
		while (effect !== null) {
			const controller = effect.ac;
			if (controller !== null) without_reactive_context(() => {
				controller.abort(STALE_REACTION);
			});
			var next = effect.next;
			if ((effect.f & 64) !== 0) effect.parent = null;
			else destroy_effect(effect, remove_dom);
			effect = next;
		}
	}
	/**
	* @param {Effect} signal
	* @returns {void}
	*/
	function destroy_block_effect_children(signal) {
		var effect = signal.first;
		while (effect !== null) {
			var next = effect.next;
			if ((effect.f & 32) === 0) destroy_effect(effect);
			effect = next;
		}
	}
	/**
	* @param {Effect} effect
	* @param {boolean} [remove_dom]
	* @returns {void}
	*/
	function destroy_effect(effect, remove_dom = true) {
		var removed = false;
		if ((remove_dom || (effect.f & 262144) !== 0) && effect.nodes !== null && effect.nodes.end !== null) {
			remove_effect_dom(effect.nodes.start, effect.nodes.end);
			removed = true;
		}
		effect.f |= DESTROYING;
		destroy_effect_children(effect, remove_dom && !removed);
		remove_reactions(effect, 0);
		var transitions = effect.nodes && effect.nodes.t;
		if (transitions !== null) for (const transition of transitions) transition.stop();
		execute_effect_teardown(effect);
		effect.f ^= DESTROYING;
		effect.f |= DESTROYED;
		var parent = effect.parent;
		if (parent !== null && parent.first !== null) unlink_effect(effect);
		effect.next = effect.prev = effect.teardown = effect.ctx = effect.deps = effect.fn = effect.nodes = effect.ac = effect.b = null;
	}
	/**
	*
	* @param {TemplateNode | null} node
	* @param {TemplateNode} end
	*/
	function remove_effect_dom(node, end) {
		while (node !== null) {
			/** @type {TemplateNode | null} */
			var next = node === end ? null : /* @__PURE__ */ get_next_sibling(node);
			node.remove();
			node = next;
		}
	}
	/**
	* Detach an effect from the effect tree, freeing up memory and
	* reducing the amount of work that happens on subsequent traversals
	* @param {Effect} effect
	*/
	function unlink_effect(effect) {
		var parent = effect.parent;
		var prev = effect.prev;
		var next = effect.next;
		if (prev !== null) prev.next = next;
		if (next !== null) next.prev = prev;
		if (parent !== null) {
			if (parent.first === effect) parent.first = next;
			if (parent.last === effect) parent.last = prev;
		}
	}
	/**
	* When a block effect is removed, we don't immediately destroy it or yank it
	* out of the DOM, because it might have transitions. Instead, we 'pause' it.
	* It stays around (in memory, and in the DOM) until outro transitions have
	* completed, and if the state change is reversed then we _resume_ it.
	* A paused effect does not update, and the DOM subtree becomes inert.
	* @param {Effect} effect
	* @param {() => void} [callback]
	* @param {boolean} [destroy]
	*/
	function pause_effect(effect, callback, destroy = true) {
		/** @type {TransitionManager[]} */
		var transitions = [];
		effect.f |= 256;
		pause_children(effect, transitions, true);
		var fn = () => {
			if (destroy) destroy_effect(effect);
			if (callback) callback();
		};
		var remaining = transitions.length;
		if (remaining > 0) {
			var check = () => --remaining || fn();
			for (var transition of transitions) transition.out(check);
		} else fn();
	}
	/**
	* @param {Effect} effect
	* @param {TransitionManager[]} transitions
	* @param {boolean} local
	*/
	function pause_children(effect, transitions, local) {
		if ((effect.f & 8192) !== 0) return;
		effect.f ^= INERT;
		var t = effect.nodes && effect.nodes.t;
		if (t !== null) {
			for (const transition of t) if (transition.is_global || local) transitions.push(transition);
		}
		var child = effect.first;
		while (child !== null) {
			var sibling = child.next;
			if ((child.f & 64) === 0) {
				var transparent = (child.f & 65536) !== 0 || (child.f & 32) !== 0 && (effect.f & 16) !== 0;
				pause_children(child, transitions, transparent ? local : false);
			}
			child = sibling;
		}
	}
	/**
	* The opposite of `pause_effect`. We call this if (for example)
	* `x` becomes falsy then truthy: `{#if x}...{/if}`
	* @param {Effect} effect
	*/
	function resume_effect(effect) {
		effect.f &= -257;
		resume_children(effect, true);
	}
	/**
	* @param {Effect} effect
	* @param {boolean} local
	*/
	function resume_children(effect, local) {
		if ((effect.f & 256) !== 0) return;
		if ((effect.f & 8192) === 0) return;
		effect.f ^= INERT;
		if ((effect.f & 1024) === 0) {
			set_signal_status(effect, DIRTY);
			Batch.ensure().schedule(effect);
		}
		var child = effect.first;
		while (child !== null) {
			var sibling = child.next;
			var transparent = (child.f & 65536) !== 0 || (child.f & 32) !== 0;
			resume_children(child, transparent ? local : false);
			child = sibling;
		}
		var t = effect.nodes && effect.nodes.t;
		if (t !== null) {
			for (const transition of t) if (transition.is_global || local) transition.in();
		}
	}
	/**
	* @param {Effect} effect
	* @param {DocumentFragment} fragment
	*/
	function move_effect(effect, fragment) {
		if (!effect.nodes) return;
		/** @type {TemplateNode | null} */
		var node = effect.nodes.start;
		var end = effect.nodes.end;
		while (node !== null) {
			/** @type {TemplateNode | null} */
			var next = node === end ? null : /* @__PURE__ */ get_next_sibling(node);
			fragment.append(node);
			node = next;
		}
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/legacy.js
	/**
	* @type {Set<Value> | null}
	* @deprecated
	*/
	var captured_signals = null;
	//#endregion
	//#region node_modules/svelte/src/internal/client/runtime.js
	/** @import { Derived, Effect, Reaction, Source, Value } from '#client' */
	/**
	* True if updating in an effect context that is reactive (i.e. not branch/root effects)
	*/
	var is_updating_effect = false;
	var is_destroying_effect = false;
	/** @param {boolean} value */
	function set_is_destroying_effect(value) {
		is_destroying_effect = value;
	}
	/** @type {null | Reaction} */
	var active_reaction = null;
	var untracking = false;
	/** @param {null | Reaction} reaction */
	function set_active_reaction(reaction) {
		active_reaction = reaction;
	}
	/** @type {null | Effect} */
	var active_effect = null;
	/** @param {null | Effect} effect */
	function set_active_effect(effect) {
		active_effect = effect;
	}
	/**
	* When sources are created within a reaction, reading and writing
	* them within that reaction should not cause a re-run
	* @type {null | Set<Source>}
	*/
	var current_sources = null;
	/** @param {Value} value */
	function push_reaction_value(value) {
		if (active_reaction !== null && (!async_mode_flag && (active_reaction.f & 2097152) !== 0 || (active_reaction.f & 2) !== 0)) (current_sources ??= /* @__PURE__ */ new Set()).add(value);
	}
	/**
	* The dependencies of the reaction that is currently being executed. In many cases,
	* the dependencies are unchanged between runs, and so this will be `null` unless
	* and until a new dependency is accessed — we track this via `skipped_deps`
	* @type {null | Value[]}
	*/
	var new_deps = null;
	var skipped_deps = 0;
	/**
	* Tracks writes that the effect it's executed in doesn't listen to yet,
	* so that the dependency can be added to the effect later on if it then reads it
	* @type {null | Source[]}
	*/
	var untracked_writes = null;
	/** @param {null | Source[]} value */
	function set_untracked_writes(value) {
		untracked_writes = value;
	}
	/**
	* @type {number} Used by sources and deriveds for handling updates.
	* Version starts from 1 so that unowned deriveds differentiate between a created effect and a run one for tracing
	**/
	var write_version = 1;
	/** @type {number} Used to version each read of a source of derived to avoid duplicating dependencies inside a reaction */
	var read_version = 0;
	var update_version = read_version;
	/** @param {number} value */
	function set_update_version(value) {
		update_version = value;
	}
	function increment_write_version() {
		return ++write_version;
	}
	/**
	* Determines whether a derived or effect is dirty.
	* If it is MAYBE_DIRTY, will set the status to CLEAN
	* @param {Reaction} reaction
	* @returns {boolean}
	*/
	function is_dirty(reaction) {
		var flags = reaction.f;
		if ((flags & 2048) !== 0) return true;
		if ((flags & 4096) !== 0) {
			var dependencies = reaction.deps;
			var length = dependencies.length;
			for (var i = 0; i < length; i++) {
				var dependency = dependencies[i];
				if (is_dirty(dependency)) update_derived(dependency);
				if (dependency.wv > reaction.wv) return true;
			}
			if ((flags & 512) !== 0 && batch_values === null) set_signal_status(reaction, CLEAN);
		}
		return false;
	}
	/**
	* @param {Value} signal
	* @param {Effect} effect
	* @param {boolean} [root]
	*/
	function schedule_possible_effect_self_invalidation(signal, effect, root = true) {
		var reactions = signal.reactions;
		if (reactions === null) return;
		if (!async_mode_flag && current_sources !== null && current_sources.has(signal)) return;
		for (var i = 0; i < reactions.length; i++) {
			var reaction = reactions[i];
			if ((reaction.f & 2) !== 0) schedule_possible_effect_self_invalidation(reaction, effect, false);
			else if (effect === reaction) {
				if (root) set_signal_status(reaction, DIRTY);
				else if ((reaction.f & 1024) !== 0) set_signal_status(reaction, MAYBE_DIRTY);
				schedule_effect(reaction);
			}
		}
	}
	/** @param {Reaction} reaction */
	function update_reaction(reaction) {
		var previous_deps = new_deps;
		var previous_skipped_deps = skipped_deps;
		var previous_untracked_writes = untracked_writes;
		var previous_reaction = active_reaction;
		var previous_sources = current_sources;
		var previous_component_context = component_context;
		var previous_untracking = untracking;
		var previous_update_version = update_version;
		var flags = reaction.f;
		new_deps = null;
		skipped_deps = 0;
		untracked_writes = null;
		active_reaction = (flags & 96) === 0 ? reaction : null;
		current_sources = null;
		set_component_context(reaction.ctx);
		untracking = false;
		update_version = ++read_version;
		if (reaction.ac !== null) {
			without_reactive_context(() => {
				/** @type {AbortController} */ reaction.ac.abort(STALE_REACTION);
			});
			reaction.ac = null;
		}
		try {
			reaction.f |= REACTION_IS_UPDATING;
			var fn = reaction.fn;
			var result = fn();
			reaction.f |= REACTION_RAN;
			var deps = update_dependencies(reaction);
			if (is_runes() && untracked_writes !== null && !untracking && deps !== null && (reaction.f & 6146) === 0) for (var i = 0; i < untracked_writes.length; i++) schedule_possible_effect_self_invalidation(untracked_writes[i], reaction);
			if (previous_reaction !== null && previous_reaction !== reaction) {
				read_version++;
				if (previous_reaction.deps !== null) for (let i = 0; i < previous_skipped_deps; i += 1) previous_reaction.deps[i].rv = read_version;
				if (previous_deps !== null) for (const dep of previous_deps) dep.rv = read_version;
				if (untracked_writes !== null) {
					if (previous_untracked_writes === null) previous_untracked_writes = untracked_writes;
					else previous_untracked_writes.push(...untracked_writes);
				}
			}
			if ((reaction.f & 8388608) !== 0) reaction.f ^= ERROR_VALUE;
			return result;
		} catch (error) {
			update_dependencies(reaction);
			return handle_error(error);
		} finally {
			reaction.f ^= REACTION_IS_UPDATING;
			new_deps = previous_deps;
			skipped_deps = previous_skipped_deps;
			untracked_writes = previous_untracked_writes;
			active_reaction = previous_reaction;
			current_sources = previous_sources;
			set_component_context(previous_component_context);
			untracking = previous_untracking;
			update_version = previous_update_version;
		}
	}
	/**
	* @param {Reaction} reaction
	*/
	function update_dependencies(reaction) {
		var deps = reaction.deps;
		var is_fork = current_batch?.is_fork;
		if (new_deps !== null) {
			var i;
			if (!is_fork) remove_reactions(reaction, skipped_deps);
			if (deps !== null && skipped_deps > 0) {
				deps.length = skipped_deps + new_deps.length;
				for (i = 0; i < new_deps.length; i++) deps[skipped_deps + i] = new_deps[i];
			} else reaction.deps = deps = new_deps;
			if (effect_tracking() && (reaction.f & 512) !== 0) for (i = skipped_deps; i < deps.length; i++) (deps[i].reactions ??= []).push(reaction);
		} else if (!is_fork && deps !== null && skipped_deps < deps.length) {
			remove_reactions(reaction, skipped_deps);
			deps.length = skipped_deps;
		}
		return deps;
	}
	/**
	* @template V
	* @param {Reaction} signal
	* @param {Value<V>} dependency
	* @returns {void}
	*/
	function remove_reaction(signal, dependency) {
		let reactions = dependency.reactions;
		if (reactions !== null) {
			var index = index_of.call(reactions, signal);
			if (index !== -1) {
				var new_length = reactions.length - 1;
				if (new_length === 0) reactions = dependency.reactions = null;
				else {
					reactions[index] = reactions[new_length];
					reactions.pop();
				}
			}
		}
		if (reactions === null && (dependency.f & 2) !== 0 && (new_deps === null || !includes.call(new_deps, dependency))) {
			var derived = dependency;
			if ((derived.f & 512) !== 0) derived.f ^= 512;
			if (derived.v !== UNINITIALIZED) update_derived_status(derived);
			if (derived.ac !== null) without_reactive_context(() => {
				/** @type {AbortController} */ derived.ac.abort(STALE_REACTION);
				derived.ac = null;
				set_signal_status(derived, DIRTY);
			});
			freeze_derived_effects(derived);
			remove_reactions(derived, 0);
		}
	}
	/**
	* @param {Reaction} signal
	* @param {number} start_index
	* @returns {void}
	*/
	function remove_reactions(signal, start_index) {
		var dependencies = signal.deps;
		if (dependencies === null) return;
		for (var i = start_index; i < dependencies.length; i++) remove_reaction(signal, dependencies[i]);
	}
	/**
	* @param {Effect} effect
	* @returns {void}
	*/
	function update_effect(effect) {
		var flags = effect.f;
		if ((flags & 16384) !== 0) return;
		set_signal_status(effect, CLEAN);
		var previous_effect = active_effect;
		var was_updating_effect = is_updating_effect;
		active_effect = effect;
		is_updating_effect = (flags & 96) === 0;
		try {
			if ((flags & 16777232) !== 0) destroy_block_effect_children(effect);
			else destroy_effect_children(effect);
			execute_effect_teardown(effect);
			var teardown = update_reaction(effect);
			effect.teardown = typeof teardown === "function" ? teardown : null;
			effect.wv = write_version;
		} finally {
			is_updating_effect = was_updating_effect;
			active_effect = previous_effect;
		}
	}
	/**
	* Returns a promise that resolves once any pending state changes have been applied.
	* @returns {Promise<void>}
	*/
	async function tick() {
		if (async_mode_flag) return new Promise((f) => {
			requestAnimationFrame(() => f());
			setTimeout(() => f());
		});
		await Promise.resolve();
		flushSync();
	}
	/**
	* @template V
	* @param {Value<V>} signal
	* @returns {V}
	*/
	function get(signal) {
		var is_derived = (signal.f & 2) !== 0;
		captured_signals?.add(signal);
		if (active_reaction !== null && !untracking) {
			if (!(active_effect !== null && (active_effect.f & 16384) !== 0) && (current_sources === null || !current_sources.has(signal))) {
				var deps = active_reaction.deps;
				if ((active_reaction.f & 2097152) !== 0) {
					if (signal.rv < read_version) {
						signal.rv = read_version;
						if (new_deps === null && deps !== null && deps[skipped_deps] === signal) skipped_deps++;
						else if (new_deps === null) new_deps = [signal];
						else new_deps.push(signal);
					}
				} else {
					active_reaction.deps ??= [];
					if (!includes.call(active_reaction.deps, signal)) active_reaction.deps.push(signal);
					var reactions = signal.reactions;
					if (reactions === null) signal.reactions = [active_reaction];
					else if (!includes.call(reactions, active_reaction)) reactions.push(active_reaction);
				}
			}
		}
		if (is_destroying_effect && old_values.has(signal)) return old_values.get(signal);
		if (is_derived) {
			var derived = signal;
			if (is_destroying_effect) {
				var value = derived.v;
				if ((derived.f & 1024) === 0 && derived.reactions !== null || depends_on_old_values(derived)) value = execute_derived(derived);
				old_values.set(derived, value);
				return value;
			}
			var should_connect = (derived.f & 512) === 0 && !untracking && active_reaction !== null && (is_updating_effect || (active_reaction.f & 512) !== 0);
			var is_new = (derived.f & REACTION_RAN) === 0;
			if (is_dirty(derived)) {
				if (should_connect) derived.f |= 512;
				update_derived(derived);
			}
			if (should_connect && !is_new) {
				unfreeze_derived_effects(derived);
				reconnect(derived);
			}
		}
		if (batch_values?.has(signal)) return batch_values.get(signal);
		if ((signal.f & 8388608) !== 0) throw signal.v;
		return signal.v;
	}
	/**
	* (Re)connect a disconnected derived, so that it is notified
	* of changes in `mark_reactions`
	* @param {Derived} derived
	*/
	function reconnect(derived) {
		derived.f |= 512;
		if (derived.deps === null) return;
		for (const dep of derived.deps) {
			(dep.reactions ??= []).push(derived);
			if ((dep.f & 2) !== 0 && (dep.f & 512) === 0) {
				unfreeze_derived_effects(dep);
				reconnect(dep);
			}
		}
	}
	/** @param {Derived} derived */
	function depends_on_old_values(derived) {
		if (derived.v === UNINITIALIZED) return true;
		if (derived.deps === null) return false;
		for (const dep of derived.deps) {
			if (old_values.has(dep)) return true;
			if ((dep.f & 2) !== 0 && depends_on_old_values(dep)) return true;
		}
		return false;
	}
	/**
	* When used inside a [`$derived`](https://svelte.dev/docs/svelte/$derived) or [`$effect`](https://svelte.dev/docs/svelte/$effect),
	* any state read inside `fn` will not be treated as a dependency.
	*
	* ```ts
	* $effect(() => {
	*   // this will run when `data` changes, but not when `time` changes
	*   save(data, {
	*     timestamp: untrack(() => time)
	*   });
	* });
	* ```
	* @template T
	* @param {() => T} fn
	* @returns {T}
	*/
	function untrack(fn) {
		var previous_untracking = untracking;
		try {
			untracking = true;
			return fn();
		} finally {
			untracking = previous_untracking;
		}
	}
	/**
	* Possibly traverse an object and read all its properties so that they're all reactive in case this is `$state`.
	* Does only check first level of an object for performance reasons (heuristic should be good for 99% of all cases).
	* @param {any} value
	* @returns {void}
	*/
	function deep_read_state(value) {
		if (typeof value !== "object" || !value || value instanceof EventTarget) return;
		if (STATE_SYMBOL in value) deep_read(value);
		else if (!Array.isArray(value)) for (let key in value) {
			const prop = value[key];
			if (typeof prop === "object" && prop && STATE_SYMBOL in prop) deep_read(prop);
		}
	}
	/**
	* Deeply traverse an object and read all its properties
	* so that they're all reactive in case this is `$state`
	* @param {any} value
	* @param {Set<any>} visited
	* @returns {void}
	*/
	function deep_read(value, visited = /* @__PURE__ */ new Set()) {
		if (typeof value === "object" && value !== null && !(value instanceof EventTarget) && !visited.has(value)) {
			visited.add(value);
			if (value instanceof Date) value.getTime();
			for (let key in value) try {
				deep_read(value[key], visited);
			} catch (e) {}
			const proto = get_prototype_of(value);
			if (proto !== Object.prototype && proto !== Array.prototype && proto !== Map.prototype && proto !== Set.prototype && proto !== Date.prototype) {
				const descriptors = get_descriptors(proto);
				for (let key in descriptors) {
					const get = descriptors[key].get;
					if (get) try {
						get.call(value);
					} catch (e) {}
				}
			}
		}
	}
	/**
	* Subset of delegated events which should be passive by default.
	* These two are already passive via browser defaults on window, document and body.
	* But since
	* - we're delegating them
	* - they happen often
	* - they apply to mobile which is generally less performant
	* we're marking them as passive by default for other elements, too.
	*/
	var PASSIVE_EVENTS = ["touchstart", "touchmove"];
	/**
	* Returns `true` if `name` is a passive event
	* @param {string} name
	*/
	function is_passive_event(name) {
		return PASSIVE_EVENTS.includes(name);
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/elements/events.js
	/**
	* Used on elements, as a map of event type -> event handler,
	* and on events themselves to track which element handled an event
	*/
	var event_symbol = Symbol("events");
	/** @type {Set<string>} */
	var all_registered_events = /* @__PURE__ */ new Set();
	/** @type {Set<(events: Array<string>) => void>} */
	var root_event_handles = /* @__PURE__ */ new Set();
	/**
	* SSR adds onload and onerror attributes to catch those events before the hydration.
	* This function detects those cases, removes the attributes and replays the events.
	* @param {HTMLElement} dom
	*/
	function replay_events(dom) {
		if (!hydrating) return;
		dom.removeAttribute("onload");
		dom.removeAttribute("onerror");
		const event = dom.__e;
		if (event !== void 0) {
			dom.__e = void 0;
			queueMicrotask(() => {
				if (dom.isConnected) dom.dispatchEvent(event);
			});
		}
	}
	/**
	* @param {string} event_name
	* @param {EventTarget} dom
	* @param {EventListener} [handler]
	* @param {AddEventListenerOptions} [options]
	*/
	function create_event(event_name, dom, handler, options = {}) {
		/**
		* @this {EventTarget}
		*/
		function target_handler(event) {
			if (!options.capture) handle_event_propagation.call(dom, event);
			if (!event.cancelBubble) return without_reactive_context(() => {
				return handler?.call(this, event);
			});
		}
		if (event_name.startsWith("pointer") || event_name.startsWith("touch") || event_name === "wheel") {
			target_handler.__removed = false;
			queue_micro_task(() => {
				if (!target_handler.__removed) dom.addEventListener(event_name, target_handler, options);
			});
		} else dom.addEventListener(event_name, target_handler, options);
		return target_handler;
	}
	/**
	* @param {string} event_name
	* @param {Element} dom
	* @param {EventListener} [handler]
	* @param {boolean} [capture]
	* @param {boolean} [passive]
	* @returns {void}
	*/
	function event(event_name, dom, handler, capture, passive) {
		var options = {
			capture,
			passive
		};
		var target_handler = create_event(event_name, dom, handler, options);
		if (dom === document.body || dom === window || dom === document || dom instanceof HTMLMediaElement) teardown(() => {
			target_handler.__removed = true;
			dom.removeEventListener(event_name, target_handler, options);
		});
	}
	/**
	* @param {string} event_name
	* @param {Element} element
	* @param {EventListener} [handler]
	* @returns {void}
	*/
	function delegated(event_name, element, handler) {
		(element[event_symbol] ??= {})[event_name] = handler;
	}
	/**
	* @param {Array<string>} events
	* @returns {void}
	*/
	function delegate(events) {
		for (var i = 0; i < events.length; i++) all_registered_events.add(events[i]);
		for (var fn of root_event_handles) fn(events);
	}
	var last_propagated_event = null;
	var last_propagated_event_clear_scheduled = false;
	/**
	* @this {EventTarget}
	* @param {Event} event
	* @returns {void}
	*/
	function handle_event_propagation(event) {
		var handler_element = this;
		var owner_document = handler_element.ownerDocument;
		var event_name = event.type;
		var path = event.composedPath?.() || [];
		var current_target = path[0] || event.target;
		last_propagated_event = event;
		if (!last_propagated_event_clear_scheduled) {
			last_propagated_event_clear_scheduled = true;
			setTimeout(() => {
				last_propagated_event_clear_scheduled = false;
				last_propagated_event = null;
			});
		}
		var path_idx = 0;
		var handled_at = last_propagated_event === event && event[event_symbol];
		if (handled_at) {
			var at_idx = path.indexOf(handled_at);
			if (at_idx !== -1 && (handler_element === document || handler_element === window)) {
				event[event_symbol] = handler_element;
				return;
			}
			var handler_idx = path.indexOf(handler_element);
			if (handler_idx === -1) return;
			if (at_idx <= handler_idx) path_idx = at_idx;
		}
		current_target = path[path_idx] || event.target;
		if (current_target === handler_element) return;
		define_property(event, "currentTarget", {
			configurable: true,
			get() {
				return current_target || owner_document;
			}
		});
		var previous_reaction = active_reaction;
		var previous_effect = active_effect;
		set_active_reaction(null);
		set_active_effect(null);
		try {
			/**
			* @type {unknown}
			*/
			var throw_error;
			/**
			* @type {unknown[]}
			*/
			var other_errors = [];
			while (current_target !== null) {
				if (current_target === handler_element) break;
				try {
					var delegated = current_target[event_symbol]?.[event_name];
					if (delegated != null && (!current_target.disabled || event.target === current_target)) delegated.call(current_target, event);
				} catch (error) {
					if (throw_error) other_errors.push(error);
					else throw_error = error;
				}
				if (event.cancelBubble) break;
				path_idx++;
				current_target = path_idx < path.length ? path[path_idx] : null;
			}
			if (throw_error) {
				for (let error of other_errors) queueMicrotask(() => {
					throw error;
				});
				throw throw_error;
			}
		} finally {
			event[event_symbol] = handler_element;
			delete event.currentTarget;
			set_active_reaction(previous_reaction);
			set_active_effect(previous_effect);
		}
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/reconciler.js
	var policy = globalThis?.window?.trustedTypes && /* @__PURE__ */ globalThis.window.trustedTypes.createPolicy("svelte-trusted-html", { 
	/** @param {string} html */
createHTML: (html) => {
		return html;
	} });
	/** @param {string} html */
	function create_trusted_html(html) {
		return policy?.createHTML(html) ?? html;
	}
	/**
	* @param {string} html
	*/
	function create_fragment_from_html(html) {
		var elem = create_element("template");
		elem.innerHTML = create_trusted_html(html.replaceAll("<!>", "<!---->"));
		return elem.content;
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/template.js
	/** @import { Effect, EffectNodes, TemplateNode } from '#client' */
	/** @import { TemplateStructure } from './types' */
	/**
	* @param {TemplateNode} start
	* @param {TemplateNode | null} end
	*/
	function assign_nodes(start, end) {
		var effect = active_effect;
		if (effect.nodes === null) effect.nodes = {
			start,
			end,
			a: null,
			t: null
		};
	}
	/**
	* @param {string} content
	* @param {number} flags
	* @returns {() => Node | Node[]}
	*/
	/*#__NO_SIDE_EFFECTS__*/
	function from_html(content, flags) {
		var is_fragment = (flags & 1) !== 0;
		var use_import_node = (flags & 2) !== 0;
		/** @type {Node} */
		var node;
		/**
		* Whether or not the first item is a text/element node. If not, we need to
		* create an additional comment node to act as `effect.nodes.start`
		*/
		var has_start = !content.startsWith("<!>");
		return () => {
			if (hydrating) {
				assign_nodes(hydrate_node, null);
				return hydrate_node;
			}
			if (node === void 0) {
				node = create_fragment_from_html(has_start ? content : "<!>" + content);
				if (!is_fragment) node = /* @__PURE__ */ get_first_child(node);
			}
			var clone = use_import_node || is_firefox ? document.importNode(node, true) : node.cloneNode(true);
			if (is_fragment) {
				var start = /* @__PURE__ */ get_first_child(clone);
				var end = clone.lastChild;
				assign_nodes(start, end);
			} else assign_nodes(clone, clone);
			return clone;
		};
	}
	/**
	* @param {string} content
	* @param {number} flags
	* @param {'svg' | 'math'} ns
	* @returns {() => Node | Node[]}
	*/
	/*#__NO_SIDE_EFFECTS__*/
	function from_namespace(content, flags, ns = "svg") {
		/**
		* Whether or not the first item is a text/element node. If not, we need to
		* create an additional comment node to act as `effect.nodes.start`
		*/
		var has_start = !content.startsWith("<!>");
		var is_fragment = (flags & 1) !== 0;
		var wrapped = `<${ns}>${has_start ? content : "<!>" + content}</${ns}>`;
		/** @type {Element | DocumentFragment} */
		var node;
		return () => {
			if (hydrating) {
				assign_nodes(hydrate_node, null);
				return hydrate_node;
			}
			if (!node) {
				var root = /* @__PURE__ */ get_first_child(create_fragment_from_html(wrapped));
				if (is_fragment) {
					node = document.createDocumentFragment();
					while (/* @__PURE__ */ get_first_child(root)) node.appendChild(/* @__PURE__ */ get_first_child(root));
				} else node = /* @__PURE__ */ get_first_child(root);
			}
			var clone = node.cloneNode(true);
			if (is_fragment) {
				var start = /* @__PURE__ */ get_first_child(clone);
				var end = clone.lastChild;
				assign_nodes(start, end);
			} else assign_nodes(clone, clone);
			return clone;
		};
	}
	/**
	* @param {string} content
	* @param {number} flags
	*/
	/*#__NO_SIDE_EFFECTS__*/
	function from_svg(content, flags) {
		return /* @__PURE__ */ from_namespace(content, flags, "svg");
	}
	/**
	* @returns {TemplateNode | DocumentFragment}
	*/
	function comment() {
		if (hydrating) {
			assign_nodes(hydrate_node, null);
			return hydrate_node;
		}
		var frag = document.createDocumentFragment();
		var start = document.createComment("");
		var anchor = create_text();
		frag.append(start, anchor);
		assign_nodes(start, anchor);
		return frag;
	}
	/**
	* Assign the created (or in hydration mode, traversed) dom elements to the current block
	* and insert the elements into the dom (in client mode).
	* @param {Text | Comment | Element} anchor
	* @param {DocumentFragment | Element} dom
	*/
	function append(anchor, dom) {
		if (hydrating) {
			var effect = active_effect;
			if ((effect.f & 32768) === 0 || effect.nodes.end === null) effect.nodes.end = hydrate_node;
			hydrate_next();
			return;
		}
		if (anchor === null) return;
		anchor.before(dom);
	}
	//#endregion
	//#region node_modules/svelte/src/reactivity/create-subscriber.js
	/**
	* Returns a `subscribe` function that integrates external event-based systems with Svelte's reactivity.
	* It's particularly useful for integrating with web APIs like `MediaQuery`, `IntersectionObserver`, or `WebSocket`.
	*
	* If `subscribe` is called inside an effect (including indirectly, for example inside a getter),
	* the `start` callback will be called with an `update` function. Whenever `update` is called, the effect re-runs.
	*
	* If `start` returns a cleanup function, it will be called when the effect is destroyed.
	*
	* If `subscribe` is called in multiple effects, `start` will only be called once as long as the effects
	* are active, and the returned teardown function will only be called when all effects are destroyed.
	*
	* It's best understood with an example. Here's an implementation of [`MediaQuery`](https://svelte.dev/docs/svelte/svelte-reactivity#MediaQuery):
	*
	* ```js
	* import { createSubscriber } from 'svelte/reactivity';
	* import { on } from 'svelte/events';
	*
	* export class MediaQuery {
	* 	#query;
	* 	#subscribe;
	*
	* 	constructor(query) {
	* 		this.#query = window.matchMedia(`(${query})`);
	*
	* 		this.#subscribe = createSubscriber((update) => {
	* 			// when the `change` event occurs, re-run any effects that read `this.current`
	* 			const off = on(this.#query, 'change', update);
	*
	* 			// stop listening when all the effects are destroyed
	* 			return () => off();
	* 		});
	* 	}
	*
	* 	get current() {
	* 		// This makes the getter reactive, if read in an effect
	* 		this.#subscribe();
	*
	* 		// Return the current state of the query, whether or not we're in an effect
	* 		return this.#query.matches;
	* 	}
	* }
	* ```
	* @param {(update: () => void) => (() => void) | void} start
	* @since 5.7.0
	*/
	function createSubscriber(start) {
		let subscribers = 0;
		let version = source(0);
		/** @type {(() => void) | void} */
		let stop;
		return () => {
			if (effect_tracking()) {
				get(version);
				render_effect(() => {
					if (subscribers === 0) stop = untrack(() => start(() => increment(version)));
					subscribers += 1;
					return () => {
						queue_micro_task(() => {
							subscribers -= 1;
							if (subscribers === 0) {
								stop?.();
								stop = void 0;
								increment(version);
							}
						});
					};
				});
			}
		};
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/blocks/boundary.js
	/** @import { Effect, Source, TemplateNode, } from '#client' */
	/**
	* @typedef {{
	* 	 onerror?: ((error: unknown, reset: () => void) => void) | null;
	*   failed?: ((anchor: Node, error: () => unknown, reset: () => () => void) => void) | null;
	*   pending?: ((anchor: Node) => void) | null;
	* }} BoundaryProps
	*/
	var flags = EFFECT_TRANSPARENT | EFFECT_PRESERVED;
	/**
	* @param {TemplateNode} node
	* @param {BoundaryProps} props
	* @param {((anchor: Node) => void)} children
	* @param {((error: unknown) => unknown) | undefined} [transform_error]
	* @returns {void}
	*/
	function boundary(node, props, children, transform_error) {
		new Boundary(node, props, children, transform_error);
	}
	var Boundary = class {
		/** @type {Boundary | null} */
		parent;
		is_pending = false;
		/**
		* API-level transformError transform function. Transforms errors before they reach the `failed` snippet.
		* Inherited from parent boundary, or defaults to identity.
		* @type {(error: unknown) => unknown}
		*/
		transform_error;
		/** @type {TemplateNode} */
		#anchor;
		/** @type {TemplateNode | null} */
		#hydrate_open = hydrating ? hydrate_node : null;
		/** @type {BoundaryProps} */
		#props;
		/** @type {((anchor: Node) => void)} */
		#children;
		/** @type {Effect} */
		#effect;
		/** @type {Effect | null} */
		#main_effect = null;
		/** @type {Effect | null} */
		#pending_effect = null;
		/** @type {Effect | null} */
		#failed_effect = null;
		/** @type {DocumentFragment | null} */
		#offscreen_fragment = null;
		#local_pending_count = 0;
		#pending_count = 0;
		#pending_count_update_queued = false;
		/** @type {Set<Effect>} */
		#dirty_effects = /* @__PURE__ */ new Set();
		/** @type {Set<Effect>} */
		#maybe_dirty_effects = /* @__PURE__ */ new Set();
		/**
		* A source containing the number of pending async deriveds/expressions.
		* Only created if `$effect.pending()` is used inside the boundary,
		* otherwise updating the source results in needless `Batch.ensure()`
		* calls followed by no-op flushes
		* @type {Source<number> | null}
		*/
		#effect_pending = null;
		#effect_pending_subscriber = createSubscriber(() => {
			this.#effect_pending = source(this.#local_pending_count);
			return () => {
				this.#effect_pending = null;
			};
		});
		/**
		* @param {TemplateNode} node
		* @param {BoundaryProps} props
		* @param {((anchor: Node) => void)} children
		* @param {((error: unknown) => unknown) | undefined} [transform_error]
		*/
		constructor(node, props, children, transform_error) {
			this.#anchor = node;
			this.#props = props;
			this.#children = (anchor) => {
				var effect = active_effect;
				effect.b = this;
				effect.f |= 128;
				children(anchor);
			};
			this.parent = active_effect.b;
			this.transform_error = transform_error ?? this.parent?.transform_error ?? ((e) => e);
			this.#effect = block(() => {
				if (hydrating) {
					const comment = this.#hydrate_open;
					hydrate_next();
					const server_rendered_pending = comment.data === "[!";
					if (comment.data.startsWith("[?")) {
						const serialized_error = JSON.parse(comment.data.slice(2));
						this.#hydrate_failed_content(serialized_error);
					} else if (server_rendered_pending) this.#hydrate_pending_content();
					else this.#hydrate_resolved_content();
				} else this.#render();
			}, flags);
			if (hydrating) this.#anchor = hydrate_node;
		}
		#hydrate_resolved_content() {
			try {
				this.#main_effect = branch(() => this.#children(this.#anchor));
			} catch (error) {
				this.error(error);
			}
		}
		/**
		* @param {unknown} error The deserialized error from the server's hydration comment
		*/
		#hydrate_failed_content(error) {
			const failed = this.#props.failed;
			const { reset, invoke_onerror } = this.#create_reset(error);
			queue_micro_task(invoke_onerror);
			if (!failed) return;
			this.#failed_effect = branch(() => {
				failed(this.#anchor, () => error, () => reset);
			});
		}
		/**
		* Creates the `reset` function for a failed boundary, along with a function
		* that invokes `onerror` with it (if provided)
		* @param {unknown} error
		* @returns {{ reset: () => void, invoke_onerror: () => void }}
		*/
		#create_reset(error) {
			var did_reset = false;
			var calling_on_error = false;
			const reset = () => {
				if (did_reset) {
					svelte_boundary_reset_noop();
					return;
				}
				did_reset = true;
				if (calling_on_error) svelte_boundary_reset_onerror();
				if (this.#failed_effect !== null) pause_effect(this.#failed_effect, () => {
					this.#failed_effect = null;
				});
				this.#run(() => {
					this.#render();
				});
			};
			const invoke_onerror = () => {
				try {
					calling_on_error = true;
					this.#props.onerror?.(error, reset);
					calling_on_error = false;
				} catch (err) {
					invoke_error_boundary(err, this.#effect && this.#effect.parent);
				}
			};
			return {
				reset,
				invoke_onerror
			};
		}
		#hydrate_pending_content() {
			const pending = this.#props.pending;
			if (!pending) return;
			this.is_pending = true;
			this.#pending_effect = branch(() => pending(this.#anchor));
			queue_micro_task(() => {
				var fragment = this.#offscreen_fragment = document.createDocumentFragment();
				var anchor = create_text();
				var handled = false;
				fragment.append(anchor);
				this.#main_effect = this.#run(() => {
					try {
						return branch(() => this.#children(anchor));
					} catch (error) {
						try {
							this.error(error);
							handled = true;
						} catch (error) {
							invoke_error_boundary(error, this.#effect.parent);
						}
						return null;
					}
				});
				if (this.#main_effect === null) {
					this.#offscreen_fragment = null;
					if (handled) this.#resolve(current_batch);
					return;
				}
				if (this.#pending_count === 0) {
					this.#anchor.before(fragment);
					this.#offscreen_fragment = null;
					pause_effect(this.#pending_effect, () => {
						this.#pending_effect = null;
					});
					this.#resolve(current_batch);
				}
			});
		}
		#render() {
			try {
				this.is_pending = this.has_pending_snippet();
				this.#pending_count = 0;
				this.#local_pending_count = 0;
				this.#main_effect = branch(() => {
					this.#children(this.#anchor);
				});
				if (this.#pending_count > 0) {
					var fragment = this.#offscreen_fragment = document.createDocumentFragment();
					move_effect(this.#main_effect, fragment);
					const pending = this.#props.pending;
					this.#pending_effect = branch(() => pending(this.#anchor));
				} else this.#resolve(current_batch);
			} catch (error) {
				this.error(error);
			}
		}
		/**
		* @param {Batch} batch
		*/
		#resolve(batch) {
			this.is_pending = false;
			batch.transfer_effects(this.#dirty_effects, this.#maybe_dirty_effects);
		}
		/**
		* Defer an effect inside a pending boundary until the boundary resolves
		* @param {Effect} effect
		*/
		defer_effect(effect) {
			defer_effect(effect, this.#dirty_effects, this.#maybe_dirty_effects);
		}
		/**
		* Returns `false` if the effect exists inside a boundary whose pending snippet is shown
		* @returns {boolean}
		*/
		is_rendered() {
			return !this.is_pending && (!this.parent || this.parent.is_rendered());
		}
		has_pending_snippet() {
			return !!this.#props.pending;
		}
		/**
		* @template T
		* @param {() => T} fn
		*/
		#run(fn) {
			var previous_effect = active_effect;
			var previous_reaction = active_reaction;
			var previous_ctx = component_context;
			set_active_effect(this.#effect);
			set_active_reaction(this.#effect);
			set_component_context(this.#effect.ctx);
			try {
				Batch.ensure();
				return fn();
			} finally {
				set_active_effect(previous_effect);
				set_active_reaction(previous_reaction);
				set_component_context(previous_ctx);
			}
		}
		/**
		* Updates the pending count associated with the currently visible pending snippet,
		* if any, such that we can replace the snippet with content once work is done
		* @param {1 | -1} d
		* @param {Batch} batch
		*/
		#update_pending_count(d, batch) {
			if (!this.has_pending_snippet()) {
				if (this.parent) this.parent.#update_pending_count(d, batch);
				return;
			}
			this.#pending_count += d;
			if (this.#pending_count === 0) {
				this.#resolve(batch);
				if (this.#pending_effect) pause_effect(this.#pending_effect, () => {
					this.#pending_effect = null;
				});
				if (this.#offscreen_fragment) {
					this.#anchor.before(this.#offscreen_fragment);
					this.#offscreen_fragment = null;
				}
			}
		}
		/**
		* Update the source that powers `$effect.pending()` inside this boundary,
		* and controls when the current `pending` snippet (if any) is removed.
		* Do not call from inside the class
		* @param {1 | -1} d
		* @param {Batch} batch
		*/
		update_pending_count(d, batch) {
			this.#update_pending_count(d, batch);
			this.#local_pending_count += d;
			if (!this.#effect_pending || this.#pending_count_update_queued) return;
			this.#pending_count_update_queued = true;
			queue_micro_task(() => {
				this.#pending_count_update_queued = false;
				if (this.#effect_pending) internal_set(this.#effect_pending, this.#local_pending_count);
			});
		}
		get_effect_pending() {
			this.#effect_pending_subscriber();
			return get(this.#effect_pending);
		}
		/** @param {unknown} error */
		error(error) {
			if (!this.#props.onerror && !this.#props.failed) throw error;
			if (current_batch?.is_fork) {
				if (this.#main_effect) current_batch.skip_effect(this.#main_effect);
				if (this.#pending_effect) current_batch.skip_effect(this.#pending_effect);
				if (this.#failed_effect) current_batch.skip_effect(this.#failed_effect);
				current_batch.oncommit(() => {
					this.#handle_error(error);
				});
			} else this.#handle_error(error);
		}
		/**
		* @param {unknown} error
		*/
		#handle_error(error) {
			if (this.#main_effect) {
				destroy_effect(this.#main_effect);
				this.#main_effect = null;
			}
			if (this.#pending_effect) {
				destroy_effect(this.#pending_effect);
				this.#pending_effect = null;
			}
			if (this.#failed_effect) {
				destroy_effect(this.#failed_effect);
				this.#failed_effect = null;
			}
			if (hydrating) {
				set_hydrate_node(this.#hydrate_open);
				next();
				set_hydrate_node(skip_nodes());
			}
			let failed = this.#props.failed;
			/** @param {unknown} transformed_error */
			const handle_error_result = (transformed_error) => {
				const { reset, invoke_onerror } = this.#create_reset(transformed_error);
				invoke_onerror();
				if (failed) this.#failed_effect = this.#run(() => {
					try {
						return branch(() => {
							var effect = active_effect;
							effect.b = this;
							effect.f |= 128;
							failed(this.#anchor, () => transformed_error, () => reset);
						});
					} catch (error) {
						invoke_error_boundary(error, this.#effect.parent);
						return null;
					}
				});
			};
			queue_micro_task(() => {
				/** @type {unknown} */
				var result;
				try {
					result = this.transform_error(error);
				} catch (e) {
					invoke_error_boundary(e, this.#effect && this.#effect.parent);
					return;
				}
				if (result !== null && typeof result === "object" && typeof result.then === "function")
 /** @type {any} */ result.then(
					handle_error_result,
					/** @param {unknown} e */
					(e) => invoke_error_boundary(e, this.#effect && this.#effect.parent)
				);
				else handle_error_result(result);
			});
		}
	};
	/**
	* @param {Element} text
	* @param {string} value
	* @returns {void}
	*/
	function set_text(text, value) {
		var str = value == null ? "" : typeof value === "object" ? `${value}` : value;
		if (str !== (text[TEXT_CACHE] ??= text.nodeValue)) {
			/** @type {any} */ text[TEXT_CACHE] = str;
			text.nodeValue = `${str}`;
		}
	}
	/**
	* Mounts a component to the given target and returns the exports and potentially the props (if compiled with `accessors: true`) of the component.
	* Transitions will play during the initial render unless the `intro` option is set to `false`.
	*
	* @template {Record<string, any>} Props
	* @template {Record<string, any>} Exports
	* @param {ComponentType<SvelteComponent<Props>> | Component<Props, Exports, any>} component
	* @param {MountOptions<Props>} options
	* @returns {Exports}
	*/
	function mount(component, options) {
		return _mount(component, options);
	}
	/** @type {Map<EventTarget, Map<string, number>>} */
	var listeners = /* @__PURE__ */ new Map();
	/**
	* @template {Record<string, any>} Exports
	* @param {ComponentType<SvelteComponent<any>> | Component<any>} Component
	* @param {MountOptions} options
	* @returns {Exports}
	*/
	function _mount(Component, { target, anchor, props = {}, events, context, intro = true, transformError }) {
		init_operations();
		/** @type {Exports} */
		var component = void 0;
		var unmount = component_root(() => {
			var anchor_node = anchor ?? target.appendChild(create_text());
			boundary(anchor_node, { pending: () => {} }, (anchor_node) => {
				push({});
				var ctx = component_context;
				if (context) ctx.c = context;
				if (events)
 /** @type {any} */ props.$$events = events;
				if (hydrating) assign_nodes(anchor_node, null);
				component = Component(anchor_node, props) || mark_as_component();
				if (hydrating) {
					/** @type {Effect & { nodes: EffectNodes }} */ active_effect.nodes.end = hydrate_node;
					if (hydrate_node === null || hydrate_node.nodeType !== 8 || hydrate_node.data !== "]") {
						hydration_mismatch();
						throw HYDRATION_ERROR;
					}
				}
				pop();
			}, transformError);
			/** @type {Set<string>} */
			var registered_events = /* @__PURE__ */ new Set();
			/** @param {Array<string>} events */
			var event_handle = (events) => {
				for (var i = 0; i < events.length; i++) {
					var event_name = events[i];
					if (registered_events.has(event_name)) continue;
					registered_events.add(event_name);
					var passive = is_passive_event(event_name);
					for (const node of [target, document]) {
						var counts = listeners.get(node);
						if (counts === void 0) {
							counts = /* @__PURE__ */ new Map();
							listeners.set(node, counts);
						}
						var count = counts.get(event_name);
						if (count === void 0) {
							node.addEventListener(event_name, handle_event_propagation, { passive });
							counts.set(event_name, 1);
						} else counts.set(event_name, count + 1);
					}
				}
			};
			event_handle(array_from(all_registered_events));
			root_event_handles.add(event_handle);
			return () => {
				for (var event_name of registered_events) for (const node of [target, document]) {
					var counts = listeners.get(node);
					var count = counts.get(event_name);
					if (--count == 0) {
						node.removeEventListener(event_name, handle_event_propagation);
						counts.delete(event_name);
						if (counts.size === 0) listeners.delete(node);
					} else counts.set(event_name, count);
				}
				root_event_handles.delete(event_handle);
				if (anchor_node !== anchor) anchor_node.parentNode?.removeChild(anchor_node);
			};
		});
		mounted_components.set(component, unmount);
		return component;
	}
	/**
	* References of the components that were mounted or hydrated.
	* Uses a `WeakMap` to avoid memory leaks.
	*/
	var mounted_components = /* @__PURE__ */ new WeakMap();
	/**
	* Unmounts a component that was previously mounted using `mount` or `hydrate`.
	*
	* Since 5.13.0, if `options.outro` is `true`, [transitions](https://svelte.dev/docs/svelte/transition) will play before the component is removed from the DOM.
	*
	* Returns a `Promise` that resolves after transitions have completed if `options.outro` is true, or immediately otherwise (prior to 5.13.0, returns `void`).
	*
	* ```js
	* import { mount, unmount } from 'svelte';
	* import App from './App.svelte';
	*
	* const app = mount(App, { target: document.body });
	*
	* // later...
	* unmount(app, { outro: true });
	* ```
	* @param {Record<string, any>} component
	* @param {{ outro?: boolean }} [options]
	* @returns {Promise<void>}
	*/
	function unmount(component, options) {
		const fn = mounted_components.get(component);
		if (fn) {
			mounted_components.delete(component);
			return fn(options);
		}
		return Promise.resolve();
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/blocks/branches.js
	/** @import { Effect, TemplateNode } from '#client' */
	/**
	* @typedef {{ effect: Effect, fragment: DocumentFragment }} Branch
	*/
	/**
	* @template Key
	*/
	var BranchManager = class {
		/** @type {TemplateNode} */
		anchor;
		/** @type {Map<Batch, Key>} */
		#batches = /* @__PURE__ */ new Map();
		/**
		* Map of keys to effects that are currently rendered in the DOM.
		* These effects are visible and actively part of the document tree.
		* Example:
		* ```
		* {#if condition}
		* 	foo
		* {:else}
		* 	bar
		* {/if}
		* ```
		* Can result in the entries `true->Effect` and `false->Effect`
		* @type {Map<Key, Effect>}
		*/
		#onscreen = /* @__PURE__ */ new Map();
		/**
		* Similar to #onscreen with respect to the keys, but contains branches that are not yet
		* in the DOM, because their insertion is deferred.
		* @type {Map<Key, Branch>}
		*/
		#offscreen = /* @__PURE__ */ new Map();
		/**
		* Keys of effects that are currently outroing
		* @type {Set<Key>}
		*/
		#outroing = /* @__PURE__ */ new Set();
		/**
		* Whether to pause (i.e. outro) on change, or destroy immediately.
		* This is necessary for `<svelte:element>`
		*/
		#transition = true;
		/**
		* @param {TemplateNode} anchor
		* @param {boolean} transition
		*/
		constructor(anchor, transition = true) {
			this.anchor = anchor;
			this.#transition = transition;
		}
		/**
		* @param {Batch} batch
		*/
		#commit = (batch) => {
			if (!this.#batches.has(batch)) return;
			var key = this.#batches.get(batch);
			var onscreen = this.#onscreen.get(key);
			if (onscreen) {
				resume_effect(onscreen);
				this.#outroing.delete(key);
			} else {
				var offscreen = this.#offscreen.get(key);
				if (offscreen) {
					resume_effect(offscreen.effect);
					this.#onscreen.set(key, offscreen.effect);
					this.#offscreen.delete(key);
					/** @type {TemplateNode} */ offscreen.fragment.lastChild.remove();
					this.anchor.before(offscreen.fragment);
					onscreen = offscreen.effect;
				}
			}
			for (const [b, k] of this.#batches) {
				this.#batches.delete(b);
				if (b === batch) break;
				const offscreen = this.#offscreen.get(k);
				if (offscreen) {
					destroy_effect(offscreen.effect);
					this.#offscreen.delete(k);
				}
			}
			for (const [k, effect] of this.#onscreen) {
				if (k === key || this.#outroing.has(k)) continue;
				const on_destroy = () => {
					if (Array.from(this.#batches.values()).includes(k)) {
						var fragment = document.createDocumentFragment();
						move_effect(effect, fragment);
						fragment.append(create_text());
						this.#offscreen.set(k, {
							effect,
							fragment
						});
					} else destroy_effect(effect);
					this.#outroing.delete(k);
					this.#onscreen.delete(k);
				};
				if (this.#transition || !onscreen) {
					this.#outroing.add(k);
					pause_effect(effect, on_destroy, false);
				} else on_destroy();
			}
		};
		/**
		* @param {Batch} batch
		*/
		#discard = (batch) => {
			this.#batches.delete(batch);
			const keys = Array.from(this.#batches.values());
			for (const [k, branch] of this.#offscreen) if (!keys.includes(k)) {
				destroy_effect(branch.effect);
				this.#offscreen.delete(k);
			}
		};
		/**
		*
		* @param {any} key
		* @param {null | ((target: TemplateNode) => void)} fn
		*/
		ensure(key, fn) {
			var batch = current_batch;
			var defer = should_defer_append();
			if (fn && !this.#onscreen.has(key) && !this.#offscreen.has(key)) {
				if (defer) {
					var fragment = document.createDocumentFragment();
					var target = create_text();
					fragment.append(target);
					this.#offscreen.set(key, {
						effect: branch(() => fn(target)),
						fragment
					});
				} else this.#onscreen.set(key, branch(() => fn(this.anchor)));
			}
			this.#batches.set(batch, key);
			if (defer) {
				for (const [k, effect] of this.#onscreen) if (k === key) batch.unskip_effect(effect);
				else batch.skip_effect(effect);
				for (const [k, branch] of this.#offscreen) if (k === key) batch.unskip_effect(branch.effect);
				else batch.skip_effect(branch.effect);
				batch.oncommit(this.#commit);
				batch.ondiscard(this.#discard);
			} else {
				if (hydrating) this.anchor = hydrate_node;
				this.#commit(batch);
			}
		}
	};
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/blocks/if.js
	/** @import { TemplateNode } from '#client' */
	/**
	* @param {TemplateNode} node
	* @param {(branch: (fn: (anchor: Node) => void, key?: number | false) => void) => void} fn
	* @param {boolean} [elseif] True if this is an `{:else if ...}` block rather than an `{#if ...}`, as that affects which transitions are considered 'local'
	* @returns {void}
	*/
	function if_block(node, fn, elseif = false) {
		/** @type {TemplateNode | undefined} */
		var marker;
		if (hydrating) {
			marker = hydrate_node;
			hydrate_next();
		}
		var branches = new BranchManager(node);
		var flags = elseif ? EFFECT_TRANSPARENT : 0;
		/**
		* @param {number | false} key
		* @param {null | ((anchor: Node) => void)} fn
		*/
		function update_branch(key, fn) {
			if (hydrating) {
				var data = read_hydration_instruction(marker);
				if (key !== parseInt(data.substring(1))) {
					var anchor = skip_nodes();
					set_hydrate_node(anchor);
					branches.anchor = anchor;
					set_hydrating(false);
					branches.ensure(key, fn);
					set_hydrating(true);
					return;
				}
			}
			branches.ensure(key, fn);
		}
		block(() => {
			var has_branch = false;
			fn((fn, key = 0) => {
				has_branch = true;
				update_branch(key, fn);
			});
			if (!has_branch) update_branch(-1, null);
		}, flags);
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/blocks/each.js
	/** @import { EachItem, EachOutroGroup, EachState, Effect, EffectNodes, MaybeSource, Source, TemplateNode, TransitionManager, Value } from '#client' */
	/** @import { Batch } from '../../reactivity/batch.js'; */
	/**
	* @param {any} _
	* @param {number} i
	*/
	function index(_, i) {
		return i;
	}
	/**
	* Pause multiple effects simultaneously, and coordinate their
	* subsequent destruction. Used in each blocks
	* @param {EachState} state
	* @param {Effect[]} to_destroy
	* @param {null | Node} controlled_anchor
	*/
	function pause_effects(state, to_destroy, controlled_anchor) {
		/** @type {TransitionManager[]} */
		var transitions = [];
		var length = to_destroy.length;
		/** @type {EachOutroGroup} */
		var group;
		var remaining = to_destroy.length;
		for (var i = 0; i < length; i++) {
			let effect = to_destroy[i];
			pause_effect(effect, () => {
				if (group) {
					group.pending.delete(effect);
					group.done.add(effect);
					if (group.pending.size === 0) {
						var groups = state.outrogroups;
						destroy_effects(state, array_from(group.done));
						groups.delete(group);
						if (groups.size === 0) state.outrogroups = null;
					}
				} else remaining -= 1;
			}, false);
		}
		if (remaining === 0) {
			var fast_path = transitions.length === 0 && controlled_anchor !== null && state.pending.size === 0;
			if (fast_path) {
				var anchor = controlled_anchor;
				var parent_node = anchor.parentNode;
				clear_text_content(parent_node);
				parent_node.append(anchor);
				state.items.clear();
			}
			destroy_effects(state, to_destroy, !fast_path);
		} else {
			group = {
				pending: new Set(to_destroy),
				done: /* @__PURE__ */ new Set()
			};
			(state.outrogroups ??= /* @__PURE__ */ new Set()).add(group);
		}
	}
	/**
	* @param {EachState} state
	* @param {Effect[]} to_destroy
	* @param {boolean} remove_dom
	*/
	function destroy_effects(state, to_destroy, remove_dom = true) {
		/** @type {Set<Effect> | undefined} */
		var preserved_effects;
		if (state.pending.size > 0) {
			preserved_effects = /* @__PURE__ */ new Set();
			for (const keys of state.pending.values()) for (const key of keys) preserved_effects.add(
				/** @type {EachItem} */
				state.items.get(key).e
			);
		}
		for (var i = 0; i < to_destroy.length; i++) {
			var e = to_destroy[i];
			if (preserved_effects?.has(e)) {
				e.f |= EFFECT_OFFSCREEN;
				move_effect(e, document.createDocumentFragment());
			} else destroy_effect(to_destroy[i], remove_dom);
		}
	}
	/** @type {TemplateNode} */
	var offscreen_anchor;
	/**
	* @template V
	* @param {Element | Comment} node The next sibling node, or the parent node if this is a 'controlled' block
	* @param {number} flags
	* @param {() => V[]} get_collection
	* @param {(value: V, index: number) => any} get_key
	* @param {(anchor: Node, item: MaybeSource<V>, index: MaybeSource<number>) => void} render_fn
	* @param {null | ((anchor: Node) => void)} fallback_fn
	* @returns {void}
	*/
	function each(node, flags, get_collection, get_key, render_fn, fallback_fn = null) {
		var anchor = node;
		/** @type {Map<any, EachItem>} */
		var items = /* @__PURE__ */ new Map();
		if ((flags & 4) !== 0) {
			var parent_node = node;
			anchor = hydrating ? set_hydrate_node(/* @__PURE__ */ get_first_child(parent_node)) : parent_node.appendChild(create_text());
		}
		if (hydrating) hydrate_next();
		/** @type {Effect | null} */
		var fallback = null;
		var each_array = /* @__PURE__ */ derived_safe_equal(() => {
			var collection = get_collection();
			return is_array(collection) ? collection : collection == null ? [] : array_from(collection);
		});
		/** @type {V[]} */
		var array;
		/** @type {Map<Batch, Set<any>>} */
		var pending = /* @__PURE__ */ new Map();
		var first_run = true;
		/**
		* @param {Batch} batch
		*/
		function commit(batch) {
			if ((state.effect.f & 16384) !== 0) return;
			state.pending.delete(batch);
			state.fallback = fallback;
			reconcile(state, array, anchor, flags, get_key);
			if (fallback !== null) {
				if (array.length === 0) {
					if ((fallback.f & 33554432) === 0) resume_effect(fallback);
					else {
						fallback.f ^= EFFECT_OFFSCREEN;
						move(fallback, null, anchor);
					}
				} else pause_effect(fallback, () => {
					fallback = null;
				});
			}
		}
		/**
		* @param {Batch} batch
		*/
		function discard(batch) {
			state.pending.delete(batch);
		}
		/** @type {EachState} */
		var state = {
			effect: block(() => {
				array = get(each_array);
				var length = array.length;
				/** `true` if there was a hydration mismatch. Needs to be a `let` or else it isn't treeshaken out */
				let mismatch = false;
				if (hydrating) {
					if (read_hydration_instruction(anchor) === "[!" !== (length === 0)) {
						anchor = skip_nodes();
						set_hydrate_node(anchor);
						set_hydrating(false);
						mismatch = true;
					}
				}
				var keys = /* @__PURE__ */ new Set();
				var batch = current_batch;
				var defer = should_defer_append();
				for (var index = 0; index < length; index += 1) {
					if (hydrating && hydrate_node.nodeType === 8 && hydrate_node.data === "]") {
						anchor = hydrate_node;
						mismatch = true;
						set_hydrating(false);
					}
					var value = array[index];
					var key = get_key(value, index);
					var item = first_run ? null : items.get(key);
					if (item) {
						if (item.v) internal_set(item.v, value);
						if (item.i) internal_set(item.i, index);
						if (defer) batch.unskip_effect(item.e);
					} else {
						item = create_item(items, first_run ? anchor : offscreen_anchor ??= create_text(), value, key, index, render_fn, flags, get_collection);
						if (!first_run) item.e.f |= EFFECT_OFFSCREEN;
						items.set(key, item);
					}
					keys.add(key);
				}
				if (length === 0 && fallback_fn && !fallback) {
					if (first_run) fallback = branch(() => fallback_fn(anchor));
					else {
						fallback = branch(() => fallback_fn(offscreen_anchor ??= create_text()));
						fallback.f |= EFFECT_OFFSCREEN;
					}
				}
				if (length > keys.size) each_key_duplicate("", "", "");
				if (hydrating && length > 0) set_hydrate_node(skip_nodes());
				if (!first_run) {
					pending.set(batch, keys);
					if (defer) {
						for (const [key, item] of items) if (!keys.has(key)) batch.skip_effect(item.e);
						batch.oncommit(commit);
						batch.ondiscard(discard);
					} else commit(batch);
				}
				if (mismatch) set_hydrating(true);
				get(each_array);
			}),
			flags,
			items,
			pending,
			outrogroups: null,
			fallback
		};
		first_run = false;
		if (hydrating) anchor = hydrate_node;
	}
	/**
	* Skip past any non-branch effects (which could be created with `createSubscriber`, for example) to find the next branch effect
	* @param {Effect | null} effect
	* @returns {Effect | null}
	*/
	function skip_to_branch(effect) {
		while (effect !== null && (effect.f & 32) === 0) effect = effect.next;
		return effect;
	}
	/**
	* Add, remove, or reorder items output by an each block as its input changes
	* @template V
	* @param {EachState} state
	* @param {Array<V>} array
	* @param {Element | Comment | Text} anchor
	* @param {number} flags
	* @param {(value: V, index: number) => any} get_key
	* @returns {void}
	*/
	function reconcile(state, array, anchor, flags, get_key) {
		var is_animated = (flags & 8) !== 0;
		var length = array.length;
		var items = state.items;
		var current = skip_to_branch(state.effect.first);
		/** @type {undefined | Set<Effect>} */
		var seen;
		/** @type {Effect | null} */
		var prev = null;
		/** @type {undefined | Set<Effect>} */
		var to_animate;
		/** @type {Effect[]} */
		var matched = [];
		/** @type {Effect[]} */
		var stashed = [];
		/** @type {V} */
		var value;
		/** @type {any} */
		var key;
		/** @type {Effect | undefined} */
		var effect;
		/** @type {number} */
		var i;
		if (is_animated) for (i = 0; i < length; i += 1) {
			value = array[i];
			key = get_key(value, i);
			effect = items.get(key).e;
			if ((effect.f & 33554432) === 0) {
				effect.nodes?.a?.measure();
				(to_animate ??= /* @__PURE__ */ new Set()).add(effect);
			}
		}
		for (i = 0; i < length; i += 1) {
			value = array[i];
			key = get_key(value, i);
			effect = items.get(key).e;
			if (state.outrogroups !== null) for (const group of state.outrogroups) {
				group.pending.delete(effect);
				group.done.delete(effect);
			}
			if ((effect.f & 8192) !== 0) {
				resume_effect(effect);
				if (is_animated) {
					effect.nodes?.a?.unfix();
					(to_animate ??= /* @__PURE__ */ new Set()).delete(effect);
				}
			}
			if ((effect.f & 33554432) !== 0) {
				effect.f ^= EFFECT_OFFSCREEN;
				if (effect === current) move(effect, null, anchor);
				else {
					var next = prev ? prev.next : current;
					if (effect === state.effect.last) state.effect.last = effect.prev;
					if (effect.prev) effect.prev.next = effect.next;
					if (effect.next) effect.next.prev = effect.prev;
					link(state, prev, effect);
					link(state, effect, next);
					move(effect, next, anchor);
					prev = effect;
					matched = [];
					stashed = [];
					current = skip_to_branch(prev.next);
					continue;
				}
			}
			if (effect !== current) {
				if (seen !== void 0 && seen.has(effect)) {
					if (matched.length < stashed.length) {
						var start = stashed[0];
						var j;
						prev = start.prev;
						var a = matched[0];
						var b = matched[matched.length - 1];
						for (j = 0; j < matched.length; j += 1) move(matched[j], start, anchor);
						for (j = 0; j < stashed.length; j += 1) seen.delete(stashed[j]);
						link(state, a.prev, b.next);
						link(state, prev, a);
						link(state, b, start);
						current = start;
						prev = b;
						i -= 1;
						matched = [];
						stashed = [];
					} else {
						seen.delete(effect);
						move(effect, current, anchor);
						link(state, effect.prev, effect.next);
						link(state, effect, prev === null ? state.effect.first : prev.next);
						link(state, prev, effect);
						prev = effect;
					}
					continue;
				}
				matched = [];
				stashed = [];
				while (current !== null && current !== effect) {
					(seen ??= /* @__PURE__ */ new Set()).add(current);
					stashed.push(current);
					current = skip_to_branch(current.next);
				}
				if (current === null) continue;
			}
			if ((effect.f & 33554432) === 0) matched.push(effect);
			prev = effect;
			current = skip_to_branch(effect.next);
		}
		if (state.outrogroups !== null) {
			for (const group of state.outrogroups) if (group.pending.size === 0) {
				destroy_effects(state, array_from(group.done));
				state.outrogroups?.delete(group);
			}
			if (state.outrogroups.size === 0) state.outrogroups = null;
		}
		if (current !== null || seen !== void 0) {
			/** @type {Effect[]} */
			var to_destroy = [];
			if (seen !== void 0) {
				for (effect of seen) if ((effect.f & 8192) === 0) to_destroy.push(effect);
			}
			while (current !== null) {
				if ((current.f & 8192) === 0 && current !== state.fallback) to_destroy.push(current);
				current = skip_to_branch(current.next);
			}
			var destroy_length = to_destroy.length;
			if (destroy_length > 0) {
				var controlled_anchor = (flags & 4) !== 0 && length === 0 ? anchor : null;
				if (is_animated) {
					for (i = 0; i < destroy_length; i += 1) to_destroy[i].nodes?.a?.measure();
					for (i = 0; i < destroy_length; i += 1) to_destroy[i].nodes?.a?.fix();
				}
				pause_effects(state, to_destroy, controlled_anchor);
			}
		}
		if (is_animated) queue_micro_task(() => {
			if (to_animate === void 0) return;
			for (effect of to_animate) effect.nodes?.a?.apply();
		});
	}
	/**
	* @template V
	* @param {Map<any, EachItem>} items
	* @param {Node} anchor
	* @param {V} value
	* @param {unknown} key
	* @param {number} index
	* @param {(anchor: Node, item: V | Source<V>, index: number | Value<number>, collection: () => V[]) => void} render_fn
	* @param {number} flags
	* @param {() => V[]} get_collection
	* @returns {EachItem}
	*/
	function create_item(items, anchor, value, key, index, render_fn, flags, get_collection) {
		var v = (flags & 1) !== 0 ? (flags & 16) === 0 ? /* @__PURE__ */ mutable_source(value, false, false) : source(value) : null;
		var i = (flags & 2) !== 0 ? source(index) : null;
		return {
			v,
			i,
			e: branch(() => {
				render_fn(anchor, v ?? value, i ?? index, get_collection);
				return () => {
					items.delete(key);
				};
			})
		};
	}
	/**
	* @param {Effect} effect
	* @param {Effect | null} next
	* @param {Text | Element | Comment} anchor
	*/
	function move(effect, next, anchor) {
		if (!effect.nodes) return;
		var node = effect.nodes.start;
		var end = effect.nodes.end;
		var dest = next && (next.f & 33554432) === 0 ? next.nodes.start : anchor;
		while (node !== null) {
			var next_node = /* @__PURE__ */ get_next_sibling(node);
			dest.before(node);
			if (node === end) return;
			node = next_node;
		}
	}
	/**
	* @param {EachState} state
	* @param {Effect | null} prev
	* @param {Effect | null} next
	*/
	function link(state, prev, next) {
		if (prev === null) state.effect.first = next;
		else prev.next = next;
		if (next === null) state.effect.last = prev;
		else next.prev = prev;
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/elements/actions.js
	/** @import { ActionPayload } from '#client' */
	/**
	* @template P
	* @param {Element} dom
	* @param {(dom: Element, value?: P) => ActionPayload<P>} action
	* @param {() => P} [get_value]
	* @returns {void}
	*/
	function action(dom, action, get_value) {
		effect(() => {
			var payload = untrack(() => action(dom, get_value?.()) || {});
			if (get_value && payload?.update) {
				var inited = false;
				/** @type {P} */
				var prev = {};
				render_effect(() => {
					var value = get_value();
					deep_read_state(value);
					if (inited && safe_not_equal(prev, value)) {
						prev = value;
						/** @type {Function} */ payload.update(value);
					}
				});
				inited = true;
			}
			if (payload?.destroy) return () => payload.destroy();
		});
	}
	//#endregion
	//#region node_modules/clsx/dist/clsx.mjs
	function r(e) {
		var t, f, n = "";
		if ("string" == typeof e || "number" == typeof e) n += e;
		else if ("object" == typeof e) if (Array.isArray(e)) {
			var o = e.length;
			for (t = 0; t < o; t++) e[t] && (f = r(e[t])) && (n && (n += " "), n += f);
		} else for (f in e) e[f] && (n && (n += " "), n += f);
		return n;
	}
	function clsx$1() {
		for (var e, t, f = 0, n = "", o = arguments.length; f < o; f++) (e = arguments[f]) && (t = r(e)) && (n && (n += " "), n += t);
		return n;
	}
	//#endregion
	//#region node_modules/svelte/src/internal/shared/attributes.js
	/**
	* Small wrapper around clsx to preserve Svelte's (weird) handling of falsy values.
	* TODO Svelte 6 revisit this, and likely turn all falsy values into the empty string (what clsx also does)
	* @param  {any} value
	*/
	function clsx(value) {
		if (typeof value === "object") return clsx$1(value);
		else return value ?? "";
	}
	var whitespace = [..." 	\n\r\f\xA0\v﻿"];
	/**
	* @param {any} value
	* @param {string | null} [hash]
	* @param {Record<string, boolean>} [directives]
	* @returns {string | null}
	*/
	function to_class(value, hash, directives) {
		var classname = value == null ? "" : "" + value;
		if (hash) classname = classname ? classname + " " + hash : hash;
		if (directives) {
			for (var key of Object.keys(directives)) if (directives[key]) classname = classname ? classname + " " + key : key;
			else if (classname.length) {
				var len = key.length;
				var a = 0;
				while ((a = classname.indexOf(key, a)) >= 0) {
					var b = a + len;
					if ((a === 0 || whitespace.includes(classname[a - 1])) && (b === classname.length || whitespace.includes(classname[b]))) classname = (a === 0 ? "" : classname.substring(0, a)) + classname.substring(b + 1);
					else a = b;
				}
			}
		}
		return classname === "" ? null : classname;
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/elements/class.js
	/**
	* @param {Element} dom
	* @param {boolean | number} is_html
	* @param {string | null} value
	* @param {string} [hash]
	* @param {Record<string, any>} [prev_classes]
	* @param {Record<string, any>} [next_classes]
	* @returns {Record<string, boolean> | undefined}
	*/
	function set_class(dom, is_html, value, hash, prev_classes, next_classes) {
		var prev = dom[CLASS_CACHE];
		if (hydrating || prev !== value || prev === void 0) {
			var next_class_name = to_class(value, hash, next_classes);
			if (!hydrating || next_class_name !== dom.getAttribute("class")) {
				if (next_class_name == null) dom.removeAttribute("class");
				else if (is_html) dom.className = next_class_name;
				else dom.setAttribute("class", next_class_name);
			}
			/** @type {any} */ dom[CLASS_CACHE] = value;
		} else if (next_classes && prev_classes !== next_classes) for (var key in next_classes) {
			var is_present = !!next_classes[key];
			if (prev_classes == null || is_present !== !!prev_classes[key]) dom.classList.toggle(key, is_present);
		}
		return next_classes;
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/elements/bindings/select.js
	/**
	* Sets the `selected` attribute on an option so form reset can restore it.
	* @param {HTMLOptionElement} option
	* @param {boolean} selected
	*/
	function set_selected(option, selected) {
		if (selected) {
			if (!option.hasAttribute("selected")) option.setAttribute("selected", "");
		} else option.removeAttribute("selected");
	}
	/**
	* Marks the options matching `__defaultValue` as selected. Without `preserve`
	* a newly matching option gets selected, as an inserted `<option selected>` would.
	* @param {HTMLSelectElement} select
	* @param {boolean} preserve
	*/
	function apply_default_select_value(select, preserve) {
		var value = select.__defaultValue;
		var multiple = select.multiple;
		var values = multiple ? value ?? [] : null;
		if (multiple && !is_array(values)) return;
		var index = select.selectedIndex;
		var selected = preserve && multiple ? new Set(select.selectedOptions) : null;
		for (var option of select.options) {
			var option_value = get_option_value(option);
			set_selected(option, multiple ? values.includes(option_value) : is(option_value, value));
		}
		if (!preserve) return;
		if (selected !== null) for (option of select.options) {
			var was_selected = selected.has(option);
			if (option.selected !== was_selected) option.selected = was_selected;
		}
		else if (select.selectedIndex !== index) select.selectedIndex = index;
	}
	/**
	* Selects the correct option(s) (depending on whether this is a multiple select)
	* @template V
	* @param {HTMLSelectElement} select
	* @param {V} value
	* @param {boolean} mounting
	*/
	function select_option(select, value, mounting = false) {
		if (select.multiple) {
			if (value == void 0) return;
			if (!is_array(value)) return select_multiple_invalid_value();
			for (var option of select.options) option.selected = value.includes(get_option_value(option));
			return;
		}
		for (option of select.options) if (is(get_option_value(option), value)) {
			option.selected = true;
			return;
		}
		if (!mounting || value !== void 0) select.selectedIndex = -1;
	}
	/**
	* Sets up a mutation observer to sync the current selection
	* and default to the dom when the options change, for example
	* when they are inside an `#each` block. Called once per `<select>`,
	* by the compiled output or by `attribute_effect` for spreads.
	* @param {HTMLSelectElement} select
	*/
	function init_select(select) {
		var observer = new MutationObserver((entries) => {
			if (entries.every(is_selectedcontent_mutation)) return;
			if ("__defaultValue" in select) apply_default_select_value(select, false);
			if ("__value" in select) select_option(select, select.__value);
		});
		observer.observe(select, {
			childList: true,
			subtree: true,
			attributes: true,
			attributeFilter: ["value"]
		});
		teardown(() => {
			observer.disconnect();
		});
	}
	/**
	* @param {HTMLSelectElement} select
	* @param {() => unknown} get
	* @param {(value: unknown) => void} set
	* @returns {void}
	*/
	function bind_select_value(select, get, set = get) {
		var batches = /* @__PURE__ */ new WeakSet();
		var mounting = true;
		listen_to_event_and_reset_event(select, "change", (is_reset) => {
			var query = is_reset ? "[selected]" : ":checked";
			/** @type {unknown} */
			var value;
			if (select.multiple) value = [].map.call(select.querySelectorAll(query), get_option_value);
			else {
				/** @type {HTMLOptionElement | null} */
				var selected_option = select.querySelector(query) ?? select.querySelector("option:not([disabled])");
				value = selected_option && get_option_value(selected_option);
			}
			set(value);
			select.__value = value;
			if (current_batch !== null) batches.add(current_batch);
		});
		effect(() => {
			var value = get();
			if (select === document.activeElement) {
				var batch = async_mode_flag ? previous_batch : current_batch;
				if (batches.has(batch)) return;
			}
			select_option(select, value, mounting);
			if (mounting && value === void 0) {
				/** @type {HTMLOptionElement | null} */
				var selected_option = select.querySelector(":checked");
				if (selected_option !== null) {
					value = get_option_value(selected_option);
					set(value);
				}
			}
			select.__value = value;
			mounting = false;
		});
	}
	/** @param {HTMLOptionElement} option */
	function get_option_value(option) {
		if ("__value" in option) return option.__value;
		else return option.value;
	}
	/**
	* Returns `true` if the mutation stems from the browser mirroring the selected
	* option's content into `<selectedcontent>`, or from us replacing the
	* `<selectedcontent>` element with a clone of itself
	* @param {MutationRecord} entry
	*/
	function is_selectedcontent_mutation(entry) {
		if (entry.target.closest("selectedcontent") !== null) return true;
		if (entry.type === "childList") {
			var nodes = [...entry.addedNodes, ...entry.removedNodes];
			return nodes.length > 0 && nodes.every((node) => node.nodeName === "SELECTEDCONTENT");
		}
		return false;
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/elements/attributes.js
	/** @import { Blocker, Effect } from '#client' */
	var IS_CUSTOM_ELEMENT = Symbol("is custom element");
	var IS_HTML = Symbol("is html");
	var LINK_TAG = IS_XHTML ? "link" : "LINK";
	var PROGRESS_TAG = IS_XHTML ? "progress" : "PROGRESS";
	/**
	* The value/checked attribute in the template actually corresponds to the defaultValue property, so we need
	* to remove it upon hydration to avoid a bug when someone resets the form value.
	* @param {HTMLInputElement} input
	* @returns {void}
	*/
	function remove_input_defaults(input) {
		if (!hydrating) return;
		var already_removed = false;
		var remove_defaults = () => {
			if (already_removed) return;
			already_removed = true;
			if (input.hasAttribute("value")) {
				var value = input.value;
				set_attribute(input, "value", null);
				input.value = value;
			}
			if (input.hasAttribute("checked")) {
				var checked = input.checked;
				set_attribute(input, "checked", null);
				input.checked = checked;
			}
		};
		/** @type {any} */ input[FORM_RESET_HANDLER] = remove_defaults;
		queue_micro_task(remove_defaults);
		add_form_reset_listener();
	}
	/**
	* @param {Element} element
	* @param {any} value
	*/
	function set_value(element, value) {
		var attributes = get_attributes(element);
		if (attributes.value === (attributes.value = value ?? void 0) || element.value === value && (value !== 0 || element.nodeName !== PROGRESS_TAG)) return;
		element.value = value ?? "";
	}
	/**
	* @param {Element} element
	* @param {boolean} checked
	*/
	function set_checked(element, checked) {
		var attributes = get_attributes(element);
		if (attributes.checked === (attributes.checked = checked ?? void 0)) return;
		element.checked = checked;
	}
	/**
	* @param {Element} element
	* @param {string} attribute
	* @param {string | null} value
	* @param {boolean} [skip_warning]
	*/
	function set_attribute(element, attribute, value, skip_warning) {
		var attributes = get_attributes(element);
		if (hydrating) {
			attributes[attribute] = element.getAttribute(attribute);
			if (attribute === "src" || attribute === "srcset" || attribute === "href" && element.nodeName === LINK_TAG) {
				if (!skip_warning);
				return;
			}
		}
		if (attributes[attribute] === (attributes[attribute] = value)) return;
		if (attribute === "loading") element[LOADING_ATTR_SYMBOL] = value;
		if (value == null) element.removeAttribute(attribute);
		else if (typeof value !== "string" && get_setters(element).has(attribute)) element[attribute] = value;
		else element.setAttribute(attribute, value);
	}
	/**
	*
	* @param {Element} element
	*/
	function get_attributes(element) {
		return element[ATTRIBUTES_CACHE] ??= {
			[IS_CUSTOM_ELEMENT]: element.nodeName.includes("-"),
			[IS_HTML]: element.namespaceURI === NAMESPACE_HTML
		};
	}
	/** @type {Map<string, Set<string>>} */
	var setters_cache = /* @__PURE__ */ new Map();
	/** @param {Element} element */
	function get_setters(element) {
		var cache_key = element.getAttribute("is") || element.nodeName;
		var setters = setters_cache.get(cache_key);
		if (setters) return setters;
		setters_cache.set(cache_key, setters = /* @__PURE__ */ new Set());
		var descriptors;
		var proto = element;
		var element_proto = Element.prototype;
		while (element_proto !== proto) {
			descriptors = get_descriptors(proto);
			for (var key in descriptors) if (descriptors[key].set && key !== "innerHTML" && key !== "textContent" && key !== "innerText") setters.add(key);
			proto = get_prototype_of(proto);
		}
		return setters;
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/elements/bindings/input.js
	/** @import { Batch } from '../../../reactivity/batch.js' */
	/**
	* @param {HTMLInputElement} input
	* @param {() => unknown} get
	* @param {(value: unknown) => void} set
	* @returns {void}
	*/
	function bind_value(input, get, set = get) {
		var batches = /* @__PURE__ */ new WeakSet();
		listen_to_event_and_reset_event(input, "input", async (is_reset) => {
			/** @type {any} */
			var value = is_reset ? input.defaultValue : input.value;
			value = is_numberlike_input(input) ? to_number(value) : value;
			set(value);
			if (current_batch !== null) batches.add(current_batch);
			await tick();
			if (value !== (value = get())) {
				var start = input.selectionStart;
				var end = input.selectionEnd;
				var length = input.value.length;
				input.value = value ?? "";
				if (end !== null) {
					var new_length = input.value.length;
					if (start === end && end === length && new_length > length) {
						input.selectionStart = new_length;
						input.selectionEnd = new_length;
					} else {
						input.selectionStart = start;
						input.selectionEnd = Math.min(end, new_length);
					}
				}
			}
		});
		if (hydrating && input.defaultValue !== input.value || untrack(get) == null && input.value) {
			set(is_numberlike_input(input) ? to_number(input.value) : input.value);
			if (current_batch !== null) batches.add(current_batch);
		}
		render_effect(() => {
			var value = get();
			if (input === document.activeElement) {
				var batch = async_mode_flag ? previous_batch : current_batch;
				if (batches.has(batch)) return;
			}
			if (is_numberlike_input(input) && value === to_number(input.value)) return;
			if (input.type === "date" && !value && !input.value) return;
			if (value !== input.value) input.value = value ?? "";
		});
	}
	/**
	* @param {HTMLInputElement} input
	*/
	function is_numberlike_input(input) {
		var type = input.type;
		return type === "number" || type === "range";
	}
	/**
	* @param {string} value
	*/
	function to_number(value) {
		return value === "" ? null : +value;
	}
	var resize_observer_border_box = /* @__PURE__ */ new class ResizeObserverSingleton {
		/** */
		#listeners = /* @__PURE__ */ new WeakMap();
		/** @type {ResizeObserver | undefined} */
		#observer;
		/** @type {ResizeObserverOptions} */
		#options;
		/** @static */
		static entries = /* @__PURE__ */ new WeakMap();
		/** @param {ResizeObserverOptions} options */
		constructor(options) {
			this.#options = options;
		}
		/**
		* @param {Element} element
		* @param {(entry: ResizeObserverEntry) => any} listener
		*/
		observe(element, listener) {
			var listeners = this.#listeners.get(element) || /* @__PURE__ */ new Set();
			listeners.add(listener);
			this.#listeners.set(element, listeners);
			this.#getObserver().observe(element, this.#options);
			return () => {
				var listeners = this.#listeners.get(element);
				listeners.delete(listener);
				if (listeners.size === 0) {
					this.#listeners.delete(element);
					/** @type {ResizeObserver} */ this.#observer.unobserve(element);
				}
			};
		}
		#getObserver() {
			return this.#observer ?? (this.#observer = new ResizeObserver(
				/** @param {any} entries */
				(entries) => {
					for (var entry of entries) {
						ResizeObserverSingleton.entries.set(entry.target, entry);
						for (var listener of this.#listeners.get(entry.target) || []) listener(entry);
					}
				}
			));
		}
	}({ box: "border-box" });
	/**
	* @param {HTMLElement} element
	* @param {'clientWidth' | 'clientHeight' | 'offsetWidth' | 'offsetHeight'} type
	* @param {(size: number) => void} set
	*/
	function bind_element_size(element, type, set) {
		var unsub = resize_observer_border_box.observe(element, () => set(element[type]));
		effect(() => {
			untrack(() => set(element[type]));
			return unsub;
		});
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/dom/elements/bindings/this.js
	/** @import { ComponentContext, Effect } from '#client' */
	/**
	* @param {any} bound_value
	* @param {Element} element_or_component
	* @returns {boolean}
	*/
	function is_bound_this(bound_value, element_or_component) {
		return bound_value === element_or_component || bound_value?.[STATE_SYMBOL] === element_or_component;
	}
	/**
	* @param {any} element_or_component
	* @param {(value: unknown, ...parts: unknown[]) => void} update
	* @param {(...parts: unknown[]) => unknown} get_value
	* @param {() => unknown[]} [get_parts] Set if the this binding is used inside an each block,
	* 										returns all the parts of the each block context that are used in the expression
	* @returns {void}
	*/
	function bind_this(element_or_component = mark_as_component(), update, get_value, get_parts) {
		var component_effect = component_context.r;
		var parent = active_effect;
		effect(() => {
			/** @type {unknown[]} */
			var old_parts;
			/** @type {unknown[]} */
			var parts;
			render_effect(() => {
				old_parts = parts;
				parts = get_parts?.() || [];
				untrack(() => {
					if (!is_bound_this(get_value(...parts), element_or_component)) {
						update(element_or_component, ...parts);
						if (old_parts && is_bound_this(get_value(...old_parts), element_or_component)) update(null, ...old_parts);
					}
				});
			});
			return () => {
				let p = parent;
				while (p !== component_effect && p.parent !== null && p.parent.f & 33554432) p = p.parent;
				const teardown = () => {
					if (parts && is_bound_this(get_value(...parts), element_or_component)) update(null, ...parts);
				};
				const original_teardown = p.teardown;
				p.teardown = () => {
					teardown();
					original_teardown?.();
				};
			};
		});
		return element_or_component;
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/reactivity/store.js
	/**
	* Whether or not the prop currently being read is a store binding, as in
	* `<Child bind:x={$y} />`. If it is, we treat the prop as mutable even in
	* runes mode, and skip `binding_property_non_reactive` validation
	*/
	var is_store_binding = false;
	/**
	* Returns a tuple that indicates whether `fn()` reads a prop that is a store binding.
	* Used to prevent `binding_property_non_reactive` validation false positives and
	* ensure that these props are treated as mutable even in runes mode
	* @template T
	* @param {() => T} fn
	* @returns {[T, boolean]}
	*/
	function capture_store_binding(fn) {
		var previous_is_store_binding = is_store_binding;
		try {
			is_store_binding = false;
			return [fn(), is_store_binding];
		} finally {
			is_store_binding = previous_is_store_binding;
		}
	}
	//#endregion
	//#region node_modules/svelte/src/internal/client/reactivity/props.js
	/** @import { Derived, Effect, Source } from './types.js' */
	/**
	* This function is responsible for synchronizing a possibly bound prop with the inner component state.
	* It is used whenever the compiler sees that the component writes to the prop, or when it has a default prop_value.
	* @template V
	* @param {Record<string, unknown>} props
	* @param {string} key
	* @param {number} flags
	* @param {V | (() => V)} [fallback]
	* @returns {(() => V | ((arg: V) => V) | ((arg: V, mutation: boolean) => V))}
	*/
	function prop(props, key, flags, fallback) {
		var runes = !legacy_mode_flag || (flags & 2) !== 0;
		var bindable = (flags & 8) !== 0;
		var lazy = (flags & 16) !== 0;
		var fallback_value = fallback;
		var fallback_dirty = true;
		var fallback_signal = void 0;
		var get_fallback = () => {
			if (lazy && runes) {
				fallback_signal ??= /* @__PURE__ */ derived(fallback);
				return get(fallback_signal);
			}
			if (fallback_dirty) {
				fallback_dirty = false;
				fallback_value = lazy ? untrack(fallback) : fallback;
			}
			return fallback_value;
		};
		/** @type {((v: V) => void) | undefined} */
		let setter;
		if (bindable) {
			var is_entry_props = STATE_SYMBOL in props || LEGACY_PROPS in props;
			setter = get_descriptor(props, key)?.set ?? (is_entry_props && key in props ? (v) => props[key] = v : void 0);
		}
		/** @type {V} */
		var initial_value;
		var is_store_sub = false;
		if (bindable) [initial_value, is_store_sub] = capture_store_binding(() => props[key]);
		else initial_value = props[key];
		if (initial_value === void 0 && fallback !== void 0) {
			initial_value = get_fallback();
			if (setter) {
				if (runes) props_invalid_value(key);
				setter(initial_value);
			}
		}
		/** @type {() => V} */
		var getter;
		if (runes) getter = () => {
			var value = props[key];
			if (value === void 0) return get_fallback();
			fallback_dirty = true;
			return value;
		};
		else getter = () => {
			var value = props[key];
			if (value !== void 0) fallback_value = void 0;
			return value === void 0 ? fallback_value : value;
		};
		if (runes && (flags & 4) === 0) return getter;
		if (setter) {
			var legacy_parent = props.$$legacy;
			return (function(value, mutation) {
				if (arguments.length > 0) {
					if (!runes || !mutation || legacy_parent || is_store_sub)
 /** @type {Function} */ setter(mutation ? getter() : value);
					return value;
				}
				return getter();
			});
		}
		var overridden = false;
		var d = ((flags & 1) !== 0 ? derived : derived_safe_equal)(() => {
			overridden = false;
			return getter();
		});
		if (bindable) get(d);
		var parent_effect = active_effect;
		return (function(value, mutation) {
			if (arguments.length > 0) {
				const new_value = mutation ? get(d) : runes && bindable ? proxy(value) : value;
				set(d, new_value);
				overridden = true;
				if (fallback_value !== void 0) fallback_value = new_value;
				return value;
			}
			if (is_destroying_effect && overridden || (parent_effect.f & 16384) !== 0) return d.v;
			return get(d);
		});
	}
	if (typeof HTMLElement === "function");
	//#endregion
	//#region node_modules/svelte/src/internal/disclose-version.js
	if (typeof window !== "undefined") ((window.__svelte ??= {}).v ??= /* @__PURE__ */ new Set()).add("5");
	//#endregion
	//#region side-pairs/src/components/Summary.svelte
	var root$9 = /* @__PURE__ */ from_html(`<a><strong> </strong><span> </span></a>`);
	var root_1$9 = /* @__PURE__ */ from_html(`<div class="side-icon-group"><a class="side-icon-head"><strong> </strong><span> </span></a> <div class="side-icon-cells"></div> <a class="side-icon-subhead"><strong>Icon review</strong><span> </span></a> <div class="side-icon-cells"></div></div>`);
	var root_2$8 = /* @__PURE__ */ from_html(`<div class="side-icon-group"><a class="side-icon-head"><strong> </strong><span> </span></a> <div class="side-icon-cells"></div></div>`);
	var root_3$8 = /* @__PURE__ */ from_html(`<section class="side-icon-summary"><p class="side-icon-total"> </p> <!> <!></section>`);
	function Summary($$anchor, $$props) {
		push($$props, true);
		const view = /* @__PURE__ */ user_derived(() => {
			$$props.store.version;
			const s = $$props.store, at72 = s.size === 72, sizes = s.sizes();
			const isText = (i) => [i.id, ...i.source_ids].some((id) => s.statuses[id]?.reason === "text_number");
			const mains = s.components.mains, subs = s.components.subs, textSubs = subs.filter(isText), iconSubs = subs.filter((i) => !isText(i));
			const count = (list, status) => list.filter((i) => i.status === status).length;
			const drawings = (list) => [...new Map(list.flatMap((i) => i.drawings).filter((d) => d.status !== "fail" && d.svg_sha256).map((d) => [d.key, d])).values()];
			const reviewState = (d) => {
				const r = s.reviews[d.key] || "ready";
				return r === "re-generated" ? "ready" : r === "disapprove" || r === "claimed" ? "pending" : r;
			};
			const tally = (list) => {
				const t = {
					approve: 0,
					ready: 0,
					pending: 0,
					rejected: 0
				};
				for (const d of list) t[reviewState(d)] = (t[reviewState(d)] || 0) + 1;
				return t;
			};
			const reviewCells = (list, family) => {
				const t = tally(list), page = "index.html?family=" + family;
				return {
					count: list.length,
					page,
					cells: [
						[
							"Approved",
							t.approve,
							"approve",
							"ok"
						],
						[
							"To review",
							t.ready,
							"ready",
							"todo"
						],
						[
							"Needs fix",
							t.pending,
							"pending",
							"fix"
						],
						[
							"Rejected",
							t.rejected,
							"rejected",
							"rej"
						]
					]
				};
			};
			const mainDrawings = drawings(mains), subDrawings = drawings(subs);
			const groups = [{
				title: at72 ? "Main icons · 54" : "Main icons",
				total: mains.length,
				page: at72 ? "index.html?family=main-54" : "side-mains.html",
				cells: [
					[
						"Generated",
						count(mains, "done"),
						"done",
						"ok"
					],
					[
						"Needs fix",
						count(mains, "failing"),
						"failing",
						"fix"
					],
					[
						"Not generated",
						count(mains, "missing"),
						"missing",
						"todo"
					]
				],
				review: reviewCells(mainDrawings, at72 ? "main-54" : "side_main")
			}, {
				title: at72 ? "Sub icons · 36" : "Sub icons",
				total: subs.length,
				page: at72 ? "index.html?family=sub-36" : "side-subs.html",
				cells: [
					[
						"Generated",
						count(iconSubs, "done"),
						"done",
						"ok"
					],
					[
						"Text",
						textSubs.length,
						"text",
						"text"
					],
					[
						"Needs fix",
						count(iconSubs, "failing"),
						"failing",
						"fix"
					],
					[
						"Not generated",
						count(iconSubs, "missing"),
						"missing",
						"todo"
					]
				],
				review: reviewCells(subDrawings, at72 ? "sub-36" : "side_sub")
			}];
			let combined = null;
			if (s.run) {
				const state = (icon) => ({
					approve: "approve",
					"re-generated": "ready",
					disapprove: "pending",
					claimed: "pending"
				})[s.reviews[icon.key]] || s.reviews[icon.key] || "ready";
				const reviewed = (st) => s.run.icons.filter((i) => state(i) === st).length, review = "index.html?family=" + sizes.combined;
				combined = {
					title: "Combined · " + sizes.canvas,
					count: s.run.count,
					page: at72 ? review : "experiment.html?type=combination",
					review,
					cells: [
						[
							"Approved",
							reviewed("approve"),
							"approve",
							"ok"
						],
						[
							"To review",
							reviewed("ready"),
							"ready",
							"todo"
						],
						[
							"Needs fix",
							reviewed("pending"),
							"pending",
							"fix"
						]
					]
				};
			}
			return {
				mains,
				subs,
				mainDrawings,
				subDrawings,
				groups,
				combined
			};
		});
		const href = (page, status) => page + (page.includes("?") ? "&" : "?") + "status=" + status;
		var section = root_3$8();
		var p = child(section);
		var text = only_child(p);
		var node = sibling(p, 2);
		each(node, 17, () => get(view).groups, (group) => group.title, ($$anchor, group) => {
			var div = root_1$9();
			var a = child(div);
			var strong = child(a);
			var text_1 = only_child(strong, true);
			var text_2 = only_child(sibling(strong));
			reset(a);
			var div_1 = sibling(a, 2);
			each(div_1, 21, () => get(group).cells, ([label, value, status, tone]) => status, ($$anchor, $$item) => {
				var $$array = /* @__PURE__ */ user_derived(() => to_array(get($$item), 4));
				let label = () => get($$array)[0];
				let value = () => get($$array)[1];
				let status = () => get($$array)[2];
				let tone = () => get($$array)[3];
				var a_1 = root$9();
				var strong_1 = child(a_1);
				var text_3 = only_child(strong_1, true);
				var text_4 = only_child(sibling(strong_1), true);
				reset(a_1);
				template_effect(($0, $1) => {
					set_class(a_1, 1, "side-icon-cell " + tone());
					set_attribute(a_1, "href", $0);
					set_text(text_3, $1);
					set_text(text_4, label());
				}, [() => href(get(group).page, status()), () => value().toLocaleString()]);
				append($$anchor, a_1);
			});
			reset(div_1);
			var a_2 = sibling(div_1, 2);
			var text_5 = only_child(sibling(child(a_2)));
			reset(a_2);
			var div_2 = sibling(a_2, 2);
			each(div_2, 21, () => get(group).review.cells, ([label, value, status, tone]) => status, ($$anchor, $$item) => {
				var $$array_1 = /* @__PURE__ */ user_derived(() => to_array(get($$item), 4));
				let label = () => get($$array_1)[0];
				let value = () => get($$array_1)[1];
				let status = () => get($$array_1)[2];
				let tone = () => get($$array_1)[3];
				var a_3 = root$9();
				var strong_2 = child(a_3);
				var text_6 = only_child(strong_2, true);
				var text_7 = only_child(sibling(strong_2), true);
				reset(a_3);
				template_effect(($0, $1) => {
					set_class(a_3, 1, "side-icon-cell " + tone());
					set_attribute(a_3, "href", $0);
					set_text(text_6, $1);
					set_text(text_7, label());
				}, [() => href(get(group).review.page, status()), () => value().toLocaleString()]);
				append($$anchor, a_3);
			});
			reset(div_2);
			reset(div);
			template_effect(($0, $1) => {
				set_attribute(a, "href", get(group).page);
				set_text(text_1, get(group).title);
				set_text(text_2, `${$0 ?? ""} icons →`);
				set_attribute(a_2, "href", get(group).review.page);
				set_text(text_5, `${$1 ?? ""} drawings →`);
			}, [() => get(group).total.toLocaleString(), () => get(group).review.count.toLocaleString()]);
			append($$anchor, div);
		});
		var node_1 = sibling(node, 2);
		var consequent = ($$anchor) => {
			var div_3 = root_2$8();
			var a_4 = child(div_3);
			var strong_3 = child(a_4);
			var text_8 = only_child(strong_3, true);
			var text_9 = only_child(sibling(strong_3));
			reset(a_4);
			var div_4 = sibling(a_4, 2);
			each(div_4, 21, () => get(view).combined.cells, ([label, value, status, tone]) => status, ($$anchor, $$item) => {
				var $$array_2 = /* @__PURE__ */ user_derived(() => to_array(get($$item), 4));
				let label = () => get($$array_2)[0];
				let value = () => get($$array_2)[1];
				let status = () => get($$array_2)[2];
				let tone = () => get($$array_2)[3];
				var a_5 = root$9();
				var strong_4 = child(a_5);
				var text_10 = only_child(strong_4, true);
				var text_11 = only_child(sibling(strong_4), true);
				reset(a_5);
				template_effect(($0) => {
					set_class(a_5, 1, "side-icon-cell " + tone());
					set_attribute(a_5, "href", get(view).combined.review + "&status=" + status());
					set_text(text_10, $0);
					set_text(text_11, label());
				}, [() => value().toLocaleString()]);
				append($$anchor, a_5);
			});
			reset(div_4);
			reset(div_3);
			template_effect(($0) => {
				set_attribute(a_4, "href", get(view).combined.page);
				set_text(text_8, get(view).combined.title);
				set_text(text_9, `${$0 ?? ""} combined icons →`);
			}, [() => get(view).combined.count.toLocaleString()]);
			append($$anchor, div_3);
		};
		if_block(node_1, ($$render) => {
			if (get(view).combined) $$render(consequent);
		});
		reset(section);
		template_effect(($0, $1, $2, $3, $4) => set_text(text, `${$0 ?? ""} side pairs, made from ${$1 ?? ""} main icons (${$2 ?? ""} drawings) and ${$3 ?? ""} sub icons (${$4 ?? ""} drawings). A source with several drawings has alternative redraws or versions; each pair uses one.`), [
			() => $$props.pairCount.toLocaleString(),
			() => get(view).mains.length.toLocaleString(),
			() => get(view).mainDrawings.length.toLocaleString(),
			() => get(view).subs.length.toLocaleString(),
			() => get(view).subDrawings.length.toLocaleString()
		]);
		append($$anchor, section);
		pop();
	}
	//#endregion
	//#region side-pairs/src/lib/rules.js
	var POSITIONS$1 = {
		br: "Bottom-right",
		bl: "Bottom-left",
		tr: "Top-right",
		tl: "Top-left",
		ri: "Right",
		le: "Left",
		bo: "Bottom",
		to: "Top"
	};
	var STATES = {
		ready: "Ready",
		fix: "Fix sub",
		fixmain: "Fix main",
		waiting: "Waiting",
		main: "Needs main",
		sub: "Needs sub",
		textsub: "Needs text sub"
	};
	var STATE_HINTS = {
		ready: "Main and sub are drawn and can be combined.",
		fix: "The sub fails a check. Fix it before combining.",
		fixmain: "A 48×48 main is drawn but fails validation or was marked needs fix, so it is not in Icon review. Fix it on the Main icons page (Needs fix).",
		waiting: "Main and sub are drawn but not combined yet.",
		main: "No 48×48 solo main icon yet.",
		sub: "No 32×32 sub icon yet.",
		textsub: "The sub is text or a number and is not drawn yet. It is generated separately."
	};
	var FILTERS = {
		"": "All",
		...STATES,
		uncombined: "Not combined",
		text: "Text sub",
		multi: "2+ subs",
		made: "From review",
		changed: "Main / sub changed",
		built: "Built",
		stale: "Stale (built from older drawings)",
		unbuilt: "Not built"
	};
	var GROUPS = {
		"": "No grouping",
		main: "Group by main",
		sub: "Group by sub"
	};
	var PAGE_SIZES = [
		24,
		48,
		96
	];
	var REVIEW_LABELS = {
		approve: "Approved",
		ready: "To review",
		"re-generated": "To review",
		pending: "Needs fix",
		disapprove: "Needs fix",
		claimed: "Being fixed",
		rejected: "Rejected"
	};
	var dataURL = (svg) => "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
	var round = (n) => Math.round(n * 10) / 10;
	var usable = (s, d) => (d.status === "pass" || s.reviews[d.key] === "approve") && !["pending", "rejected"].includes(s.reviews[d.key]);
	function drawingProblems(s, d) {
		if (!d || usable(s, d)) return [];
		if (d.status !== "pass") return d.errors?.length ? d.errors : ["Fails validation"];
		return [s.reviews[d.key] === "rejected" ? "Rejected in Icon review" : "Disapproved — needs fix"];
	}
	function ink(item, sub) {
		if (sub && item.ink32) return [item.ink32.ink_width, item.ink32.ink_height];
		const b = item.bounds;
		if (!b) return [0, 0];
		return [b[2] - b[0] + 4, b[3] - b[1] + 4];
	}
	var EXCEPTION_SIZES = [
		"side-source-fit",
		"side-32x48",
		"side-one-axis32"
	];
	function subProblems(s, item, flagged = () => false) {
		const problems = [], [w, h] = ink(item, true);
		if (item.model_validation && item.model_validation !== "pass") problems.push("Model validation: " + item.model_validation);
		if (!item.stale_form && ["needs_redraw", "needs_review"].includes(item.sub32_status)) problems.push(item.sub32_reason || "Needs a SUB32 redraw");
		if (!item.stale_form && !item.native_text && !EXCEPTION_SIZES.includes(item.sizing_mode) && (w > 32.01 || h > 32.01)) problems.push(`Ink ${round(w)}×${round(h)} exceeds 32×32`);
		if (flagged(item)) problems.push("Disapproved — needs fix");
		return problems;
	}
	var currentSub = (pair) => pair.subs[0];
	var mainOf = (pair) => pair.mains.find((m) => m.family === "solo" || m.family === "combination_main") || pair.mains[0];
	function subIsText(s, row, pair) {
		const refs = s.catalog.references;
		if ([row.sub_id, refs[row.sub_id]?.canonical_id].some((id) => id && s.statuses[id]?.reason === "text_number")) return true;
		return !!pair?.subs.length && currentSub(pair).sizing_kind === "text";
	}
	function key(s, row, flagged) {
		const pair = s.pairs.get(row.id), main = s.componentStatus.main.get(row.main_id), sub = s.componentStatus.sub.get(row.sub_id);
		const textSub = sub === "missing" && subIsText(s, row, pair);
		if (main === "failing") return "fixmain";
		if (main !== "done") return sub === "missing" ? textSub ? "both-text" : "both" : "main";
		if (sub === "missing") return textSub ? "textsub" : "sub";
		if (sub === "failing") return "fix";
		if (pair?.mains.length && pair.subs.length) return subProblems(s, currentSub(pair), flagged).length ? "fix" : "ready";
		return "waiting";
	}
	function category(s, row, flagged, buildState) {
		const pair = s.pairs.get(row.id), k = key(s, row, flagged);
		const both = k.startsWith("both");
		const uncombined = ![
			"main",
			"fixmain",
			"sub",
			"textsub"
		].includes(k) && !both && !s.previews[row.id];
		const subNeeded = k === "fixmain" && s.componentStatus.sub.get(row.sub_id) === "missing" ? subIsText(s, row, pair) ? "textsub" : "sub" : null;
		return {
			[buildState || "unbuilt"]: true,
			made: !!pair?.custom && !pair.published,
			changed: !!pair?.published,
			[both ? "main" : k]: true,
			...both ? { [k === "both" ? "sub" : "textsub"]: true } : {},
			...subNeeded ? { [subNeeded]: true } : {},
			uncombined,
			multi: (pair?.subs.length || 0) > 1,
			text: subIsText(s, row, pair)
		};
	}
	function editableDrawing(s, row, role, item) {
		const source = row[role + "_id"];
		const drawings = (s.components?.[role === "main" ? "mains" : "subs"] || []).find((c) => c.id === source || c.source_ids.includes(source))?.drawings || [], k = item?.model_key || item?.key;
		return (k ? drawings.find((d) => d.key === k) : null) || (item?.icon ? drawings.find((d) => d.icon_id === item.icon) : drawings[0]);
	}
	function parts(s, row, flagged) {
		const refs = s.catalog.references, pair = s.pairs.get(row.id);
		const k = key(s, row, flagged), hasMain = ![
			"main",
			"fixmain",
			"both",
			"both-text"
		].includes(k);
		const hasSub = ![
			"sub",
			"textsub",
			"both",
			"both-text"
		].includes(k) && !(k === "fixmain" && s.componentStatus.sub.get(row.sub_id) === "missing");
		if (pair?.mains.length && pair.subs.length && hasMain && hasSub) return {
			pair,
			key: k,
			main: mainOf(pair),
			sub: currentSub(pair),
			ready: true
		};
		const main = (refs[row.main_id]?.generated || []).find((g) => /^(solo|combination_main|main-54)\//.test(g.key));
		const sub = (row.sub_generated ?? refs[row.sub_id]?.generated ?? []).find((g) => /^(sub|text|sub-36)\//.test(g.key));
		return {
			pair,
			key: k,
			main: hasMain && main && {
				icon: main.icon_id,
				preview_url: main.preview_url,
				pending: true
			},
			sub: hasSub && sub && {
				icon: sub.icon_id,
				preview_url: sub.preview_url,
				pending: true
			},
			ready: false
		};
	}
	function state(s, row, p) {
		const k = p.key.startsWith("both") ? "main" : p.key, subMissing = k === "fixmain" && s.componentStatus.sub.get(row.sub_id) === "missing";
		return [
			p.key === "both" ? "Needs main + sub" : p.key === "both-text" ? "Needs main + text sub" : subMissing ? "Fix main + needs sub" : STATES[k],
			{
				ready: "ready",
				fix: "fix",
				fixmain: "fix",
				waiting: "waiting",
				textsub: "info"
			}[k] || "needed",
			STATE_HINTS[k]
		];
	}
	function display(s, row, role, item) {
		const drawing = editableDrawing(s, row, role, item);
		if (item && drawing && item.sha256 === drawing.svg_sha256 && !drawing.preview_url?.includes("/api/icon-artwork/")) return item;
		return drawing ? {
			...item,
			icon: drawing.icon_id,
			key: drawing.key,
			model_key: drawing.key,
			family: drawing.family,
			preview_url: drawing.preview_url,
			document: null,
			pending: item?.pending ?? true
		} : item;
	}
	function matches(s, row, query) {
		const q = query.trim().toLowerCase();
		if (!q) return true;
		const refs = s.catalog.references, pair = s.pairs.get(row.id);
		return [
			row.concept,
			row.id,
			row.main_id,
			row.sub_id,
			refs[row.main_id]?.concept,
			refs[row.sub_id]?.concept,
			...pair ? [...pair.mains, ...pair.subs].map((m) => m.icon) : []
		].join(" ").toLowerCase().includes(q);
	}
	function groups(s, rows, by, flagged) {
		const refs = s.catalog.references, out = /* @__PURE__ */ new Map();
		for (const row of rows) {
			const item = parts(s, row, flagged)[by], sourceId = by === "main" ? row.main_id : row.sub_id;
			const k = item ? by + "/" + item.icon : "needed/" + sourceId;
			if (!out.has(k)) out.set(k, {
				key: k,
				item,
				title: item ? item.icon : refs[sourceId]?.concept || sourceId,
				rows: []
			});
			out.get(k).rows.push(row);
		}
		return [...out.values()].sort((a, b) => b.rows.length - a.rows.length || a.title.localeCompare(b.title));
	}
	//#endregion
	//#region side-pairs/src/lib/inspect.svelte.js
	var NS = "http://www.w3.org/2000/svg";
	var inspect = proxy({
		open: false,
		shown: 0,
		label: "",
		item: null,
		size: 48,
		concept: "",
		view: "both",
		svg: null,
		facts: [],
		error: ""
	});
	var svgEl = (name, attrs) => {
		const e = document.createElementNS(NS, name);
		for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);
		return e;
	};
	async function documentOf(item) {
		if (item.document) return item.document;
		const r = await fetch(item.preview_url, { cache: "no-store" });
		if (!r.ok) throw Error("Artwork unavailable");
		return r.text();
	}
	function inspectSVG(text) {
		const source = new DOMParser().parseFromString(text, "image/svg+xml").documentElement;
		if (source.nodeName !== "svg") throw Error("Artwork is not an SVG");
		const box = (source.getAttribute("viewBox") || `0 0 ${source.getAttribute("width") || 48} ${source.getAttribute("height") || 48}`).split(/[\s,]+/).map(Number), [x, y, w, h] = box;
		const svg = svgEl("svg", {
			viewBox: box.join(" "),
			class: "side-component-canvas",
			role: "img"
		});
		const grid = svgEl("g", { "aria-hidden": "true" });
		for (let i = 0; i <= w; i++) grid.append(svgEl("line", {
			x1: x + i,
			y1: y,
			x2: x + i,
			y2: y + h,
			stroke: i % 8 === 0 ? "#9eb3bd" : "#dae4e9",
			"stroke-width": i % 8 === 0 ? .1 : .045
		}));
		for (let i = 0; i <= h; i++) grid.append(svgEl("line", {
			x1: x,
			y1: y + i,
			x2: x + w,
			y2: y + i,
			stroke: i % 8 === 0 ? "#9eb3bd" : "#dae4e9",
			"stroke-width": i % 8 === 0 ? .1 : .045
		}));
		const art = svgEl("g", { class: "side-component-art" }), line = svgEl("g", {
			class: "side-component-centerline",
			"aria-hidden": "true"
		});
		for (const a of [
			"fill",
			"stroke",
			"stroke-width",
			"stroke-linecap",
			"stroke-linejoin"
		]) if (source.hasAttribute(a)) art.setAttribute(a, source.getAttribute(a));
		if (!art.hasAttribute("stroke")) art.setAttribute("stroke", "currentColor");
		for (const child of [...source.children]) {
			if ([
				"title",
				"desc",
				"metadata"
			].includes(child.localName)) continue;
			art.append(document.importNode(child, true));
		}
		const trace = art.cloneNode(true);
		for (const e of [trace, ...trace.querySelectorAll("*")]) {
			e.removeAttribute("id");
			if (e !== trace && e.getAttribute("fill") && e.getAttribute("fill") !== "none" && !e.hasAttribute("stroke")) continue;
			e.setAttribute("stroke", "#ef4444");
			e.setAttribute("stroke-width", ".3");
			e.setAttribute("fill", "none");
		}
		line.append(...trace.childNodes);
		svg.append(grid, art, line);
		return {
			svg,
			width: w,
			height: h
		};
	}
	var opened = 0;
	async function openInspect(label, item, size, concept, factsOf) {
		const request = ++opened;
		Object.assign(inspect, {
			open: true,
			shown: inspect.shown + 1,
			label,
			item,
			size,
			concept,
			svg: null,
			facts: [],
			error: ""
		});
		try {
			const { svg, width, height } = inspectSVG(await documentOf(item));
			svg.setAttribute("aria-label", `${item.icon} on a ${width} by ${height} grid`);
			if (request === opened) {
				inspect.svg = svg;
				inspect.facts = factsOf(width, height);
			}
		} catch (error) {
			if (request === opened) inspect.error = error.message;
		}
	}
	//#endregion
	//#region side-pairs/src/components/PartFigure.svelte
	var root$8 = /* @__PURE__ */ from_html(`<span class="side-fix-badge"> </span>`);
	var root_1$8 = /* @__PURE__ */ from_html(`<div tabindex="0" role="button"><img loading="lazy"/> <!></div>`);
	var root_2$7 = /* @__PURE__ */ from_html(`<div><span> </span></div>`);
	var root_3$7 = /* @__PURE__ */ from_html(`<figure><!> <figcaption> </figcaption></figure>`);
	function PartFigure($$anchor, $$props) {
		push($$props, true);
		const caption = /* @__PURE__ */ user_derived(() => !$$props.item ? `${$$props.label} · ${$$props.size}×${$$props.size}` : $$props.item.native_text ? `${$$props.label} ${round($$props.item.canvas_width)}×${round($$props.item.canvas_height)} · native` : $$props.item.document ? `${$$props.label} ${round(ink($$props.item, $$props.isSub)[0])}×${round(ink($$props.item, $$props.isSub)[1])} / ${$$props.size}` : `${$$props.label} · generated`);
		const own = /* @__PURE__ */ user_derived(() => ($$props.s.version, $$props.isSub && $$props.item?.document ? subProblems($$props.s, $$props.item, $$props.s.flagged) : []));
		const shown = /* @__PURE__ */ user_derived(() => ($$props.s.version, !get(own).length && $$props.item ? drawingProblems($$props.s, $$props.drawing) : []));
		const problems = /* @__PURE__ */ user_derived(() => get(own).length ? get(own) : get(shown));
		const badge = /* @__PURE__ */ user_derived(() => get(own).length ? "Fix sub" : get(shown).length ? "Fix " + $$props.label.toLowerCase() : "");
		const text = /* @__PURE__ */ user_derived(() => get(shown).length ? `${$$props.label} · ${$$props.drawing.status === "pass" ? "needs fix" : "fails validation"}` : get(caption));
		function factsOf(width, height) {
			const rows = [
				["Pair", $$props.concept],
				["Family", $$props.item.family || $$props.item.model_key?.split("/")[0] || "generated"],
				["Canvas", `${round(width)}×${round(height)}`]
			];
			if ($$props.item.bounds) {
				const [w, h] = ink($$props.item, $$props.isSub);
				rows.push(["Ink", `${round(w)}×${round(h)} / ${$$props.size}`]);
			}
			if ($$props.item.sizing_kind) rows.push(["Sizing", $$props.item.sizing_kind]);
			if ($$props.item.model_validation) rows.push(["Validation", $$props.item.model_validation]);
			if ($$props.item.sub32_status) rows.push(["SUB32 status", $$props.item.sub32_status + ($$props.item.sub32_reason ? " · " + $$props.item.sub32_reason : "")]);
			if ($$props.isSub && $$props.item.document) rows.push(["Problems", subProblems($$props.s, $$props.item, $$props.s.flagged).join(" · ") || "None"]);
			if ($$props.item.pending) rows.push(["Status", "Waiting to combine"]);
			if ($$props.item.python_source) rows.push(["Python model", $$props.item.python_source]);
			if ($$props.item.svg) rows.push(["SVG", $$props.item.svg]);
			return rows;
		}
		const open = () => openInspect($$props.label, $$props.item, $$props.size, $$props.concept, factsOf);
		var figure = root_3$7();
		let classes;
		var node = child(figure);
		var consequent_1 = ($$anchor) => {
			var div = root_1$8();
			var img = child(div);
			var node_1 = sibling(img, 2);
			var consequent = ($$anchor) => {
				var span = root$8();
				var text_1 = only_child(span, true);
				template_effect(($0) => {
					set_attribute(span, "title", $0);
					set_text(text_1, get(badge));
				}, [() => get(problems).join(" · ")]);
				append($$anchor, span);
			};
			if_block(node_1, ($$render) => {
				if (get(badge)) $$render(consequent);
			});
			reset(div);
			template_effect(($0, $1) => {
				set_class(div, 1, "side-part-art side-grid-" + $$props.size + " side-inspectable");
				set_attribute(div, "aria-label", $0);
				set_attribute(img, "src", $1);
				set_attribute(img, "alt", $$props.label + " " + $$props.item.icon);
			}, [() => `Inspect ${$$props.label.toLowerCase()} ${$$props.item.icon}`, () => $$props.item.document ? dataURL($$props.item.document) : $$props.item.preview_url]);
			delegated("click", div, open);
			delegated("keydown", div, (e) => {
				if (e.key === "Enter" || e.key === " ") {
					e.preventDefault();
					open();
				}
			});
			append($$anchor, div);
		};
		var alternate = ($$anchor) => {
			var div_1 = root_2$7();
			var text_2 = only_child(child(div_1));
			reset(div_1);
			template_effect(() => {
				set_class(div_1, 1, "side-part-art side-grid-" + $$props.size + " side-part-missing");
				set_text(text_2, `${$$props.label ?? ""} needed`);
			});
			append($$anchor, div_1);
		};
		if_block(node, ($$render) => {
			if ($$props.item) $$render(consequent_1);
			else $$render(alternate, -1);
		});
		var text_3 = only_child(sibling(node, 2), true);
		reset(figure);
		template_effect(($0) => {
			classes = set_class(figure, 1, "side-part", null, classes, { "needs-fix": get(problems).length > 0 });
			set_attribute(figure, "title", $0);
			set_text(text_3, get(text));
		}, [() => get(problems).join(" · ")]);
		append($$anchor, figure);
		pop();
	}
	delegate(["click", "keydown"]);
	//#endregion
	//#region side-pairs/src/lib/actions.js
	function combinedPopup(image, { concept, result }) {
		if (result) window.SideCombinationPopup?.attach(image, concept, result);
		return { update: (next) => {
			if (next.result) window.SideCombinationPopup?.attach(image, next.concept, next.result);
		} };
	}
	function mountBefore(anchor, make) {
		let node = null;
		const place = (make) => {
			node?.remove();
			node = make?.() || null;
			if (node) anchor.before(node);
		};
		place(make);
		return {
			update: place,
			destroy: () => node?.remove()
		};
	}
	//#endregion
	//#region side-pairs/src/components/CombinedFigure.svelte
	var root$7 = /* @__PURE__ */ from_html(`<span class="side-combined-empty"> </span>`);
	var root_1$7 = /* @__PURE__ */ from_html(`<span class="side-combined-empty">Rendering…</span>`);
	var root_2$6 = /* @__PURE__ */ from_html(`<img width="128" height="128"/>`);
	var root_3$6 = /* @__PURE__ */ from_html(`<img width="128" height="128" role="button" tabindex="0"/>`);
	var root_4$6 = /* @__PURE__ */ from_html(`<div class="side-combined"><!></div>`);
	function CombinedFigure($$anchor, $$props) {
		push($$props, true);
		const found = /* @__PURE__ */ user_derived(() => ($$props.store.version, $$props.store.combined($$props.pair, $$props.sub)));
		user_effect(() => {
			if (!get(found)) $$props.store.requestRender($$props.pair, $$props.sub);
		});
		let note = /* @__PURE__ */ state$1("");
		async function open() {
			try {
				const c = await window.SideData.compose($$props.pair.id);
				window.SideCombinationPopup?.open($$props.pair.concept, {
					...c.result,
					svg: c.svg
				});
			} catch (e) {
				set(note, e.message, true);
			}
		}
		var div = root_4$6();
		var node = child(div);
		var consequent = ($$anchor) => {
			var span = root$7();
			var text = only_child(span, true);
			template_effect(() => set_text(text, get(found).error));
			append($$anchor, span);
		};
		var consequent_1 = ($$anchor) => {
			append($$anchor, root_1$7());
		};
		var consequent_2 = ($$anchor) => {
			var img = root_2$6();
			action(img, ($$node, $$action_arg) => combinedPopup?.($$node, $$action_arg), () => ({
				concept: $$props.pair.concept,
				result: get(found).result
			}));
			template_effect(($0) => {
				set_attribute(img, "src", $0);
				set_attribute(img, "alt", $$props.pair.concept + " — combined");
			}, [() => get(found).url || dataURL(get(found).result.svg)]);
			replay_events(img);
			append($$anchor, img);
		};
		var alternate = ($$anchor) => {
			var img_1 = root_3$6();
			template_effect(() => {
				set_attribute(img_1, "src", get(found).url);
				set_attribute(img_1, "alt", $$props.pair.concept + " — combined");
				set_attribute(img_1, "aria-label", "Inspect " + $$props.pair.concept);
				set_attribute(img_1, "title", get(note));
			});
			delegated("click", img_1, open);
			delegated("keydown", img_1, (e) => {
				if (e.key === "Enter" || e.key === " ") {
					e.preventDefault();
					open();
				}
			});
			append($$anchor, img_1);
		};
		if_block(node, ($$render) => {
			if (get(found)?.error) $$render(consequent);
			else if (!get(found)) $$render(consequent_1, 1);
			else if (get(found).result) $$render(consequent_2, 2);
			else $$render(alternate, -1);
		});
		reset(div);
		append($$anchor, div);
		pop();
	}
	delegate(["click", "keydown"]);
	//#endregion
	//#region side-pairs/src/components/CombinedReview.svelte
	var root$6 = /* @__PURE__ */ from_html(`<span class="side-review side-combined-review"><span class="side-review-chip"><b>Combined</b> </span> <button type="button" class="requires-login" data-action="approve">Approve</button> <button type="button" class="requires-login" data-action="disapprove">Disapprove</button> <span class="side-editor-message" role="status"> </span></span>`);
	function CombinedReview($$anchor, $$props) {
		push($$props, true);
		let store = prop($$props, "store", 7);
		const icon = /* @__PURE__ */ user_derived(() => (store().version, store().item($$props.pair.id)?.icon));
		const status = /* @__PURE__ */ user_derived(() => (store().version, get(icon) ? store().reviews[get(icon).key] || get(icon).review || "ready" : "ready"));
		const waiting = /* @__PURE__ */ user_derived(() => (store().version, [["main", $$props.main], ["sub", $$props.sub]].filter(([, item]) => item && store().reviews[item.model_key] !== "approve").map(([role]) => role)));
		let message = /* @__PURE__ */ state$1("");
		let busy = /* @__PURE__ */ state$1(false);
		async function send(body) {
			set(busy, true);
			set(message, "Saving…");
			try {
				const response = await fetch("/api/reviews", {
					method: "POST",
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify({
						icon: get(icon).key,
						svg_sha256: get(icon).svg_sha256,
						...body
					})
				});
				const data = await response.json().catch(() => ({}));
				if (!response.ok) throw Error(data.error || "Could not save the review.");
				store().reviews[get(icon).key] = body.status;
				set(message, "");
				await store().refresh($$props.pair.id);
			} catch (error) {
				set(message, error.message, true);
			} finally {
				set(busy, false);
			}
		}
		function disapprove() {
			const note = prompt("What needs fixing in the combined icon?");
			if (note) send({
				status: "pending",
				reason: "other",
				feedback: note
			});
		}
		var fragment = comment();
		var node = first_child(fragment);
		var consequent = ($$anchor) => {
			var span = root$6();
			var span_1 = child(span);
			var text = sibling(child(span_1));
			reset(span_1);
			var button = sibling(span_1, 2);
			var button_1 = sibling(button, 2);
			var text_1 = only_child(sibling(button_1, 2), true);
			reset(span);
			template_effect(($0) => {
				set_attribute(span, "data-status", get(status));
				set_text(text, ` ${(REVIEW_LABELS[get(status)] || get(status)) ?? ""}`);
				button.disabled = get(busy) || get(status) === "approve" || get(waiting).length > 0;
				set_attribute(button, "title", $0);
				button_1.disabled = get(busy) || get(status) === "pending";
				set_text(text_1, get(message));
			}, [() => get(waiting).length ? "Approve the " + get(waiting).join(" and ") + " first" : ""]);
			delegated("click", button, () => send({ status: "approve" }));
			delegated("click", button_1, disapprove);
			append($$anchor, span);
		};
		if_block(node, ($$render) => {
			if (get(icon)) $$render(consequent);
		});
		append($$anchor, fragment);
		pop();
	}
	delegate(["click"]);
	//#endregion
	//#region node_modules/svelte/src/reactivity/map.js
	/** @import { Source } from '#client' */
	/**
	* A reactive version of the built-in [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) object.
	* Reading contents of the map (by iterating, or by reading `map.size` or calling `map.get(...)` or `map.has(...)` as in the [tic-tac-toe example](https://svelte.dev/playground/0b0ff4aa49c9443f9b47fe5203c78293) below) in an [effect](https://svelte.dev/docs/svelte/$effect) or [derived](https://svelte.dev/docs/svelte/$derived)
	* will cause it to be re-evaluated as necessary when the map is updated.
	*
	* Note that values in a reactive map are _not_ made [deeply reactive](https://svelte.dev/docs/svelte/$state#Deep-state).
	*
	* ```svelte
	* <script>
	* 	import { SvelteMap } from 'svelte/reactivity';
	* 	import { result } from './game.js';
	*
	* 	let board = new SvelteMap();
	* 	let player = $state('x');
	* 	let winner = $derived(result(board));
	*
	* 	function reset() {
	* 		player = 'x';
	* 		board.clear();
	* 	}
	* <\/script>
	*
	* <div class="board">
	* 	{#each Array(9), i}
	* 		<button
	* 			disabled={board.has(i) || winner}
	* 			onclick={() => {
	* 				board.set(i, player);
	* 				player = player === 'x' ? 'o' : 'x';
	* 			}}
	* 		>{board.get(i)}</button>
	* 	{/each}
	* </div>
	*
	* {#if winner}
	* 	<p>{winner} wins!</p>
	* 	<button onclick={reset}>reset</button>
	* {:else}
	* 	<p>{player} is next</p>
	* {/if}
	* ```
	*
	* @template K
	* @template V
	* @extends {Map<K, V>}
	*/
	var SvelteMap = class extends Map {
		/** @type {Map<K, Source<number>>} */
		#sources = /* @__PURE__ */ new Map();
		#version = /* @__PURE__ */ state$1(0);
		#size = /* @__PURE__ */ state$1(0);
		#update_version = update_version || -1;
		/**
		* @param {Iterable<readonly [K, V]> | null | undefined} [value]
		*/
		constructor(value) {
			super();
			if (value) {
				for (var [key, v] of value) super.set(key, v);
				this.#size.v = super.size;
			}
		}
		/**
		* If the source is being created inside the same reaction as the SvelteMap instance,
		* we use `state` so that it will not be a dependency of the reaction. Otherwise we
		* use `source` so it will be.
		*
		* @template T
		* @param {T} value
		* @returns {Source<T>}
		*/
		#source(value) {
			return update_version === this.#update_version ? /* @__PURE__ */ state$1(value) : source(value);
		}
		/** @param {K} key */
		has(key) {
			var sources = this.#sources;
			var s = sources.get(key);
			if (s === void 0) {
				if (super.has(key)) {
					s = this.#source(0);
					sources.set(key, s);
				} else {
					get(this.#version);
					return false;
				}
			}
			get(s);
			return true;
		}
		/**
		* @param {(value: V, key: K, map: Map<K, V>) => void} callbackfn
		* @param {any} [this_arg]
		*/
		forEach(callbackfn, this_arg) {
			this.#read_all();
			super.forEach(callbackfn, this_arg);
		}
		/** @param {K} key */
		get(key) {
			var sources = this.#sources;
			var s = sources.get(key);
			if (s === void 0) {
				if (super.has(key)) {
					s = this.#source(0);
					sources.set(key, s);
				} else {
					get(this.#version);
					return;
				}
			}
			get(s);
			return super.get(key);
		}
		/**
		* @param {K} key
		* @param {V} value
		* */
		getOrInsert(key, value) {
			if (!super.has(key)) this.set(key, value);
			return this.get(key);
		}
		/**
		* @param {K} key
		* @param {(key: K) => V} callbackFn
		*/
		getOrInsertComputed(key, callbackFn) {
			if (!super.has(key)) this.set(key, callbackFn(key));
			return this.get(key);
		}
		/**
		* @param {K} key
		* @param {V} value
		* */
		set(key, value) {
			var sources = this.#sources;
			var s = sources.get(key);
			var prev_res = super.get(key);
			var res = super.set(key, value);
			var version = this.#version;
			if (s === void 0) {
				s = this.#source(0);
				sources.set(key, s);
				set(this.#size, super.size);
				increment(version);
			} else if (prev_res !== value) {
				increment(s);
				var v_reactions = version.reactions === null ? null : new Set(version.reactions);
				if (v_reactions === null || !s.reactions?.every((r) => v_reactions.has(r))) increment(version);
			}
			return res;
		}
		/** @param {K} key */
		delete(key) {
			var sources = this.#sources;
			var s = sources.get(key);
			var res = super.delete(key);
			if (s !== void 0) {
				sources.delete(key);
				set(s, -1);
			}
			if (res) {
				set(this.#size, super.size);
				increment(this.#version);
			}
			return res;
		}
		clear() {
			if (super.size === 0) return;
			super.clear();
			var sources = this.#sources;
			set(this.#size, 0);
			for (var s of sources.values()) set(s, -1);
			increment(this.#version);
			sources.clear();
		}
		#read_all() {
			get(this.#version);
			var sources = this.#sources;
			if (this.#size.v !== sources.size) {
				for (var key of super.keys()) if (!sources.has(key)) {
					var s = this.#source(0);
					sources.set(key, s);
				}
			}
			for ([, s] of this.#sources) get(s);
		}
		keys() {
			get(this.#version);
			return super.keys();
		}
		values() {
			this.#read_all();
			return super.values();
		}
		entries() {
			this.#read_all();
			return super.entries();
		}
		[Symbol.iterator]() {
			return this.entries();
		}
		get size() {
			get(this.#size);
			return super.size;
		}
	};
	//#endregion
	//#region side-pairs/src/lib/picker.svelte.js
	var POSITIONS = {
		br: "Bottom-right",
		bl: "Bottom-left",
		tr: "Top-right",
		tl: "Top-left",
		ri: "Right",
		le: "Left",
		bo: "Bottom",
		to: "Top"
	};
	var ROLES = {
		main: {
			label: "Main icon",
			family: "solo",
			hint: "A 48×48 solo icon",
			example: "eye"
		},
		sub: {
			label: "Sub icon",
			family: "sub",
			hint: "A 32×32 sub icon",
			example: "light bulb"
		}
	};
	var STATUS = {
		needs_both: ["Needs main + sub drawn", "todo"],
		needs_main: ["Needs main drawn", "todo"],
		needs_sub: ["Needs sub drawn", "todo"],
		waiting: ["On the side page", "drawn"],
		generated: ["Combined", "generated"]
	};
	var TRACK = "primitives.html?view=side&side=made";
	var forms = new SvelteMap();
	var notices = new SvelteMap();
	var pairs = new SvelteMap();
	var pairRequests = /* @__PURE__ */ new Map();
	var size = () => window.SideData?.size() || 64;
	async function readJSON(response, fallback) {
		let data = {};
		try {
			data = await response.json();
		} catch {}
		if (!response.ok) throw Error(data.error || fallback);
		return data;
	}
	var post = async (url, body, fallback) => readJSON(await fetch(url, {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify(body)
	}), fallback);
	var iconURL = (key, sha) => "/api/icon-artwork/svg?" + new URLSearchParams({
		icon: key,
		...sha ? { v: sha.slice(0, 12) } : {}
	});
	var iconName = (i) => i?.icon?.replace(/-/g, " ") || "";
	var partName = (r, role) => r[role + "s"]?.length ? iconName(r[role + "s"][0]) : "to draw: " + (r[role + "_name"] || "?");
	var combinedURL = (uuid, version) => "combination-previews/" + encodeURIComponent(uuid) + ".svg" + (version ? "?v=" + encodeURIComponent(version) : "");
	function pairEntry(item) {
		const part = (role) => item.parts.find((p) => p.role === role) || {}, m = part("main"), s = part("sub");
		const icon = (p) => p.icon ? [{
			icon: p.icon.split("/")[1],
			family: p.icon.split("/")[0],
			model_key: p.icon,
			preview_url: iconURL(p.icon, p.current_sha)
		}] : [];
		const status = !m.icon && !s.icon ? "needs_both" : !m.icon ? "needs_main" : !s.icon ? "needs_sub" : item.state === "built" ? "generated" : "waiting";
		const formKey = (f) => f && !f.native_text ? f.model_key || f.family + "/" + f.icon : null;
		return {
			row: {
				id: item.reference_id,
				position: s.position,
				mains: icon(m),
				subs: icon(s),
				generated: item.icon ? { at: item.icon.svg_sha256 } : null,
				main_name: m.icon ? null : m.draw_name || null,
				sub_name: s.icon ? null : s.draw_name || null,
				forms: {
					main: formKey(m.form),
					sub: formKey(s.form)
				}
			},
			status,
			main: m.icon ? { preview_url: icon(m)[0].preview_url } : null,
			sub: s.icon ? { preview_url: icon(s)[0].preview_url } : null
		};
	}
	function loadPair(uuid) {
		if (pairRequests.has(uuid)) return pairRequests.get(uuid);
		const request = fetch("/api/combinations?" + new URLSearchParams({
			kind: "side",
			size: String(size()),
			q: uuid,
			limit: "5",
			forms: "1"
		}), { cache: "no-store" }).then((r) => r.ok ? r.json() : { items: [] }).catch(() => ({ items: [] })).then((data) => {
			const item = data.items.find((i) => i.reference_id === uuid);
			if (item) pairs.set(uuid, pairEntry(item));
			else pairs.delete(uuid);
		});
		pairRequests.set(uuid, request);
		return request;
	}
	async function findCandidates(role, query) {
		const ask = async (q) => (await readJSON(await fetch("/api/combinations/candidates?" + new URLSearchParams({
			role,
			size: String(size()),
			q
		}), { cache: "no-store" }), "Search failed.")).map((c) => ({
			key: c.key,
			icon_id: c.key.split("/")[1],
			name: c.name,
			approved: c.review === "approve",
			preview_url: iconURL(c.key, c.svg_sha256 || "")
		}));
		const found = await ask(query.trim());
		if (found.length || !query.trim()) return found;
		const seen = /* @__PURE__ */ new Map();
		for (const word of query.toLowerCase().split(/[^a-z0-9]+/).filter((w) => w.length > 2).sort((a, b) => b.length - a.length)) for (const c of await ask(word)) if (!seen.has(c.key)) seen.set(c.key, c);
		return [...seen.values()].slice(0, 40);
	}
	async function savePair(row, body) {
		const id = row.uuid;
		if (body.remove) {
			const saved = pairs.get(id);
			if (row.published && saved) {
				for (const role of ["main", "sub"]) if (saved.row.forms[role]) await post("/api/combinations/parts", {
					reference_id: id,
					role,
					icon: saved.row.forms[role],
					size: size()
				}, "Could not restore the published icons.");
			} else await post("/api/combinations/pair", {
				reference_id: id,
				remove: true
			}, "Could not remove the side pair.");
			return { removed: true };
		}
		if (!pairs.has(id)) await post("/api/combinations/pair", {
			reference_id: id,
			position: body.position || "br"
		}, "Could not make the side pair.");
		for (const role of ["main", "sub"]) if (body[role]) await post("/api/combinations/parts", {
			reference_id: id,
			role,
			icon: body[role],
			size: size()
		}, "Could not save the " + role + ".");
		else if (body[role + "_name"] !== void 0) await post("/api/combinations/parts", {
			reference_id: id,
			role,
			draw_name: body[role + "_name"] || null,
			size: size()
		}, "Could not save the " + role + " to draw.");
		let got = await window.SideData?.refresh(id);
		const sub = got?.item.parts.find((p) => p.role === "sub");
		if (got && body.position && sub?.position !== body.position && got.item.parts.every((p) => p.icon || p.form?.native_text)) {
			const composed = await window.SideData.compose(id, { position: body.position });
			const [built] = await window.SideData.build([composed.request]);
			if (!built?.ok) throw Error(built?.error || "Could not save the side.");
			got = await window.SideData.refresh(id);
		}
		const entry = got ? pairEntry(got.item) : null;
		if (entry) pairs.set(id, entry);
		return entry ? {
			pair: entry.row,
			status: entry.status
		} : {
			pair: {
				id,
				position: body.position,
				mains: [],
				subs: []
			},
			status: "needs_both"
		};
	}
	function pairBody(form) {
		const part = (role) => form.draw[role] !== null ? { [role + "_name"]: form.draw[role].trim() } : form[role] && form[role] !== form.saved?.[role] ? { [role]: form[role] } : {};
		return {
			...part("main"),
			...part("sub"),
			position: form.position
		};
	}
	async function openForm(row) {
		await loadPair(row.uuid);
		const saved = pairs.get(row.uuid), r = saved?.row;
		notices.delete(row.uuid);
		const form = proxy({
			uuid: row.uuid,
			loaded: false,
			busy: false,
			message: "",
			main: "",
			sub: "",
			position: r?.position || row.position || "",
			queries: {
				main: "",
				sub: ""
			},
			candidates: {
				main: [],
				sub: []
			},
			chosen: {
				main: null,
				sub: null
			},
			draw: {
				main: null,
				sub: null
			},
			brief: {
				main: "",
				sub: ""
			},
			saved: {},
			sub_position: null
		});
		for (const role of ["main", "sub"]) {
			const i = r?.[role + "s"]?.[0];
			if (i) {
				form[role] = form.saved[role] = i.model_key;
				form.chosen[role] = {
					key: i.model_key,
					icon_id: i.icon,
					name: iconName(i),
					preview_url: saved?.[role]?.preview_url || i.preview_url
				};
			} else if (r?.[role + "_name"]) form.draw[role] = r[role + "_name"];
		}
		forms.set(row.uuid, form);
		try {
			const status = (await fetch("/api/primitives/status", { cache: "no-store" }).then((x) => x.ok ? x.json() : {}).catch(() => ({})))[row.uuid] || {};
			const brief = (b) => typeof b === "string" ? (() => {
				try {
					return JSON.parse(b);
				} catch {
					return { name: b };
				}
			})() : b;
			for (const role of ["main", "sub"]) {
				const name = brief(status[role + "_brief"])?.name || row.current?.[role]?.name || (r?.[role + "s"]?.[0] ? iconName(r[role + "s"][0]) : "");
				form.queries[role] = form.brief[role] = name || "";
				form.candidates[role] = await findCandidates(role, form.queries[role]);
				const now = !r && row.current?.[role];
				if (now) {
					form[role] = now.key;
					form.chosen[role] = now;
				} else if (!r && form.candidates[role][0]) {
					form[role] = form.candidates[role][0].key;
					form.chosen[role] = form.candidates[role][0];
				}
			}
			form.position ||= {
				"bottom-right": "br",
				"bottom-left": "bl",
				"top-right": "tr",
				"top-left": "tl",
				right: "ri",
				left: "le",
				bottom: "bo",
				top: "to"
			}[status.sub_position] || "";
			form.sub_position = status.sub_position;
		} catch (error) {
			form.message = error.message;
		}
		form.loaded = true;
	}
	async function send(row, form, body, working) {
		form.busy = true;
		form.message = working;
		try {
			return await savePair(row, body);
		} catch (error) {
			form.message = error.message;
			return null;
		} finally {
			form.busy = false;
		}
	}
	//#endregion
	//#region side-pairs/src/components/PairPicker.svelte
	var root$5 = /* @__PURE__ */ from_html(`<p class="muted">Finding the main and sub icons…</p>`);
	var root_1$6 = /* @__PURE__ */ from_html(`<div class="side-pair-chosen to-draw"><span>To draw:</span> <input maxlength="120"/></div> <button type="button">Pick an existing icon instead</button>`, 1);
	var root_2$5 = /* @__PURE__ */ from_html(`<img alt=""/>`);
	var root_3$5 = /* @__PURE__ */ from_html(`<!> <span> </span>`, 1);
	var root_4$5 = /* @__PURE__ */ from_html(`<span class="muted">Nothing chosen yet: click an icon below.</span>`);
	var root_5$5 = /* @__PURE__ */ from_html(`<img alt="" loading="lazy"/>`);
	var root_6$5 = /* @__PURE__ */ from_html(`<span class="badge generated">Approved</span>`);
	var root_7$4 = /* @__PURE__ */ from_html(`<span class="badge failed">Fails</span>`);
	var root_8$2 = /* @__PURE__ */ from_html(`<button type="button"><!> <span> </span> <!></button>`);
	var root_9$2 = /* @__PURE__ */ from_html(`<span class="muted"> </span>`);
	var root_10$2 = /* @__PURE__ */ from_html(`<div class="side-pair-chosen"><!></div> <input type="search"/> <div class="side-pair-candidates"></div> <button type="button" class="side-pair-none">None of these: it needs drawing</button>`, 1);
	var root_11$2 = /* @__PURE__ */ from_html(`<div class="side-pair-role"><strong> </strong><span class="muted"> </span> <!></div>`);
	var root_12$2 = /* @__PURE__ */ from_html(`<option> </option>`);
	var root_13$2 = /* @__PURE__ */ from_html(`<p class="muted">Classified as center: a side pair needs one of the eight side positions.</p>`);
	var root_14$2 = /* @__PURE__ */ from_html(`<button type="button"> </button>`);
	var root_15$2 = /* @__PURE__ */ from_html(`<!> <label>Sub position <select><option>Choose…</option><!></select></label> <!> <div class="side-pair-actions"><button type="button" class="primary">Save</button> <button type="button">Close</button> <!></div>`, 1);
	var root_16$2 = /* @__PURE__ */ from_html(`<p class="side-pair-message" role="status"> </p>`);
	var root_17$2 = /* @__PURE__ */ from_html(`<div class="side-pair-form"><!></div> <!>`, 1);
	function PairPicker($$anchor, $$props) {
		push($$props, true);
		let onSaved = prop($$props, "onSaved", 3, null);
		const form = /* @__PURE__ */ user_derived(() => forms.get($$props.row.uuid));
		let timers = {};
		function search(role, value) {
			get(form).queries[role] = value;
			clearTimeout(timers[role]);
			timers[role] = setTimeout(async () => {
				const query = value;
				try {
					const candidates = await findCandidates(role, query);
					if (get(form).queries[role] === query) get(form).candidates[role] = candidates;
				} catch (error) {
					get(form).message = error.message;
				}
			}, 250);
		}
		function choose(role, c) {
			get(form)[role] = c.key;
			get(form).chosen[role] = c;
			get(form).draw[role] = null;
		}
		async function save() {
			const data = await send($$props.row, get(form), pairBody(get(form)), "Saving…");
			if (!data) return;
			if (data.pair && !pairs.has($$props.row.uuid)) pairs.set($$props.row.uuid, {
				row: data.pair,
				status: data.status
			});
			forms.delete($$props.row.uuid);
			if (onSaved()) {
				onSaved()(data);
				return;
			}
			notices.set($$props.row.uuid, data.status === "waiting" ? "Saved to Side combination. Combine it there. " : "Saved to Side combination. It waits there until the " + (data.status === "needs_both" ? "main and sub are" : data.status === "needs_main" ? "main is" : "sub is") + " drawn. ");
		}
		async function remove() {
			if (!await send($$props.row, get(form), { remove: true }, "Removing…")) return;
			pairs.delete($$props.row.uuid);
			if (onSaved()) {
				forms.delete($$props.row.uuid);
				onSaved()({ removed: true });
				return;
			}
			get(form).message = "Removed.";
		}
		var fragment = comment();
		var node = first_child(fragment);
		var consequent_10 = ($$anchor) => {
			var fragment_1 = root_17$2();
			var div = first_child(fragment_1);
			var node_1 = child(div);
			var consequent = ($$anchor) => {
				append($$anchor, root$5());
			};
			var alternate_2 = ($$anchor) => {
				var fragment_2 = root_15$2();
				var node_2 = first_child(fragment_2);
				each(node_2, 16, () => ["main", "sub"], (role) => role, ($$anchor, role) => {
					const info = /* @__PURE__ */ user_derived(() => ROLES[role]);
					var div_1 = root_11$2();
					var strong = child(div_1);
					var text = only_child(strong, true);
					var span = sibling(strong);
					var text_1 = only_child(span);
					var node_3 = sibling(span, 2);
					var consequent_1 = ($$anchor) => {
						var fragment_3 = root_1$6();
						var div_2 = first_child(fragment_3);
						var input = sibling(child(div_2), 2);
						remove_input_defaults(input);
						reset(div_2);
						var button = sibling(div_2, 2);
						template_effect(() => {
							set_attribute(input, "placeholder", "Name of the " + role + " icon to draw");
							set_attribute(input, "aria-label", "Name of the " + role + " icon to draw");
						});
						bind_value(input, () => get(form).draw[role], ($$value) => get(form).draw[role] = $$value);
						delegated("click", button, () => {
							get(form).draw[role] = null;
						});
						append($$anchor, fragment_3);
					};
					var alternate_1 = ($$anchor) => {
						var fragment_4 = root_10$2();
						var div_3 = first_child(fragment_4);
						var node_4 = child(div_3);
						var consequent_3 = ($$anchor) => {
							var fragment_5 = root_3$5();
							var node_5 = first_child(fragment_5);
							var consequent_2 = ($$anchor) => {
								var img = root_2$5();
								template_effect(() => set_attribute(img, "src", get(form).chosen[role].preview_url));
								append($$anchor, img);
							};
							if_block(node_5, ($$render) => {
								if (get(form).chosen[role].preview_url) $$render(consequent_2);
							});
							var text_2 = only_child(sibling(node_5, 2), true);
							template_effect(() => set_text(text_2, get(form).chosen[role].name || get(form).chosen[role].icon_id));
							append($$anchor, fragment_5);
						};
						var alternate = ($$anchor) => {
							append($$anchor, root_4$5());
						};
						if_block(node_4, ($$render) => {
							if (get(form).chosen[role]) $$render(consequent_3);
							else $$render(alternate, -1);
						});
						reset(div_3);
						var input_1 = sibling(div_3, 2);
						remove_input_defaults(input_1);
						var div_4 = sibling(input_1, 2);
						each(div_4, 21, () => get(form).candidates[role] || [], (c) => c.key, ($$anchor, c) => {
							var button_1 = root_8$2();
							var node_6 = child(button_1);
							var consequent_4 = ($$anchor) => {
								var img_1 = root_5$5();
								template_effect(() => set_attribute(img_1, "src", get(c).preview_url));
								append($$anchor, img_1);
							};
							if_block(node_6, ($$render) => {
								if (get(c).preview_url) $$render(consequent_4);
							});
							var span_3 = sibling(node_6, 2);
							var text_3 = only_child(span_3, true);
							var node_7 = sibling(span_3, 2);
							var consequent_5 = ($$anchor) => {
								append($$anchor, root_6$5());
							};
							var consequent_6 = ($$anchor) => {
								append($$anchor, root_7$4());
							};
							if_block(node_7, ($$render) => {
								if (get(c).approved) $$render(consequent_5);
								else if (get(c).build_failed) $$render(consequent_6, 1);
							});
							reset(button_1);
							template_effect(() => {
								set_class(button_1, 1, "side-pair-candidate" + (!get(form).draw[role] && get(form)[role] === get(c).key ? " chosen" : ""));
								set_attribute(button_1, "title", get(c).icon_id + (get(c).build_failed ? " · fails the build check" : "") + (get(c).approved ? " · approved" : ""));
								set_text(text_3, get(c).name || get(c).icon_id);
							});
							delegated("click", button_1, () => choose(role, get(c)));
							append($$anchor, button_1);
						}, ($$anchor) => {
							var span_6 = root_9$2();
							var text_4 = only_child(span_6, true);
							template_effect(() => set_text(text_4, get(form).queries[role] ? "No " + get(info).family + " icon matches “" + get(form).queries[role] + "”." : "Type a name to search."));
							append($$anchor, span_6);
						});
						reset(div_4);
						var button_2 = sibling(div_4, 2);
						template_effect(($0) => {
							set_attribute(div_3, "title", get(form).chosen[role]?.icon_id || "");
							set_value(input_1, get(form).queries[role]);
							set_attribute(input_1, "placeholder", "Search by name, e.g. " + get(info).example);
							set_attribute(input_1, "aria-label", $0);
						}, [() => "Search " + get(info).label.toLowerCase()]);
						delegated("input", input_1, (e) => search(role, e.currentTarget.value));
						delegated("click", button_2, () => {
							get(form).draw[role] = get(form).brief[role] || get(form).queries[role] || "";
						});
						append($$anchor, fragment_4);
					};
					if_block(node_3, ($$render) => {
						if (get(form).draw[role] !== null) $$render(consequent_1);
						else $$render(alternate_1, -1);
					});
					reset(div_1);
					template_effect(() => {
						set_text(text, get(info).label);
						set_text(text_1, ` · ${get(info).hint ?? ""}`);
					});
					append($$anchor, div_1);
				});
				var label = sibling(node_2, 2);
				var select = sibling(child(label));
				var option = child(select);
				option.value = option.__value = "";
				each(sibling(option), 17, () => Object.entries(POSITIONS), ([k, v]) => k, ($$anchor, $$item) => {
					var $$array = /* @__PURE__ */ user_derived(() => to_array(get($$item), 2));
					let k = () => get($$array)[0];
					let v = () => get($$array)[1];
					var option_1 = root_12$2();
					var text_5 = only_child(option_1, true);
					var option_1_value = {};
					template_effect(() => {
						set_text(text_5, v());
						if (option_1_value !== (option_1_value = k())) option_1.value = (option_1.__value = option_1_value) ?? "";
					});
					append($$anchor, option_1);
				});
				reset(select);
				init_select(select);
				reset(label);
				var node_9 = sibling(label, 2);
				var consequent_7 = ($$anchor) => {
					append($$anchor, root_13$2());
				};
				if_block(node_9, ($$render) => {
					if (get(form).sub_position === "center") $$render(consequent_7);
				});
				var div_5 = sibling(node_9, 2);
				var button_3 = child(div_5);
				var button_4 = sibling(button_3, 2);
				var node_10 = sibling(button_4, 2);
				var consequent_8 = ($$anchor) => {
					var button_5 = root_14$2();
					var text_6 = only_child(button_5, true);
					template_effect(() => {
						button_5.disabled = get(form).busy;
						set_text(text_6, $$props.row.published ? "Use published main / sub" : "Remove pair");
					});
					delegated("click", button_5, remove);
					append($$anchor, button_5);
				};
				var d = /* @__PURE__ */ user_derived(() => pairs.has($$props.row.uuid));
				if_block(node_10, ($$render) => {
					if (get(d)) $$render(consequent_8);
				});
				reset(div_5);
				template_effect(() => button_3.disabled = get(form).busy);
				bind_select_value(select, () => get(form).position, ($$value) => get(form).position = $$value);
				delegated("click", button_3, save);
				delegated("click", button_4, () => forms.delete($$props.row.uuid));
				append($$anchor, fragment_2);
			};
			if_block(node_1, ($$render) => {
				if (!get(form).loaded) $$render(consequent);
				else $$render(alternate_2, -1);
			});
			reset(div);
			var node_11 = sibling(div, 2);
			var consequent_9 = ($$anchor) => {
				var p_2 = root_16$2();
				var text_7 = only_child(p_2, true);
				template_effect(() => set_text(text_7, get(form).message));
				append($$anchor, p_2);
			};
			if_block(node_11, ($$render) => {
				if (get(form).message) $$render(consequent_9);
			});
			append($$anchor, fragment_1);
		};
		if_block(node, ($$render) => {
			if (get(form)) $$render(consequent_10);
		});
		append($$anchor, fragment);
		pop();
	}
	delegate(["click", "input"]);
	//#endregion
	//#region side-pairs/src/components/PairRow.svelte
	var root$4 = /* @__PURE__ */ from_html(`<span class="side-state info">Text sub</span>`);
	var root_1$5 = /* @__PURE__ */ from_html(`<span class="side-state info">Main / sub changed</span>`);
	var root_2$4 = /* @__PURE__ */ from_html(`<span class="side-state info">From review</span>`);
	var root_3$4 = /* @__PURE__ */ from_html(`<span class="side-state info"> </span>`);
	var root_4$4 = /* @__PURE__ */ from_html(`<span class="side-state info" title="Main / sub positions and sizes were set by hand.">Adjusted layout</span>`);
	var root_5$4 = /* @__PURE__ */ from_html(`<span class="side-state info">Outdated: recombine</span>`);
	var root_6$4 = /* @__PURE__ */ from_html(`<img loading="lazy"/>`);
	var root_7$3 = /* @__PURE__ */ from_html(`<span class="side-combined-empty">Reference missing</span>`);
	var root_8$1 = /* @__PURE__ */ from_html(`<p class="side-step-name"> </p>`);
	var root_9$1 = /* @__PURE__ */ from_html(`<div class="requires-login"><button type="button" class="side-edit-component"> </button> <p class="side-editor-message" role="status"> </p></div>`);
	var root_10$1 = /* @__PURE__ */ from_html(`<div class="side-step"><p class="side-step-label"> </p> <!> <!> <!> <!></div>`);
	var root_11$1 = /* @__PURE__ */ from_html(`<div class="side-combined"><span class="side-combined-empty">Not combined yet</span></div>`);
	var root_12$1 = /* @__PURE__ */ from_html(`<div class="requires-login"><button type="button" class="side-edit-component" title="Use the latest saved main and sub with automatic placement"> </button> <p class="side-editor-message" role="status"> </p></div> <p class="login-prompt"><a href="login.html">Log in</a> to recombine this icon or adjust its layout.</p> <button type="button" class="side-layout-open" title="Move and resize the main, the sub or chosen elements, snapped to the grid">Edit layout</button>`, 1);
	var root_13$1 = /* @__PURE__ */ from_html(`<button type="button" class="login-only">Change main / sub</button>`);
	var root_14$1 = /* @__PURE__ */ from_html(`<div class="component-brief side-pair side-pair-editor"><!></div>`);
	var root_15$1 = /* @__PURE__ */ from_html(`<span hidden=""></span>`);
	var root_16$1 = /* @__PURE__ */ from_html(`<span hidden=""></span> <span hidden=""></span>`, 1);
	var root_17$1 = /* @__PURE__ */ from_html(`<div class="pair-card-actions"><!> <!> <!></div>`);
	var root_18$1 = /* @__PURE__ */ from_html(`<article class="side-row"><div class="side-row-head"><h3> </h3> <span class="side-meta"> </span> <span> </span> <!> <!> <!> <!> <!></div> <div class="side-steps"><div class="side-step"><p class="side-step-label">Original</p> <div class="side-original"><!></div></div> <!> <div class="side-step"><p class="side-step-label"> </p> <!> <!></div></div> <!> <!></article>`);
	function PairRow($$anchor, $$props) {
		push($$props, true);
		const view = /* @__PURE__ */ user_derived(() => {
			$$props.store.version;
			const p = parts($$props.store, $$props.row, $$props.store.flagged), { pair, main, sub } = p;
			const [label, tone, hint] = state($$props.store, $$props.row, p);
			return {
				p,
				pair,
				main,
				sub,
				label,
				tone,
				hint,
				changed: p.ready && $$props.store.previews[pair.id]?.built ? $$props.store.staleRoles(pair.id) : [],
				shownMain: display($$props.store, $$props.row, "main", main),
				shownSub: display($$props.store, $$props.row, "sub", sub),
				ref: $$props.store.catalog.references[$$props.row.id],
				adjusted: p.ready && !!$$props.store.handLayout(pair.id),
				text: subIsText($$props.store, $$props.row, pair),
				mainDrawing: editableDrawing($$props.store, $$props.row, "main", main),
				subDrawing: editableDrawing($$props.store, $$props.row, "sub", sub)
			};
		});
		const sizes = /* @__PURE__ */ user_derived(() => ($$props.store.version, $$props.store.sizes()));
		let message = /* @__PURE__ */ state$1("");
		let recombining = /* @__PURE__ */ state$1(false);
		let editMessage = proxy({
			main: "",
			sub: ""
		});
		async function recombine() {
			set(recombining, true);
			set(message, "");
			try {
				const done = await window.SideData.buildPairs([get(view).pair.id]), result = done.results[0];
				if (done.skipped.length) throw Error(done.skipped[0].error);
				if (!result.ok) throw Error(result.error);
				set(message, window.SideData.outcome(result), true);
				await $$props.store.refresh(get(view).pair.id);
			} catch (error) {
				set(message, error.message, true);
			} finally {
				set(recombining, false);
			}
		}
		async function editIcon(role, drawing) {
			editMessage[role] = "";
			try {
				await window.SideComponentEditor.open(drawing, `${role === "main" ? "Main" : "Sub"} · ${drawing.icon_id}`);
			} catch (error) {
				editMessage[role] = error.message;
			}
		}
		const pickerRow = /* @__PURE__ */ user_derived(() => {
			const { pair, main, sub } = get(view);
			if (!pair || pair.native_text) return null;
			const current = (item, family) => {
				const key = item ? item.model_key || item.key || item.family + "/" + item.icon : "";
				return key?.startsWith(family + "/") ? {
					key,
					icon_id: item.icon,
					name: item.icon.replace(/-/g, " "),
					preview_url: item.document ? dataURL(item.document) : item.preview_url
				} : null;
			};
			const published = !pair.custom || !!pair.published;
			return {
				uuid: $$props.row.id,
				concept: $$props.row.concept,
				published,
				position: pair.position,
				current: published && !pair.custom ? {
					main: current(main, "solo"),
					sub: current(sub, "sub")
				} : null
			};
		});
		const reviewItem = (role, item) => {
			const d = editableDrawing($$props.store, $$props.row, role, item);
			return d ? {
				...item,
				model_key: d.key,
				sha256: d.svg_sha256
			} : item;
		};
		const download = /* @__PURE__ */ user_derived(() => ($$props.store.version, get(view).p.ready ? $$props.store.combined(get(view).pair, get(view).sub) : null));
		var article = root_18$1();
		var div = child(article);
		var h3 = child(div);
		var text = only_child(h3, true);
		var span = sibling(h3, 2);
		var text_1 = only_child(span);
		var span_1 = sibling(span, 2);
		var text_2 = only_child(span_1, true);
		var node = sibling(span_1, 2);
		var consequent = ($$anchor) => {
			append($$anchor, root$4());
		};
		if_block(node, ($$render) => {
			if (get(view).text) $$render(consequent);
		});
		var node_1 = sibling(node, 2);
		var consequent_1 = ($$anchor) => {
			var span_3 = root_1$5();
			template_effect(() => set_attribute(span_3, "title", "The published main / sub was changed here: " + $$props.row.main_id + " + " + $$props.row.sub_id + "."));
			append($$anchor, span_3);
		};
		var consequent_2 = ($$anchor) => {
			var span_4 = root_2$4();
			template_effect(() => set_attribute(span_4, "title", "Made from a combination primitive on the review page: " + $$props.row.main_id + " + " + $$props.row.sub_id + "."));
			append($$anchor, span_4);
		};
		if_block(node_1, ($$render) => {
			if (get(view).pair?.published) $$render(consequent_1);
			else if (get(view).pair?.custom) $$render(consequent_2, 1);
		});
		var node_2 = sibling(node_1, 2);
		var consequent_3 = ($$anchor) => {
			var span_5 = root_3$4();
			var text_3 = only_child(span_5);
			template_effect(() => set_text(text_3, `${get(view).pair.mains.length ?? ""} mains · showing first`));
			append($$anchor, span_5);
		};
		if_block(node_2, ($$render) => {
			if (get(view).pair?.mains.length > 1) $$render(consequent_3);
		});
		var node_3 = sibling(node_2, 2);
		var consequent_4 = ($$anchor) => {
			append($$anchor, root_4$4());
		};
		if_block(node_3, ($$render) => {
			if (get(view).adjusted) $$render(consequent_4);
		});
		var node_4 = sibling(node_3, 2);
		var consequent_5 = ($$anchor) => {
			var span_7 = root_5$4();
			template_effect(($0) => set_attribute(span_7, "title", $0), [() => `The ${get(view).changed.join(" and ")} changed after this icon was combined. Use Recombine this icon (or Adjust layout) to rebuild it from the current drawings.`]);
			append($$anchor, span_7);
		};
		if_block(node_4, ($$render) => {
			if (get(view).p.ready && get(view).changed.length) $$render(consequent_5);
		});
		reset(div);
		var div_1 = sibling(div, 2);
		var div_2 = child(div_1);
		var div_3 = sibling(child(div_2), 2);
		var node_5 = child(div_3);
		var consequent_6 = ($$anchor) => {
			var img = root_6$4();
			template_effect(() => {
				set_attribute(img, "src", get(view).ref.reference_url);
				set_attribute(img, "alt", $$props.row.concept + " — original");
			});
			append($$anchor, img);
		};
		var alternate = ($$anchor) => {
			append($$anchor, root_7$3());
		};
		if_block(node_5, ($$render) => {
			if (get(view).ref?.reference_url) $$render(consequent_6);
			else $$render(alternate, -1);
		});
		reset(div_3);
		reset(div_2);
		var node_6 = sibling(div_2, 2);
		each(node_6, 17, () => [[
			"main",
			get(view).shownMain,
			get(view).mainDrawing,
			get(sizes).main
		], [
			"sub",
			get(view).shownSub,
			get(view).subDrawing,
			get(sizes).sub
		]], ([role, item, drawing, size]) => role, ($$anchor, $$item) => {
			var $$array = /* @__PURE__ */ user_derived(() => to_array(get($$item), 4));
			let role = () => get($$array)[0];
			let item = () => get($$array)[1];
			let drawing = () => get($$array)[2];
			let size = () => get($$array)[3];
			var div_4 = root_10$1();
			var p_1 = child(div_4);
			var text_4 = only_child(p_1, true);
			var node_7 = sibling(p_1, 2);
			{
				let $0 = /* @__PURE__ */ user_derived(() => role() === "main" ? "Main" : "Sub");
				let $1 = /* @__PURE__ */ user_derived(() => role() === "sub");
				PartFigure(node_7, {
					get s() {
						return $$props.store;
					},
					get label() {
						return get($0);
					},
					get item() {
						return item();
					},
					get size() {
						return size();
					},
					get isSub() {
						return get($1);
					},
					get drawing() {
						return drawing();
					},
					get concept() {
						return $$props.row.concept;
					}
				});
			}
			var node_8 = sibling(node_7, 2);
			var consequent_7 = ($$anchor) => {
				var p_2 = root_8$1();
				var text_5 = only_child(p_2, true);
				template_effect(() => set_text(text_5, item().icon));
				append($$anchor, p_2);
			};
			if_block(node_8, ($$render) => {
				if (item()?.icon) $$render(consequent_7);
			});
			var node_9 = sibling(node_8, 2);
			var consequent_8 = ($$anchor) => {
				var p_3 = root_8$1();
				var text_6 = only_child(p_3);
				template_effect(() => set_text(text_6, `To draw: ${get(view).pair[role() + "_name"] ?? ""}`));
				append($$anchor, p_3);
			};
			if_block(node_9, ($$render) => {
				if (get(view).pair && !get(view).pair[role() + "s"].length && get(view).pair[role() + "_name"]) $$render(consequent_8);
			});
			var node_10 = sibling(node_9, 2);
			var consequent_9 = ($$anchor) => {
				var div_5 = root_9$1();
				var button = child(div_5);
				var text_7 = only_child(button);
				var text_8 = only_child(sibling(button, 2), true);
				reset(div_5);
				template_effect(() => {
					set_text(text_7, `Edit ${role() ?? ""} icon`);
					set_text(text_8, editMessage[role()]);
				});
				delegated("click", button, () => editIcon(role(), drawing()));
				append($$anchor, div_5);
			};
			if_block(node_10, ($$render) => {
				if (drawing() && drawing().profile !== "TEXT_NATIVE_V2" && window.SideComponentEditor) $$render(consequent_9);
			});
			reset(div_4);
			template_effect(() => set_text(text_4, role() === "sub" && get(view).sub?.native_text ? "Sub · native" : (role() === "main" ? "Main · " : "Sub · ") + size()));
			append($$anchor, div_4);
		});
		var div_6 = sibling(node_6, 2);
		var p_5 = child(div_6);
		var text_9 = only_child(p_5, true);
		var node_11 = sibling(p_5, 2);
		var consequent_10 = ($$anchor) => {
			CombinedFigure($$anchor, {
				get store() {
					return $$props.store;
				},
				get pair() {
					return get(view).pair;
				},
				get sub() {
					return get(view).sub;
				}
			});
		};
		var alternate_1 = ($$anchor) => {
			append($$anchor, root_11$1());
		};
		if_block(node_11, ($$render) => {
			if (get(view).p.ready) $$render(consequent_10);
			else $$render(alternate_1, -1);
		});
		var node_12 = sibling(node_11, 2);
		var consequent_11 = ($$anchor) => {
			var fragment_1 = root_12$1();
			var div_8 = first_child(fragment_1);
			var button_1 = child(div_8);
			var text_10 = only_child(button_1, true);
			var text_11 = only_child(sibling(button_1, 2), true);
			reset(div_8);
			var button_2 = sibling(div_8, 4);
			template_effect(() => {
				button_1.disabled = get(recombining);
				set_text(text_10, get(recombining) ? "Recombining…" : get(view).changed.length ? "Recombine (outdated)" : "Recombine this icon");
				set_text(text_11, get(message));
			});
			delegated("click", button_1, recombine);
			delegated("click", button_2, () => $$props.editor.show(get(view).pair, get(view).main, get(view).sub, () => $$props.store.refresh(get(view).pair.id), $$props.store.handLayout(get(view).pair.id)));
			append($$anchor, fragment_1);
		};
		if_block(node_12, ($$render) => {
			if (get(view).p.ready && !get(view).pair.mapped_native) $$render(consequent_11);
		});
		reset(div_6);
		reset(div_1);
		var node_13 = sibling(div_1, 2);
		var consequent_13 = ($$anchor) => {
			var div_9 = root_14$1();
			var node_14 = child(div_9);
			var consequent_12 = ($$anchor) => {
				PairPicker($$anchor, {
					get row() {
						return get(pickerRow);
					},
					onSaved: () => $$props.store.refresh($$props.row.id)
				});
			};
			var d_1 = /* @__PURE__ */ user_derived(() => forms.get($$props.row.id));
			var alternate_2 = ($$anchor) => {
				var button_3 = root_13$1();
				delegated("click", button_3, () => openForm(get(pickerRow)));
				append($$anchor, button_3);
			};
			if_block(node_14, ($$render) => {
				if (get(d_1)) $$render(consequent_12);
				else $$render(alternate_2, -1);
			});
			reset(div_9);
			append($$anchor, div_9);
		};
		if_block(node_13, ($$render) => {
			if (get(pickerRow)) $$render(consequent_13);
		});
		var node_15 = sibling(node_13, 2);
		var consequent_16 = ($$anchor) => {
			var div_10 = root_17$1();
			var node_16 = child(div_10);
			var consequent_14 = ($$anchor) => {
				var span_9 = root_15$1();
				action(span_9, ($$node, $$action_arg) => mountBefore?.($$node, $$action_arg), () => () => {
					const a = document.createElement("a");
					a.href = get(download).url || dataURL(get(download).result.svg);
					a.download = get(view).pair.id + ".svg";
					return window.SideRepairFlags?.download(a) || a;
				});
				append($$anchor, span_9);
			};
			if_block(node_16, ($$render) => {
				if (get(download)?.url || get(download)?.result?.svg) $$render(consequent_14);
			});
			var node_17 = sibling(node_16, 2);
			var consequent_15 = ($$anchor) => {
				var fragment_3 = root_16$1();
				var span_10 = first_child(fragment_3);
				action(span_10, ($$node, $$action_arg) => mountBefore?.($$node, $$action_arg), () => () => window.SideRepairFlags.button("main", reviewItem("main", get(view).main), get(view).pair));
				action(sibling(span_10, 2), ($$node, $$action_arg) => mountBefore?.($$node, $$action_arg), () => () => window.SideRepairFlags.button("sub", reviewItem("sub", get(view).sub), get(view).pair));
				append($$anchor, fragment_3);
			};
			if_block(node_17, ($$render) => {
				if (window.SideRepairFlags && !get(view).pair.native_text) $$render(consequent_15);
			});
			CombinedReview(sibling(node_17, 2), {
				get store() {
					return $$props.store;
				},
				get pair() {
					return get(view).pair;
				},
				get main() {
					return get(view).main;
				},
				get sub() {
					return get(view).sub;
				}
			});
			reset(div_10);
			append($$anchor, div_10);
		};
		if_block(node_15, ($$render) => {
			if (get(view).p.ready) $$render(consequent_16);
		});
		reset(article);
		template_effect(($0) => {
			set_attribute(article, "data-pair-id", $$props.row.id);
			set_text(text, $$props.row.concept);
			set_text(text_1, `${(POSITIONS$1[get(view).pair?.position] || get(view).pair?.position || "Side") ?? ""} · ${$0 ?? ""}`);
			set_class(span_1, 1, "side-state " + get(view).tone);
			set_attribute(span_1, "title", get(view).hint);
			set_text(text_2, get(view).label);
			set_text(text_9, get(view).pair?.native_text ? "Combined · native" : "Combined · " + get(sizes).canvas);
		}, [() => get(view).pair?.native_text ? `${round(get(view).pair.canvas_width)}×${round(get(view).pair.canvas_height)}` : `${get(sizes).canvas}×${get(sizes).canvas}`]);
		append($$anchor, article);
		pop();
	}
	delegate(["click"]);
	//#endregion
	//#region side-pairs/src/components/GroupSection.svelte
	var root$3 = /* @__PURE__ */ from_html(`<img alt="" loading="lazy"/>`);
	var root_1$4 = /* @__PURE__ */ from_html(`<details class="container-group side-group"><summary class="container-group-heading"><!> <span class="container-group-label"><strong> </strong><span class="muted"> </span></span> <span class="chip"> </span></summary> <div class="side-list container-group-items"><!></div></details>`);
	function GroupSection($$anchor, $$props) {
		push($$props, true);
		let open = /* @__PURE__ */ state$1(proxy($$props.openGroups.has($$props.group.key)));
		const size = /* @__PURE__ */ user_derived(() => $$props.by === "main" ? $$props.store.sizes().main : $$props.store.sizes().sub);
		const item = /* @__PURE__ */ user_derived(() => $$props.group.item);
		const detail = /* @__PURE__ */ user_derived(() => !get(item) ? `${$$props.by === "main" ? "Main" : "Sub"} needed` : get(item).pending ? `Drawn ${$$props.by} · waiting` : get(item).document ? `Shared ${$$props.by} · ${round(ink(get(item), $$props.by === "sub")[0])}×${round(ink(get(item), $$props.by === "sub")[1])} / ${get(size)}` : `Shared ${$$props.by}`);
		function toggle(e) {
			set(open, e.currentTarget.open, true);
			if (get(open)) $$props.openGroups.add($$props.group.key);
			else $$props.openGroups.delete($$props.group.key);
		}
		var details = root_1$4();
		var summary = child(details);
		var node = child(summary);
		var consequent = ($$anchor) => {
			var img = root$3();
			template_effect(($0) => set_attribute(img, "src", $0), [() => get(item).document ? dataURL(get(item).document) : get(item).preview_url]);
			append($$anchor, img);
		};
		if_block(node, ($$render) => {
			if (get(item)) $$render(consequent);
		});
		var span = sibling(node, 2);
		var strong = child(span);
		var text = only_child(strong, true);
		var text_1 = only_child(sibling(strong), true);
		reset(span);
		var text_2 = only_child(sibling(span, 2));
		reset(summary);
		var div = sibling(summary, 2);
		var node_1 = child(div);
		var consequent_1 = ($$anchor) => {
			var fragment = comment();
			each(first_child(fragment), 17, () => $$props.group.rows, (row) => row.id, ($$anchor, row) => {
				PairRow($$anchor, {
					get store() {
						return $$props.store;
					},
					get row() {
						return get(row);
					},
					get editor() {
						return $$props.editor;
					}
				});
			});
			append($$anchor, fragment);
		};
		if_block(node_1, ($$render) => {
			if (get(open)) $$render(consequent_1);
		});
		reset(div);
		reset(details);
		template_effect(($0) => {
			details.open = get(open);
			set_text(text, $$props.group.title);
			set_text(text_1, get(detail));
			set_text(text_2, `${$0 ?? ""} pair${$$props.group.rows.length === 1 ? "" : "s"}`);
		}, [() => $$props.group.rows.length.toLocaleString()]);
		event("toggle", details, toggle);
		append($$anchor, details);
		pop();
	}
	//#endregion
	//#region side-pairs/src/components/PartInspect.svelte
	var root$2 = /* @__PURE__ */ from_html(`<button type="button"> </button>`);
	var root_1$3 = /* @__PURE__ */ from_html(`<a target="_blank" rel="noopener">Open SVG</a>`);
	var root_2$3 = /* @__PURE__ */ from_html(`<p class="muted"> </p>`);
	var root_3$3 = /* @__PURE__ */ from_html(`<p class="muted">Loading artwork…</p>`);
	var root_4$3 = /* @__PURE__ */ from_html(`<div></div>`);
	var root_5$3 = /* @__PURE__ */ from_html(`<dt> </dt><dd> </dd>`, 1);
	var root_6$3 = /* @__PURE__ */ from_html(`<dialog class="side-inspect side-component-inspect"><header><h2> </h2><button type="button" class="side-inspect-close">Close</button></header> <div class="side-component-controls" role="group" aria-label="Display"><!> <!></div> <div class="side-stage"><!></div> <dl class="side-component-facts"></dl></dialog>`);
	function PartInspect($$anchor, $$props) {
		push($$props, true);
		let dialog = /* @__PURE__ */ state$1(void 0);
		user_effect(() => {
			inspect.shown;
			if (inspect.open && get(dialog) && !get(dialog).open) get(dialog).showModal();
			else if (!inspect.open && get(dialog)?.open) get(dialog).close();
		});
		function place(element, svg) {
			element.replaceChildren();
			if (svg) element.append(svg);
			return { update: (next) => {
				element.replaceChildren();
				if (next) element.append(next);
			} };
		}
		function backdrop(e) {
			if (e.target !== get(dialog)) return;
			const r = get(dialog).getBoundingClientRect();
			if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) inspect.open = false;
		}
		var dialog_1 = root_6$3();
		var header = child(dialog_1);
		var h2 = child(header);
		var text = only_child(h2);
		var button = sibling(h2);
		reset(header);
		var div = sibling(header, 2);
		var node = child(div);
		each(node, 16, () => [
			["both", "Artwork + centerline"],
			["art", "Artwork"],
			["line", "Centerline only"]
		], ([view, label]) => view, ($$anchor, $$item) => {
			var $$array = /* @__PURE__ */ user_derived(() => to_array($$item, 2));
			let view = () => get($$array)[0];
			let label = () => get($$array)[1];
			var button_1 = root$2();
			var text_1 = only_child(button_1, true);
			template_effect(($0) => {
				set_attribute(button_1, "data-view", view());
				set_attribute(button_1, "aria-pressed", $0);
				set_text(text_1, label());
			}, [() => String(inspect.view === view())]);
			delegated("click", button_1, () => {
				inspect.view = view();
			});
			append($$anchor, button_1);
		});
		var node_1 = sibling(node, 2);
		var consequent = ($$anchor) => {
			var a = root_1$3();
			template_effect(($0) => set_attribute(a, "href", $0), [() => inspect.item.document ? dataURL(inspect.item.document) : inspect.item.preview_url]);
			append($$anchor, a);
		};
		if_block(node_1, ($$render) => {
			if (inspect.item) $$render(consequent);
		});
		reset(div);
		var div_1 = sibling(div, 2);
		var node_2 = child(div_1);
		var consequent_1 = ($$anchor) => {
			var p = root_2$3();
			var text_2 = only_child(p, true);
			template_effect(() => set_text(text_2, inspect.error));
			append($$anchor, p);
		};
		var consequent_2 = ($$anchor) => {
			append($$anchor, root_3$3());
		};
		var alternate = ($$anchor) => {
			var div_2 = root_4$3();
			action(div_2, ($$node, $$action_arg) => place?.($$node, $$action_arg), () => inspect.svg);
			append($$anchor, div_2);
		};
		if_block(node_2, ($$render) => {
			if (inspect.error) $$render(consequent_1);
			else if (!inspect.svg) $$render(consequent_2, 1);
			else $$render(alternate, -1);
		});
		reset(div_1);
		var dl = sibling(div_1, 2);
		each(dl, 21, () => inspect.facts, ([k, v]) => k, ($$anchor, $$item) => {
			var $$array_1 = /* @__PURE__ */ user_derived(() => to_array(get($$item), 2));
			let k = () => get($$array_1)[0];
			let v = () => get($$array_1)[1];
			var fragment = root_5$3();
			var dt = first_child(fragment);
			var text_3 = only_child(dt, true);
			var text_4 = only_child(sibling(dt), true);
			template_effect(() => {
				set_text(text_3, k());
				set_text(text_4, v());
			});
			append($$anchor, fragment);
		});
		reset(dl);
		reset(dialog_1);
		bind_this(dialog_1, ($$value) => set(dialog, $$value), () => get(dialog));
		template_effect(() => {
			set_attribute(dialog_1, "data-view", inspect.view);
			set_text(text, `${inspect.label ?? ""} · ${(inspect.item?.icon || "") ?? ""}`);
		});
		event("close", dialog_1, () => {
			inspect.open = false;
		});
		delegated("click", dialog_1, backdrop);
		delegated("click", button, () => {
			inspect.open = false;
		});
		append($$anchor, dialog_1);
		pop();
	}
	delegate(["click"]);
	var PRESET_SETS = {
		64: {
			main: {
				base: 48,
				sizes: Array.from({ length: 9 }, (_v, i) => 32 + 4 * i),
				label: "Main"
			},
			sub: {
				base: 32,
				sizes: Array.from({ length: 7 }, (_v, i) => 20 + 4 * i),
				label: "Sub"
			}
		},
		72: {
			main: {
				base: 54,
				sizes: Array.from({ length: 9 }, (_v, i) => 38 + 4 * i),
				label: "Main"
			},
			sub: {
				base: 36,
				sizes: Array.from({ length: 7 }, (_v, i) => 24 + 4 * i),
				label: "Sub"
			}
		}
	};
	var KEYSHAPES72 = {
		main: {
			CIRCLE: [
				2,
				2,
				50,
				50
			],
			SQUARE: [
				4,
				4,
				46,
				46
			],
			portrait_L: [
				6,
				2,
				42,
				50
			],
			landscape_L: [
				2,
				6,
				50,
				42
			],
			tall_M: [
				8,
				2,
				38,
				50
			],
			wide_M: [
				2,
				8,
				50,
				38
			],
			slim_S: [
				11,
				2,
				32,
				50
			],
			flat_S: [
				2,
				11,
				50,
				32
			]
		},
		sub: {
			CIRCLE: [
				0,
				0,
				36,
				36
			],
			SQUARE: [
				0,
				0,
				36,
				36
			],
			portrait_L: [
				2,
				0,
				32,
				36
			],
			landscape_L: [
				0,
				2,
				36,
				32
			],
			tall_M: [
				4,
				0,
				28,
				36
			],
			wide_M: [
				0,
				4,
				36,
				28
			],
			slim_S: [
				6,
				0,
				24,
				36
			],
			flat_S: [
				0,
				6,
				36,
				24
			]
		}
	};
	var ANCHORS = {
		br: [1, 1],
		bl: [0, 1],
		tr: [1, 0],
		tl: [0, 0],
		ri: [1, .5],
		le: [0, .5],
		bo: [.5, 1],
		to: [.5, 0]
	};
	var SIDES = {
		br: "Bottom-right",
		bl: "Bottom-left",
		tr: "Top-right",
		tl: "Top-left",
		ri: "Right",
		le: "Left",
		bo: "Bottom",
		to: "Top"
	};
	var fmt = (n) => String(Math.round(n * 100) / 100);
	var scales = (u) => {
		const sw = u.src[2] - u.src[0], sh = u.src[3] - u.src[1];
		const sx = sw > 1e-9 ? u.w / sw : null, sy = sh > 1e-9 ? u.h / sh : null;
		return [sx ?? sy ?? 1, sy ?? sx ?? 1];
	};
	var boxOf = (u) => [
		u.x,
		u.y,
		u.x + u.w,
		u.y + u.h
	];
	var unionOf = (list) => list.map(boxOf).reduce((a, b) => [
		Math.min(a[0], b[0]),
		Math.min(a[1], b[1]),
		Math.max(a[2], b[2]),
		Math.max(a[3], b[3])
	]);
	var keyOf = (role, i) => role + ":" + i;
	var keyshapesLoaded = null;
	function contractKeyshapes() {
		return keyshapesLoaded ??= fetch("laboratory.json", { cache: "no-cache" }).then((r) => r.ok ? r.json() : null).catch(() => null).then((d) => {
			const of = (profile) => Object.fromEntries(Object.entries(d?.keyshapes?.resolved?.[profile] || {}).map(([n, k]) => [n, k.centerline_bounds]).filter(([, b]) => Array.isArray(b)));
			return {
				main: of("SOLO48"),
				sub: of("SUB32")
			};
		});
	}
	var keyshapes72 = () => Object.fromEntries(Object.entries(KEYSHAPES72).map(([role, table]) => [role, Object.fromEntries(Object.entries(table).map(([name, [x, y, w, h]]) => [name, [
		x + 2,
		y + 2,
		x + w - 2,
		y + h - 2
	]]))]));
	var LayoutEditor = class {
		#version = /* @__PURE__ */ state$1(0);
		get version() {
			return get(this.#version);
		}
		set version(value) {
			set(this.#version, value, true);
		}
		#open = /* @__PURE__ */ state$1(false);
		get open() {
			return get(this.#open);
		}
		set open(value) {
			set(this.#open, value, true);
		}
		#shown = /* @__PURE__ */ state$1(0);
		get shown() {
			return get(this.#shown);
		}
		set shown(value) {
			set(this.#shown, value, true);
		}
		#readout = /* @__PURE__ */ state$1(proxy({
			text: "",
			bad: false
		}));
		get readout() {
			return get(this.#readout);
		}
		set readout(value) {
			set(this.#readout, value, true);
		}
		#error = /* @__PURE__ */ state$1("");
		get error() {
			return get(this.#error);
		}
		set error(value) {
			set(this.#error, value, true);
		}
		#centerline = /* @__PURE__ */ state$1(true);
		get centerline() {
			return get(this.#centerline);
		}
		set centerline(value) {
			set(this.#centerline, value, true);
		}
		pairsWithMain = () => [];
		applied = () => {};
		ctx = null;
		presets = PRESET_SETS[64];
		constructor() {
			try {
				this.centerline = localStorage.getItem("side-layout-centerline") !== "off";
			} catch {}
		}
		touchView() {
			this.version++;
		}
		setCenterline(on) {
			this.centerline = on;
			try {
				localStorage.setItem("side-layout-centerline", on ? "on" : "off");
			} catch {}
			this.touchView();
		}
		async combine(body) {
			const data = window.SideData, composed = await data.compose(body.id, { layout: body.layout ?? null });
			const out = {
				...composed.result,
				svg: composed.svg
			};
			if (body.elements) {
				try {
					out.elements = Object.fromEntries(["main", "sub"].map((role) => [role, data.elements(composed, role, body.layout?.[role])]));
				} catch (e) {
					out.elements = null;
					out.elements_error = e.message;
				}
				out.keyshapes = data.size() === 72 ? keyshapes72() : await contractKeyshapes();
			}
			return out;
		}
		async show(pair, main, sub, onSaved, saved = null) {
			this.open = true;
			this.shown++;
			await this.load(pair, main, sub, onSaved, saved);
		}
		close() {
			this.open = false;
			this.touchView();
		}
		async load(pair, main, sub, onSaved, saved) {
			this.presets = PRESET_SETS[window.SideData.size()] || PRESET_SETS[64];
			this.ctx = {
				pair,
				main,
				sub,
				onSaved,
				saved,
				canvas: window.SideData.sizes().canvas,
				roles: {},
				dirty: /* @__PURE__ */ new Set(),
				sel: /* @__PURE__ */ new Set(),
				level: this.ctx?.level || "whole",
				busy: false,
				token: 0,
				result: null,
				stale: false,
				combining: false,
				targets: null,
				applyResults: null,
				applyOpen: this.ctx?.applyOpen,
				preset: {},
				shapes: null,
				keyshapes: {},
				loaded: false
			};
			const ctx = this.ctx;
			this.error = "";
			this.readout = {
				text: "Loading elements…",
				bad: false
			};
			this.touchView();
			let data;
			try {
				data = await this.combine({
					id: pair.id,
					elements: true,
					...saved ? { layout: saved } : {}
				});
			} catch (e) {
				if (!saved) {
					this.readout = {
						text: "",
						bad: false
					};
					this.error = e.message;
					this.touchView();
					return;
				}
				try {
					data = await this.combine({
						id: pair.id,
						elements: true
					});
					this.error = "The saved layout no longer fits these drawings: " + e.message;
				} catch (e2) {
					this.readout = {
						text: "",
						bad: false
					};
					this.error = e2.message;
					this.touchView();
					return;
				}
			}
			if (this.ctx !== ctx) return;
			ctx.result = data;
			if (!data.elements) {
				this.readout = {
					text: "",
					bad: false
				};
				this.error = data.elements_error || "This pair cannot be adjusted.";
				this.touchView();
				return;
			}
			ctx.canvas = data.canvas || 64;
			ctx.keyshapes = data.keyshapes || {};
			for (const [role, c] of Object.entries(data.elements)) {
				ctx.roles[role] = {
					markup: c.markup,
					names: c.names,
					sources: c.sources,
					units: c.groups.map((g) => {
						const b = g.box;
						return {
							paths: g.paths,
							src: g.source,
							x: b[0],
							y: b[1],
							w: b[2] - b[0],
							h: b[3] - b[1]
						};
					})
				};
				if (saved?.[role]) ctx.dirty.add(role);
			}
			ctx.loaded = true;
			const pairs = this.pairsWithMain(main.icon, pair.id);
			ctx.targets = new Set(pairs.filter((p) => p.position === pair.position).map((p) => p.id));
			this.status();
		}
		selected() {
			const ctx = this.ctx;
			return [...ctx.sel].map((k) => {
				const [role, i] = k.split(":");
				return ctx.roles[role]?.units[Number(i)];
			}).filter(Boolean);
		}
		selectedRoles() {
			return new Set([...this.ctx.sel].map((k) => k.split(":")[0]));
		}
		outside(b) {
			const c = this.ctx.canvas;
			return b[0] - 2 < -1e-6 || b[1] - 2 < -1e-6 || b[2] + 2 > c + 1e-6 || b[3] + 2 > c + 1e-6;
		}
		anyOutside() {
			return Object.values(this.ctx.roles).some((r) => r.units.some((u) => this.outside(boxOf(u))));
		}
		touch(roles) {
			for (const role of roles) {
				if (this.ctx.dirty.has(role)) continue;
				this.ctx.dirty.add(role);
				for (const u of this.ctx.roles[role].units) {
					const x1 = Math.round(u.x + u.w), y1 = Math.round(u.y + u.h);
					u.x = Math.round(u.x);
					u.y = Math.round(u.y);
					u.w = x1 - u.x;
					u.h = y1 - u.y;
				}
			}
		}
		layout() {
			const out = {};
			for (const role of this.ctx.dirty) out[role] = this.ctx.roles[role].units.map((u) => ({
				paths: u.paths,
				x: u.x,
				y: u.y,
				w: u.w,
				h: u.h
			}));
			return Object.keys(out).length ? out : null;
		}
		splitUnits(targets) {
			const ctx = this.ctx;
			this.touch(new Set([...targets].map((k) => k.split(":")[0])));
			const remap = /* @__PURE__ */ new Map(), byPath = {};
			for (const [role, r] of Object.entries(ctx.roles)) {
				const units = [];
				byPath[role] = {};
				r.units.forEach((u, i) => {
					const old = keyOf(role, i);
					if (!targets.has(old) || u.paths.length < 2) {
						const key = keyOf(role, units.length);
						remap.set(old, [key]);
						for (const p of u.paths) byPath[role][p] = key;
						units.push(u);
						return;
					}
					const [sx, sy] = scales(u), keys = [];
					for (const p of u.paths) {
						const s = r.sources[p], x0 = Math.round(u.x + (s[0] - u.src[0]) * sx), y0 = Math.round(u.y + (s[1] - u.src[1]) * sy);
						const x1 = Math.round(u.x + (s[2] - u.src[0]) * sx), y1 = Math.round(u.y + (s[3] - u.src[1]) * sy);
						const key = keyOf(role, units.length);
						keys.push(key);
						byPath[role][p] = key;
						units.push({
							paths: [p],
							src: s,
							x: x0,
							y: y0,
							w: s[2] - s[0] > 1e-9 ? x1 - x0 : 0,
							h: s[3] - s[1] > 1e-9 ? y1 - y0 : 0
						});
					}
					remap.set(old, keys);
				});
				r.units = units;
			}
			ctx.sel = new Set([...ctx.sel].flatMap((k) => remap.get(k) || []));
			return byPath;
		}
		split() {
			this.splitUnits(new Set(this.ctx.sel));
			this.ctx.level = "path";
			this.refresh();
		}
		setLevel(level) {
			this.ctx.level = level;
			this.status();
		}
		clearSelection() {
			this.ctx.sel.clear();
			this.status();
		}
		toggleUnit(role, i, on) {
			const k = keyOf(role, i);
			if (on) this.ctx.sel.add(k);
			else this.ctx.sel.delete(k);
			this.status();
		}
		selectRole(role) {
			this.ctx.roles[role].units.forEach((_u, i) => this.ctx.sel.add(keyOf(role, i)));
			this.status();
		}
		pickPath(role, i, p) {
			const key = this.splitUnits(/* @__PURE__ */ new Set([keyOf(role, i)]))[role][p];
			this.ctx.sel.add(key);
			this.ctx.level = "path";
			this.refresh();
		}
		roleSource(role) {
			const r = this.ctx.roles[role];
			if (!r) return null;
			const boxes = r.sources.filter(Boolean);
			return boxes.length ? boxes.reduce((a, b) => [
				Math.min(a[0], b[0]),
				Math.min(a[1], b[1]),
				Math.max(a[2], b[2]),
				Math.max(a[3], b[3])
			]) : null;
		}
		roleCanvas(role) {
			return (role === "main" ? this.ctx.main.canvas : this.ctx.sub.canvas) || this.presets[role].base;
		}
		shapes(role) {
			const ctx = this.ctx;
			ctx.shapes ??= {};
			if (ctx.shapes[role]) return ctx.shapes[role];
			const unique = /* @__PURE__ */ new Map();
			for (const [name, b] of Object.entries(ctx.keyshapes?.[role] || {})) {
				const k = (name === "CIRCLE" ? "c:" : "") + b.join(",");
				if (!unique.has(k)) unique.set(k, {
					names: [],
					bounds: b
				});
				unique.get(k).names.push(name);
			}
			const list = [...unique.values()].map((s) => ({
				...s,
				w: s.bounds[2] - s.bounds[0],
				h: s.bounds[3] - s.bounds[1],
				circle: s.names.includes("CIRCLE")
			}));
			const tall = list.filter((s) => s.h > s.w).sort((a, b) => b.w - a.w), wide = list.filter((s) => s.w > s.h).sort((a, b) => b.h - a.h);
			const named = (kind, group) => group.map((s, i) => [
				`${kind.toLowerCase()}-${i}`,
				group.length <= 2 ? i ? `${kind} small` : kind : `${kind} ${s.names[0].split("_").pop()}`,
				s
			]);
			const order = [[
				"square",
				"Square",
				list.find((s) => s.w === s.h && !s.circle)
			], [
				"circle",
				"Circle",
				list.find((s) => s.circle)
			]];
			for (let i = 0; i < Math.max(tall.length, wide.length); i++) order.push(...named("Tall", tall).slice(i, i + 1), ...named("Wide", wide).slice(i, i + 1));
			return ctx.shapes[role] = order.filter(([, , s]) => s).map(([id, label, s]) => ({
				id,
				label,
				...s
			}));
		}
		ownShape(role) {
			const src = this.roleSource(role);
			if (!src || Math.abs(this.roleCanvas(role) - this.presets[role].base) > 1e-6) return null;
			return this.shapes(role).find((s) => s.bounds.every((v, i) => Math.abs(v - src[i]) < .05))?.id || null;
		}
		presetBox(role, size, shapeId) {
			const ctx = this.ctx, [px, py] = ANCHORS[ctx.pair.position] || [1, 1], [ax, ay] = role === "main" ? [1 - px, 1 - py] : [px, py];
			const c = ctx.canvas, shape = this.shapes(role).find((s) => s.id === shapeId), base = this.presets[role].base;
			let w, h;
			if (shape) {
				w = shape.w + size - base;
				h = shape.h + size - base;
			} else {
				const src = this.roleSource(role);
				if (!src) return null;
				const k = size / this.roleCanvas(role);
				w = Math.round((src[2] - src[0]) * k);
				h = Math.round((src[3] - src[1]) * k);
			}
			if (w < 4 || h < 4 || w + 4 > c - 4 || h + 4 > c - 4) return null;
			const x = Math.round(2 + (c - 4 - w - 4) * ax) + 2, y = Math.round(2 + (c - 4 - h - 4) * ay) + 2;
			return [
				x,
				y,
				x + w,
				y + h
			];
		}
		hasPresets(role) {
			return !!this.ctx.roles[role] && !(role === "sub" && this.ctx.pair.native_text);
		}
		currentPreset(role) {
			const r = this.ctx.roles[role];
			if (!r) return null;
			const box = unionOf(r.units), chosen = this.ctx.preset?.[role];
			const same = (a, b) => a && b && a.every((v, i) => Math.abs(v - b[i]) < 1e-6);
			if (chosen?.size && chosen.shape && same(box, this.presetBox(role, chosen.size, chosen.shape))) return { ...chosen };
			const ids = [this.ownShape(role) || "own", ...this.shapes(role).map((s) => s.id)];
			for (const id of ids) for (const size of this.presets[role].sizes) if (same(box, this.presetBox(role, size, id))) return {
				size,
				shape: id
			};
			return null;
		}
		presetState(role) {
			const now = this.currentPreset(role), state = this.ctx.preset[role] ??= {};
			if (now) Object.assign(state, now);
			state.size ??= this.presets[role].base;
			state.shape ??= this.ownShape(role) || "own";
			return {
				state,
				now
			};
		}
		applyPreset(role, size, shapeId) {
			const r = this.ctx.roles[role], target = this.presetBox(role, size, shapeId);
			if (!r || !target) return;
			this.touch([role]);
			this.ctx.preset[role] = {
				size,
				shape: shapeId
			};
			const from = unionOf(r.units), fw = from[2] - from[0], fh = from[3] - from[1];
			const mapX = (v) => Math.round(fw > 1e-9 ? target[0] + (v - from[0]) * (target[2] - target[0]) / fw : target[0]);
			const mapY = (v) => Math.round(fh > 1e-9 ? target[1] + (v - from[1]) * (target[3] - target[1]) / fh : target[1]);
			for (const u of r.units) {
				const x0 = mapX(u.x), y0 = mapY(u.y), x1 = mapX(u.x + u.w), y1 = mapY(u.y + u.h);
				u.x = x0;
				u.y = y0;
				u.w = u.w > 0 ? Math.max(1, x1 - x0) : 0;
				u.h = u.h > 0 ? Math.max(1, y1 - y0) : 0;
			}
			this.ctx.sel = new Set(r.units.map((_u, i) => keyOf(role, i)));
			this.refresh();
		}
		free(role) {
			this.ctx.level = "whole";
			this.ctx.sel = new Set(this.ctx.roles[role].units.map((_u, i) => keyOf(role, i)));
			this.status();
		}
		scale(list, before, fx, fy, pinX, pinY) {
			list.forEach((u, i) => {
				const b = before[i], sw = b.src[2] - b.src[0], sh = b.src[3] - b.src[1];
				if (fx != null) {
					const x0 = Math.round(pinX + (b.x - pinX) * fx), x1 = Math.round(pinX + (b.x + b.w - pinX) * fx);
					u.x = sw > 1e-9 ? Math.min(x0, x1 - 1) : Math.round(pinX + (b.x - pinX) * fx);
					u.w = sw > 1e-9 ? Math.max(1, x1 - u.x) : 0;
				}
				if (fy != null) {
					const y0 = Math.round(pinY + (b.y - pinY) * fy), y1 = Math.round(pinY + (b.y + b.h - pinY) * fy);
					u.y = sh > 1e-9 ? Math.min(y0, y1 - 1) : Math.round(pinY + (b.y - pinY) * fy);
					u.h = sh > 1e-9 ? Math.max(1, y1 - u.y) : 0;
				}
			});
		}
		press(hit, additive) {
			const ctx = this.ctx;
			let target = hit;
			if (hit.move && hit.under) {
				const u = hit.under, k = keyOf(u.role, u.unit), unit = ctx.roles[u.role].units[u.unit];
				if (ctx.level === "path") {
					if (additive || unit.paths.length > 1 || !ctx.sel.has(k)) target = u;
				} else if ((additive || !ctx.sel.has(k)) && (ctx.level === "element" || !this.selectedRoles().has(u.role) || additive)) target = u;
			}
			if (!target.handle && !target.move) {
				if (target.role == null) {
					if (!additive) ctx.sel.clear();
					this.status();
					return null;
				}
				const role = target.role;
				let keys;
				if (ctx.level === "path") {
					const unit = ctx.roles[role].units[target.unit], p = target.path ?? unit.paths[0];
					keys = [unit.paths.length > 1 ? this.splitUnits(/* @__PURE__ */ new Set([keyOf(role, target.unit)]))[role][p] : keyOf(role, target.unit)];
				} else keys = ctx.level === "element" ? [keyOf(role, target.unit)] : ctx.roles[role].units.map((_u, i) => keyOf(role, i));
				if (additive) {
					const on = keys.every((k) => ctx.sel.has(k));
					for (const k of keys) on ? ctx.sel.delete(k) : ctx.sel.add(k);
					this.status();
					return null;
				}
				if (!keys.every((k) => ctx.sel.has(k)) || keys.length !== ctx.sel.size) ctx.sel = new Set(keys);
			}
			if (!ctx.sel.size) return null;
			this.touch(this.selectedRoles());
			const list = this.selected(), before = list.map((u) => ({ ...u })), box = unionOf(list);
			this.status();
			return {
				list,
				before,
				box,
				corner: target.handle || null,
				moved: false
			};
		}
		drag(d, start, [px, py], shift) {
			d.moved = true;
			if (!d.corner) {
				const dx = Math.round(px - start[0]), dy = Math.round(py - start[1]);
				d.list.forEach((u, i) => {
					u.x = d.before[i].x + dx;
					u.y = d.before[i].y + dy;
				});
			} else {
				const box = d.box, corner = d.corner, w = box[2] - box[0], h = box[3] - box[1];
				const pinX = corner.includes("w") ? box[2] : box[0], pinY = corner.includes("n") ? box[3] : box[1];
				const edgeX = corner.includes("w") ? Math.round(px + 2) : Math.round(px - 2), edgeY = corner.includes("n") ? Math.round(py + 2) : Math.round(py - 2);
				let fx = /[ew]/.test(corner) && w > 1e-9 ? Math.max(1, Math.abs(edgeX - pinX)) / w : null, fy = /[ns]/.test(corner) && h > 1e-9 ? Math.max(1, Math.abs(edgeY - pinY)) / h : null;
				if (shift) {
					const f = Math.max(fx ?? 0, fy ?? 0) || 1;
					fx = w > 1e-9 ? f : null;
					fy = h > 1e-9 ? f : null;
				}
				this.scale(d.list, d.before, fx, fy, pinX, pinY);
			}
			this.touchView();
		}
		release(d) {
			if (d?.moved) this.refresh();
		}
		key(e) {
			const ctx = this.ctx;
			if (!ctx?.sel.size) return false;
			const list = this.selected(), steps = {
				ArrowLeft: [-1, 0],
				ArrowRight: [1, 0],
				ArrowUp: [0, -1],
				ArrowDown: [0, 1]
			}, box = unionOf(list), w = box[2] - box[0], h = box[3] - box[1];
			const resize = (dw, dh) => {
				this.touch(this.selectedRoles());
				const before = list.map((u) => ({ ...u }));
				this.scale(list, before, dw && w > 1e-9 && w + dw >= 1 ? (w + dw) / w : null, dh && h > 1e-9 && h + dh >= 1 ? (h + dh) / h : null, box[0], box[1]);
				this.refresh();
			};
			if (steps[e.key] && e.altKey) resize(steps[e.key][0], steps[e.key][1]);
			else if (steps[e.key]) {
				this.touch(this.selectedRoles());
				const n = e.shiftKey ? 8 : 1;
				for (const u of list) {
					u.x += steps[e.key][0] * n;
					u.y += steps[e.key][1] * n;
				}
				this.refresh();
			} else if (["+", "="].includes(e.key)) resize(1, 1);
			else if (["-", "_"].includes(e.key)) resize(-1, -1);
			else if (e.key === "Escape") {
				ctx.sel.clear();
				this.status();
			} else return false;
			return true;
		}
		refresh() {
			this.ctx.token++;
			this.ctx.stale = true;
			this.status();
		}
		async applyLayout() {
			const ctx = this.ctx;
			if (this.anyOutside()) {
				this.error = "Move the artwork back inside the canvas first.";
				this.touchView();
				return;
			}
			const token = ++ctx.token, body = { id: ctx.pair.id }, l = this.layout();
			if (l) body.layout = l;
			ctx.combining = true;
			this.error = "";
			this.status();
			let done = false;
			try {
				const data = await this.combine(body);
				if (token === ctx.token) {
					ctx.stale = false;
					ctx.result = data;
					done = true;
				}
			} catch (e) {
				if (token === ctx.token) this.error = e.message;
			} finally {
				ctx.combining = false;
				this.status();
				if (done) this.readout = {
					text: "Combined with this layout. Click Save layout to keep it.",
					bad: false
				};
			}
		}
		async post(body) {
			const ctx = this.ctx;
			ctx.busy = true;
			this.error = "";
			this.status();
			try {
				const composed = await window.SideData.compose(body.pair_id, { layout: body.layout });
				const [built] = await window.SideData.build([composed.request]);
				if (!built?.ok) throw Error(built?.error || "Could not save the layout.");
				const data = {
					layout: { layout: body.layout },
					result: {
						...composed.result,
						svg: composed.svg
					},
					built
				};
				ctx.onSaved?.(data);
				return data;
			} finally {
				ctx.busy = false;
				this.status();
			}
		}
		async save() {
			const l = this.layout();
			if (!l) return;
			try {
				const data = await this.post({
					pair_id: this.ctx.pair.id,
					layout: l
				});
				this.ctx.saved = data.layout.layout;
				this.ctx.stale = false;
				this.ctx.result = data.result;
				const note = window.SideData.outcome(data.built);
				this.readout = {
					text: note || "Layout saved.",
					bad: !!note
				};
			} catch (e) {
				this.error = e.message;
			}
			this.touchView();
		}
		async reset() {
			try {
				await this.post({
					pair_id: this.ctx.pair.id,
					layout: null
				});
				await this.load(this.ctx.pair, this.ctx.main, this.ctx.sub, this.ctx.onSaved, null);
			} catch (e) {
				this.error = e.message;
				this.touchView();
			}
		}
		discard() {
			const c = this.ctx;
			return this.load(c.pair, c.main, c.sub, c.onSaved, c.saved);
		}
		async applyHere(l, targets) {
			const data = window.SideData, ctx = this.ctx;
			const source = await data.compose(ctx.pair.id, { layout: l }), requests = [source.request], outcome = [];
			const sourceSub = data.part(data.item(ctx.pair.id), "sub");
			for (const target of targets) try {
				const sub = data.part(data.item(target.pair_id), "sub");
				const auto = await data.compose(target.pair_id, { layout: null });
				const moved = window.CombineSide.transfer(l, ctx.pair.position, sourceSub.icon, sub.position, sub.icon, auto.result.canvas, sub.icon !== sourceSub.icon ? data.elements(auto, "sub", null).groups : null);
				const composed = await data.compose(target.pair_id, { layout: moved });
				requests.push(composed.request);
				outcome.push({
					pair_id: target.pair_id,
					index: requests.length - 1
				});
			} catch (e) {
				outcome.push({
					pair_id: target.pair_id,
					ok: false,
					error: e.message
				});
			}
			const built = await data.build(requests);
			if (!built[0]?.ok) throw Error(built[0]?.error || "Could not save the layout.");
			const results = outcome.map((o) => o.index === void 0 ? o : built[o.index]?.ok ? {
				pair_id: o.pair_id,
				ok: true
			} : {
				pair_id: o.pair_id,
				ok: false,
				error: built[o.index]?.error || "Not saved."
			});
			return {
				source: {
					layout: { layout: l },
					result: {
						...source.result,
						svg: source.svg
					}
				},
				results
			};
		}
		async applyToTargets() {
			const ctx = this.ctx, l = this.layout(), pairs = this.pairsWithMain(ctx.main.icon, ctx.pair.id);
			if (!l) return;
			const targets = pairs.filter((p) => ctx.targets.has(p.id)).map((p) => ({
				pair_id: p.id,
				sub: p.sub
			}));
			ctx.busy = true;
			this.error = "";
			this.status();
			this.readout = {
				text: `Applying to ${targets.length} pairs…`,
				bad: false
			};
			let message = "";
			try {
				const data = await this.applyHere(l, targets);
				ctx.onSaved?.(data.source);
				ctx.saved = data.source.layout.layout;
				ctx.stale = false;
				ctx.result = data.source.result;
				ctx.applyResults = Object.fromEntries(data.results.map((x) => [x.pair_id, x]));
				await this.applied(data.results);
				const ok = data.results.filter((x) => x.ok).length;
				message = `Saved. Applied to ${ok} of ${data.results.length} pairs${ok < data.results.length ? " — see the list for the ones that could not take it" : ""}.`;
			} catch (e) {
				this.error = e.message;
			} finally {
				ctx.busy = false;
				this.status();
				if (message) this.readout = {
					text: message,
					bad: false
				};
			}
		}
		status() {
			if (this.ctx?.loaded) {
				const bad = this.anyOutside(), list = this.selected();
				if (!list.length) this.readout = {
					text: bad ? "Part of the artwork is outside the canvas." : "Select the main, the sub or some elements to adjust them.",
					bad
				};
				else {
					const b = unionOf(list), what = list.length === 1 ? "1 element" : `${list.length} elements`;
					this.readout = {
						text: `${what}: painted ${fmt(b[2] - b[0] + 4)}×${fmt(b[3] - b[1] + 4)} at (${fmt(b[0] - 2)}, ${fmt(b[1] - 2)})` + (bad ? " · outside the canvas" : ""),
						bad
					};
				}
			}
			this.touchView();
		}
	};
	//#endregion
	//#region side-pairs/src/components/LayoutEditorDialog.svelte
	var root_1$2 = /* @__PURE__ */ from_html(`<button type="button"> </button>`);
	var root_2$2 = /* @__PURE__ */ from_svg(`<circle cx="11" cy="11" fill="none" stroke="currentColor" stroke-width="1.6"></circle>`);
	var root_3$2 = /* @__PURE__ */ from_svg(`<rect rx="2" fill="none" stroke="currentColor" stroke-width="1.6"></rect>`);
	var root_4$2 = /* @__PURE__ */ from_html(`<button type="button" class="side-layout-shape"><svg viewBox="0 0 22 22" width="22" height="22" aria-hidden="true"><!></svg> <span> </span><small> </small></button>`);
	var root_5$2 = /* @__PURE__ */ from_html(`<div><span> </span> <!> <button type="button">Free</button> <small> </small></div> <div><span> </span> <!></div>`, 1);
	var root_6$2 = /* @__PURE__ */ from_svg(`<line y1="0"></line><line x1="0"></line>`, 1);
	var root_7$2 = /* @__PURE__ */ from_svg(`<circle fill="none"></circle>`);
	var root_8 = /* @__PURE__ */ from_svg(`<rect fill="none" rx="1"></rect>`);
	var root_9 = /* @__PURE__ */ from_svg(`<g></g>`);
	var root_10 = /* @__PURE__ */ from_svg(`<g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"></g>`);
	var root_11 = /* @__PURE__ */ from_svg(`<g class="trace" fill="none" stroke="#ef4444"></g>`);
	var root_12 = /* @__PURE__ */ from_svg(`<rect></rect>`);
	var root_13 = /* @__PURE__ */ from_svg(`<rect width="1.6" height="1.6"></rect>`);
	var root_14 = /* @__PURE__ */ from_svg(`<!><rect class="move" data-move=""></rect><rect></rect><text class="size-label"> </text><!>`, 1);
	var root_15 = /* @__PURE__ */ from_svg(`<g pointer-events="none"></g><!><!><!><!>`, 1);
	var root_16 = /* @__PURE__ */ from_html(`<p class="side-layout-stale"> </p>`);
	var root_17 = /* @__PURE__ */ from_html(`<div></div>`);
	var root_18 = /* @__PURE__ */ from_html(`<span> </span>`);
	var root_19 = /* @__PURE__ */ from_html(`<figure><img/><figcaption> </figcaption></figure>`);
	var root_20 = /* @__PURE__ */ from_html(`<label class="child"><input type="checkbox"/><span> </span></label>`);
	var root_21 = /* @__PURE__ */ from_html(`<label><input type="checkbox"/> <span> <small> </small></span></label> <!>`, 1);
	var root_22 = /* @__PURE__ */ from_html(`<section><h3> </h3> <!> <div class="row-actions"><button type="button">Select all</button></div></section>`);
	var root_23 = /* @__PURE__ */ from_html(`<div class="row-actions"><button type="button" title="Resize the paths of a connected element one by one">Split into paths</button> <button type="button">Clear selection</button></div>`);
	var root_24 = /* @__PURE__ */ from_html(`<img alt="" loading="lazy"/>`);
	var root_25 = /* @__PURE__ */ from_html(`<span class="none"></span>`);
	var root_26 = /* @__PURE__ */ from_html(`<span class="badge">different sub</span>`);
	var root_27 = /* @__PURE__ */ from_html(`<span class="badge warn" title="This pair has its own saved layout; applying replaces it.">adjusted</span>`);
	var root_28 = /* @__PURE__ */ from_html(`<small> </small>`);
	var root_29 = /* @__PURE__ */ from_html(`<label class="target"><input type="checkbox"/> <!> <span> <small> </small> <!><!> <!></span></label>`);
	var root_30 = /* @__PURE__ */ from_html(`<h4> </h4> <div class="targets"></div>`, 1);
	var root_31 = /* @__PURE__ */ from_html(`<details class="side-layout-apply"><summary> </summary> <p>Main and sub carry over. Other sides are re-anchored: main and sub keep their size and edits, each in its own corner. A different sub keeps its own shape, fitted to the edited sub's box.</p> <!> <div class="actions"><button type="button">Select all</button> <button type="button">Select none</button> <button type="button" class="side-layout-save apply-go"> </button> <small class="apply-note"> </small></div></details>`);
	var root_32 = /* @__PURE__ */ from_html(`<dialog class="side-layout"><header><h2> </h2><button type="button">Close</button></header> <div class="side-layout-bar side-layout-presets" role="group" aria-label="Main and sub size"></div> <div class="side-layout-bar"><span>Click selects</span> <!> <label><input type="checkbox"/> Centerline</label><span class="spacer"></span> <button type="button">Reset to automatic</button> <button type="button">Discard changes</button> <button type="button" title="Combine the main and sub with this layout to see the result"> </button> <button type="button" class="side-layout-save">Save layout</button></div> <div class="side-layout-stages"><figure><svg class="side-layout-canvas" tabindex="0" role="application"><!></svg> <figcaption>Editing view: main and sub drawn whole, centerline in red.</figcaption></figure> <div class="side-layout-result-column"><figure><div class="side-layout-preview"><!> <!></div> <figcaption>Combined result (the sub erases the main where they meet).</figcaption></figure> <div class="side-layout-output" aria-label="Output SVG at 32, 48 and 64 pixels"><!></div></div> <div class="side-layout-list" aria-label="Elements"><!> <!></div></div> <!> <p role="status"> </p> <p class="side-layout-hint">The main and sub sizes (every 4) and a keyshape snap the main / sub onto that keyshape at that size (purple / teal dashes) — the middle size on the own keyshape is automatic; Free lets you drag it to any size. Click selects a whole icon, a connected element, or one path of it (Path splits that element for you). Shift- or ⌘-click (or tick the list) to choose several. Drag to move; drag a corner or edge to resize — width and height change independently, hold Shift to keep proportions. Arrow keys move 1 unit (Shift: 8); Alt+arrows change width / height by 1; + and − change both. Everything snaps to the grid; the stroke stays 4. Edits do not combine by themselves: click Apply layout to see the combined result, then Save layout to keep it.</p> <p class="side-layout-error" role="alert"> </p></dialog>`);
	function LayoutEditorDialog($$anchor, $$props) {
		push($$props, true);
		let editor = prop($$props, "editor", 7);
		let dialog = /* @__PURE__ */ state$1(void 0);
		let canvas = /* @__PURE__ */ state$1(void 0);
		let width = /* @__PURE__ */ state$1(0);
		user_effect(() => {
			editor().shown;
			if (editor().open && get(dialog) && !get(dialog).open) get(dialog).showModal();
			else if (!editor().open && get(dialog)?.open) get(dialog).close();
		});
		const ctx = /* @__PURE__ */ user_derived(() => (editor().version, editor().ctx && { ...editor().ctx }));
		const loaded = /* @__PURE__ */ user_derived(() => !!get(ctx)?.loaded);
		const c = /* @__PURE__ */ user_derived(() => get(ctx)?.canvas || 64);
		const px = /* @__PURE__ */ user_derived(() => get(width) > 0 ? get(width) / (get(c) + 2) : 6);
		const roles = /* @__PURE__ */ user_derived(() => (editor().version, get(loaded) ? Object.entries(get(ctx).roles).map(([role, r]) => [role, {
			...r,
			units: r.units.map((u) => ({ ...u }))
		}]) : []));
		const list = /* @__PURE__ */ user_derived(() => (editor().version, get(loaded) ? editor().selected().map((u) => ({ ...u })) : []));
		const box = /* @__PURE__ */ user_derived(() => get(list).length ? unionOf(get(list)) : null);
		const bad = /* @__PURE__ */ user_derived(() => (editor().version, get(loaded) && editor().anyOutside()));
		const pairs = /* @__PURE__ */ user_derived(() => (editor().version, get(loaded) ? editor().pairsWithMain(get(ctx).main.icon, get(ctx).pair.id) : []));
		const layoutNow = /* @__PURE__ */ user_derived(() => (editor().version, get(loaded) ? editor().layout() : null));
		function unitArt(group, { markup, paths, px, trace }) {
			const draw = ({ markup, paths, px, trace }) => {
				group.replaceChildren();
				[...new DOMParser().parseFromString(`<svg xmlns="http://www.w3.org/2000/svg">${paths.map((p) => markup[p]).join("")}</svg>`, "image/svg+xml").documentElement.children].forEach((child, n) => {
					const e = document.importNode(child, true);
					e.setAttribute("data-path", paths[n]);
					e.setAttribute("vector-effect", "non-scaling-stroke");
					if (trace) {
						e.setAttribute("stroke", "#ef4444");
						e.setAttribute("stroke-width", 1.3);
						e.setAttribute("fill", "none");
					} else e.setAttribute("stroke-width", 4 * px);
					group.append(e);
				});
			};
			draw({
				markup,
				paths,
				px,
				trace
			});
			return { update: draw };
		}
		function result(element, { svg, centerline }) {
			const draw = ({ svg, centerline }) => {
				element.replaceChildren();
				if (!svg) return;
				const root = new DOMParser().parseFromString(svg, "image/svg+xml").documentElement;
				root.setAttribute("class", "side-layout-result");
				root.removeAttribute("width");
				root.removeAttribute("height");
				root.setAttribute("role", "img");
				root.setAttribute("aria-label", "Combined result");
				if (centerline) for (const id of ["main-icon-clipped", "state-icon"]) {
					const g = root.querySelector(`[id="${id}"]`);
					if (!g) continue;
					const t = g.cloneNode(true);
					t.setAttribute("opacity", "1");
					for (const n of [t, ...t.querySelectorAll("*")]) {
						n.removeAttribute("id");
						n.setAttribute("stroke", "#ef4444");
						n.setAttribute("fill", "none");
						n.setAttribute("stroke-width", "1.2");
						n.setAttribute("vector-effect", "non-scaling-stroke");
					}
					g.setAttribute("opacity", ".35");
					root.append(t);
				}
				element.append(document.importNode(root, true));
			};
			draw({
				svg,
				centerline
			});
			return { update: draw };
		}
		const output = /* @__PURE__ */ user_derived(() => get(ctx)?.result?.svg ? "data:image/svg+xml;charset=utf-8," + encodeURIComponent(get(ctx).result.svg.replace(/currentColor/g, "#000000")) : "");
		const point = (e) => {
			const p = new DOMPoint(e.clientX, e.clientY).matrixTransform(get(canvas).getScreenCTM().inverse());
			return [p.x, p.y];
		};
		function down(e) {
			const additive = e.shiftKey || e.metaKey || e.ctrlKey, target = e.target;
			const unitOf = (el) => {
				const art = el?.closest?.(".art");
				return art ? {
					role: art.dataset.role,
					unit: Number(art.dataset.unit),
					path: el.closest("[data-path]") ? Number(el.closest("[data-path]").dataset.path) : null
				} : null;
			};
			const hit = {
				handle: target.dataset?.handle || null,
				move: target.hasAttribute?.("data-move"),
				...unitOf(target) || { role: null }
			};
			if (hit.move) {
				const nodes = document.elementsFromPoint(e.clientX, e.clientY);
				const art = nodes.map((n) => n.closest?.(".art")).find(Boolean), path = nodes.map((n) => n.closest?.("[data-path]")).find((n) => n?.closest(".art"));
				if (art) hit.under = {
					role: art.dataset.role,
					unit: Number(art.dataset.unit),
					path: path ? Number(path.dataset.path) : null
				};
			}
			const d = editor().press(hit, additive);
			if (!d) return;
			get(canvas).focus();
			get(canvas).setPointerCapture?.(e.pointerId);
			e.preventDefault();
			const start = point(e);
			const move = (ev) => editor().drag(d, start, point(ev), ev.shiftKey);
			const up = () => {
				get(canvas).removeEventListener("pointermove", move);
				get(canvas).removeEventListener("pointerup", up);
				get(canvas).removeEventListener("pointercancel", up);
				editor().release(d);
			};
			get(canvas).addEventListener("pointermove", move);
			get(canvas).addEventListener("pointerup", up);
			get(canvas).addEventListener("pointercancel", up);
		}
		function key(e) {
			if (editor().key(e)) {
				e.preventDefault();
				e.stopPropagation();
			}
		}
		const presetRows = /* @__PURE__ */ user_derived(() => {
			editor().version;
			if (!get(loaded)) return [];
			return ["main", "sub"].filter((role) => editor().hasPresets(role)).map((role) => {
				const r = get(ctx).roles[role], own = editor().ownShape(role), { state, now } = editor().presetState(role), { base, sizes, label } = editor().presets[role];
				const current = unionOf(r.units);
				const shapes = [...own ? [] : [{
					id: "own",
					label: "Own shape"
				}], ...editor().shapes(role)].map((s) => ({
					s,
					b: editor().presetBox(role, state.size, s.id)
				})).filter((x) => x.b);
				return {
					role,
					own,
					state,
					now,
					base,
					label,
					painted: `${current[2] - current[0] + 4}×${current[3] - current[1] + 4}`,
					sizes: sizes.filter((size) => editor().presetBox(role, size, state.shape)),
					shapes
				};
			});
		});
		const shapeIcon = (w, h, circle) => {
			const k = 18 / Math.max(w, h);
			return {
				sw: w * k,
				sh: h * k,
				circle
			};
		};
		const guides = /* @__PURE__ */ user_derived(() => {
			editor().version;
			if (!get(loaded)) return [];
			return ["main", "sub"].flatMap((role) => {
				const state = get(ctx).preset?.[role];
				if (!editor().hasPresets(role) || !state?.size) return [];
				const b = editor().presetBox(role, state.size, state.shape);
				if (!b) return [];
				return [{
					role,
					circle: !!editor().shapes(role).find((s) => s.id === state.shape)?.circle,
					p: [
						b[0] - 2,
						b[1] - 2,
						b[2] + 2,
						b[3] + 2
					]
				}];
			});
		});
		const handles = /* @__PURE__ */ user_derived(() => get(box) ? (() => {
			const p = [
				get(box)[0] - 2,
				get(box)[1] - 2,
				get(box)[2] + 2,
				get(box)[3] + 2
			], mx = (p[0] + p[2]) / 2, my = (p[1] + p[3]) / 2;
			return {
				p,
				list: [
					[
						"nw",
						p[0],
						p[1]
					],
					[
						"n",
						mx,
						p[1]
					],
					[
						"ne",
						p[2],
						p[1]
					],
					[
						"e",
						p[2],
						my
					],
					[
						"se",
						p[2],
						p[3]
					],
					[
						"s",
						mx,
						p[3]
					],
					[
						"sw",
						p[0],
						p[3]
					],
					[
						"w",
						p[0],
						my
					]
				]
			};
		})() : null);
		const named = (r, u) => u.paths.some((p) => ![
			"path",
			"circle",
			"ellipse",
			"rect",
			"line",
			"polyline",
			"polygon"
		].includes(r.names[p]));
		const nTargets = /* @__PURE__ */ user_derived(() => (editor().version, get(ctx)?.targets?.size || 0));
		var dialog_1 = root_32();
		var header = child(dialog_1);
		var h2 = child(header);
		var text = only_child(h2);
		var button = sibling(h2);
		reset(header);
		var div = sibling(header, 2);
		each(div, 21, () => get(presetRows), (row) => row.role, ($$anchor, row) => {
			var fragment = root_5$2();
			var div_1 = first_child(fragment);
			var span = child(div_1);
			var text_1 = only_child(span);
			var node = sibling(span, 2);
			each(node, 16, () => get(row).sizes, (size) => size, ($$anchor, size) => {
				var button_1 = root_1$2();
				var text_2 = only_child(button_1, true);
				template_effect(($0) => {
					set_attribute(button_1, "aria-pressed", $0);
					set_attribute(button_1, "title", size === get(row).base ? "Automatic size" : null);
					set_text(text_2, size);
				}, [() => String(!!get(row).now && get(row).now.size === size)]);
				delegated("click", button_1, () => {
					editor().applyPreset(get(row).role, size, get(row).state.shape);
					get(canvas)?.focus();
				});
				append($$anchor, button_1);
			});
			var button_2 = sibling(node, 2);
			var text_3 = only_child(sibling(button_2, 2));
			reset(div_1);
			var div_2 = sibling(div_1, 2);
			var span_1 = child(div_2);
			var text_4 = only_child(span_1);
			each(sibling(span_1, 2), 17, () => get(row).shapes, ({ s, b }) => s.id, ($$anchor, $$item) => {
				let s = () => get($$item).s;
				let b = () => get($$item).b;
				const w = /* @__PURE__ */ user_derived(() => b()[2] - b()[0] + 4);
				const h = /* @__PURE__ */ user_derived(() => b()[3] - b()[1] + 4);
				const icon = /* @__PURE__ */ user_derived(() => shapeIcon(get(w), get(h), s().circle));
				var button_3 = root_4$2();
				var svg_1 = child(button_3);
				var node_2 = child(svg_1);
				var consequent = ($$anchor) => {
					var circle_1 = root_2$2();
					template_effect(() => set_attribute(circle_1, "r", get(icon).sw / 2));
					append($$anchor, circle_1);
				};
				var alternate = ($$anchor) => {
					var rect = root_3$2();
					template_effect(() => {
						set_attribute(rect, "x", 11 - get(icon).sw / 2);
						set_attribute(rect, "y", 11 - get(icon).sh / 2);
						set_attribute(rect, "width", get(icon).sw);
						set_attribute(rect, "height", get(icon).sh);
					});
					append($$anchor, rect);
				};
				if_block(node_2, ($$render) => {
					if (get(icon).circle) $$render(consequent);
					else $$render(alternate, -1);
				});
				reset(svg_1);
				var span_2 = sibling(svg_1, 2);
				var text_5 = only_child(span_2, true);
				var text_6 = only_child(sibling(span_2));
				reset(button_3);
				template_effect(($0, $1) => {
					set_attribute(button_3, "aria-pressed", $0);
					set_attribute(button_3, "title", $1);
					set_text(text_5, s().label);
					set_text(text_6, `${get(w) ?? ""}×${get(h) ?? ""}${s().id === get(row).own ? " · own" : ""}`);
				}, [() => String(!!get(row).now && get(row).now.shape === s().id), () => `${s().label}${s().names ? " (" + s().names.join(", ") + ")" : ""}: painted ${get(w)}×${get(h)} at size ${get(row).state.size}`]);
				delegated("click", button_3, () => {
					editor().applyPreset(get(row).role, get(row).state.size, s().id);
					get(canvas)?.focus();
				});
				append($$anchor, button_3);
			});
			reset(div_2);
			template_effect(($0) => {
				set_class(div_1, 1, "side-layout-sizes " + get(row).role);
				set_text(text_1, `${get(row).label ?? ""} size`);
				set_attribute(button_2, "aria-pressed", $0);
				set_attribute(button_2, "title", `Resize the ${get(row).role} freely: drag its handles`);
				set_text(text_3, `painted ${get(row).painted ?? ""}`);
				set_class(div_2, 1, "side-layout-shapes " + get(row).role);
				set_text(text_4, `${get(row).label ?? ""} keyshape at ${get(row).state.size ?? ""}`);
			}, [() => String(!get(row).now)]);
			delegated("click", button_2, () => {
				editor().free(get(row).role);
				get(canvas)?.focus();
			});
			append($$anchor, fragment);
		});
		reset(div);
		var div_3 = sibling(div, 2);
		var node_3 = sibling(child(div_3), 2);
		each(node_3, 16, () => [
			[
				"whole",
				"Whole icon",
				null
			],
			[
				"element",
				"Element",
				null
			],
			[
				"path",
				"Path",
				"One path of a connected element (the stand of a monitor)"
			]
		], ([level, label, title]) => level, ($$anchor, $$item) => {
			var $$array = /* @__PURE__ */ user_derived(() => to_array($$item, 3));
			let level = () => get($$array)[0];
			let label = () => get($$array)[1];
			let title = () => get($$array)[2];
			var button_4 = root_1$2();
			var text_7 = only_child(button_4, true);
			template_effect(($0) => {
				set_attribute(button_4, "aria-pressed", $0);
				set_attribute(button_4, "title", title());
				button_4.disabled = !get(loaded);
				set_text(text_7, label());
			}, [() => String(get(ctx)?.level === level())]);
			delegated("click", button_4, () => editor().setLevel(level()));
			append($$anchor, button_4);
		});
		var label_1 = sibling(node_3, 2);
		var input = child(label_1);
		remove_input_defaults(input);
		next();
		reset(label_1);
		var button_5 = sibling(label_1, 3);
		var button_6 = sibling(button_5, 2);
		var button_7 = sibling(button_6, 2);
		let classes;
		var text_8 = only_child(button_7, true);
		var button_8 = sibling(button_7, 2);
		reset(div_3);
		var div_4 = sibling(div_3, 2);
		var figure = child(div_4);
		var svg_2 = child(figure);
		var node_4 = child(svg_2);
		var consequent_5 = ($$anchor) => {
			var fragment_1 = root_15();
			var g_1 = first_child(fragment_1);
			each(g_1, 20, () => Array.from({ length: get(c) + 1 }, (_v, i) => i), (i) => i, ($$anchor, i) => {
				var fragment_2 = root_6$2();
				var line = first_child(fragment_2);
				var line_1 = sibling(line);
				template_effect(() => {
					set_attribute(line, "x1", i);
					set_attribute(line, "x2", i);
					set_attribute(line, "y2", get(c));
					set_attribute(line, "stroke", i % 8 === 0 ? "#9eb3bd" : "#dae4e9");
					set_attribute(line, "stroke-width", i % 8 === 0 ? .13 : .055);
					set_attribute(line_1, "y1", i);
					set_attribute(line_1, "x2", get(c));
					set_attribute(line_1, "y2", i);
					set_attribute(line_1, "stroke", i % 8 === 0 ? "#9eb3bd" : "#dae4e9");
					set_attribute(line_1, "stroke-width", i % 8 === 0 ? .13 : .055);
				});
				append($$anchor, fragment_2);
			});
			reset(g_1);
			var node_5 = sibling(g_1);
			each(node_5, 17, () => get(guides), (g) => g.role, ($$anchor, g) => {
				var fragment_3 = comment();
				var node_6 = first_child(fragment_3);
				var consequent_1 = ($$anchor) => {
					var circle_2 = root_7$2();
					template_effect(() => {
						set_class(circle_2, 0, "guide " + get(g).role);
						set_attribute(circle_2, "cx", (get(g).p[0] + get(g).p[2]) / 2);
						set_attribute(circle_2, "cy", (get(g).p[1] + get(g).p[3]) / 2);
						set_attribute(circle_2, "r", (get(g).p[2] - get(g).p[0]) / 2);
					});
					append($$anchor, circle_2);
				};
				var alternate_1 = ($$anchor) => {
					var rect_1 = root_8();
					template_effect(() => {
						set_class(rect_1, 0, "guide " + get(g).role);
						set_attribute(rect_1, "x", get(g).p[0]);
						set_attribute(rect_1, "y", get(g).p[1]);
						set_attribute(rect_1, "width", get(g).p[2] - get(g).p[0]);
						set_attribute(rect_1, "height", get(g).p[3] - get(g).p[1]);
					});
					append($$anchor, rect_1);
				};
				if_block(node_6, ($$render) => {
					if (get(g).circle) $$render(consequent_1);
					else $$render(alternate_1, -1);
				});
				append($$anchor, fragment_3);
			});
			var node_7 = sibling(node_5);
			each(node_7, 17, () => get(roles), ([role, r]) => role, ($$anchor, $$item) => {
				var $$array_1 = /* @__PURE__ */ user_derived(() => to_array(get($$item), 2));
				let role = () => get($$array_1)[0];
				let r = () => get($$array_1)[1];
				var g_2 = root_10();
				each(g_2, 23, () => r().units, (u, i) => role() + i + ":" + u.paths.join(","), ($$anchor, u, i) => {
					const computed_const = /* @__PURE__ */ user_derived(() => {
						const [sx, sy] = scales(get(u));
						return {
							sx,
							sy
						};
					});
					var g_3 = root_9();
					action(g_3, ($$node, $$action_arg) => unitArt?.($$node, $$action_arg), () => ({
						markup: r().markup,
						paths: get(u).paths,
						px: get(px),
						trace: false
					}));
					template_effect(($0) => {
						set_class(g_3, 0, $0);
						set_attribute(g_3, "data-role", role());
						set_attribute(g_3, "data-unit", get(i));
						set_attribute(g_3, "transform", `matrix(${get(computed_const).sx} 0 0 ${get(computed_const).sy} ${get(u).x - get(u).src[0] * get(computed_const).sx} ${get(u).y - get(u).src[1] * get(computed_const).sy})`);
					}, [() => "art" + (get(ctx).sel.has(keyOf(role(), get(i))) ? " picked" : "")]);
					append($$anchor, g_3);
				});
				reset(g_2);
				append($$anchor, g_2);
			});
			var node_8 = sibling(node_7);
			var consequent_2 = ($$anchor) => {
				var g_4 = root_11();
				each(g_4, 21, () => get(roles), ([role, r]) => role, ($$anchor, $$item) => {
					var $$array_2 = /* @__PURE__ */ user_derived(() => to_array(get($$item), 2));
					let role = () => get($$array_2)[0];
					let r = () => get($$array_2)[1];
					var fragment_4 = comment();
					each(first_child(fragment_4), 19, () => r().units, (u, i) => role() + i + ":" + u.paths.join(","), ($$anchor, u) => {
						const computed_const_1 = /* @__PURE__ */ user_derived(() => {
							const [sx, sy] = scales(get(u));
							return {
								sx,
								sy
							};
						});
						var g_5 = root_9();
						action(g_5, ($$node, $$action_arg) => unitArt?.($$node, $$action_arg), () => ({
							markup: r().markup,
							paths: get(u).paths,
							px: get(px),
							trace: true
						}));
						template_effect(() => set_attribute(g_5, "transform", `matrix(${get(computed_const_1).sx} 0 0 ${get(computed_const_1).sy} ${get(u).x - get(u).src[0] * get(computed_const_1).sx} ${get(u).y - get(u).src[1] * get(computed_const_1).sy})`));
						append($$anchor, g_5);
					});
					append($$anchor, fragment_4);
				});
				reset(g_4);
				append($$anchor, g_4);
			};
			if_block(node_8, ($$render) => {
				if (editor().centerline) $$render(consequent_2);
			});
			var node_10 = sibling(node_8);
			var consequent_4 = ($$anchor) => {
				var fragment_5 = root_14();
				var node_11 = first_child(fragment_5);
				each(node_11, 17, () => get(list), index, ($$anchor, u) => {
					const b = /* @__PURE__ */ user_derived(() => boxOf(get(u)));
					var fragment_6 = comment();
					var node_12 = first_child(fragment_6);
					var consequent_3 = ($$anchor) => {
						var rect_2 = root_12();
						template_effect(($0) => {
							set_class(rect_2, 0, $0);
							set_attribute(rect_2, "x", get(b)[0] - 2);
							set_attribute(rect_2, "y", get(b)[1] - 2);
							set_attribute(rect_2, "width", get(b)[2] - get(b)[0] + 4);
							set_attribute(rect_2, "height", get(b)[3] - get(b)[1] + 4);
						}, [() => "unit" + (editor().outside(get(b)) ? " out" : "")]);
						append($$anchor, rect_2);
					};
					var d_1 = /* @__PURE__ */ user_derived(() => get(list).length > 1 || editor().outside(get(b)));
					if_block(node_12, ($$render) => {
						if (get(d_1)) $$render(consequent_3);
					});
					append($$anchor, fragment_6);
				});
				var rect_3 = sibling(node_11);
				var rect_4 = sibling(rect_3);
				var text_9 = sibling(rect_4);
				var text_10 = only_child(text_9);
				each(sibling(text_9), 17, () => get(handles).list, ([name, x, y]) => name, ($$anchor, $$item) => {
					var $$array_3 = /* @__PURE__ */ user_derived(() => to_array(get($$item), 3));
					let name = () => get($$array_3)[0];
					let x = () => get($$array_3)[1];
					let y = () => get($$array_3)[2];
					var rect_5 = root_13();
					template_effect(() => {
						set_class(rect_5, 0, "handle " + name());
						set_attribute(rect_5, "data-handle", name());
						set_attribute(rect_5, "x", x() - .8);
						set_attribute(rect_5, "y", y() - .8);
					});
					append($$anchor, rect_5);
				});
				template_effect(($0, $1, $2, $3, $4, $5, $6) => {
					set_attribute(rect_3, "x", get(handles).p[0]);
					set_attribute(rect_3, "y", get(handles).p[1]);
					set_attribute(rect_3, "width", get(handles).p[2] - get(handles).p[0]);
					set_attribute(rect_3, "height", get(handles).p[3] - get(handles).p[1]);
					set_class(rect_4, 0, $0);
					set_attribute(rect_4, "x", get(handles).p[0]);
					set_attribute(rect_4, "y", get(handles).p[1]);
					set_attribute(rect_4, "width", get(handles).p[2] - get(handles).p[0]);
					set_attribute(rect_4, "height", get(handles).p[3] - get(handles).p[1]);
					set_attribute(text_9, "x", get(handles).p[0]);
					set_attribute(text_9, "y", get(handles).p[1] > 4 ? get(handles).p[1] - 1.2 : get(handles).p[3] + 3.2);
					set_text(text_10, `ink ${$1 ?? ""}×${$2 ?? ""} · box ${$3 ?? ""}×${$4 ?? ""} · at ${$5 ?? ""},${$6 ?? ""}`);
				}, [
					() => "sel" + (editor().outside(get(box)) ? " out" : ""),
					() => fmt(get(handles).p[2] - get(handles).p[0]),
					() => fmt(get(handles).p[3] - get(handles).p[1]),
					() => fmt(get(box)[2] - get(box)[0]),
					() => fmt(get(box)[3] - get(box)[1]),
					() => fmt(get(handles).p[0]),
					() => fmt(get(handles).p[1])
				]);
				append($$anchor, fragment_5);
			};
			if_block(node_10, ($$render) => {
				if (get(handles)) $$render(consequent_4);
			});
			append($$anchor, fragment_1);
		};
		if_block(node_4, ($$render) => {
			if (get(loaded)) $$render(consequent_5);
		});
		reset(svg_2);
		bind_this(svg_2, ($$value) => set(canvas, $$value), () => get(canvas));
		next(2);
		reset(figure);
		var div_5 = sibling(figure, 2);
		var figure_1 = child(div_5);
		var div_6 = child(figure_1);
		var node_14 = child(div_6);
		var consequent_6 = ($$anchor) => {
			var p_1 = root_16();
			var text_11 = only_child(p_1, true);
			template_effect(() => set_text(text_11, get(bad) ? "Move the artwork back inside the canvas, then Apply layout." : "Layout changed. Click Apply layout to see the combined result."));
			append($$anchor, p_1);
		};
		if_block(node_14, ($$render) => {
			if (get(ctx)?.stale) $$render(consequent_6);
		});
		var node_15 = sibling(node_14, 2);
		var consequent_7 = ($$anchor) => {
			var div_7 = root_17();
			action(div_7, ($$node, $$action_arg) => result?.($$node, $$action_arg), () => ({
				svg: get(ctx).result.svg,
				centerline: editor().centerline
			}));
			append($$anchor, div_7);
		};
		var alternate_2 = ($$anchor) => {
			var span_3 = root_18();
			var text_12 = only_child(span_3, true);
			template_effect(() => set_text(text_12, get(ctx) ? "Loading…" : ""));
			append($$anchor, span_3);
		};
		if_block(node_15, ($$render) => {
			if (get(ctx)?.result) $$render(consequent_7);
			else $$render(alternate_2, -1);
		});
		reset(div_6);
		next(2);
		reset(figure_1);
		var div_8 = sibling(figure_1, 2);
		var node_16 = child(div_8);
		var consequent_8 = ($$anchor) => {
			var fragment_7 = comment();
			each(first_child(fragment_7), 16, () => [
				32,
				48,
				64
			], (size) => size, ($$anchor, size) => {
				var figure_2 = root_19();
				var img = child(figure_2);
				var text_13 = only_child(sibling(img));
				reset(figure_2);
				template_effect(() => {
					set_attribute(img, "src", get(output));
					set_attribute(img, "width", size);
					set_attribute(img, "height", size);
					set_attribute(img, "alt", `Output at ${size} pixels`);
					set_text(text_13, `${size ?? ""} px`);
				});
				append($$anchor, figure_2);
			});
			append($$anchor, fragment_7);
		};
		if_block(node_16, ($$render) => {
			if (get(output)) $$render(consequent_8);
		});
		reset(div_8);
		reset(div_5);
		var div_9 = sibling(div_5, 2);
		var node_18 = child(div_9);
		each(node_18, 17, () => get(roles), ([role, r]) => role, ($$anchor, $$item) => {
			var $$array_4 = /* @__PURE__ */ user_derived(() => to_array(get($$item), 2));
			let role = () => get($$array_4)[0];
			let r = () => get($$array_4)[1];
			var section = root_22();
			var h3 = child(section);
			var text_14 = only_child(h3, true);
			var node_19 = sibling(h3, 2);
			each(node_19, 19, () => r().units, (u, i) => role() + i + ":" + u.paths.join(","), ($$anchor, u, i) => {
				const isNamed = /* @__PURE__ */ user_derived(() => named(r(), get(u)));
				var fragment_8 = root_21();
				var label_2 = first_child(fragment_8);
				var input_1 = child(label_2);
				remove_input_defaults(input_1);
				var span_4 = sibling(input_1, 2);
				var text_15 = child(span_4, true);
				var text_16 = only_child(sibling(text_15));
				reset(span_4);
				reset(label_2);
				var node_20 = sibling(label_2, 2);
				var consequent_9 = ($$anchor) => {
					var fragment_9 = comment();
					each(first_child(fragment_9), 16, () => get(u).paths, (p) => p, ($$anchor, p) => {
						var label_3 = root_20();
						var input_2 = child(label_3);
						var text_17 = only_child(sibling(input_2), true);
						reset(label_3);
						template_effect(() => set_text(text_17, get(isNamed) ? r().names[p] : `path ${p + 1}`));
						delegated("change", input_2, () => editor().pickPath(role(), get(i), p));
						append($$anchor, label_3);
					});
					append($$anchor, fragment_9);
				};
				if_block(node_20, ($$render) => {
					if (get(u).paths.length > 1) $$render(consequent_9);
				});
				template_effect(($0, $1, $2, $3) => {
					set_checked(input_1, $0);
					set_text(text_15, $1);
					set_text(text_16, ` · ${$2 ?? ""}×${$3 ?? ""}`);
				}, [
					() => get(ctx).sel.has(keyOf(role(), get(i))),
					() => get(isNamed) ? get(u).paths.map((p) => r().names[p]).join(" + ") : `${role() === "sub" && get(ctx).pair.native_text ? "Glyph" : "Element"} ${get(i) + 1}`,
					() => fmt(get(u).w + 4),
					() => fmt(get(u).h + 4)
				]);
				delegated("change", input_1, (e) => editor().toggleUnit(role(), get(i), e.currentTarget.checked));
				append($$anchor, fragment_8);
			});
			var button_9 = only_child(sibling(node_19, 2));
			reset(section);
			template_effect(() => set_text(text_14, role() === "main" ? "Main elements" : "Sub elements"));
			delegated("click", button_9, () => editor().selectRole(role()));
			append($$anchor, section);
		});
		var node_22 = sibling(node_18, 2);
		var consequent_10 = ($$anchor) => {
			var div_11 = root_23();
			var button_10 = child(div_11);
			var button_11 = sibling(button_10, 2);
			reset(div_11);
			template_effect(($0) => {
				button_10.disabled = $0;
				button_11.disabled = !get(ctx).sel.size;
			}, [() => !get(list).some((u) => u.paths.length > 1)]);
			delegated("click", button_10, () => editor().split());
			delegated("click", button_11, () => editor().clearSelection());
			append($$anchor, div_11);
		};
		if_block(node_22, ($$render) => {
			if (get(loaded)) $$render(consequent_10);
		});
		reset(div_9);
		reset(div_4);
		var node_23 = sibling(div_4, 2);
		var consequent_16 = ($$anchor) => {
			var details = root_31();
			var summary = child(details);
			var text_18 = only_child(summary);
			var node_24 = sibling(summary, 4);
			each(node_24, 17, () => [[`Same side · ${SIDES[get(ctx).pair.position] || get(ctx).pair.position}`, get(pairs).filter((p) => p.position === get(ctx).pair.position)], ["Other sides", get(pairs).filter((p) => p.position !== get(ctx).pair.position)]], ([title, group]) => title, ($$anchor, $$item) => {
				var $$array_5 = /* @__PURE__ */ user_derived(() => to_array(get($$item), 2));
				let title = () => get($$array_5)[0];
				let group = () => get($$array_5)[1];
				var fragment_10 = comment();
				var node_25 = first_child(fragment_10);
				var consequent_15 = ($$anchor) => {
					var fragment_11 = root_30();
					var h4 = first_child(fragment_11);
					var text_19 = only_child(h4);
					var div_12 = sibling(h4, 2);
					each(div_12, 21, group, (p) => p.id, ($$anchor, p, $$index_16, $$array_6) => {
						const result = /* @__PURE__ */ user_derived(() => get(ctx).applyResults?.[get(p).id]);
						var label_4 = root_29();
						var input_3 = child(label_4);
						remove_input_defaults(input_3);
						var node_26 = sibling(input_3, 2);
						var consequent_11 = ($$anchor) => {
							var img_1 = root_24();
							template_effect(() => set_attribute(img_1, "src", get(p).preview));
							append($$anchor, img_1);
						};
						var alternate_3 = ($$anchor) => {
							append($$anchor, root_25());
						};
						if_block(node_26, ($$render) => {
							if (get(p).preview) $$render(consequent_11);
							else $$render(alternate_3, -1);
						});
						var span_7 = sibling(node_26, 2);
						var text_20 = child(span_7, true);
						var small_3 = sibling(text_20);
						var text_21 = only_child(small_3);
						var node_27 = sibling(small_3, 2);
						var consequent_12 = ($$anchor) => {
							append($$anchor, root_26());
						};
						if_block(node_27, ($$render) => {
							if (get(p).sub !== get(ctx).sub.icon) $$render(consequent_12);
						});
						var node_28 = sibling(node_27);
						var consequent_13 = ($$anchor) => {
							append($$anchor, root_27());
						};
						if_block(node_28, ($$render) => {
							if (get(p).adjusted) $$render(consequent_13);
						});
						var node_29 = sibling(node_28, 2);
						var consequent_14 = ($$anchor) => {
							var small_4 = root_28();
							var text_22 = only_child(small_4, true);
							template_effect(() => {
								set_class(small_4, 1, clsx(get(result).ok ? "ok" : "fail"));
								set_text(text_22, get(result).ok ? "✓ applied" : "✕ " + get(result).error);
							});
							append($$anchor, small_4);
						};
						if_block(node_29, ($$render) => {
							if (get(result)) $$render(consequent_14);
						});
						reset(span_7);
						reset(label_4);
						template_effect(($0) => {
							set_checked(input_3, $0);
							set_text(text_20, get(p).concept);
							set_text(text_21, `${(SIDES[get(p).position] || get(p).position) ?? ""} · ${get(p).sub ?? ""}`);
						}, [() => get(ctx).targets.has(get(p).id)]);
						delegated("change", input_3, (e) => {
							if (e.currentTarget.checked) get(ctx).targets.add(get(p).id);
							else get(ctx).targets.delete(get(p).id);
							editor().touchView();
						});
						append($$anchor, label_4);
					});
					reset(div_12);
					template_effect(() => set_text(text_19, `${title() ?? ""} (${group().length ?? ""})`));
					append($$anchor, fragment_11);
				};
				if_block(node_25, ($$render) => {
					if (group().length) $$render(consequent_15);
				});
				append($$anchor, fragment_10);
			});
			var div_13 = sibling(node_24, 2);
			var button_12 = child(div_13);
			var button_13 = sibling(button_12, 2);
			var button_14 = sibling(button_13, 2);
			var text_23 = only_child(button_14);
			var text_24 = only_child(sibling(button_14, 2), true);
			reset(div_13);
			reset(details);
			template_effect(() => {
				details.open = get(ctx).applyOpen !== false;
				set_text(text_18, `Also apply to pairs using this main (${get(pairs).length ?? ""})`);
				button_14.disabled = get(ctx).busy || !get(nTargets) || !get(layoutNow) || get(bad);
				set_text(text_23, `Save + apply to ${get(nTargets) ?? ""} pair${get(nTargets) === 1 ? "" : "s"}`);
				set_text(text_24, get(layoutNow) ? "" : "Adjust this pair first; its layout is what gets applied.");
			});
			event("toggle", details, (e) => {
				editor().ctx.applyOpen = e.currentTarget.open;
			});
			delegated("click", button_12, () => {
				get(pairs).forEach((p) => get(ctx).targets.add(p.id));
				editor().touchView();
			});
			delegated("click", button_13, () => {
				get(ctx).targets.clear();
				editor().touchView();
			});
			delegated("click", button_14, () => editor().applyToTargets());
			append($$anchor, details);
		};
		if_block(node_23, ($$render) => {
			if (get(loaded) && get(pairs).length) $$render(consequent_16);
		});
		var p_2 = sibling(node_23, 2);
		let classes_1;
		var text_25 = only_child(p_2, true);
		var text_26 = only_child(sibling(p_2, 4), true);
		reset(dialog_1);
		bind_this(dialog_1, ($$value) => set(dialog, $$value), () => get(dialog));
		template_effect(() => {
			set_text(text, `Adjust layout · ${(get(ctx)?.pair.concept || "") ?? ""}`);
			set_checked(input, editor().centerline);
			button_5.disabled = !get(loaded) || get(ctx).busy || !get(ctx).saved;
			button_6.disabled = !get(ctx);
			button_7.disabled = !get(loaded) || get(ctx).busy || get(ctx).combining || get(bad);
			classes = set_class(button_7, 1, "", null, classes, { "side-layout-stale-button": get(ctx)?.stale && !get(ctx)?.combining });
			set_text(text_8, get(ctx)?.combining ? "Combining…" : "Apply layout");
			button_8.disabled = !get(loaded) || get(ctx).busy || get(bad) || !get(ctx).dirty.size;
			set_attribute(svg_2, "aria-label", `Layout editor, ${get(c)} by ${get(c)} grid`);
			set_attribute(svg_2, "viewBox", `-1 -1 ${get(c) + 2} ${get(c) + 2}`);
			set_attribute(svg_2, "data-centerline", editor().centerline ? "" : null);
			classes_1 = set_class(p_2, 1, "side-layout-readout", null, classes_1, { bad: editor().readout.bad });
			set_text(text_25, editor().readout.text);
			set_text(text_26, editor().error);
		});
		event("close", dialog_1, () => editor().close());
		delegated("click", button, () => editor().close());
		delegated("change", input, (e) => editor().setCenterline(e.currentTarget.checked));
		delegated("click", button_5, () => editor().reset());
		delegated("click", button_6, () => editor().discard());
		delegated("click", button_7, () => editor().applyLayout());
		delegated("click", button_8, () => editor().save());
		delegated("pointerdown", svg_2, function(...$$args) {
			(get(loaded) ? down : null)?.apply(this, $$args);
		});
		delegated("keydown", svg_2, key);
		bind_element_size(figure, "clientWidth", ($$value) => set(width, $$value));
		append($$anchor, dialog_1);
		pop();
	}
	delegate([
		"click",
		"change",
		"pointerdown",
		"keydown"
	]);
	//#endregion
	//#region side-pairs/src/components/App.svelte
	var root$1 = /* @__PURE__ */ from_html(`<button type="button">Retry</button>`);
	var root_1$1 = /* @__PURE__ */ from_html(`<p class="muted"> </p> <!>`, 1);
	var root_2$1 = /* @__PURE__ */ from_html(`<div class="pager"><button type="button">← Previous</button> <span class="muted"> </span> <button type="button">Next →</button></div>`);
	var root_3$1 = /* @__PURE__ */ from_html(`<p class="side-status" role="status"> </p>`);
	var root_4$1 = /* @__PURE__ */ from_html(`<option> </option>`);
	var root_5$1 = /* @__PURE__ */ from_html(`<p class="muted">No side pairs match these filters.</p>`);
	var root_6$1 = /* @__PURE__ */ from_html(`<!> <p class="muted">Pair badges: Waiting = main and sub are drawn but not combined yet. Lists: <a href="side-mains.html">Main icons →</a> · <a href="side-subs.html">Sub icons →</a></p> <div class="toolbar side-combine"><button type="button" class="requires-login"> </button> <button type="button" class="requires-login" title="Pairs built before a main or sub was redrawn"> </button> <span class="muted" role="status"> </span></div> <section id="pairGallery"><!> <div class="toolbar"><select aria-label="Pair size"><option>64 · 48 main + 32 sub</option><option>72 · 54 main + 36 sub</option></select> <input type="search" placeholder="Search concept, component ID or icon name" aria-label="Search side pairs"/> <select aria-label="Side pair filter"></select> <select aria-label="Group side pairs"></select> <select aria-label="Items per page"></select></div> <!> <div class="side-list"><!> <!></div> <!></section>`, 1);
	var root_7$1 = /* @__PURE__ */ from_html(`<div><h2>Side combination</h2> <p class="muted"> </p> <!></div> <!> <!>`, 1);
	function App($$anchor, $$props) {
		push($$props, true);
		let store = prop($$props, "store", 7), editor = prop($$props, "editor", 7);
		let filter = /* @__PURE__ */ state$1(proxy(FILTERS[$$props.params.get("side")] ? $$props.params.get("side") : ""));
		let groupBy = /* @__PURE__ */ state$1(proxy(GROUPS[$$props.params.get("group")] ? $$props.params.get("group") : ""));
		let pageSize = /* @__PURE__ */ state$1(proxy(PAGE_SIZES.includes(Number($$props.params.get("size"))) ? Number($$props.params.get("size")) : 24));
		let query = /* @__PURE__ */ state$1(proxy($$props.page.query()));
		let current = /* @__PURE__ */ state$1(proxy($$props.page.page()));
		let host = /* @__PURE__ */ state$1(void 0);
		let searchBox = /* @__PURE__ */ state$1(void 0);
		const openGroups = /* @__PURE__ */ new Set();
		const sizes = /* @__PURE__ */ user_derived(() => (store().version, store().sizes()));
		const all = /* @__PURE__ */ user_derived(() => (store().version, store().ready ? [...store().catalog.rows] : []));
		const categories = /* @__PURE__ */ user_derived(() => new Map(get(all).map((r) => [r.id, category(store(), r, store().flagged, store().buildState(r.id))])));
		const rows = /* @__PURE__ */ user_derived(() => (store().version, get(all).filter((r) => (!get(filter) || get(categories).get(r.id)?.[get(filter)]) && matches(store(), r, get(query)))));
		const grouped = /* @__PURE__ */ user_derived(() => (store().version, get(groupBy) ? groups(store(), get(rows), get(groupBy), store().flagged) : null));
		const items = /* @__PURE__ */ user_derived(() => get(grouped) || get(rows));
		const pages = /* @__PURE__ */ user_derived(() => Math.max(1, Math.ceil(get(items).length / get(pageSize))));
		const visible = /* @__PURE__ */ user_derived(() => get(items).slice((Math.min(get(current), get(pages)) - 1) * get(pageSize), Math.min(get(current), get(pages)) * get(pageSize)));
		const buildable = /* @__PURE__ */ user_derived(() => (store().version, store().ready ? get(all).filter((r) => key(store(), r, store().flagged) === "ready" && (!store().previews[r.id]?.built || store().staleRoles(r.id).length)).map((r) => r.id) : []));
		const stale = /* @__PURE__ */ user_derived(() => (store().version, store().ready ? get(all).filter((r) => store().buildState(r.id) === "stale").map((r) => r.id) : []));
		function rebuildStale() {
			if (get(stale).length && confirm(`Rebuild all ${get(stale).length} stale side pairs from their parts' current drawings?`)) store().buildPairs(get(stale), "Rebuilding");
		}
		user_effect(() => {
			if (!store().ready) return;
			if (get(current) > get(pages)) set(current, get(pages), true);
			$$props.page.setQuery(get(query));
			$$props.page.setPage(get(current));
			$$props.page.writeURL();
			const u = new URL(location.href);
			for (const [name, value, fallback] of [
				[
					"side",
					get(filter),
					""
				],
				[
					"size",
					get(pageSize),
					24
				],
				[
					"group",
					get(groupBy),
					""
				],
				[
					"grid",
					store().size === 72 ? "72" : "",
					""
				]
			]) if (value !== fallback) u.searchParams.set(name, value);
			else u.searchParams.delete(name);
			history.replaceState(null, "", u);
		});
		user_effect(() => {
			store().pairsVersion;
			if (store().ready) untrack(() => window.SideRepairFlags?.setRows([...store().pairs.values()]));
		});
		let timer;
		function search(e) {
			const value = e.currentTarget.value;
			clearTimeout(timer);
			timer = setTimeout(() => {
				set(query, value, true);
				set(current, 1);
			}, 180);
		}
		const restart = () => {
			set(current, 1);
		};
		function setSize(e) {
			set(current, 1);
			store().setSize(Number(e.currentTarget.value));
		}
		function go(step) {
			set(current, Math.min(get(pages), Math.max(1, get(current) + step)), true);
			get(host)?.scrollIntoView();
		}
		editor().pairsWithMain = (icon, exceptId) => [...store().pairs.values()].filter((p) => p.id !== exceptId && !p.mapped_native && p.subs.length && p.mains.some((m) => m.icon === icon)).map((p) => {
			const sub = currentSub(p), found = store().combined(p, sub);
			return {
				id: p.id,
				concept: p.concept,
				position: p.position,
				sub: sub.icon,
				adjusted: !!store().handLayout(p.id),
				preview: found?.url || (found?.result?.svg ? dataURL(found.result.svg) : null)
			};
		});
		editor().applied = async (results) => {
			for (const r of results) if (r.ok) await store().refresh(r.pair_id);
		};
		let followed = false;
		user_effect(() => {
			if (store().ready && !followed) {
				followed = true;
				follow();
			}
		});
		async function follow() {
			const edit = $$props.params.get("edit"), make = $$props.params.get("make");
			const strip = () => {
				const u = new URL(location.href);
				for (const k of [
					"edit",
					"make",
					"position"
				]) u.searchParams.delete(k);
				history.replaceState(null, "", u);
			};
			const click = (id, selector) => tick().then(() => document.querySelector(`.side-row[data-pair-id="${CSS.escape(id)}"] ${selector}`)?.click());
			if (make) {
				try {
					if (!store().pairs.has(make)) {
						const response = await fetch("/api/combinations/pair", {
							method: "POST",
							headers: { "Content-Type": "application/json" },
							body: JSON.stringify({
								reference_id: make,
								position: $$props.params.get("position") || "br"
							})
						});
						const data = await response.json().catch(() => ({}));
						if (!response.ok) throw Error(data.error || "Could not make the side pair.");
						await store().refresh(make);
					}
					set(query, make, true);
					set(current, 1);
					strip();
					click(make, ".side-pair-editor button");
				} catch (error) {
					store().status = "Could not make the side pair: " + error.message;
					strip();
				}
				return;
			}
			if (edit && store().pairs.has(edit)) {
				set(query, edit, true);
				set(current, 1);
				strip();
				click(edit, ".side-layout-open");
			}
		}
		var fragment = root_7$1();
		var div = first_child(fragment);
		var p_1 = sibling(child(div), 2);
		var text = only_child(p_1);
		var node = sibling(p_1, 2);
		var consequent_1 = ($$anchor) => {
			var fragment_1 = root_1$1();
			var p_2 = first_child(fragment_1);
			var text_1 = only_child(p_2, true);
			var node_1 = sibling(p_2, 2);
			var consequent = ($$anchor) => {
				var button = root$1();
				delegated("click", button, () => {
					store().error = "";
					store().load();
				});
				append($$anchor, button);
			};
			if_block(node_1, ($$render) => {
				if (store().error) $$render(consequent);
			});
			template_effect(() => set_text(text_1, store().error || "Loading side pairs…"));
			append($$anchor, fragment_1);
		};
		var alternate_1 = ($$anchor) => {
			var fragment_2 = root_6$1();
			var node_2 = first_child(fragment_2);
			Summary(node_2, {
				get store() {
					return store();
				},
				get pairCount() {
					return get(all).length;
				}
			});
			var div_1 = sibling(node_2, 4);
			var button_1 = child(div_1);
			var text_2 = only_child(button_1);
			var button_2 = sibling(button_1, 2);
			var text_3 = only_child(button_2);
			var text_4 = only_child(sibling(button_2, 2), true);
			reset(div_1);
			var section = sibling(div_1, 2);
			{
				const pager = ($$anchor) => {
					var div_2 = root_2$1();
					var button_3 = child(div_2);
					var span_1 = sibling(button_3, 2);
					var text_5 = only_child(span_1);
					var button_4 = sibling(span_1, 2);
					reset(div_2);
					template_effect(($0, $1, $2) => {
						button_3.disabled = get(current) <= 1;
						set_text(text_5, `${$0 ?? ""} pairs${$1 ?? ""} · Page ${$2 ?? ""} of ${get(pages) ?? ""}`);
						button_4.disabled = get(current) >= get(pages);
					}, [
						() => get(rows).length.toLocaleString(),
						() => get(grouped) ? ` · ${get(grouped).length.toLocaleString()} ${get(groupBy) === "main" ? "main" : "sub"} icons` : "",
						() => Math.min(get(current), get(pages))
					]);
					delegated("click", button_3, () => go(-1));
					delegated("click", button_4, () => go(1));
					append($$anchor, div_2);
				};
				var node_3 = child(section);
				var consequent_2 = ($$anchor) => {
					var p_3 = root_3$1();
					var text_6 = only_child(p_3, true);
					template_effect(() => set_text(text_6, store().status));
					append($$anchor, p_3);
				};
				if_block(node_3, ($$render) => {
					if (store().status) $$render(consequent_2);
				});
				var div_3 = sibling(node_3, 2);
				var select = child(div_3);
				var option = child(select);
				option.value = option.__value = "64";
				var option_1 = sibling(option);
				option_1.value = option_1.__value = "72";
				reset(select);
				var select_value;
				init_select(select);
				var input = sibling(select, 2);
				remove_input_defaults(input);
				bind_this(input, ($$value) => set(searchBox, $$value), () => get(searchBox));
				var select_1 = sibling(input, 2);
				each(select_1, 21, () => Object.entries(FILTERS), ([k, v]) => k, ($$anchor, $$item) => {
					var $$array = /* @__PURE__ */ user_derived(() => to_array(get($$item), 2));
					let k = () => get($$array)[0];
					let v = () => get($$array)[1];
					var option_2 = root_4$1();
					var text_7 = only_child(option_2, true);
					var option_2_value = {};
					template_effect(() => {
						set_text(text_7, v());
						if (option_2_value !== (option_2_value = k())) option_2.value = (option_2.__value = option_2_value) ?? "";
					});
					append($$anchor, option_2);
				});
				reset(select_1);
				init_select(select_1);
				var select_2 = sibling(select_1, 2);
				each(select_2, 21, () => Object.entries(GROUPS), ([k, v]) => k, ($$anchor, $$item) => {
					var $$array_1 = /* @__PURE__ */ user_derived(() => to_array(get($$item), 2));
					let k = () => get($$array_1)[0];
					let v = () => get($$array_1)[1];
					var option_3 = root_4$1();
					var text_8 = only_child(option_3, true);
					var option_3_value = {};
					template_effect(() => {
						set_text(text_8, v());
						if (option_3_value !== (option_3_value = k())) option_3.value = (option_3.__value = option_3_value) ?? "";
					});
					append($$anchor, option_3);
				});
				reset(select_2);
				init_select(select_2);
				var select_3 = sibling(select_2, 2);
				each(select_3, 20, () => PAGE_SIZES, (n) => n, ($$anchor, n) => {
					var option_4 = root_4$1();
					var text_9 = only_child(option_4);
					var option_4_value = {};
					template_effect(() => {
						set_text(text_9, `${n ?? ""}${get(groupBy) ? " groups" : " pairs"} per page`);
						if (option_4_value !== (option_4_value = n)) option_4.value = (option_4.__value = option_4_value) ?? "";
					});
					append($$anchor, option_4);
				});
				reset(select_3);
				init_select(select_3);
				reset(div_3);
				var node_4 = sibling(div_3, 2);
				pager(node_4);
				var div_4 = sibling(node_4, 2);
				var node_5 = child(div_4);
				var consequent_3 = ($$anchor) => {
					var fragment_3 = comment();
					each(first_child(fragment_3), 17, () => get(visible), (group) => get(groupBy) + group.key, ($$anchor, group) => {
						GroupSection($$anchor, {
							get store() {
								return store();
							},
							get group() {
								return get(group);
							},
							get by() {
								return get(groupBy);
							},
							get editor() {
								return editor();
							},
							get openGroups() {
								return openGroups;
							}
						});
					});
					append($$anchor, fragment_3);
				};
				var alternate = ($$anchor) => {
					var fragment_5 = comment();
					each(first_child(fragment_5), 17, () => get(visible), (row) => row.id, ($$anchor, row) => {
						PairRow($$anchor, {
							get store() {
								return store();
							},
							get row() {
								return get(row);
							},
							get editor() {
								return editor();
							}
						});
					});
					append($$anchor, fragment_5);
				};
				if_block(node_5, ($$render) => {
					if (get(grouped)) $$render(consequent_3);
					else $$render(alternate, -1);
				});
				var node_8 = sibling(node_5, 2);
				var consequent_4 = ($$anchor) => {
					append($$anchor, root_5$1());
				};
				if_block(node_8, ($$render) => {
					if (!get(rows).length) $$render(consequent_4);
				});
				reset(div_4);
				pager(sibling(div_4, 2));
				reset(section);
				template_effect(($0, $1, $2, $3) => {
					if (select_value !== (select_value = $3)) select.value = (select.__value = select_value) ?? "", select_option(select, select_value);
					set_value(input, get(query));
				}, [
					() => get(buildable).length.toLocaleString(),
					() => get(stale).length.toLocaleString(),
					() => store().combine.status === "running" ? store().combine.message : store().combine.status === "error" ? store().combine.message + " You can retry." : `${get(buildable).length.toLocaleString()} ready side pairs not built yet or built from older drawings · ${(store().run?.count || 0).toLocaleString()} built`,
					() => String(store().size)
				]);
				delegated("change", select, setSize);
				delegated("input", input, search);
				delegated("change", select_1, restart);
				bind_select_value(select_1, () => get(filter), ($$value) => set(filter, $$value));
				delegated("change", select_2, restart);
				bind_select_value(select_2, () => get(groupBy), ($$value) => set(groupBy, $$value));
				delegated("change", select_3, restart);
				bind_select_value(select_3, () => get(pageSize), ($$value) => set(pageSize, $$value));
			}
			template_effect(($0, $1, $2, $3) => {
				button_1.disabled = store().combine.status === "running" || !get(buildable).length;
				set_text(text_2, `Build ${$0 ?? ""} side pair${get(buildable).length === 1 ? "" : "s"}`);
				button_2.disabled = store().combine.status === "running" || !get(stale).length;
				set_text(text_3, `Rebuild ${$1 ?? ""} stale pair${get(stale).length === 1 ? "" : "s"}`);
				set_text(text_4, $2);
			}, [
				() => get(buildable).length.toLocaleString(),
				() => get(stale).length.toLocaleString(),
				() => store().combine.status === "running" ? store().combine.message : store().combine.status === "error" ? store().combine.message + " You can retry." : `${get(buildable).length.toLocaleString()} ready side pairs not built yet or built from older drawings · ${(store().run?.count || 0).toLocaleString()} built`,
				() => String(store().size)
			]);
			delegated("click", button_1, () => store().buildPairs(get(buildable), "Building"));
			delegated("click", button_2, rebuildStale);
			append($$anchor, fragment_2);
		};
		if_block(node, ($$render) => {
			if (!store().ready) $$render(consequent_1);
			else $$render(alternate_1, -1);
		});
		reset(div);
		bind_this(div, ($$value) => set(host, $$value), () => get(host));
		var node_10 = sibling(div, 2);
		PartInspect(node_10, {});
		LayoutEditorDialog(sibling(node_10, 2), { get editor() {
			return editor();
		} });
		template_effect(() => set_text(text, `Work on each pair as Original → Main → Sub → Combined: one ${get(sizes).main ?? ""}-unit main and one ${get(sizes).sub ?? ""}×${get(sizes).sub ?? ""} sub. Group by main or sub to see where an icon is reused. Finished outputs live on Experiment › Side combination.`));
		append($$anchor, fragment);
		pop();
	}
	delegate([
		"click",
		"change",
		"input"
	]);
	//#endregion
	//#region side-pairs/src/components/PairSection.svelte
	var root = /* @__PURE__ */ from_html(`<span> </span>`);
	var root_1 = /* @__PURE__ */ from_html(`<img class="side-pair-result" loading="lazy"/>`);
	var root_2 = /* @__PURE__ */ from_html(`<p> </p> <!>`, 1);
	var root_3 = /* @__PURE__ */ from_html(`<p class="muted">Not on the Side combination page yet. Pick its main and sub icons to save it.</p>`);
	var root_4 = /* @__PURE__ */ from_html(`<button type="button" class="brief-edit login-only"> </button>`);
	var root_5 = /* @__PURE__ */ from_html(`<p class="side-pair-message" role="status"> <a>Open it →</a></p>`);
	var root_6 = /* @__PURE__ */ from_html(`<a>All saved side pairs →</a>`);
	var root_7 = /* @__PURE__ */ from_html(`<section class="component-brief side-pair"><div class="side-pair-head"><strong>Side pair</strong> <!></div> <!> <!><!><!></section>`);
	function PairSection($$anchor, $$props) {
		push($$props, true);
		user_effect(() => {
			loadPair($$props.row.uuid);
		});
		const saved = /* @__PURE__ */ user_derived(() => pairs.get($$props.row.uuid));
		const form = /* @__PURE__ */ user_derived(() => forms.get($$props.row.uuid));
		var section = root_7();
		var div = child(section);
		var node = sibling(child(div), 2);
		var consequent = ($$anchor) => {
			const computed_const = /* @__PURE__ */ user_derived(() => {
				const [label, tone] = STATUS[get(saved).status] || STATUS.waiting;
				return {
					label,
					tone
				};
			});
			var span = root();
			var text = only_child(span, true);
			template_effect(() => {
				set_class(span, 1, "badge " + get(computed_const).tone);
				set_text(text, get(computed_const).label);
			});
			append($$anchor, span);
		};
		if_block(node, ($$render) => {
			if (get(saved)) $$render(consequent);
		});
		reset(div);
		var node_1 = sibling(div, 2);
		var consequent_2 = ($$anchor) => {
			var fragment = root_2();
			var p = first_child(fragment);
			var text_1 = only_child(p);
			var node_2 = sibling(p, 2);
			var consequent_1 = ($$anchor) => {
				var img = root_1();
				template_effect(($0) => {
					set_attribute(img, "src", $0);
					set_attribute(img, "alt", $$props.row.concept + " — combined");
				}, [() => combinedURL($$props.row.uuid, get(saved).row.generated?.at)]);
				append($$anchor, img);
			};
			if_block(node_2, ($$render) => {
				if (!get(form) && get(saved).status === "generated") $$render(consequent_1);
			});
			template_effect(($0, $1) => set_text(text_1, `Main: ${$0 ?? ""} · Sub: ${$1 ?? ""} · ${(POSITIONS[get(saved).row.position] || "position not set") ?? ""}`), [() => partName(get(saved).row, "main"), () => partName(get(saved).row, "sub")]);
			append($$anchor, fragment);
		};
		var consequent_3 = ($$anchor) => {
			append($$anchor, root_3());
		};
		if_block(node_1, ($$render) => {
			if (get(saved)) $$render(consequent_2);
			else if (!get(form)) $$render(consequent_3, 1);
		});
		var node_3 = sibling(node_1, 2);
		var consequent_4 = ($$anchor) => {
			PairPicker($$anchor, { get row() {
				return $$props.row;
			} });
		};
		var alternate = ($$anchor) => {
			var button = root_4();
			var text_2 = only_child(button, true);
			template_effect(() => set_text(text_2, get(saved) ? "Change side pair" : "Make side pair"));
			delegated("click", button, () => openForm($$props.row));
			append($$anchor, button);
		};
		if_block(node_3, ($$render) => {
			if (get(form)) $$render(consequent_4);
			else $$render(alternate, -1);
		});
		var node_4 = sibling(node_3);
		var consequent_5 = ($$anchor) => {
			var p_2 = root_5();
			var text_3 = child(p_2, true);
			var a = sibling(text_3);
			reset(p_2);
			template_effect(($0, $1) => {
				set_text(text_3, $0);
				set_attribute(a, "href", $1);
			}, [() => notices.get($$props.row.uuid), () => "primitives.html?view=side&q=" + encodeURIComponent($$props.row.uuid)]);
			append($$anchor, p_2);
		};
		var d = /* @__PURE__ */ user_derived(() => !get(form) && notices.has($$props.row.uuid));
		if_block(node_4, ($$render) => {
			if (get(d)) $$render(consequent_5);
		});
		var node_5 = sibling(node_4);
		var consequent_6 = ($$anchor) => {
			var a_1 = root_6();
			template_effect(() => set_attribute(a_1, "href", TRACK));
			append($$anchor, a_1);
		};
		if_block(node_5, ($$render) => {
			if (get(saved) || get(form)) $$render(consequent_6);
		});
		reset(section);
		append($$anchor, section);
		pop();
	}
	delegate(["click"]);
	//#endregion
	//#region side-pairs/src/lib/store.svelte.js
	var data = () => window.SideData;
	var SideStore = class {
		#version = /* @__PURE__ */ state$1(0);
		get version() {
			return get(this.#version);
		}
		set version(value) {
			set(this.#version, value, true);
		}
		#pairsVersion = /* @__PURE__ */ state$1(0);
		get pairsVersion() {
			return get(this.#pairsVersion);
		}
		set pairsVersion(value) {
			set(this.#pairsVersion, value, true);
		}
		#loading = /* @__PURE__ */ state$1(false);
		get loading() {
			return get(this.#loading);
		}
		set loading(value) {
			set(this.#loading, value, true);
		}
		#error = /* @__PURE__ */ state$1("");
		get error() {
			return get(this.#error);
		}
		set error(value) {
			set(this.#error, value, true);
		}
		#status = /* @__PURE__ */ state$1("");
		get status() {
			return get(this.#status);
		}
		set status(value) {
			set(this.#status, value, true);
		}
		#ready = /* @__PURE__ */ state$1(false);
		get ready() {
			return get(this.#ready);
		}
		set ready(value) {
			set(this.#ready, value, true);
		}
		#size = /* @__PURE__ */ state$1(64);
		get size() {
			return get(this.#size);
		}
		set size(value) {
			set(this.#size, value, true);
		}
		#combine = /* @__PURE__ */ state$1(proxy({
			status: "idle",
			message: ""
		}));
		get combine() {
			return get(this.#combine);
		}
		set combine(value) {
			set(this.#combine, value, true);
		}
		pairs = /* @__PURE__ */ new Map();
		previews = {};
		components = null;
		componentStatus = {
			main: /* @__PURE__ */ new Map(),
			sub: /* @__PURE__ */ new Map()
		};
		reviews = {};
		statuses = {};
		run = null;
		catalog = {
			rows: [],
			references: {}
		};
		rendered = new SvelteMap();
		#queue = [];
		#active = 0;
		constructor(size) {
			this.size = data().setSize(size);
		}
		touch() {
			this.version++;
		}
		sizes() {
			return data().sizes();
		}
		item(id) {
			return data().item(id);
		}
		flagged = (item) => !!window.SideRepairFlags?.flagged(item);
		async setSize(size) {
			this.size = data().setSize(size);
			this.ready = false;
			this.pairs = /* @__PURE__ */ new Map();
			this.previews = {};
			this.rendered.clear();
			this.componentStatus = {
				main: /* @__PURE__ */ new Map(),
				sub: /* @__PURE__ */ new Map()
			};
			await this.load();
		}
		async load() {
			if (this.loading) return;
			this.loading = true;
			try {
				const got = await data().load();
				this.catalog = got.catalog;
				this.pairs = got.pairs;
				this.previews = got.previews;
				this.error = "";
				this.components = got.components;
				this.reviews = got.reviews;
				this.run = got.run;
				this.statuses = got.statuses;
				if (Object.keys(this.reviews).length) window.SideRepairFlags?.setReviews(this.reviews);
				this.componentStatus = {
					main: /* @__PURE__ */ new Map(),
					sub: /* @__PURE__ */ new Map()
				};
				for (const item of [...this.components.mains, ...this.components.subs]) item.status = item.drawings.some((d) => usable(this, d)) ? "done" : item.drawings.length ? "failing" : "missing";
				for (const [role, list] of [["main", this.components.mains], ["sub", this.components.subs]]) for (const item of list) for (const id of item.source_ids) this.componentStatus[role].set(id, item.status);
				this.madeStatuses();
				this.ready = true;
				this.pairsVersion++;
			} catch (error) {
				this.error = error.message;
			} finally {
				this.loading = false;
				this.touch();
			}
		}
		madeStatuses() {
			for (const pair of this.pairs.values()) for (const role of ["main", "sub"]) {
				const id = pair[role + "_id"], item = pair[role + "s"][0];
				if (!id || !item || this.componentStatus[role].get(id) === "done") continue;
				this.componentStatus[role].set(id, usable(this, {
					key: item.model_key,
					status: "pass"
				}) ? "done" : "failing");
			}
		}
		async refresh(id) {
			const got = await data().refresh(id).catch((error) => {
				this.status = error.message;
			});
			if (got) {
				this.pairs.set(id, got.pair);
				Object.assign(this.catalog.references, got.references);
				const rows = this.catalog.rows, at = rows.findIndex((r) => r.id === id);
				if (at < 0) rows.unshift(got.row);
				else rows[at] = got.row;
				if (got.preview) this.previews[id] = got.preview;
				else delete this.previews[id];
				this.madeStatuses();
			} else if (got === null) {
				this.pairs.delete(id);
				delete this.previews[id];
				this.catalog.rows = this.catalog.rows.filter((r) => r.id !== id);
			}
			if (got !== void 0) this.pairsVersion++;
			for (const k of [...this.rendered.keys()]) if (k.startsWith(id + "|")) this.rendered.delete(k);
			this.touch();
		}
		combined(pair, sub) {
			const prebuilt = this.previews[pair.id];
			if (prebuilt?.built) return prebuilt;
			return this.rendered.get(pair.id + "|" + sub.icon);
		}
		requestRender(pair, sub) {
			const k = pair.id + "|" + sub.icon;
			if (this.rendered.has(k) || this.#queue.some((q) => q.k === k)) return;
			this.#queue.push({
				k,
				pair
			});
			this.#drain();
		}
		#drain() {
			while (this.#active < 2 && this.#queue.length) {
				const { k, pair } = this.#queue.shift();
				this.#active++;
				data().compose(pair.id).then((c) => this.rendered.set(k, { result: {
					...c.result,
					svg: c.svg
				} })).catch((error) => this.rendered.set(k, { error: error.message })).finally(() => {
					this.#active--;
					this.#drain();
				});
			}
		}
		buildState(id) {
			return data().item(id)?.state;
		}
		handLayout(id) {
			return data().handLayout(id);
		}
		staleRoles(id) {
			return data().staleRoles(id);
		}
		async buildPairs(ids, label) {
			this.combine = {
				status: "running",
				message: `${label} 0 / ${ids.length}…`
			};
			try {
				const { results, skipped } = await data().buildPairs(ids, (n, total) => {
					this.combine = {
						status: "running",
						message: `${label} ${n.toLocaleString()} / ${total.toLocaleString()}…`
					};
				});
				const failed = results.filter((r) => !r.ok), unchanged = results.filter((r) => r.unchanged).length, waiting = results.filter((r) => r.ok && !r.unchanged && r.build_failed).length;
				this.combine = {
					status: "idle",
					message: ""
				};
				const done = results.filter((r) => r.ok).length.toLocaleString();
				this.status = (label === "Rebuilding" ? `Rebuilt ${done} stale side pairs.` : `Built ${done} side pairs.`) + (failed.length ? ` ${failed.length} refused (${failed[0].reference_id}: ${failed[0].error}).` : "") + (skipped.length ? ` ${skipped.length} could not be drawn (${skipped[0].reference_id}: ${skipped[0].error}).` : "") + (unchanged ? ` ${unchanged.toLocaleString()} came out the same as before (their Icon review status stays).` : "") + (waiting ? ` ${waiting.toLocaleString()} wait under Failed in Icon review until their main or sub is approved.` : "");
				this.ready = false;
				this.rendered.clear();
				await this.load();
			} catch (error) {
				this.combine = {
					status: "error",
					message: error.message
				};
			}
		}
	};
	//#endregion
	//#region side-pairs/src/main.js
	var params = new URLSearchParams(location.search);
	var app = null;
	var store = null;
	var editor = new LayoutEditor();
	window.addEventListener("side-component-approved", () => {
		if (store) {
			store.rendered.clear();
			store.load();
		}
	});
	document.addEventListener("side-repair-flags-change", () => store?.touch());
	function show(host, page) {
		if (app && host.contains(app.host)) return;
		if (app) unmount(app.component);
		store ??= new SideStore(params.get("grid") === "72" ? 72 : 64);
		if (!store.ready && !store.loading) store.load();
		const element = document.createElement("div");
		host.replaceChildren(element);
		app = {
			host: element,
			component: mount(App, {
				target: element,
				props: {
					store,
					editor,
					page,
					params
				}
			})
		};
	}
	function hide() {
		if (app) {
			unmount(app.component);
			app = null;
		}
	}
	var cards = /* @__PURE__ */ new Set();
	function section(row) {
		for (const card of [...cards]) if (!card.element.isConnected) {
			unmount(card.component);
			cards.delete(card);
		}
		const element = document.createElement("div");
		element.className = "side-pair-card";
		cards.add({
			element,
			component: mount(PairSection, {
				target: element,
				props: { row }
			})
		});
		return element;
	}
	window.SidePairMaker = {
		section,
		editing: () => forms.size > 0
	};
	//#endregion
	exports.hide = hide;
	exports.show = show;
	return exports;
})({});
