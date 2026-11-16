    // ==================== DATA ====================
    const CONCEPTS = /*CONCEPTS_JSON*/;
    const CATS = /*CATS_JSON*/;
    const plain = (s) => String(s).replace(/&amp;/g, '&');
    const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
    const ic = (n, c = 'w-4 h-4') => `<i data-lucide="${n}" class="${c}"></i>`;
    const card = (inner, cls = '') => `<div class="card rounded-2xl p-5 sm:p-6 ${cls}">${inner}</div>`;
    const ls = { get: (k, d) => { try { const v = JSON.parse(localStorage.getItem(k)); return v === null ? d : v; } catch (e) { return d; } }, set: (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} } };
    const KEY = { unlock: 'felron_demo_unlock_v1', prog: 'felron_member_prog_v2', quiz: 'felron_member_quiz_v2', track: 'felron_member_track_v1', triage: 'felron_triage_v1' };
    const money = (x, d = 0) => (x < 0 ? '-' : '') + '$' + Math.abs(x).toLocaleString(undefined, { minimumFractionDigits: d, maximumFractionDigits: d });

    // ==================== ROUTER ====================
    const VIEWS = ['home', 'services', 'how', 'pricing', 'roi', 'codex', 'lab', 'flywheel', 'dispatch', 'members', 'about', 'contact', 'book', 'legal', 'waiver'];
    const TITLES = { home: 'Before the Lawyer. Before the CPA. Call FelRon First.', services: 'Services', how: 'How It Works', pricing: 'Pricing', roi: 'Machine ROI & Sourcing', codex: 'Concept Codex & Vault', lab: 'LEAPS & Perps Lab', flywheel: 'Capital Flywheel', dispatch: 'First-Call Dispatch', members: 'Members Preview', about: 'About', contact: 'Contact', book: 'Book & Enroll', legal: 'Legal Framework', waiver: 'Client Acknowledgment' };
    const TOOLVIEWS = ['roi', 'codex', 'lab', 'flywheel', 'dispatch'];
    function currentView() { const h = (location.hash.replace(/^#\/?/, '').split('?')[0] || 'home'); return VIEWS.includes(h) ? h : 'home'; }
    function hashParam(name) { return new URLSearchParams(location.hash.split('?')[1] || '').get(name); }
    const CH = {};
    function clearHosts() {
      Object.keys(CH).forEach((k) => { try { CH[k].destroy(); } catch (e) {} delete CH[k]; });
      TOOLVIEWS.forEach((t) => { const h = document.getElementById('host-' + t); if (h) h.innerHTML = ''; });
      const mb = document.getElementById('m-body'); if (mb) mb.innerHTML = '';
    }
    function route() {
      if (location.hash && !location.hash.startsWith('#/')) return;
      const id = currentView();
      document.querySelectorAll('.view').forEach((v) => v.classList.toggle('on', v.id === 'view-' + id));
      document.querySelectorAll('[data-nav]').forEach((a) => a.classList.toggle('active', a.dataset.nav === id));
      document.getElementById('mobile-menu').classList.add('hidden');
      document.title = 'FelRon IT-Legacy-Capital | ' + TITLES[id];
      clearHosts();
      if (TOOLVIEWS.includes(id)) renderTool(id, document.getElementById('host-' + id), false);
      if (id === 'book') initEnroll();
      if (id === 'members') initMembers();
      window.scrollTo(0, 0);
      refreshIcons();
    }
    function toggleMenu() { document.getElementById('mobile-menu').classList.toggle('hidden'); }
    function refreshIcons() { if (window.lucide) lucide.createIcons(); }
    window.addEventListener('hashchange', route);
    function renderTool(id, host, full) {
      ({ roi: toolROI, codex: toolCodex, lab: toolLab, flywheel: toolFlywheel, dispatch: toolDispatch, estimate: toolEstimate }[id])(host, full);
      refreshIcons();
    }
    function copyText(t) {
      const done = () => { const el = document.getElementById('toast'); el.classList.remove('hidden'); setTimeout(() => el.classList.add('hidden'), 2000); };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(done).catch(() => {});
      else { const a = document.createElement('textarea'); a.value = t; document.body.appendChild(a); a.select(); try { document.execCommand('copy'); done(); } catch (e) {} a.remove(); }
    }
    function lockedTeaser(title, text) {
      return `<div class="relative rounded-2xl overflow-hidden border-2 border-dashed border-gold-400/40 p-6 sm:p-8 text-center space-y-3 bg-navy-900/60"><span class="icon-tile mx-auto">${ic('lock', 'w-5 h-5')}</span><div class="eyebrow">Members only</div><h3 class="serif text-2xl font-bold text-white">${title}</h3><p class="text-sm text-gray-400 max-w-xl mx-auto">${text}</p><div class="flex flex-wrap gap-3 justify-center"><a href="#/members" class="btn-gold">${ic('lock-open')}Preview the members area</a><a href="#/pricing" class="btn-ghost">See packages</a></div></div>`;
    }
    const chartColors = { gold: '#d4af37', goldA: 'rgba(212,175,55,.18)', grey: '#94a3b8', grid: 'rgba(148,163,184,.12)' };
    function mkChart(key, canvas, cfg) {
      if (!window.Chart || !canvas) return;
      if (CH[key]) CH[key].destroy();
      Chart.defaults.color = '#cbd5e1'; Chart.defaults.font.family = 'JetBrains Mono, monospace'; Chart.defaults.font.size = 11;
      cfg.options = Object.assign({ responsive: true, maintainAspectRatio: false, animation: false, plugins: { legend: { labels: { boxWidth: 14 } } } }, cfg.options || {});
      CH[key] = new Chart(canvas, cfg);
    }
    const sl = (id, label, min, max, step, val, fmt, on) => `<div class="space-y-1"><div class="rowlbl"><span>${label}</span><b id="${id}-v">${fmt(val)}</b></div><input type="range" id="${id}" min="${min}" max="${max}" step="${step}" value="${val}" oninput="${on}" /></div>`;
    const kpi = (id, label, sub = '') => `<div class="kpi"><div class="l">${label}</div><div class="v" id="${id}">–</div><div class="l" id="${id}-s">${sub}</div></div>`;
    const setT = (id, t) => { const e = document.getElementById(id); if (e) e.textContent = t; };
    const num = (id) => parseFloat(document.getElementById(id).value);

    // ==================== INTAKE ====================
    function intakeMsg(p) {
      const v = (s) => document.getElementById(p + '-' + s).value.trim();
      const pref = (document.querySelector(`input[name="${p}-pref"]:checked`) || {}).value || 'Call';
      return { text: `Hi Matthew,\n\nMy name is ${v('name') || '[first name]'}.\nThe friction: ${v('type')}\nWhat's going on: ${v('desc') || '[a sentence or two]'}\n\nBest way to reach me: ${pref} at ${v('reach') || '[phone or email]'}\n\n(Sent from the FelRon website)`, type: v('type') };
    }
    function updateIntake(p) {
      const m = intakeMsg(p);
      document.getElementById(p + '-sms').href = 'sms:+12105354987?&body=' + encodeURIComponent(m.text);
      document.getElementById(p + '-mail').href = 'mailto:MattDiazSA@gmail.com?subject=' + encodeURIComponent('FelRon: ' + m.type) + '&body=' + encodeURIComponent(m.text);
    }

    // ==================== ENROLL ====================
    const ENROLL = [
      { id: 'starter', label: 'Starter package ($75)', detail: ['Any 3 learning modules', 'One 1-hour walkthrough session', '3 months of the FelRon App and members area'] },
      { id: 'builder', label: 'Builder package ($175)', detail: ['All ' + CONCEPTS.length + ' learning modules + the full Concept Vault', '3 walkthrough sessions', '6 months of the FelRon App: every tool, quiz and worksheet'] },
      { id: 'full', label: 'Full-Service (from $375 or $75/mo)', detail: ['Everything in Builder', 'Quote gathering and comparison', 'Hands-on help and handyman coordination', 'Machine sourcing and plug-in setup'] },
      { id: 'hourly', label: 'Hands-on help or a single session ($30–50/hr)', detail: ['Handyman fixes, IT help, machine setup, errands or a walkthrough', 'Bigger jobs quoted upfront', 'Written recap included'] },
      { id: 'quotes', label: 'Get my quotes gathered and compared', detail: ['I make the calls', 'Side-by-side comparison of price, scope, warranty and timeline', 'Billed hourly, quoted upfront'] },
      { id: 'handyman', label: 'Painting or handyman job (quoted per job)', detail: ['I line up the handyman I work with', 'I coordinate the job and keep you updated'] },
      { id: 'machine', label: 'Crypto machine sourcing & plug-in setup', detail: ['Vendor quote audit and sourcing', 'Plug-in setup and pool configuration', '12-month ROI outlook'] },
      { id: 'module', label: 'A single learning module ($29)', detail: ['Lesson + 1-on-1 walkthrough', 'Vault deliverables and quiz in the members area'] },
      { id: 'app', label: 'The FelRon App only ($9.50/mo or $49/yr)', detail: ['Members area, Concept Vault, tools, guides and worksheets'] },
      { id: 'unsure', label: 'Not sure yet: book the free 15-min call', detail: ['We figure out the right fit together'] }
    ];
    function initEnroll() {
      const sel = document.getElementById('enroll-item');
      if (!sel.options.length) sel.innerHTML = ENROLL.map((o) => `<option value="${o.id}">${o.label}</option>`).join('');
      const want = hashParam('item'); if (want && ENROLL.some((o) => o.id === want)) sel.value = want;
      updateEnroll();
    }
    function updateEnroll() {
      const o = ENROLL.find((x) => x.id === document.getElementById('enroll-item').value) || ENROLL[0];
      document.getElementById('enroll-summary').innerHTML = `<div class="font-bold text-white">${o.label}</div>` + o.detail.map((d) => `<div>✓ ${d}</div>`).join('') + '<div class="text-xs text-gray-500 pt-1">Starting price, subject to change. Confirmed in writing before payment.</div>';
      const body = 'Hi Matthew,\n\nI\'d like to book a free 15-minute first call.\nInterested in: ' + o.label + '\nBest times to reach me: \n\nThanks!';
      document.getElementById('enroll-mail').href = 'mailto:MattDiazSA@gmail.com?subject=' + encodeURIComponent('FelRon: book my free first call') + '&body=' + encodeURIComponent(body);
    }

    // ==================== TOOL: MACHINE ROI & SOURCING ====================
    const ROI_PRESETS = {
      z15: { label: 'Antminer Z15 (Equihash)', count: 1, volt: 240, circ: 20, vendor: 1650, target: 1250, watts: 1510, rate: 0.095, yld: 7.80 },
      z9: { label: '4x Antminer Z9 Mini Cluster', count: 4, volt: 240, circ: 20, vendor: 620, target: 450, watts: 430, rate: 0.095, yld: 2.35 },
      gpu: { label: '24GB GPU DePIN AI Compute Node', count: 1, volt: 120, circ: 15, vendor: 2400, target: 1850, watts: 450, rate: 0.095, yld: 4.20 }
    };
    let roiPreset = 'z15';
    const SOURCING_STEPS = ['Confirm the exact model, hashrate and wattage you are targeting.', 'Collect at least three seller quotes and compute price-per-hash for each.', 'Request hashboard photos, chip-test screenshots, PSU model and serial number.', 'Confirm warranty or return terms in writing; pay with a traceable method.', 'Inspect on arrival: fans, boards, connectors and a burn-in test.', 'Plan circuit load (80% rule), airflow, noise and a PDU if needed.', 'Plug in, set a static IP and configure primary + failover pools.', 'Log daily yield vs. kWh cost and schedule cleaning every 1–3 months.'];
    function toolROI(host, full) {
      const p = ROI_PRESETS[roiPreset];
      const f0 = (x) => '$' + Math.round(x).toLocaleString(), f2 = (x) => '$' + (+x).toFixed(2), f3 = (x) => '$' + (+x).toFixed(3);
      host.innerHTML = `<div class="space-y-6">
        <div class="flex flex-wrap gap-2">${Object.entries(ROI_PRESETS).map(([k, v]) => `<button class="chip ${k === roiPreset ? 'on' : ''}" onclick="roiPreset='${k}';renderTool('roi',this.closest('[data-host]'),${full})">${v.label}</button>`).join('')}</div>
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
          ${card(`<div class="eyebrow mb-3">Machine &amp; site inputs</div><div class="space-y-4">
            <div class="grid grid-cols-3 gap-2"><label class="text-xs text-gray-400">Units<input id="r-count" type="number" min="1" max="50" value="${p.count}" class="field !py-1.5 mt-1" oninput="calcROI()" /></label>
            <label class="text-xs text-gray-400">Volts<select id="r-volt" class="field !py-1.5 mt-1" onchange="calcROI()">${[120, 240].map((v) => `<option ${v === p.volt ? 'selected' : ''}>${v}</option>`).join('')}</select></label>
            <label class="text-xs text-gray-400">Circuit (A)<select id="r-circ" class="field !py-1.5 mt-1" onchange="calcROI()">${[15, 20, 30].map((v) => `<option ${v === p.circ ? 'selected' : ''}>${v}</option>`).join('')}</select></label></div>
            ${sl('r-vendor', 'Vendor quote / unit', 100, 6000, 10, p.vendor, f0, 'calcROI()')}
            ${sl('r-target', 'Sourced target / unit', 100, 6000, 10, p.target, f0, 'calcROI()')}
            ${sl('r-watts', 'Power draw / unit (W)', 100, 4000, 10, p.watts, (x) => x + ' W', 'calcROI()')}
            ${sl('r-rate', 'Electricity rate ($/kWh)', 0.05, 0.25, 0.005, p.rate, f3, 'calcROI()')}
            ${sl('r-yld', 'Est. gross yield / unit / day', 0, 30, 0.05, p.yld, f2, 'calcROI()')}
          </div>`, 'lg:col-span-5')}
          <div class="lg:col-span-7 space-y-4 min-w-0">
            <div class="grid grid-cols-2 gap-3">${kpi('r-k1', 'Sourcing savings')}${kpi('r-k2', 'Monthly power cost')}${kpi('r-k3', 'Monthly net yield')}${kpi('r-k4', 'Break-even (sourced)')}</div>
            <div id="r-audit" class="p-4 rounded-xl border text-sm leading-relaxed"></div>
            ${card(`<div class="flex items-center justify-between mb-2"><div class="font-bold text-white text-sm">12-month cumulative cash position</div><span class="text-[10px] font-mono text-gray-500 uppercase">hypothetical</span></div><div class="chart-box"><canvas id="r-chart"></canvas></div>`, '!p-4')}
          </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">${[['search-check', '01 • Sourcing &amp; inspection', 'I compare seller quotes, check board photos and test results, and confirm warranty terms before you pay.'], ['plug', '02 • Plug-in setup &amp; pool', 'I plug in, set the network and configure your pool with failover, then confirm hashrate on your dashboard.'], ['refresh-cw', '03 • Flywheel routing', 'You see what the machine nets monthly, and how I personally route compute yield in my own flywheel.']].map(([i, t, d]) => card(`<span class="icon-tile !w-10 !h-10">${ic(i)}</span><div class="font-bold text-white mt-3">${t}</div><p class="text-sm text-gray-400 mt-1">${d}</p>`)).join('')}</div>
        ${full ? card(`<div class="eyebrow">Member vault • procurement checklist</div><h3 class="serif text-2xl font-bold text-white mt-1">Source it right, step by step.</h3><ol class="mt-4 space-y-2">${SOURCING_STEPS.map((s, i) => `<li><label class="flex gap-3 items-start p-3 rounded-xl bg-navy-950/60 border border-gray-800 cursor-pointer"><input type="checkbox" class="mt-1" /><span class="text-sm text-gray-200"><span class="font-mono text-gold-300 font-bold mr-1.5">${String(i + 1).padStart(2, '0')}</span>${s}</span></label></li>`).join('')}</ol>`, 'border-gold-400/50') : lockedTeaser('Full procurement checklist &amp; price-per-hash benchmarks', 'Members get the step-by-step ASIC and DePIN sourcing checklist, the secondary-market benchmark sheet, the circuit load worksheet and the pool setup guide.')}
        <p class="text-xs text-gray-500">Illustration only. Yields, difficulty, coin prices and power rates change daily, and results are not guaranteed.</p>
      </div>`;
      host.setAttribute('data-host', '1');
      calcROI();
    }
    function calcROI() {
      const count = Math.max(1, num('r-count') || 1), volt = num('r-volt'), circ = num('r-circ'), vendor = num('r-vendor'), target = num('r-target'), watts = num('r-watts'), rate = num('r-rate'), yld = num('r-yld');
      setT('r-vendor-v', '$' + vendor.toLocaleString()); setT('r-target-v', '$' + target.toLocaleString()); setT('r-watts-v', watts + ' W'); setT('r-rate-v', '$' + rate.toFixed(3)); setT('r-yld-v', '$' + yld.toFixed(2));
      const kwh = watts * count / 1000 * 24 * 30.4, power = kwh * rate, gross = yld * count * 30.4, net = gross - power;
      const save = (vendor - target) * count, amps = watts * count / volt, cap = circ * 0.8;
      const be = net > 0 ? target * count / net : Infinity, beV = net > 0 ? vendor * count / net : Infinity;
      setT('r-k1', money(save)); setT('r-k1-s', 'vs. vendor quote');
      setT('r-k2', money(power, 2)); setT('r-k2-s', `${amps.toFixed(1)}A @ ${volt}V • ${Math.round(kwh).toLocaleString()} kWh`);
      setT('r-k3', money(net, 2)); setT('r-k3-s', 'gross ' + money(gross, 2) + '/mo');
      setT('r-k4', isFinite(be) ? be.toFixed(1) + ' mo' : 'Not at these inputs'); setT('r-k4-s', isFinite(beV) ? 'vs. ' + beV.toFixed(1) + ' mo at vendor quote' : 'adjust yield or power rate');
      const ok = amps <= cap, a = document.getElementById('r-audit');
      a.className = 'p-4 rounded-xl border text-sm leading-relaxed ' + (ok ? 'border-gold-400/40 bg-gold-400/5 text-gray-200' : 'border-amber-400/40 bg-amber-400/5 text-gray-200');
      a.innerHTML = `<strong class="text-gold-300">Sourcing audit:</strong> ${save > 0 ? `Sourcing at ${money(target)}/unit instead of ${money(vendor)} keeps ${money(save)} in your pocket${isFinite(be) && isFinite(beV) ? ` and reaches break-even ${(beV - be).toFixed(1)} months sooner` : ''}.` : 'The vendor quote is already at or below the sourced target.'} <strong class="text-gold-300">Load check:</strong> ${amps.toFixed(1)}A on a ${circ}A circuit ${ok ? `fits within the 80% continuous guideline (${cap}A).` : `is above the 80% continuous guideline (${cap}A). Plan an additional dedicated circuit; I can gather and compare quotes from licensed electricians.`}`;
      const m = [...Array(13).keys()];
      mkChart('roi', document.getElementById('r-chart'), { type: 'line', data: { labels: m.map((x) => 'M' + x), datasets: [
        { label: 'Sourced', data: m.map((x) => +(-target * count + net * x).toFixed(2)), borderColor: chartColors.gold, backgroundColor: chartColors.goldA, fill: true, tension: .25, pointRadius: 2 },
        { label: 'Vendor quote', data: m.map((x) => +(-vendor * count + net * x).toFixed(2)), borderColor: chartColors.grey, borderDash: [5, 4], tension: .25, pointRadius: 0 }
      ] }, options: { scales: { x: { grid: { color: chartColors.grid } }, y: { grid: { color: chartColors.grid }, ticks: { callback: (v) => '$' + v.toLocaleString() } } } } });
    }

    // ==================== TOOL: LEAPS & PERPS LAB ====================
    const LAB_PRESETS = {
      ladder: { label: '$5 LEAPS call ladder', strat: 'call', spot: 5, strike: 5, target: 8, dte: 240, iv: 60, n: 2 },
      strangle: { label: 'Protective strangle', strat: 'strangle', spot: 50, strike: 55, target: 40, dte: 60, iv: 45, n: 1 }
    };
    let labPreset = 'ladder', perpDir = 1;
    function nCdf(x) { const t = 1 / (1 + 0.2316419 * Math.abs(x)), d = 0.3989423 * Math.exp(-x * x / 2); const p = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274)))); return x > 0 ? 1 - p : p; }
    function bs(type, S, K, T, v, r = 0.045) {
      if (T <= 0) return { p: Math.max(0, type === 'c' ? S - K : K - S), d: type === 'c' ? (S > K ? 1 : 0) : (S < K ? -1 : 0) };
      const d1 = (Math.log(S / K) + (r + v * v / 2) * T) / (v * Math.sqrt(T)), d2 = d1 - v * Math.sqrt(T);
      return type === 'c' ? { p: S * nCdf(d1) - K * Math.exp(-r * T) * nCdf(d2), d: nCdf(d1) } : { p: K * Math.exp(-r * T) * nCdf(-d2) - S * nCdf(-d1), d: nCdf(d1) - 1 };
    }
    function legs(strat, S, K) { return strat === 'call' ? [['c', K]] : strat === 'put' ? [['p', K]] : [['c', K], ['p', Math.max(0.5, +(2 * S - K).toFixed(2))]]; }
    function posVal(lg, S, T, v) { return lg.reduce((a, [t, k]) => { const x = bs(t, S, k, T, v); return { p: a.p + x.p, d: a.d + x.d }; }, { p: 0, d: 0 }); }
    function toolLab(host, full) {
      const p = LAB_PRESETS[labPreset], f2 = (x) => '$' + (+x).toFixed(2);
      host.innerHTML = `<div class="space-y-8">
        <div class="space-y-4"><div class="flex flex-wrap items-center justify-between gap-3"><div><div class="eyebrow">Options payoff simulator</div><h3 class="serif text-2xl font-bold text-white">LEAPS ladders, strangles and the theta clock.</h3></div><div class="flex flex-wrap gap-2">${Object.entries(LAB_PRESETS).map(([k, v]) => `<button class="chip ${k === labPreset ? 'on' : ''}" onclick="labPreset='${k}';renderTool('lab',this.closest('[data-host]'),${full})">${v.label}</button>`).join('')}</div></div>
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
          ${card(`<div class="space-y-4"><label class="text-xs text-gray-400 block">Strategy<select id="o-strat" class="field !py-1.5 mt-1" onchange="calcLab()">${[['call', 'Long call (LEAPS)'], ['put', 'Long put (protection)'], ['strangle', 'Long strangle (call + put)']].map(([k, l]) => `<option value="${k}" ${k === p.strat ? 'selected' : ''}>${l}</option>`).join('')}</select></label>
            ${sl('o-spot', 'Stock price today', 1, 500, 0.5, p.spot, f2, 'calcLab()')}
            ${sl('o-strike', 'Call strike', 1, 500, 0.5, p.strike, f2, 'calcLab()')}
            ${sl('o-target', 'Target price at expiry', 0.5, 600, 0.5, p.target, f2, 'calcLab()')}
            ${sl('o-dte', 'Days to expiration', 7, 760, 1, p.dte, (x) => x + ' d', 'calcLab()')}
            ${sl('o-iv', 'Implied volatility', 10, 150, 1, p.iv, (x) => x + '%', 'calcLab()')}
            ${sl('o-n', 'Contracts', 1, 20, 1, p.n, (x) => x, 'calcLab()')}</div>`, 'lg:col-span-5')}
          <div class="lg:col-span-7 space-y-4 min-w-0">
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-3">${kpi('o-k1', 'Premium paid (max loss)')}${kpi('o-k2', 'Break-even at expiry')}${kpi('o-k3', 'P/L at target')}${kpi('o-k4', 'Trim gate (+20%)')}${kpi('o-k5', 'Delta • leverage')}${kpi('o-k6', 'Theta zone')}</div>
            <div id="o-note" class="p-4 rounded-xl border border-gold-400/40 bg-gold-400/5 text-sm text-gray-200 leading-relaxed"></div>
            ${card(`<div class="flex items-center justify-between mb-2"><div class="font-bold text-white text-sm">Payoff: today vs. at expiration</div><span class="text-[10px] font-mono text-gray-500 uppercase">Black-Scholes estimate</span></div><div class="chart-box"><canvas id="o-chart"></canvas></div>`, '!p-4')}
          </div></div></div>
        <div class="space-y-4"><div><div class="eyebrow">Perpetual futures calculator</div><h3 class="serif text-2xl font-bold text-white">Liquidation distance, P/L and funding.</h3></div>
          ${full ? perpsUI() : `<div class="relative"><div class="locked-blur pointer-events-none select-none" aria-hidden="true">${perpsUI()}</div><div class="absolute inset-0 flex items-center justify-center p-4">${lockedTeaser('The perps calculator lives in the members area', 'Model isolated margin, leverage, liquidation price, unrealized P/L and funding drag on hypothetical positions.')}</div></div>`}
        </div>
        <p class="text-xs text-gray-500">Education and simulation only, not a recommendation. Options can lose 100% of the premium; leveraged futures can be liquidated. Estimates use a simplified pricing model.</p>
      </div>`;
      host.setAttribute('data-host', '1');
      calcLab(); calcPerp();
    }
    function perpsUI() {
      const f2 = (x) => '$' + (+x).toFixed(2);
      return `<div class="grid grid-cols-1 lg:grid-cols-12 gap-6">${card(`<div class="space-y-4"><div class="flex gap-2"><button id="pp-long" class="seg-btn ${perpDir === 1 ? 'on' : ''}" onclick="perpDir=1;calcPerp()">Long</button><button id="pp-short" class="seg-btn ${perpDir === -1 ? 'on' : ''}" onclick="perpDir=-1;calcPerp()">Short</button></div>
        ${sl('pp-margin', 'Isolated margin', 50, 10000, 50, 500, (x) => '$' + x, 'calcPerp()')}
        ${sl('pp-lev', 'Leverage', 1, 20, 1, 5, (x) => x + 'x', 'calcPerp()')}
        ${sl('pp-entry', 'Entry price', 1, 1000, 0.5, 245, f2, 'calcPerp()')}
        ${sl('pp-mark', 'Mark price', 1, 1000, 0.5, 260, f2, 'calcPerp()')}
        ${sl('pp-fund', 'Funding rate per 8h', -0.05, 0.05, 0.005, 0.01, (x) => (+x).toFixed(3) + '%', 'calcPerp()')}</div>`, 'lg:col-span-5')}
        <div class="lg:col-span-7 space-y-3 min-w-0"><div class="grid grid-cols-2 gap-3">${kpi('pp-k1', 'Position notional')}${kpi('pp-k2', 'Est. liquidation price')}${kpi('pp-k3', 'Unrealized P/L')}${kpi('pp-k4', 'Funding per day')}</div>
        <div id="pp-note" class="p-4 rounded-xl border border-gray-800 bg-navy-950/60 text-sm text-gray-300"></div></div></div>`;
    }
    function calcLab() {
      const strat = document.getElementById('o-strat').value, S = num('o-spot'), K = num('o-strike'), X = num('o-target'), dte = num('o-dte'), v = num('o-iv') / 100, n = num('o-n'), T = dte / 365;
      [['o-spot', '$' + S.toFixed(2)], ['o-strike', '$' + K.toFixed(2)], ['o-target', '$' + X.toFixed(2)], ['o-dte', dte + ' d'], ['o-iv', Math.round(v * 100) + '%'], ['o-n', n]].forEach(([i, t]) => setT(i + '-v', t));
      const lg = legs(strat, S, K), now = posVal(lg, S, T, v), prem = now.p, cost = prem * 100 * n;
      const intr = (s) => lg.reduce((a, [t, k]) => a + Math.max(0, t === 'c' ? s - k : k - s), 0);
      const pl = (intr(X) - prem) * 100 * n, theta = (posVal(lg, S, Math.max(0, T - 1 / 365), v).p - prem) * 100 * n;
      const lev = cost > 0 ? Math.abs(now.d) * S * 100 * n / cost : 0;
      const be = strat === 'call' ? '$' + (K + prem).toFixed(2) : strat === 'put' ? '$' + (K - prem).toFixed(2) : '$' + (lg[1][1] - prem).toFixed(2) + ' / $' + (K + prem).toFixed(2);
      setT('o-k1', money(cost, 2)); setT('o-k1-s', '$' + prem.toFixed(2) + '/share');
      setT('o-k2', be); setT('o-k2-s', strat === 'strangle' ? 'put strike $' + lg[1][1].toFixed(2) : 'stock price needed');
      setT('o-k3', money(pl, 2)); setT('o-k3-s', (cost ? (pl / cost * 100).toFixed(0) : 0) + '% on premium');
      setT('o-k4', '$' + (prem * 1.2).toFixed(2)); setT('o-k4-s', 'contract price to start trimming');
      setT('o-k5', now.d.toFixed(2) + ' • ' + lev.toFixed(1) + 'x'); setT('o-k5-s', 'theta ' + money(theta, 2) + '/day');
      const zone = dte >= 180 ? 'SAFE' : dte >= 45 ? 'WATCH' : 'CLIFF'; setT('o-k6', zone); setT('o-k6-s', dte >= 180 ? '≥180 days: slow decay' : dte >= 45 ? '45–180 days: decay building' : '<45 days: decay accelerates');
      document.getElementById('o-note').innerHTML = `<strong class="text-gold-300">How I read it (education):</strong> ${zone === 'SAFE' ? 'Plenty of time on the clock, so daily decay is small relative to the premium.' : zone === 'WATCH' ? 'Decay is picking up. My own rule is to review the position and the trim plan weekly here.' : 'Inside 45 days time value melts fastest. My own rule is to have exited or rolled before this zone.'} My personal trim rule is to start scaling out once the contract trades above the +20% gate ($${(prem * 1.2).toFixed(2)}).`;
      const lo = Math.max(0.1, Math.min(S, X, K) * 0.4), hi = Math.max(S, X, K) * 1.6, pts = [...Array(31).keys()].map((i) => lo + (hi - lo) * i / 30);
      mkChart('lab', document.getElementById('o-chart'), { type: 'line', data: { labels: pts.map((x) => '$' + x.toFixed(x < 20 ? 2 : 0)), datasets: [
        { label: 'At expiration', data: pts.map((s) => +((intr(s) - prem) * 100 * n).toFixed(2)), borderColor: chartColors.gold, backgroundColor: chartColors.goldA, fill: true, pointRadius: 0, tension: 0 },
        { label: 'Today (est.)', data: pts.map((s) => +((posVal(lg, s, T, v).p - prem) * 100 * n).toFixed(2)), borderColor: chartColors.grey, borderDash: [5, 4], pointRadius: 0, tension: .3 }
      ] }, options: { scales: { x: { grid: { color: chartColors.grid }, ticks: { maxTicksLimit: 8 } }, y: { grid: { color: chartColors.grid }, ticks: { callback: (v) => '$' + v.toLocaleString() } } } } });
    }
    function calcPerp() {
      if (!document.getElementById('pp-margin')) return;
      const m = num('pp-margin'), L = num('pp-lev'), E = num('pp-entry'), M = num('pp-mark'), fr = num('pp-fund');
      [['pp-margin', '$' + m], ['pp-lev', L + 'x'], ['pp-entry', '$' + E.toFixed(2)], ['pp-mark', '$' + M.toFixed(2)], ['pp-fund', fr.toFixed(3) + '%']].forEach(([i, t]) => setT(i + '-v', t));
      document.getElementById('pp-long').classList.toggle('on', perpDir === 1); document.getElementById('pp-short').classList.toggle('on', perpDir === -1);
      const notional = m * L, qty = notional / E, liq = perpDir === 1 ? E * (1 - 1 / L + 0.01) : E * (1 + 1 / L - 0.01);
      const upnl = Math.max(-m, qty * (M - E) * perpDir), fund = -perpDir * notional * fr / 100 * 3;
      const hit = perpDir === 1 ? M <= liq : M >= liq;
      setT('pp-k1', money(notional, 2)); setT('pp-k1-s', qty.toFixed(4) + ' units');
      setT('pp-k2', '$' + liq.toFixed(2)); setT('pp-k2-s', ((Math.abs(E - liq) / E) * 100).toFixed(1) + '% from entry');
      setT('pp-k3', money(upnl, 2)); setT('pp-k3-s', (upnl / m * 100).toFixed(1) + '% on margin');
      setT('pp-k4', money(fund, 2)); setT('pp-k4-s', fund >= 0 ? 'you receive (est.)' : 'you pay (est.)');
      document.getElementById('pp-note').innerHTML = hit ? `<strong class="text-amber-300">Mark is past the estimated liquidation price.</strong> In isolated margin the most this position can lose is the $${m} posted.` : `<strong class="text-gold-300">Isolated margin:</strong> the most this position can lose is the $${m} posted. Liquidation estimate assumes about 1% maintenance margin; each exchange differs.`;
    }

    // ==================== TOOL: CONCEPT CODEX & VAULT ====================
    let cxMode = 'pub', cxCat = 'all', cxQ = '';
    const UNLOCKED_N = [1, 18, 19]; // demo: a Starter member's 3 modules
    const triage = () => ls.get(KEY.triage, []);
    function toggleTriage(n) { const t = triage(); const i = t.indexOf(n); if (i >= 0) t.splice(i, 1); else t.push(n); ls.set(KEY.triage, t); }
    function toolCodex(host, full) {
      host.setAttribute('data-host', '1'); host.dataset.full = full ? '1' : '';
      const counts = { all: CONCEPTS.length }; CONCEPTS.forEach((c) => { counts[c.cat] = (counts[c.cat] || 0) + 1; });
      host.innerHTML = `<div class="space-y-5">
        <div class="card rounded-2xl p-4 flex flex-col lg:flex-row gap-3 lg:items-center lg:justify-between">
          <div class="inline-flex flex-wrap gap-1 p-1 rounded-xl bg-navy-950 border border-gray-800">${[['pub', 'Public view'], ['vault', 'Paid vault'], ['both', 'Side-by-side']].map(([k, l]) => `<button class="seg-btn ${k === cxMode ? 'on' : ''}" onclick="cxMode='${k}';drawCodex()">${l}</button>`).join('')}</div>
          <div class="relative lg:w-72"><span class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500">${ic('search', 'w-4 h-4')}</span><input id="cx-q" class="field !pl-9" placeholder="Search concepts…" value="${esc(cxQ)}" oninput="cxQ=this.value;drawCodex(true)" /></div>
        </div>
        <div class="flex gap-2 overflow-x-auto pb-1">${[['all', 'All concepts']].concat(Object.entries(CATS)).map(([k, l]) => `<button class="chip ${k === cxCat ? 'on' : ''}" onclick="cxCat='${k}';drawCodex()">${k === 'all' ? '' : k + ' • '}${l} (${counts[k] || 0})</button>`).join('')}</div>
        ${full ? '' : `<div class="p-4 rounded-xl border border-gold-400/40 bg-gold-400/5 text-sm text-gray-200 flex flex-wrap items-center justify-between gap-3"><span>${ic('lock', 'w-4 h-4 inline text-gold-300')} <strong class="text-gold-300">Toggle "Paid vault"</strong> to see what each module delivers behind the paywall. The deliverables unlock with any package or a $29 module.</span><a href="#/members?demo=1&tab=vault" class="btn-gold !py-1.5 !px-3 !text-xs">Preview the vault</a></div>`}
        <div class="text-xs font-mono text-gray-500" id="cx-count"></div>
        <div id="cx-grid" class="grid grid-cols-1 md:grid-cols-2 gap-4"></div>
      </div>`;
      drawCodex(true);
    }
    function drawCodex(gridOnly) {
      const host = document.getElementById('cx-grid').closest('[data-host]'), full = !!host.dataset.full;
      if (!gridOnly) { toolCodex(host, full); refreshIcons(); return; }
      const q = cxQ.toLowerCase(), t = triage();
      const list = CONCEPTS.filter((c) => (cxCat === 'all' || c.cat === cxCat) && (!q || plain(c.title + ' ' + c.pub + ' ' + c.vault).toLowerCase().includes(q)));
      setT('cx-count', `${list.length} of ${CONCEPTS.length} concepts • ${t.length} in your triage scope`);
      document.getElementById('cx-grid').innerHTML = list.map((c) => {
        const inT = t.includes(c.n), open = full && UNLOCKED_N.includes(c.n);
        const pubBox = `<div class="p-3.5 rounded-xl bg-navy-950/60 border border-gray-800"><div class="text-[10px] font-mono uppercase tracking-wider text-gray-500 mb-1">Public overview</div><p class="text-sm text-gray-300 leading-relaxed">${c.pub}</p></div>`;
        const act = open ? `<div class="flex flex-wrap gap-2 mt-3">${c.guide ? `<button onclick="openLesson('${c.guide}')" class="btn-gold !py-1.5 !px-3 !text-xs">${ic('book-open', 'w-3.5 h-3.5')}Open lesson</button>` : ''}${c.tool && c.tool !== 'estimate' ? `<button onclick="mShow('${c.tool}')" class="btn-ghost !py-1.5 !px-3 !text-xs">${ic('wrench', 'w-3.5 h-3.5')}Open tool</button>` : ''}${c.tool === 'estimate' ? `<button onclick="mShow('estimate')" class="btn-ghost !py-1.5 !px-3 !text-xs">${ic('calculator', 'w-3.5 h-3.5')}Open worksheet</button>` : ''}</div>`
          : `<div class="mt-3"><a href="${full ? '#/pricing' : '#/members?demo=1&tab=vault'}" class="inline-flex items-center gap-1.5 text-xs font-bold text-gold-300 hover:underline">${ic('lock', 'w-3.5 h-3.5')}${full ? 'Unlock with Builder or $29' : 'Unlock in the members area'}</a></div>`;
        const vaultBox = `<div class="p-3.5 rounded-xl border ${open ? 'border-gold-400/60 bg-gold-400/10' : 'border-gold-400/30 bg-gold-400/5'}"><div class="text-[10px] font-mono uppercase tracking-wider text-gold-300 mb-1 flex items-center gap-1.5">${ic(open ? 'lock-open' : 'lock', 'w-3 h-3')}${open ? 'Vault deliverable • unlocked' : 'Paid vault deliverable'}</div><p class="text-sm text-gray-200 leading-relaxed">${c.vault}</p>${act}</div>`;
        const body = cxMode === 'pub' ? pubBox : cxMode === 'vault' ? vaultBox : `<div class="grid grid-cols-1 xl:grid-cols-2 gap-3">${pubBox}${vaultBox}</div>`;
        return `<article class="card rounded-2xl p-5 flex flex-col gap-3 ${cxMode === 'both' ? 'md:col-span-2' : ''}">
          <div class="flex items-start justify-between gap-3"><div class="text-[10px] font-mono uppercase tracking-wider text-gold-300">#${String(c.n).padStart(2, '0')} • ${c.cat} • ${CATS[c.cat]}</div>
          <button onclick="toggleTriage(${c.n});drawCodex(true)" class="shrink-0 text-[11px] font-bold px-2.5 py-1 rounded-lg border ${inT ? 'bg-gold-400 text-navy-950 border-gold-400' : 'border-gold-400/40 text-gold-300 hover:bg-gold-400/10'}">${inT ? '✓ In triage' : '+ Add to Triage'}</button></div>
          <div class="flex items-center gap-3"><span class="icon-tile !w-10 !h-10 shrink-0">${ic(c.icon)}</span><h3 class="font-bold text-white leading-snug">${c.title}</h3></div>
          ${body}
          <div class="text-xs text-gray-400 flex gap-2"><span class="text-gold-300 shrink-0">${ic('check-circle-2', 'w-3.5 h-3.5')}</span><span><strong class="text-gray-300">Direct capability:</strong> ${c.cap}</span></div>
        </article>`;
      }).join('') || '<div class="text-sm text-gray-400">No concepts match that search.</div>';
      refreshIcons();
    }

    // ==================== TOOL: CAPITAL FLYWHEEL ====================
    const FW_STAGES = [
      ['split', 'Stage 1 • Partition', 'Bills, tax reserves and savings for upcoming quotes are set aside first, so nothing is ever forced to sell.'],
      ['shield', 'Stage 2 • 401(k) anchor', 'My core retirement money sits in stable-value, income and broad index funds. It is the defensive base.'],
      ['zap', 'Stage 3 • LEAPS spear', 'A small, fixed slice of each check goes to long-dated options, 6+ months out. I trim above my +20% gate and exit before the 45-day cliff.'],
      ['cpu', 'Stage 4 • Hardware &amp; hard assets', 'Trimmed gains get recycled into compute machines and physical gold and silver, which feed cashflow back into Stage 1.']
    ];
    function toolFlywheel(host, full) {
      host.setAttribute('data-host', '1');
      host.innerHTML = `<div class="space-y-6">
        <div class="p-4 rounded-xl border border-gold-400/40 bg-gold-400/5 text-sm text-gray-200">${ic('info', 'w-4 h-4 inline text-gold-300')} <strong class="text-gold-300">What I do personally.</strong> This is my own system, shared as an educational example and not a recommendation for your money. Options can lose 100% of the premium.</div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">${FW_STAGES.map(([i, t, d]) => card(`<span class="icon-tile !w-10 !h-10">${ic(i)}</span><div class="font-bold text-white mt-3">${t}</div><p class="text-sm text-gray-400 mt-1">${d}</p>`)).join('')}</div>
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
          <div class="lg:col-span-5 relative">${card(`<div class="eyebrow mb-3">${full ? 'Your sample inputs' : 'Sample numbers'}</div><fieldset ${full ? '' : 'disabled'} class="space-y-4 ${full ? '' : 'opacity-70'}">
            ${sl('f-sur', 'Surplus per paycheck', 100, 2000, 25, 600, (x) => '$' + x, 'calcFly()')}
            ${sl('f-leap', 'Share to the LEAPS spear', 0, 80, 1, 45, (x) => x + '%', 'calcFly()')}
            ${sl('f-bond', '401(k) fixed-income share', 0, 100, 1, 48, (x) => x + '%', 'calcFly()')}</fieldset>
            ${full ? '' : `<div class="mt-4 p-3 rounded-xl border border-dashed border-gold-400/40 text-xs text-gray-300 flex items-center justify-between gap-2 flex-wrap"><span>${ic('lock', 'w-3.5 h-3.5 inline text-gold-300')} Interactive controls unlock in the members area.</span><a href="#/members?demo=1&tab=flywheel" class="text-gold-300 font-bold hover:underline">Preview →</a></div>`}`)}</div>
          <div class="lg:col-span-7 space-y-4 min-w-0">
            <div class="grid grid-cols-2 gap-3">${kpi('f-k1', 'Flywheel capital / year')}${kpi('f-k2', 'LEAPS spear / check')}${kpi('f-k3', 'Hardware &amp; bullion / check')}${kpi('f-k4', '401(k) split')}</div>
            ${card(`<div class="flex items-center justify-between mb-2"><div class="font-bold text-white text-sm">Sample allocation picture</div><span class="text-[10px] font-mono text-gray-500 uppercase">educational</span></div><div class="chart-box"><canvas id="f-chart"></canvas></div>`, '!p-4')}
          </div></div>
        <p class="text-xs text-gray-500">Hypothetical illustration based on 26 paychecks a year. Not investment advice. Your situation, goals and risk tolerance are your own.</p>
      </div>`;
      calcFly();
    }
    function calcFly() {
      const s = num('f-sur'), lp = num('f-leap'), b = num('f-bond');
      setT('f-sur-v', '$' + s); setT('f-leap-v', lp + '%'); setT('f-bond-v', b + '%');
      const leap = s * lp / 100, hw = s - leap;
      setT('f-k1', money(s * 26)); setT('f-k1-s', '$' + s + ' × 26 checks');
      setT('f-k2', money(leap)); setT('f-k2-s', money(leap * 26) + ' / year');
      setT('f-k3', money(hw)); setT('f-k3-s', money(hw * 26) + ' / year');
      setT('f-k4', b + ' / ' + (100 - b)); setT('f-k4-s', 'fixed income / equities');
      mkChart('fly', document.getElementById('f-chart'), { type: 'bar', data: { labels: ['401(k) fixed income', '401(k) equities', 'LEAPS spear', 'Hardware & bullion'], datasets: [{ label: '% of bucket', data: [b, 100 - b, lp, 100 - lp], backgroundColor: ['#64748b', '#94a3b8', '#d4af37', '#f3d98b'], borderRadius: 6 }] }, options: { plugins: { legend: { display: false } }, scales: { x: { grid: { display: false } }, y: { max: 100, grid: { color: chartColors.grid }, ticks: { callback: (v) => v + '%' } } } } });
    }

    // ==================== TOOL: FIRST-CALL DISPATCH ====================
    const FORMATS = ['01 • Crypto Hardware Sourcing, Setup & ROI Audit', '02 • Quote & Estimate Comparison', '03 • Handyman Fixes & Painting', '04 • Markets & Flywheel Education', '05 • Pre-CPA Paperwork & Taxes Prep', '06 • Business Setup', '07 • IT, Wi-Fi & Web3 Help', '08 • General First Call'];
    function toolDispatch(host) {
      host.setAttribute('data-host', '1');
      const t = triage();
      host.innerHTML = `<div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <div class="lg:col-span-7 space-y-4 min-w-0">${card(`<div class="eyebrow mb-3">01 • About you</div><div class="grid grid-cols-1 sm:grid-cols-2 gap-3"><label class="text-xs text-gray-400">First name or alias<input id="d-alias" class="field mt-1" placeholder="e.g. Sam (an alias is fine)" oninput="buildBrief()" /></label><label class="text-xs text-gray-400">Engagement format<select id="d-fmt" class="field mt-1" onchange="buildBrief()">${FORMATS.map((f) => `<option>${f}</option>`).join('')}</select></label></div>
          <label class="text-xs text-gray-400 block mt-3">What's the friction? (optional)<textarea id="d-note" rows="3" class="field mt-1" placeholder="A sentence or two. Please don't include passwords or account numbers." oninput="buildBrief()"></textarea></label>`)}
          ${card(`<div class="flex flex-wrap items-center justify-between gap-2 mb-3"><div class="eyebrow">02 • Pick the concepts in scope</div><div class="flex gap-3 text-xs"><button class="text-gold-300 hover:underline" onclick="setAllTriage(true)">Select all</button><button class="text-gray-400 hover:underline" onclick="setAllTriage(false)">Clear</button></div></div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">${CONCEPTS.map((c) => `<label class="flex items-start gap-2 p-2.5 rounded-lg bg-navy-950/60 border border-gray-800 text-xs text-gray-300 cursor-pointer"><input type="checkbox" class="mt-0.5 d-chk" value="${c.n}" ${t.includes(c.n) ? 'checked' : ''} onchange="syncTriage()" /><span><span class="font-mono text-gold-300">#${String(c.n).padStart(2, '0')}</span> ${c.title}</span></label>`).join('')}</div>`)}</div>
        <div class="lg:col-span-5 space-y-4 min-w-0">${card(`<div class="eyebrow mb-2">03 • Your first-call brief</div><pre id="d-brief" class="whitespace-pre-wrap break-words text-xs font-mono text-gray-200 bg-navy-950 border border-gray-800 rounded-xl p-4 max-h-[460px] overflow-y-auto"></pre>
          <div class="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-1 xl:grid-cols-3 gap-2 mt-3"><button onclick="copyText(document.getElementById('d-brief').textContent)" class="btn-ghost !py-2">${ic('copy')}Copy</button><a id="d-sms" class="btn-gold !py-2">${ic('message-square')}Text</a><a id="d-mail" class="btn-ghost !py-2">${ic('mail')}Email</a></div>
          <p class="text-[11px] text-gray-500 mt-2">Nothing is sent until you press send in your own messages or email app. Keep it to first name and the problem: no passwords, keys or account numbers.</p>`, 'lg:sticky lg:top-36')}</div>
      </div>`;
      buildBrief();
    }
    function syncTriage() { ls.set(KEY.triage, [...document.querySelectorAll('.d-chk:checked')].map((x) => +x.value)); buildBrief(); }
    function setAllTriage(on) { document.querySelectorAll('.d-chk').forEach((x) => { x.checked = on; }); syncTriage(); }
    function buildBrief() {
      const alias = document.getElementById('d-alias').value.trim() || '[first name]', fmt = document.getElementById('d-fmt').value, note = document.getElementById('d-note').value.trim();
      const sel = triage().slice().sort((a, b) => a - b).map((n) => CONCEPTS.find((c) => c.n === n)).filter(Boolean);
      const text = `FELRON FIRST-CALL BRIEF\n\nClient: ${alias}\nFormat: ${fmt}\n${note ? 'The friction: ' + note + '\n' : ''}\nConcepts in scope (${sel.length}):\n${sel.length ? sel.map((c) => `• #${String(c.n).padStart(2, '0')} ${plain(c.title)}`).join('\n') : '• (none picked yet: we will sort it out on the call)'}\n\nNext step: free 15-minute first call.\n(Education and hands-on help, flat fees. Sent from the FelRon website.)`;
      document.getElementById('d-brief').textContent = text;
      document.getElementById('d-sms').href = 'sms:+12105354987?&body=' + encodeURIComponent(text);
      document.getElementById('d-mail').href = 'mailto:MattDiazSA@gmail.com?subject=' + encodeURIComponent('FelRon first-call brief: ' + alias) + '&body=' + encodeURIComponent(text);
    }
    function toolEstimate(host) { host.innerHTML = mEstimate(); calcEstimate(); }

    // ==================== MEMBERS AREA (PREVIEW) ====================
    const GUIDES = [
      { id: 'hardware', icon: 'cpu', title: 'Crypto Hardware Sourcing & Setup', did: 'I run my own ASIC and DePIN hardware at home, and I have sourced, cleaned and configured machines bought from distributors and the secondary market.',
        steps: ['Pick the target: the coin or network and the machine model (for example an Antminer Z15 for Equihash). Note its hashrate and power draw.',
          'Get at least three seller quotes and compare price-per-hash against secondary-market listings.',
          'Ask for hashboard photos, chip-test screenshots, the PSU model, warranty or return terms and a serial number.',
          'Check your power: watts ÷ volts = amps. Keep continuous load at or under 80% of the circuit rating, and plan airflow and noise.',
          'Plug in, set a static IP and configure the pool with a primary and a failover address.',
          'Track kWh cost vs. daily yield in the ROI tool, and schedule board cleaning and fan checks.'],
        together: 'I source and inspect the machine with you, plug it in, configure the pool and leave you a written maintenance recap.',
        resources: [['CPS Energy', 'https://www.cpsenergy.com', 'San Antonio electricity rates for your kWh cost.'], ['Bitmain Support', 'https://support.bitmain.com', 'Official Antminer manuals and firmware.'], ['TDLR License Search', 'https://www.tdlr.texas.gov/LicenseSearch/', 'Look up a licensed electrician for added circuits.']] },
      { id: 'web3', icon: 'shield-check', title: 'Web3 Self-Custody & DePIN Hygiene', did: 'I hold my own keys in cold storage, keep burner and vault wallets separate, and run DePIN nodes on my home network.',
        steps: ['Buy a hardware wallet only from the maker or an authorized seller, and check that the package is sealed.',
          'Generate the seed phrase offline and write it on paper or steel. Never type it into a phone or computer.',
          'Split wallets: a small burner for apps and a vault wallet that only receives.',
          'Turn on app-based 2FA for exchange and email accounts, and bookmark the real sites to avoid phishing.',
          'Before joining a DePIN network, read its hardware, bandwidth and payout terms, and isolate the device on a guest network.'],
        together: 'You stay at the keyboard for every password and seed phrase while I walk you through each screen.',
        resources: [['CISA: Secure Our World', 'https://www.cisa.gov/secure-our-world', 'Simple steps to stay safe online.'], ['FTC: Cryptocurrency scams', 'https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams', 'Spot and avoid crypto scams.']] },
      { id: 'homefix', icon: 'paintbrush', title: 'Handyman Fixes, Painting & AC Filter Basics', did: 'I have painted, patched and maintained homes for family, and I keep a simple maintenance calendar for my own place.',
        steps: ['Walk the house and list every small fix: paint touch-ups, drywall dings, caulk lines, loose hardware, and anything to mount or assemble.',
          'Group them into one visit. Small jobs cost less when they are done together.',
          'AC filter: find the size printed on the filter frame, check it monthly and replace it every 1–3 months.',
          'Before an AC service call, run the checklist: thermostat mode and batteries, a clean filter, and clear vents and returns.',
          'Write down the symptoms (warm air, noise, short cycling) and the model and serial number from the unit label, with photos.',
          'For AC, electrical or plumbing repairs, send me those details. I gather and compare quotes from licensed pros so you choose the best value.'],
        together: 'I handle the quick fixes or line up the handyman I work with for painting and patch work, coordinate the visit, and compare quotes for anything bigger.',
        resources: [['TDLR License Search', 'https://www.tdlr.texas.gov/LicenseSearch/', 'Look up a licensed AC or electrical pro.'], ['Energy Saver (DOE)', 'https://www.energy.gov/energysaver', 'Heating, cooling and efficiency basics.'], ['CPS Energy', 'https://www.cpsenergy.com', 'San Antonio utility programs and rebates.']] },
      { id: 'estimates', icon: 'scale', title: 'Getting & Comparing Estimates', did: 'Years of retail and assistant-GM work taught me pricing, vendors and margins. I know what fair pricing looks like, and I use the same process to compare contractor and shop quotes.',
        steps: ['Write a one-paragraph scope: what needs doing, where, and by when.',
          'Get at least three quotes on the same scope so they can be compared.',
          'Ask each provider for a license number (if the trade requires one), proof of insurance, the warranty on parts and labor, the timeline, and what is not included.',
          'Line them up in the Estimate Worksheet. Anything 20% or more above the median gets a second look.',
          'Verify licenses on TDLR and check reviews and complaints.',
          'Get the final scope and price in writing before work starts, and avoid paying the full amount upfront.'],
        together: 'Send me the scope. I make the calls, gather the quotes and walk you through the comparison. You pick the provider.',
        resources: [['TDLR License Search', 'https://www.tdlr.texas.gov/LicenseSearch/', 'Look up licensed trade pros.'], ['Better Business Bureau', 'https://www.bbb.org', 'Business reviews and complaints.'], ['Texas AG Consumer Protection', 'https://www.texasattorneygeneral.gov/consumer-protection', 'Home repair and contractor consumer tips.']] },
      { id: 'auto', icon: 'car', title: 'Car Basics', did: 'I keep my own car running: battery swaps, bulbs, code reads and the pre-road-trip checks I learned growing up.',
        steps: ['Check-engine light on? Get the code read with an OBD-II reader (many parts stores do it free) and write it down.',
          'Look up what the code means, then confirm the cause before buying parts.',
          'Slow crank or clicking? Test the battery. Most last about 3–5 years.',
          'Bulbs and wipers: find the part number in your owner\'s manual or a parts-store lookup.',
          'Check tire pressure monthly (the sticker is in the driver\'s door jamb), plus fluids before road trips.',
          'For bigger repairs, get at least two shop quotes. I call around and compare them for you.'],
        together: 'I help with the basics like code reads, bulbs and battery checks, and I call shops and compare quotes for bigger repairs.',
        resources: [['NHTSA Recalls', 'https://www.nhtsa.gov/recalls', 'Check your VIN for open recalls.'], ['Texas DMV', 'https://www.txdmv.gov', 'Registration and title help.']] },
      { id: 'business', icon: 'briefcase', title: 'Start or Grow a Business', did: 'I\'m building FelRon itself one filing at a time, and I\'ll show you each form I used.',
        steps: ['Outline your business on one page: what you sell, to whom, and for how much.', 'Choose a name and check that it\'s available.',
          'Using your own name? You can start as a sole proprietor. Using a different business name? File an assumed name (DBA) certificate with the Bexar County Clerk.',
          'Considering an LLC? It\'s filed with the Texas Secretary of State through SOSDirect. Talk with an attorney or a free SCORE mentor about whether it fits.',
          'Get a free EIN from the IRS, then open a separate business bank account.', 'Selling taxable goods or services? Check whether you need a Texas sales tax permit from the Comptroller.'],
        together: 'We fill out the forms side by side, and you review, sign and submit.',
        resources: [['SBA San Antonio District Office', 'https://www.sba.gov/district/san-antonio', 'Free local small-business programs.'], ['SCORE Southwest Texas', 'https://www.score.org/tx/southwest-texas/', 'Free 1-on-1 business mentoring.'], ['Bexar County Clerk: Assumed Names (DBA)', 'https://www.bexar.org/2958/Assumed-Business-NamesDBAs', 'File a DBA in Bexar County.'], ['Texas SOS: SOSDirect', 'https://www.sos.state.tx.us/corp/sosda/index.shtml', 'File an LLC or search names.'], ['IRS: Get an EIN (free)', 'https://www.irs.gov/businesses/small-businesses-self-employed/get-an-employer-identification-number', 'Apply directly with the IRS.'], ['Texas Comptroller: Sales Tax Permit', 'https://comptroller.texas.gov/taxes/permit/', 'Sales and use tax permit.'], ['State Bar of Texas', 'https://www.texasbar.com', 'Find a licensed Texas attorney.']] },
      { id: 'money', icon: 'trending-up', title: 'Money & Investing Basics', did: 'I trade my own account with written rules and defined risk, and I\'ll show you my real process, mistakes included. Past results are not a promise.',
        steps: ['Write down your goal in one sentence (an emergency fund, understanding your 401(k), learning about options).', 'Gather your own statements: 401(k) fund menu, pay stub and any brokerage statements. Keep the passwords to yourself.',
          'Work through the matching module and quiz, then book a 1-on-1 education session. You get a written recap.', 'For a personal allocation or investment plan, take your notes to a licensed fiduciary adviser and check them first on BrokerCheck.'],
        together: 'We walk through your own platform\'s screens and your own written checklist. You place your own trades and make every decision.',
        resources: [['FINRA BrokerCheck', 'https://brokercheck.finra.org', 'Check a broker or adviser\'s record.'], ['SEC Investment Adviser Search', 'https://adviserinfo.sec.gov', 'Registered investment advisers.'], ['Investor.gov (SEC)', 'https://www.investor.gov', 'Free investing education.'], ['Texas State Securities Board', 'https://www.ssb.texas.gov', 'Texas investor protection.'], ['NAPFA: Find a Fee-Only Fiduciary', 'https://www.napfa.org/find-an-advisor', 'Fee-only fiduciary directory.'], ['Consumer Financial Protection Bureau', 'https://www.consumerfinance.gov', 'Credit, debt and banking help.']] },
      { id: 'it', icon: 'monitor', title: 'IT & Tech Rescue', did: 'I run my own home network, self-custody wallets and mining hardware, and I\'ve fixed plenty of locked-up computers and dead Wi-Fi.',
        steps: ['Write down what\'s broken or what you want set up, and take a photo of any error message.', 'Restart the device and the router (unplug 30 seconds) and note whether anything changes.',
          'Back up photos and documents before any big change.', 'Set up a password manager and turn on 2-factor for email and banking first.', 'Keep a written record of what was changed and how to maintain it.'],
        together: 'Remote or on-site in San Antonio. You stay at the keyboard for passwords, keys and seed phrases.',
        resources: [['CISA: Secure Our World', 'https://www.cisa.gov/secure-our-world', 'Simple steps to stay safe online.'], ['IdentityTheft.gov (FTC)', 'https://www.identitytheft.gov', 'Recovery plan for identity theft.']] },
      { id: 'paperwork', icon: 'file-text', title: 'Taxes, Insurance & Paperwork', did: 'I\'ve untangled insurance letters, bills and records for family, and I keep my own records in a simple labeled system.',
        steps: ['Gather everything in one place: W-2s, 1099s, receipts, insurance letters and policy documents.', 'Sort it into a clean, labeled system (paper or digital) and list what\'s missing.',
          'For tax returns: use free IRS VITA help or IRS Free File if you qualify. Otherwise, bring the organized file to a CPA.', 'For insurance: read the policy together for coverage and deadlines. You file the claim with your insurer, and the Texas Department of Insurance can help if you get stuck.'],
        together: 'We sort your documents together, put deadlines on your calendar and prep a clean file for your preparer.',
        resources: [['IRS VITA: Free Tax Prep', 'https://www.irs.gov/individuals/free-tax-return-preparation-for-qualifying-taxpayers', 'Free tax help for qualifying taxpayers.'], ['Find a VITA Site', 'https://irs.treasury.gov/freetaxprep/', 'VITA locations by ZIP.'], ['IRS Free File', 'https://www.irs.gov/filing/irs-free-file-do-your-taxes-for-free', 'File free online if eligible.'], ['Texas Department of Insurance', 'https://www.tdi.texas.gov/consumer/', 'Insurance consumer help.'], ['Texas HHS Long-Term Care Search', 'https://apps.hhs.texas.gov/LTCSearch/', 'Licensed assisted-living facilities.'], ['TexasLawHelp.org', 'https://texaslawhelp.org', 'Free legal information for Texans.']] }
    ];
    const MOD_LIST = CONCEPTS.map((c) => [c.n, c.title, c.icon, c.guide, c.tool]);
    const UNLOCKED = ['hardware', 'estimates', 'homefix']; // guides for the demo Starter member's 3 modules (#1, #18, #19)
    const QUIZZES = {
      estimates: { title: 'Getting & Comparing Estimates', items: [
        { q: 'What makes two quotes truly comparable?', a: ['They came from the same week', 'They cover the same scope of work', 'They have the same company logo', 'They are both under $500'], c: 1, why: 'Quotes only compare apples to apples when the scope is the same.' },
        { q: 'One quote is 35% above the median. Best next step?', a: ['Take it, it must be better', 'Ask what\'s included and compare scope and warranty', 'Ignore the others', 'Pay upfront to lock it in'], c: 1, why: 'Outliers deserve a second look: scope, parts, warranty or padding.' },
        { q: 'Before hiring a pro for a bigger job, what should you check?', a: ['Only the price', 'License (when the trade needs one), insurance and reviews', 'Their logo', 'Nothing, if they sound confident'], c: 1, why: 'Licenses, insurance and reviews protect you before any work starts.' },
        { q: 'A good payment practice for a big job is…', a: ['Pay 100% in cash upfront', 'Written scope and price, traceable payments, not all upfront', 'No paperwork needed', 'Pay whoever calls first'], c: 1, why: 'Written scope and traceable, staged payments protect you.' }
      ] },
      options: { title: 'Options & LEAPS Education', items: [
        { q: 'When you BUY a call option, what is the most you can lose?', a: ['The premium you paid', 'Unlimited', 'Twice the premium', 'The full stock price × 100'], c: 0, why: 'A long option\'s maximum loss is the premium paid.' },
        { q: 'What does "LEAPS" generally refer to?', a: ['Options that expire in about a week', 'Options with roughly a year or more until expiration', 'A type of savings account', 'Leveraged crypto tokens'], c: 1, why: 'LEAPS are long-dated options, typically a year or more out.' },
        { q: 'Time decay (theta) usually…', a: ['Stays the same every day', 'Speeds up as expiration gets closer', 'Only affects stocks', 'Increases an option\'s value'], c: 1, why: 'Time value tends to shrink faster in the final weeks.' },
        { q: 'One standard U.S. equity option contract usually covers…', a: ['1 share', '10 shares', '100 shares', '1,000 shares'], c: 2, why: 'Standard equity options cover 100 shares.' }
      ] },
      treasuries: { title: 'Stocks & Treasuries', items: [
        { q: 'When Treasury bond PRICES fall, their yields generally…', a: ['Fall too', 'Rise', 'Stay the same', 'Become negative'], c: 1, why: 'Bond prices and yields move in opposite directions.' },
        { q: 'Rising Treasury yields tend to pressure…', a: ['Growth and small-cap stocks', 'Cash in savings', 'Short-term T-bills', 'Nothing'], c: 0, why: 'Higher yields raise discount rates and borrowing costs.' },
        { q: 'The "10-year" usually refers to…', a: ['A 10-year CD', 'The 10-year U.S. Treasury note yield', 'The S&P 500\'s 10-year return', 'A 10-year mortgage'], c: 1, why: 'The 10-year Treasury yield is a key benchmark.' }
      ] }
    };
    let mTab = 'dash', lessonId = 'hardware', quizId = 'estimates';
    const guide = (id) => GUIDES.find((g) => g.id === id);

    function initMembers() {
      if (hashParam('demo') === '1') ls.set(KEY.unlock, true);
      const on = ls.get(KEY.unlock, false);
      document.getElementById('m-gate').classList.toggle('hidden', on);
      document.getElementById('m-app').classList.toggle('locked-blur', !on);
      const t = hashParam('tab'); if (t) mTab = t;
      if (!document.querySelector(`#m-tabs .mtab[data-t="${mTab}"]`)) mTab = 'dash';
      mShow(mTab);
    }
    function unlockDemo() { ls.set(KEY.unlock, true); initMembers(); }
    function lockDemo() { ls.set(KEY.unlock, false); initMembers(); window.scrollTo(0, 0); }
    function progress() {
      const p = ls.get(KEY.prog, {}); let done = 0, total = 0;
      UNLOCKED.forEach((id) => { const g = guide(id); total += g.steps.length; g.steps.forEach((_, i) => { if (p[id + ':' + i]) done++; }); });
      return { done, total, pct: total ? Math.round(done / total * 100) : 0 };
    }
    function mShow(t) {
      mTab = t;
      document.querySelectorAll('#m-tabs .mtab').forEach((b) => b.classList.toggle('on', b.dataset.t === t));
      Object.keys(CH).forEach((k) => { try { CH[k].destroy(); } catch (e) {} delete CH[k]; });
      const TOOLT = { vault: 'codex', roi: 'roi', lab: 'lab', flywheel: 'flywheel' };
      if (TOOLT[t]) { const head = { vault: ['Concept Vault', 'Every module, public overview and vault deliverable.'], roi: ['Machine ROI &amp; Sourcing', 'Full simulator plus the procurement checklist.'], lab: ['LEAPS &amp; Perps Lab', 'Options payoff simulator and the perps calculator.'], flywheel: ['Capital Flywheel', 'Interactive model: what I do personally, not a recommendation.'] }[t];
        document.getElementById('m-body').innerHTML = `<div><div class="eyebrow">Members tool</div><h2 class="serif text-3xl font-bold text-white">${head[0]}</h2><p class="text-sm text-gray-400 mt-1">${head[1]}</p></div><div id="m-tool"></div>`;
        if (t === 'vault') cxMode = 'both';
        renderTool(TOOLT[t], document.getElementById('m-tool'), true); return; }
      const R = { dash: mDash, modules: mModules, lesson: mLesson, guides: mGuides, resources: mResources, quiz: mQuiz, estimate: mEstimate, tracker: mTracker }[t] || mDash;
      document.getElementById('m-body').innerHTML = R();
      if (t === 'estimate') calcEstimate();
      if (t === 'quiz') { const b = ls.get(KEY.quiz, {})[quizId]; document.getElementById('quiz-score').textContent = b != null ? 'Best score on this device: ' + b + '/' + QUIZZES[quizId].items.length : ''; }
      refreshIcons();
    }
    function openLesson(id) { lessonId = id; mShow('lesson'); document.getElementById('m-body').scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    function modRow([n, title, icon, gid, tool]) {
      const open = UNLOCKED_N.includes(n);
      const btn = open ? (gid ? `<button onclick="openLesson('${gid}')" class="btn-gold !py-1.5 !px-3 !text-xs">${ic('lock-open', 'w-3.5 h-3.5')}Open</button>` : `<button onclick="mShow('${tool === 'estimate' ? 'estimate' : 'vault'}')" class="btn-gold !py-1.5 !px-3 !text-xs">${ic('lock-open', 'w-3.5 h-3.5')}Open</button>`) : `<a href="#/pricing" class="btn-ghost !py-1.5 !px-3 !text-xs">${ic('lock', 'w-3.5 h-3.5')}$29</a>`;
      return `<div class="flex items-center gap-3 p-3.5 rounded-xl border ${open ? 'border-gold-400/40 bg-gold-400/5' : 'border-gray-800 bg-navy-950/60'}">
        <span class="icon-tile !w-10 !h-10 shrink-0 ${open ? '' : 'opacity-50'}">${ic(icon)}</span>
        <div class="flex-1 min-w-0"><div class="text-[10px] font-mono text-gold-300">#${String(n).padStart(2, '0')}</div><div class="text-sm font-semibold ${open ? 'text-white' : 'text-gray-400'}">${title}</div><div class="text-[11px] ${open ? 'text-gold-300' : 'text-gray-500'}">${open ? 'Unlocked • lesson, vault, tools, quiz' : 'Locked • included in Builder, or $29'}</div></div>
        ${btn}
      </div>`;
    }
    function mDash() {
      const pr = progress(), tr = trackerRows();
      return `<div class="rounded-2xl p-6 sm:p-7 bg-gradient-to-br from-navy-700 to-navy-900 border border-gold-400/30 flex flex-wrap items-center justify-between gap-4">
          <div><div class="eyebrow">Welcome back</div><h2 class="serif text-3xl font-bold text-white">Demo Member</h2><p class="text-sm text-gray-300 mt-1">Pick up where you left off, or send me a new friction point.</p></div>
          <div class="flex gap-2 flex-wrap"><button onclick="openLesson('hardware')" class="btn-gold">${ic('book-open')}Continue lesson</button><button onclick="mShow('tracker')" class="btn-ghost">${ic('send')}New request</button></div></div>
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
          ${[['book-open', UNLOCKED_N.length + ' / ' + MOD_LIST.length, 'Modules unlocked'], ['list-checks', pr.pct + '%', 'Checklist progress'], ['clipboard-list', tr.filter((r) => r.status !== 'Done').length, 'Open requests'], ['calendar', 'Tue 10 AM', 'Next session (sample)']].map(([i, v, l]) => card(`<div class="text-gold-300">${ic(i, 'w-5 h-5')}</div><div class="text-2xl font-extrabold text-white mt-2">${v}</div><div class="text-xs text-gray-400">${l}</div>`, '!p-4')).join('')}
        </div>
        ${card(`<div class="flex items-center justify-between mb-2"><div class="font-bold text-white">Your progress</div><div class="font-mono text-gold-300 text-sm">${pr.done}/${pr.total} steps</div></div><div class="h-2.5 rounded-full bg-navy-950 overflow-hidden"><div class="h-full bg-gold-400 rounded-full" style="width:${pr.pct}%"></div></div>`)}
        <div class="grid grid-cols-1 xl:grid-cols-2 gap-6">
          ${card(`<div class="flex items-center justify-between mb-3"><div class="font-bold text-white">Continue learning</div><button onclick="mShow('modules')" class="text-xs text-gold-300 hover:underline">All modules →</button></div><div class="space-y-2.5">${MOD_LIST.filter((m) => UNLOCKED_N.includes(m[0])).concat(MOD_LIST.filter((m) => !UNLOCKED_N.includes(m[0])).slice(0, 2)).map(modRow).join('')}</div>`)}
          ${card(`<div class="flex items-center justify-between mb-3"><div class="font-bold text-white">Recent requests</div><button onclick="mShow('tracker')" class="text-xs text-gold-300 hover:underline">Tracker →</button></div><div class="space-y-2.5">${tr.slice(0, 4).map((r) => `<div class="flex items-center justify-between gap-3 p-3 rounded-xl bg-navy-950/60 border border-gray-800"><div class="min-w-0"><div class="text-sm text-white font-semibold truncate">${esc(r.title)}</div><div class="text-[11px] text-gray-500">${esc(r.type)}</div></div>${badge(r.status)}</div>`).join('')}</div>`)}
        </div>`;
    }
    function mModules() {
      return card(`<div class="flex flex-wrap items-end justify-between gap-2 mb-4"><div><div class="eyebrow">My modules</div><h2 class="serif text-2xl font-bold text-white">${UNLOCKED_N.length} unlocked, ${MOD_LIST.length - UNLOCKED_N.length} available</h2></div><a href="#/pricing" class="text-xs text-gold-300 hover:underline">Upgrade to Builder to unlock all →</a></div><div class="grid grid-cols-1 md:grid-cols-2 gap-3">${MOD_LIST.map(modRow).join('')}</div>`);
    }
    function mLesson() {
      const g = guide(lessonId), p = ls.get(KEY.prog, {});
      return `<div class="flex flex-wrap gap-2">${UNLOCKED.map((id) => `<button onclick="openLesson('${id}')" class="${id === lessonId ? 'btn-gold' : 'btn-ghost'} !py-1.5 !px-3 !text-xs">${guide(id).title}</button>`).join('')}</div>
        ${card(`<div class="flex items-center gap-3"><span class="icon-tile">${ic(g.icon, 'w-5 h-5')}</span><div><div class="eyebrow">Unlocked module</div><h2 class="serif text-3xl font-bold text-white">${g.title}</h2></div></div>`)}
        ${card(`<div class="eyebrow">01 • How I did it</div><p class="text-gray-300 mt-2 leading-relaxed">${g.did}</p>`)}
        ${card(`<div class="flex items-center justify-between"><div class="eyebrow">02 • How you can do it: step by step</div><span class="text-[11px] font-mono text-gray-500">check off as you go</span></div><ol class="mt-3 space-y-2.5">${g.steps.map((s, i) => `<li><label class="flex gap-3 items-start p-3 rounded-xl bg-navy-950/60 border border-gray-800 cursor-pointer"><input type="checkbox" class="mt-1" ${p[g.id + ':' + i] ? 'checked' : ''} onchange="toggleStep('${g.id}:${i}')" /><span class="text-sm text-gray-200"><span class="font-mono text-gold-300 font-bold mr-1.5">${String(i + 1).padStart(2, '0')}</span>${s}</span></label></li>`).join('')}</ol>`)}
        ${card(`<div class="eyebrow">03 • Let's get it done together</div><p class="text-gray-300 mt-2">${g.together}</p><div class="flex flex-wrap gap-2 mt-3"><a href="#/contact" class="btn-gold">${ic('calendar')}Book a walkthrough</a><button onclick="mShow('estimate')" class="btn-ghost">${ic('calculator')}Open estimate worksheet</button></div>`, 'border-gold-400/50')}
        ${card(`<div class="eyebrow">Trusted resources for this module</div><ul class="mt-3 grid grid-cols-1 md:grid-cols-2 gap-3">${g.resources.map(resItem).join('')}</ul>`)}`;
    }
    function toggleStep(k) { const p = ls.get(KEY.prog, {}); p[k] = !p[k]; ls.set(KEY.prog, p); }
    const resItem = ([n, u, d]) => `<li class="p-3 rounded-xl bg-navy-950/60 border border-gray-800"><a href="${u}" target="_blank" rel="noopener noreferrer" class="text-gold-300 font-semibold text-sm hover:underline">${n} ↗</a><div class="text-xs text-gray-400 mt-0.5">${d}</div></li>`;
    function mGuides() {
      return `<div><div class="eyebrow">Step-by-step guides</div><h2 class="serif text-3xl font-bold text-white">Your next steps, written down.</h2><p class="text-sm text-gray-400 mt-1">The full walkthroughs behind every service. Tap a guide to expand it.</p></div>` +
        GUIDES.map((g, n) => `<details class="card rounded-2xl p-5" ${n === 0 ? 'open' : ''}><summary class="flex items-center gap-3 cursor-pointer list-none"><span class="icon-tile !w-10 !h-10">${ic(g.icon)}</span><span class="font-bold text-white flex-1">${g.title}</span><span class="text-xs text-gold-300 font-mono">${g.steps.length} steps</span></summary>
          <ol class="mt-4 space-y-2 list-decimal pl-5 text-sm text-gray-300 leading-relaxed">${g.steps.map((s) => `<li>${s}</li>`).join('')}</ol>
          <div class="mt-3 p-3 rounded-xl bg-gold-400/10 border border-gold-400/30 text-sm text-gray-200"><strong class="text-gold-300">Done together:</strong> ${g.together}</div></details>`).join('');
    }
    function mResources() {
      return `<div><div class="eyebrow">Resource directory</div><h2 class="serif text-3xl font-bold text-white">Trusted outside resources.</h2><p class="text-sm text-gray-400 mt-1">Official government and nonprofit sources, organized by topic. FelRon is not affiliated with them.</p></div>` +
        GUIDES.map((g) => card(`<div class="flex items-center gap-2 mb-3 text-white font-bold">${ic(g.icon, 'w-4 h-4 text-gold-300')}${g.title}</div><ul class="grid grid-cols-1 md:grid-cols-2 gap-3">${g.resources.map(resItem).join('')}</ul>`)).join('');
    }
    function mQuiz() {
      const Q = QUIZZES[quizId];
      return card(`<div class="flex flex-wrap items-end justify-between gap-3"><div><div class="eyebrow">Quizzes &amp; testing</div><h2 class="serif text-2xl font-bold text-white">${Q.title}</h2></div><select class="field !w-auto" onchange="quizId=this.value;mShow('quiz')">${Object.entries(QUIZZES).map(([k, v]) => `<option value="${k}" ${k === quizId ? 'selected' : ''}>${v.title}</option>`).join('')}</select></div>
        <div class="mt-4 space-y-3">${Q.items.map((x, i) => `<div class="p-4 rounded-xl bg-navy-950/60 border border-gray-800" id="qz-${i}"><div class="text-sm font-semibold text-white mb-2">${i + 1}. ${x.q}</div><div class="grid grid-cols-1 sm:grid-cols-2 gap-2">${x.a.map((t, j) => `<label class="flex items-start gap-2 text-sm text-gray-300 cursor-pointer"><input type="radio" name="qz${i}" value="${j}" class="mt-1" />${t}</label>`).join('')}</div><div class="qz-fb text-xs mt-2"></div></div>`).join('')}</div>
        <div class="flex flex-wrap items-center gap-3 mt-4"><button onclick="gradeQuiz()" class="btn-gold">Grade my quiz</button><span id="quiz-score" class="text-sm text-gold-300"></span></div>`);
    }
    function gradeQuiz() {
      const Q = QUIZZES[quizId].items; let s = 0;
      Q.forEach((x, i) => { const pick = document.querySelector(`input[name="qz${i}"]:checked`); const ok = pick && +pick.value === x.c; if (ok) s++; const fb = document.querySelector(`#qz-${i} .qz-fb`); fb.className = 'qz-fb text-xs mt-2 ' + (ok ? 'text-gold-300' : 'text-rose-300'); fb.textContent = (ok ? '✓ Correct. ' : pick ? '✕ Not quite. ' : '• Unanswered. ') + x.why; });
      const b = ls.get(KEY.quiz, {}); b[quizId] = Math.max(s, b[quizId] || 0); ls.set(KEY.quiz, b);
      document.getElementById('quiz-score').textContent = `Score: ${s}/${Q.length} (best ${b[quizId]}/${Q.length})`;
    }
    const EST_DEFAULT = [['Provider A', 385, 12, 2, true], ['Provider B', 560, 6, 1, true], ['Provider C', 410, 12, 3, true], ['', '', '', '', false]];
    function mEstimate() {
      return card(`<div class="flex flex-wrap items-end justify-between gap-2"><div><div class="eyebrow">Estimate comparison worksheet</div><h2 class="serif text-2xl font-bold text-white">Line up your quotes, side by side.</h2><p class="text-sm text-gray-400 mt-1">Same scope for every quote. Anything 20%+ above the median is flagged for a second look.</p></div></div>
        <div class="overflow-x-auto mt-4"><table class="w-full text-sm min-w-[620px]"><thead><tr class="text-left text-[11px] font-mono uppercase tracking-wider text-gray-500"><th class="pb-2">Provider</th><th class="pb-2">Price ($)</th><th class="pb-2">Warranty (mo)</th><th class="pb-2">Start (days)</th><th class="pb-2">Licensed / insured</th><th class="pb-2">Check</th></tr></thead>
        <tbody>${EST_DEFAULT.map((r, i) => `<tr class="border-t border-gray-800"><td class="py-2 pr-2"><input class="field !py-1.5" id="e${i}n" value="${r[0]}" placeholder="Provider" oninput="calcEstimate()" /></td><td class="pr-2"><input class="field !py-1.5" type="number" id="e${i}p" value="${r[1]}" oninput="calcEstimate()" /></td><td class="pr-2"><input class="field !py-1.5" type="number" id="e${i}w" value="${r[2]}" oninput="calcEstimate()" /></td><td class="pr-2"><input class="field !py-1.5" type="number" id="e${i}d" value="${r[3]}" oninput="calcEstimate()" /></td><td class="text-center"><input type="checkbox" id="e${i}l" ${r[4] ? 'checked' : ''} onchange="calcEstimate()" /></td><td id="e${i}f" class="text-xs"></td></tr>`).join('')}</tbody></table></div>
        <div id="est-out" class="grid grid-cols-2 lg:grid-cols-4 gap-3 mt-5"></div>
        <p class="text-xs text-gray-500 mt-3">A planning tool, not a guarantee of fair price. Verify licenses on TDLR and get the final scope in writing.</p>`);
    }
    function calcEstimate() {
      const rows = [0, 1, 2, 3].map((i) => ({ i, n: document.getElementById('e' + i + 'n').value.trim(), p: parseFloat(document.getElementById('e' + i + 'p').value), w: parseFloat(document.getElementById('e' + i + 'w').value) || 0, l: document.getElementById('e' + i + 'l').checked })).filter((r) => r.p > 0);
      [0, 1, 2, 3].forEach((i) => { document.getElementById('e' + i + 'f').innerHTML = ''; });
      if (!rows.length) { document.getElementById('est-out').innerHTML = ''; return; }
      const ps = rows.map((r) => r.p).sort((a, b) => a - b), mid = ps.length % 2 ? ps[(ps.length - 1) / 2] : (ps[ps.length / 2 - 1] + ps[ps.length / 2]) / 2;
      rows.forEach((r) => { const d = (r.p - mid) / mid * 100; document.getElementById('e' + r.i + 'f').innerHTML = d >= 20 ? `<span class="text-rose-300 font-semibold">+${d.toFixed(0)}% look again</span>` : !r.l ? '<span class="text-amber-300">verify license</span>' : '<span class="text-gold-300">✓ in range</span>'; });
      const ok = rows.filter((r) => r.l && (r.p - mid) / mid < 0.2).sort((a, b) => a.p - b.p || b.w - a.w)[0];
      const f = (x) => '$' + Math.round(x).toLocaleString();
      document.getElementById('est-out').innerHTML = [['Lowest', f(ps[0])], ['Median', f(mid)], ['Highest', f(ps[ps.length - 1])], ['Best value (licensed, in range)', ok ? esc(ok.n || 'Provider') + ' • ' + f(ok.p) : '—']].map(([l, v]) => `<div class="p-4 rounded-xl bg-navy-950/60 border border-gray-800"><div class="text-[11px] font-mono uppercase text-gray-500">${l}</div><div class="text-lg font-bold text-white mt-1">${v}</div></div>`).join('');
    }
    const SAMPLE_TRACK = [
      { title: 'AC blowing warm air', type: 'AC or heating', status: 'Quotes compared', note: '3 licensed-pro quotes compared side by side (sample)' },
      { title: 'Wi-Fi dead zone upstairs', type: 'Computer, Wi-Fi or tech', status: 'Done', note: 'Mesh node added, recap sent (sample)' },
      { title: 'File a DBA for side business', type: 'Start or grow a business', status: 'In progress', note: 'Name search done; Bexar County form next (sample)' },
      { title: 'Antminer Z15 vendor quote', type: 'Crypto hardware sourcing', status: 'In progress', note: '3 seller quotes in; ROI outlook sent (sample)' },
      { title: 'Paint the hallway + patch 2 dings', type: 'Handyman or painting', status: 'Received', note: 'Handyman visit being lined up (sample)' }
    ];
    function trackerRows() { return ls.get(KEY.track, []).concat(SAMPLE_TRACK); }
    function badge(s) { const m = { Received: 'bg-sky-400/15 text-sky-300 border-sky-400/30', 'In progress': 'bg-amber-400/15 text-amber-300 border-amber-400/30', 'Quotes compared': 'bg-gold-400/15 text-gold-300 border-gold-400/30', Done: 'bg-emerald-400/15 text-emerald-300 border-emerald-400/30' }; return `<span class="shrink-0 text-[11px] font-semibold px-2 py-0.5 rounded-full border ${m[s] || m.Received}">${s}</span>`; }
    function mTracker() {
      const types = ['Handyman or painting', 'AC or heating', 'Car trouble', 'Get and compare quotes', 'Crypto hardware sourcing', 'Computer, Wi-Fi or tech', 'Crypto wallet or security', 'Money and markets education', 'Start or grow a business', 'Taxes, insurance or paperwork', 'Senior care or family logistics', 'Something else'];
      return card(`<div class="eyebrow">Request tracker</div><h2 class="serif text-2xl font-bold text-white">Every friction point, tracked to done.</h2>
          <div class="grid grid-cols-1 md:grid-cols-12 gap-3 mt-4"><input id="tr-title" class="field md:col-span-5" placeholder="What's the friction? (e.g. garage door is noisy)" /><select id="tr-type" class="field md:col-span-4">${types.map((t) => `<option>${t}</option>`).join('')}</select><button onclick="addRequest()" class="btn-gold md:col-span-3">${ic('send')}Add request</button></div>
          <p class="text-[11px] text-gray-500 mt-2">Preview: requests you add are saved only in this browser.</p>`) +
        card(`<div class="overflow-x-auto"><table class="w-full text-sm min-w-[560px]"><thead><tr class="text-left text-[11px] font-mono uppercase tracking-wider text-gray-500"><th class="pb-2">Request</th><th class="pb-2">Type</th><th class="pb-2">Status</th><th class="pb-2">Latest</th></tr></thead><tbody>${trackerRows().map((r) => `<tr class="border-t border-gray-800"><td class="py-3 pr-3 text-white font-semibold">${esc(r.title)}</td><td class="pr-3 text-gray-400">${esc(r.type)}</td><td class="pr-3">${badge(r.status)}</td><td class="text-gray-400 text-xs">${esc(r.note)}</td></tr>`).join('')}</tbody></table></div>`) +
        `<div class="flex flex-wrap gap-3 text-xs"><button onclick="ls.set(KEY.track, []);mShow('tracker')" class="text-gray-400 hover:text-gold-300">Clear my demo requests</button><button onclick="lockDemo()" class="text-gray-400 hover:text-gold-300">Re-lock preview</button></div>`;
    }
    function addRequest() {
      const t = document.getElementById('tr-title').value.trim(); if (!t) return;
      const list = ls.get(KEY.track, []); list.unshift({ title: t, type: document.getElementById('tr-type').value, status: 'Received', note: 'Just added (preview).' }); ls.set(KEY.track, list); mShow('tracker');
    }

    // ==================== INIT ====================
    ['hi', 'ci'].forEach(updateIntake);
    route();
