    // ==================== ROUTER ====================
    const VIEWS = ['home','services','how','pricing','members','about','contact','book','legal','waiver'];
    const TITLES = { home: 'The Physical Side of AI', services: 'Services', how: 'How It Works', pricing: 'Pricing', members: 'Members Preview', about: 'About', contact: 'Contact', book: 'Book & Enroll', legal: 'Legal Framework', waiver: 'Client Acknowledgment' };
    function currentView() { const h = (location.hash.replace(/^#\/?/, '').split('?')[0] || 'home'); return VIEWS.includes(h) ? h : 'home'; }
    function hashParam(name) { return new URLSearchParams(location.hash.split('?')[1] || '').get(name); }
    function route() {
      if (location.hash && !location.hash.startsWith('#/')) return; // in-page anchors
      const id = currentView();
      document.querySelectorAll('.view').forEach((v) => v.classList.toggle('on', v.id === 'view-' + id));
      document.querySelectorAll('[data-nav]').forEach((a) => a.classList.toggle('active', a.dataset.nav === id));
      document.getElementById('mobile-menu').classList.add('hidden');
      document.title = 'FelRon IT-Legacy-Capital | ' + TITLES[id];
      if (id === 'book') initEnroll();
      if (id === 'members') initMembers();
      window.scrollTo(0, 0);
      refreshIcons();
    }
    function toggleMenu() { document.getElementById('mobile-menu').classList.toggle('hidden'); }
    function refreshIcons() { if (window.lucide) lucide.createIcons(); }
    window.addEventListener('hashchange', route);

    // ==================== INTAKE (friction funnel) ====================
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
      { id: 'builder', label: 'Builder package ($175)', detail: ['All learning modules', '3 walkthrough sessions', '6 months of the FelRon App, every quiz and worksheet'] },
      { id: 'full', label: 'Full-Service (from $375 or $75/mo)', detail: ['Everything in Builder', 'Quote gathering and comparison', 'Hands-on help and partner coordination', 'Priority scheduling'] },
      { id: 'hourly', label: 'Hands-on help or a single session ($30–50/hr)', detail: ['Everyday fixes, IT help, errands or a walkthrough', 'Bigger jobs quoted upfront', 'Written recap included'] },
      { id: 'quotes', label: 'Get my quotes gathered and compared', detail: ['I make the calls', 'Side-by-side comparison of price, scope, warranty and timeline', 'Billed hourly, quoted upfront'] },
      { id: 'partner', label: 'Partner project: remodeling, mechanic, electrical or AC', detail: ['Quoted per job', 'Quotes compared before you commit', 'I coordinate start to finish'] },
      { id: 'module', label: 'A single learning module ($29)', detail: ['Lesson + 1-on-1 walkthrough', 'Guide, checklist and quiz in the members area'] },
      { id: 'app', label: 'The FelRon App only ($9.50/mo or $49/yr)', detail: ['Members area, guides, quizzes and worksheets', 'Progress tracking'] },
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

    // ==================== MEMBERS AREA (PREVIEW) ====================
    const GUIDES = [
      { id: 'homefix', icon: 'wrench', title: 'Home Fixes & AC Basics', did: 'I learned AC and electrical concepts in HVAC coursework, then put it to work on real systems: filters, thermostats, drain lines and part swaps.',
        steps: ['Find your AC filter size (printed on the filter frame). Check it monthly and replace it every 1–3 months.',
          'Before a service call, check the basics: thermostat mode and batteries, the breaker, and the outdoor disconnect switch.',
          'Warm air and ice on the lines? Turn the system off and let it thaw for a few hours, then restart with a clean filter.',
          'Clear the condensate drain line with a wet/dry vac at the outdoor end, and keep the drain pan clear.',
          'Write down the symptoms (noise, smell, short cycling, warm air) and the model and serial number from the unit label.',
          'Capacitors, contactors, refrigerant and wiring store charge and carry high voltage. Book those with FelRon so my licensed HVAC partner handles them.'],
        together: 'Text me photos of the unit label and the symptoms. I troubleshoot with you, handle the quick fixes, and bring in my licensed HVAC partner for regulated repairs.',
        resources: [['TDLR License Search', 'https://www.tdlr.texas.gov/LicenseSearch/', 'Verify an HVAC or electrical license.'], ['Energy Saver (DOE)', 'https://www.energy.gov/energysaver', 'Heating, cooling and efficiency basics.'], ['CPS Energy', 'https://www.cpsenergy.com', 'San Antonio utility programs and rebates.']] },
      { id: 'estimates', icon: 'scale', title: 'Getting & Comparing Estimates', did: 'Years of retail and assistant-GM work taught me pricing, vendors and margins. I use the same process to compare contractor and shop quotes.',
        steps: ['Write a one-paragraph scope: what needs doing, where, and by when.',
          'Get at least three quotes on the same scope so they can be compared.',
          'Ask each provider for a license number (if the trade requires one), proof of insurance, the warranty on parts and labor, the timeline, and what is not included.',
          'Line them up in the Estimate Worksheet. Anything 20% or more above the median gets a second look.',
          'Verify licenses on TDLR and check reviews and complaints.',
          'Get the final scope and price in writing before work starts, and avoid paying the full amount upfront.'],
        together: 'Send me the scope. I make the calls, gather the quotes and walk you through the comparison. You pick the provider.',
        resources: [['TDLR License Search', 'https://www.tdlr.texas.gov/LicenseSearch/', 'Electrical and HVAC licenses.'], ['Better Business Bureau', 'https://www.bbb.org', 'Business reviews and complaints.'], ['Texas AG Consumer Protection', 'https://www.texasattorneygeneral.gov/consumer-protection', 'Home repair and contractor consumer tips.']] },
      { id: 'auto', icon: 'car', title: 'Car Basics', did: 'I keep my own car running: battery swaps, bulbs, code reads and the pre-road-trip checks I learned growing up.',
        steps: ['Check-engine light on? Get the code read with an OBD-II reader (many parts stores do it free) and write it down.',
          'Look up what the code means, then confirm the cause before buying parts.',
          'Slow crank or clicking? Test the battery. Most last about 3–5 years.',
          'Bulbs and wipers: find the part number in your owner\'s manual or a parts-store lookup.',
          'Check tire pressure monthly (the sticker is in the driver\'s door jamb), plus fluids before road trips.',
          'For bigger repairs, get two shop quotes. I compare them, and my mechanic partner can quote too.'],
        together: 'I come out for the quick fixes and code reads, and coordinate my mechanic partner for bigger repairs.',
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
    const MOD_LIST = [
      ['homefix', 'Home Fixes & AC Basics', 'wrench'], ['estimates', 'Getting & Comparing Estimates', 'scale'], ['business', 'Business Setup (DBA / LLC / EIN)', 'briefcase'],
      ['auto', 'Car Basics', 'car'], ['it', 'Home/Office IT Rescue', 'monitor'], ['crypto', 'Crypto Self-Custody & Security', 'shield-check'], ['paperwork', 'Tax Records & Paperwork', 'file-text'],
      ['insurance', 'Insurance & Claims Paperwork', 'heart-handshake'], ['money', 'Money Basics & Budgeting', 'badge-dollar-sign'], ['market', 'How the Market Works', 'trending-up'],
      ['treasuries', 'Stocks & Treasuries', 'graduation-cap'], ['ai', 'Ticker Evaluation with AI', 'bot'], ['options', 'Options & LEAPS Education', 'zap']
    ];
    const UNLOCKED = ['homefix', 'estimates', 'business']; // demo: a Starter member's 3 modules
    const QUIZZES = {
      estimates: { title: 'Getting & Comparing Estimates', items: [
        { q: 'What makes two quotes truly comparable?', a: ['They came from the same week', 'They cover the same scope of work', 'They have the same company logo', 'They are both under $500'], c: 1, why: 'Quotes only compare apples to apples when the scope is the same.' },
        { q: 'One quote is 35% above the median. Best next step?', a: ['Take it, it must be better', 'Ask what\'s included and compare scope and warranty', 'Ignore the others', 'Pay upfront to lock it in'], c: 1, why: 'Outliers deserve a second look: scope, parts, warranty or padding.' },
        { q: 'In Texas, which of these trades requires a TDLR license?', a: ['Furniture assembly', 'Electrical and air-conditioning work', 'Picture hanging', 'Car washing'], c: 1, why: 'TDLR licenses electricians and air conditioning & refrigeration contractors.' },
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
    const KEY = { unlock: 'felron_demo_unlock_v1', prog: 'felron_member_prog_v1', quiz: 'felron_member_quiz_v1', track: 'felron_member_track_v1' };
    const ls = { get: (k, d) => { try { return JSON.parse(localStorage.getItem(k)) ?? d; } catch (e) { return d; } }, set: (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} } };
    let mTab = 'dash', lessonId = 'homefix', quizId = 'estimates';
    const ic = (n, c = 'w-4 h-4') => `<i data-lucide="${n}" class="${c}"></i>`;
    const card = (inner, cls = '') => `<div class="card rounded-2xl p-5 sm:p-6 ${cls}">${inner}</div>`;
    const guide = (id) => GUIDES.find((g) => g.id === id);

    function initMembers() {
      if (hashParam('demo') === '1') ls.set(KEY.unlock, true);
      const on = ls.get(KEY.unlock, false);
      document.getElementById('m-gate').classList.toggle('hidden', on);
      document.getElementById('m-app').classList.toggle('locked-blur', !on);
      const t = hashParam('tab'); if (t) mTab = t;
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
      const R = { dash: mDash, modules: mModules, lesson: mLesson, guides: mGuides, resources: mResources, quiz: mQuiz, estimate: mEstimate, tracker: mTracker }[t] || mDash;
      document.getElementById('m-body').innerHTML = R();
      if (t === 'estimate') calcEstimate();
      if (t === 'quiz') { const b = ls.get(KEY.quiz, {})[quizId]; document.getElementById('quiz-score').textContent = b != null ? 'Best score on this device: ' + b + '/' + QUIZZES[quizId].items.length : ''; }
      refreshIcons();
    }
    function openLesson(id) { lessonId = id; mShow('lesson'); document.getElementById('m-body').scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    function modRow([id, title, icon]) {
      const open = UNLOCKED.includes(id);
      return `<div class="flex items-center gap-3 p-3.5 rounded-xl border ${open ? 'border-gold-400/40 bg-gold-400/5' : 'border-gray-800 bg-navy-950/60'}">
        <span class="icon-tile !w-10 !h-10 ${open ? '' : 'opacity-50'}">${ic(icon)}</span>
        <div class="flex-1 min-w-0"><div class="text-sm font-semibold ${open ? 'text-white' : 'text-gray-400'}">${title}</div><div class="text-[11px] ${open ? 'text-gold-300' : 'text-gray-500'}">${open ? 'Unlocked • lesson, guide, checklist, quiz' : 'Locked • included in Builder, or $29'}</div></div>
        ${open ? `<button onclick="openLesson('${id}')" class="btn-gold !py-1.5 !px-3 !text-xs">${ic('lock-open', 'w-3.5 h-3.5')}Open</button>` : `<a href="#/pricing" class="btn-ghost !py-1.5 !px-3 !text-xs">${ic('lock', 'w-3.5 h-3.5')}Unlock</a>`}
      </div>`;
    }
    function mDash() {
      const pr = progress(), tr = trackerRows();
      return `<div class="rounded-2xl p-6 sm:p-7 bg-gradient-to-br from-navy-700 to-navy-900 border border-gold-400/30 flex flex-wrap items-center justify-between gap-4">
          <div><div class="eyebrow">Welcome back</div><h2 class="serif text-3xl font-bold text-white">Demo Member</h2><p class="text-sm text-gray-300 mt-1">Pick up where you left off, or send me a new friction point.</p></div>
          <div class="flex gap-2 flex-wrap"><button onclick="openLesson('homefix')" class="btn-gold">${ic('book-open')}Continue lesson</button><button onclick="mShow('tracker')" class="btn-ghost">${ic('send')}New request</button></div></div>
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
          ${[['book-open', UNLOCKED.length + ' / ' + MOD_LIST.length, 'Modules unlocked'], ['list-checks', pr.pct + '%', 'Checklist progress'], ['clipboard-list', tr.filter((r) => r.status !== 'Done').length, 'Open requests'], ['calendar', 'Tue 10 AM', 'Next session (sample)']].map(([i, v, l]) => card(`<div class="text-gold-300">${ic(i, 'w-5 h-5')}</div><div class="text-2xl font-extrabold text-white mt-2">${v}</div><div class="text-xs text-gray-400">${l}</div>`, '!p-4')).join('')}
        </div>
        ${card(`<div class="flex items-center justify-between mb-2"><div class="font-bold text-white">Your progress</div><div class="font-mono text-gold-300 text-sm">${pr.done}/${pr.total} steps</div></div><div class="h-2.5 rounded-full bg-navy-950 overflow-hidden"><div class="h-full bg-gold-400 rounded-full" style="width:${pr.pct}%"></div></div>`)}
        <div class="grid grid-cols-1 xl:grid-cols-2 gap-6">
          ${card(`<div class="flex items-center justify-between mb-3"><div class="font-bold text-white">Continue learning</div><button onclick="mShow('modules')" class="text-xs text-gold-300 hover:underline">All modules →</button></div><div class="space-y-2.5">${MOD_LIST.slice(0, 5).map(modRow).join('')}</div>`)}
          ${card(`<div class="flex items-center justify-between mb-3"><div class="font-bold text-white">Recent requests</div><button onclick="mShow('tracker')" class="text-xs text-gold-300 hover:underline">Tracker →</button></div><div class="space-y-2.5">${tr.slice(0, 4).map((r) => `<div class="flex items-center justify-between gap-3 p-3 rounded-xl bg-navy-950/60 border border-gray-800"><div class="min-w-0"><div class="text-sm text-white font-semibold truncate">${esc(r.title)}</div><div class="text-[11px] text-gray-500">${esc(r.type)}</div></div>${badge(r.status)}</div>`).join('')}</div>`)}
        </div>`;
    }
    function mModules() {
      return card(`<div class="flex flex-wrap items-end justify-between gap-2 mb-4"><div><div class="eyebrow">My modules</div><h2 class="serif text-2xl font-bold text-white">${UNLOCKED.length} unlocked, ${MOD_LIST.length - UNLOCKED.length} available</h2></div><a href="#/pricing" class="text-xs text-gold-300 hover:underline">Upgrade to Builder to unlock all →</a></div><div class="grid grid-cols-1 md:grid-cols-2 gap-3">${MOD_LIST.map(modRow).join('')}</div>`);
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
      { title: 'AC blowing warm air', type: 'AC or heating', status: 'Quotes compared', note: '3 quotes gathered; partner visit Tue (sample)' },
      { title: 'Wi-Fi dead zone upstairs', type: 'Computer, Wi-Fi or tech', status: 'Done', note: 'Mesh node added, recap sent (sample)' },
      { title: 'File a DBA for side business', type: 'Start or grow a business', status: 'In progress', note: 'Name search done; Bexar County form next (sample)' },
      { title: 'Check-engine light', type: 'Car trouble', status: 'Received', note: 'Code read scheduled (sample)' }
    ];
    function trackerRows() { return ls.get(KEY.track, []).concat(SAMPLE_TRACK); }
    const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
    function badge(s) { const m = { Received: 'bg-sky-400/15 text-sky-300 border-sky-400/30', 'In progress': 'bg-amber-400/15 text-amber-300 border-amber-400/30', 'Quotes compared': 'bg-gold-400/15 text-gold-300 border-gold-400/30', Done: 'bg-emerald-400/15 text-emerald-300 border-emerald-400/30' }; return `<span class="shrink-0 text-[11px] font-semibold px-2 py-0.5 rounded-full border ${m[s] || m.Received}">${s}</span>`; }
    function mTracker() {
      const types = ['Home repair or fix', 'AC or heating', 'Car trouble', 'Get and compare quotes', 'Remodel or bigger project', 'Computer, Wi-Fi or tech', 'Crypto wallet or security', 'Money and markets education', 'Start or grow a business', 'Taxes, insurance or paperwork', 'Senior care or family logistics', 'Something else'];
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
