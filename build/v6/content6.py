"""FelRon v6 content data: module catalog (17 Gemini concepts + v5 modules, deduped to 20), services, intake."""
import html
V = '/workspace/felron-site/build/v6/'
R = lambda f: open(V + f).read()
PHONE, PHONE_TEL, EMAIL = '(210) 535-4987', '+12105354987', 'MattDiazSA@gmail.com'
NAME = 'Matthew Alexander Diaz'
def ic(name, cls='w-5 h-5'):
    return f'<i data-lucide="{name}" class="{cls}"></i>'

CATS = {'I': 'Hardware, IT &amp; Web3', 'II': 'Flywheel &amp; Markets', 'III': 'Quotes, Paperwork &amp; Business', 'IV': 'Direct Execution &amp; Care'}
def C(n, cat, icon, title, pub, vault, cap, tool='', guide=''):
    return dict(n=n, cat=cat, icon=icon, title=title, pub=pub, vault=vault, cap=cap, tool=tool, guide=guide)
CONCEPTS = [
 C(1, 'I', 'cpu', 'Crypto Hardware &amp; Machine Sourcing, Setup &amp; ROI Outlook',
   'Buying ASIC miners (Antminer Z9, Z11, Z15 or S-Series) or GPU compute nodes blind often means overpaying or getting worn-out boards. I source vetted machines, compare vendor quotes, set up plug-in miners and pools, and model your realistic electricity-vs-yield ROI.',
   'Step-by-step ASIC &amp; DePIN procurement checklist, secondary-market price-per-hash benchmark sheet, circuit load &amp; PDU worksheet, pool configuration guide and board-cleaning maintenance protocol.',
   'Source vetted ASIC/compute hardware, audit seller quotes, configure plug-in miners and calculate 12-month payback.', 'roi', 'hardware'),
 C(2, 'I', 'shield-check', 'Web3 Self-Custody, DePIN &amp; Zero-Knowledge Hygiene',
   'Web3 means holding your digital assets in your own vault, where you control the keys. You stay at the keyboard for every password and seed phrase while I walk you through cold storage, home-network security and DePIN participation.',
   'Air-gapped seed generation worksheet, multi-wallet compartmentalization (burner vs. vault), DePIN network overview, phishing defense drill and 2FA/encrypted-communication hardening.',
   'Guided client-held wallet setup, cold-storage backup workflow, and home/office network security tune-up.', '', 'web3'),
 C(3, 'II', 'refresh-cw', 'Capital Flywheel, 401(k) Barbell &amp; Treasuries',
   'How I personally connect cashflow, a defensive 401(k) anchor and a small high-conviction sleeve, and why Treasury yields matter to all of it. Shared as education, never as a recommendation for your money.',
   'Interactive Capital Flywheel model, 401(k) fund-menu reading worksheet and a 10-year yield &amp; macro watchlist template.',
   'Plain-English walkthrough of your own 401(k) menu and a personal cashflow map you control.', 'flywheel', 'money'),
 C(4, 'II', 'calendar-range', 'LEAPS (Long-Term 6–24+ Month Equity Option Ladders)',
   'LEAPS are options that expire a year or more out, so time decay works slower. I show how I ladder them, my written rules and the mistakes I have made along the way.',
   'LEAPS ladder planner, theta-zone calendar and roll/trim checklist.', 'Platform walkthrough on your own account. You place your own trades.', 'lab'),
 C(5, 'II', 'shield', 'Margin (Isolated vs. Cross Collateral Protection)',
   "Isolated margin caps a position's loss at the collateral you post. Cross margin can draw on your whole account. Knowing the difference is the first line of defense.",
   'Isolated vs. cross scenario worksheet and a liquidation drill.', 'Walkthrough of margin settings on your own platform.', 'lab'),
 C(6, 'II', 'gauge', 'Leverage (Convexity vs. Debt Multipliers)',
   'Options create leverage through convexity with a capped loss. Borrowed leverage multiplies gains and losses alike. We compare the two side by side.',
   'Leverage comparison calculator and a position-sizing rules template.', 'Side-by-side math on hypothetical examples.', 'lab'),
 C(7, 'II', 'infinity', 'Perps (24/7 Perpetual Futures Mechanics)',
   'Perps are 24/7 contracts that track an asset without an expiration date. I explain how long and short perps work, how liquidations are calculated, and how traders use them to hedge spot holdings.',
   'Perpetual futures position-sizing calculator, liquidation-distance formulas and delta-neutral hedging walkthroughs.', 'Educational simulation of perpetual contract mechanics, stop placement and collateral sizing.', 'lab'),
 C(8, 'II', 'git-branch', 'Derivatives (Asymmetric Risk Transfer)',
   'A derivative is a contract whose value comes from an underlying asset. Used like insurance, it can lock in prices or cap downside while most of your cash stays in safe reserves.',
   'Visual taxonomy of spot vs. options vs. perpetual derivatives and how each fits the Capital Flywheel.', 'Plain-English breakdown of how derivatives transfer risk.'),
 C(9, 'II', 'zap', 'Options / Contracts (Calls, Puts &amp; Protective Strangles)',
   'Calls and puts control 100 shares per contract with a strict dollar cap on risk. I teach how calls capture upside and how protective puts or strangles behave during market dips.',
   'Option-chain reading guide (Delta, Gamma, Theta, Vega, implied volatility) and payoff worksheets.', 'Learn to read option chains, bid-ask spreads and breakeven math before placing a trade.', 'lab'),
 C(10, 'II', 'list-checks', 'Rule-Based Trading, AI-Assisted Research &amp; the +20% Profit Gate',
   'Disciplined rules written before entry: the exact price that invalidates the idea, and a +20% gate before trimming gains. Plus how I use AI tools to research tickers, with a human making every decision.',
   'Pre-trade decision scorecard, invalidation-level logbook, AI research prompt pack and +20% profit-trimming tracker.', 'Set up a personal rule-based trading log and an emotion-free checklist.'),
 C(11, 'II', 'percent', 'Funding Rate (Perpetual Carry Costs)',
   'Perpetual contracts charge or pay a funding rate every 8 hours to keep price near spot. I show how that quiet carry cost adds up over days and weeks.',
   'Funding carry calculator and a daily cost tracker.', 'Calculate the real holding cost of a perp position.', 'lab'),
 C(12, 'II', 'bar-chart-3', 'Volume Profile &amp; Reading the Market',
   'Where buyers and sellers actually traded: volume profile, order types, bid/ask spreads and reading a quote screen and a basic chart.',
   'Volume-profile annotation guide and an order-type cheat sheet.', "Read your own platform's quote screen and chart with confidence."),
 C(13, 'II', 'crosshair', 'Mark Price (Liquidation Reference Price)',
   'Exchanges liquidate on a composite mark price, not the last trade or a quick wick. Knowing which price matters keeps stops and alerts honest.',
   'Mark vs. last price drill and an alert-setup checklist.', 'Audit order triggers so stops and alerts reference composite mark price.', 'lab'),
 C(14, 'III', 'file-text', 'Pre-CPA Tax Records, Insurance Paperwork &amp; Assisted-Living Logistics',
   "A shoebox of receipts, a confusing insurance letter or a parent's assisted-living forms. I sort it, explain it and prep a clean file before billable hours start.",
   'Pre-CPA tax binder checklist, insurance claim deadline tracker and a Texas HHS assisted-living comparison worksheet.', 'Organize tax and insurance packets before CPA billing starts and coordinate family care logistics.', '', 'paperwork'),
 C(15, 'III', 'briefcase', 'Business Planning, LLC/EIN Setup Navigation, Python/Go APIs &amp; MCP',
   'Have a business or side hustle that needs structure? I help organize your business plan, walk you through where to file your Texas LLC or DBA and free IRS EIN, and connect Python/Go scripts or AI MCP tools to automate admin work.',
   'Direct-filing roadmap (Texas SOSDirect, Bexar County DBA, free IRS EIN, business banking readiness), inventory velocity sheets and AI/MCP automation blueprints.', 'Organize business formation paperwork without third-party junk fees, and automate workflows with APIs/MCP.', '', 'business'),
 C(16, 'IV', 'messages-square', '1-on-1 Guidance, Education &amp; Written Maintenance Recaps',
   'Every session translates technical, hardware or financial friction into plain English, ending with a clear written recap of what was set up, how the math works and how to maintain it.',
   'Library of 1-page client handoffs, glossary cheat sheets, and curated directories of official free Texas and federal resources (VITA, SCORE, SBA, TDLR, TexasLawHelp).', 'Book a 1-on-1 session in San Antonio or remotely, with a custom written recap.'),
 C(17, 'IV', 'piggy-bank', 'Savings Planning, Budgeting &amp; Direct Cashflow Execution',
   'A budget that actually runs: a bills calendar, savings automation and cashflow partitions, set up with you on accounts you own.',
   'Budget &amp; bills-calendar template, savings automation checklist and an emergency-fund tracker.', 'Hands-on budget and savings setup, with you approving every step.', '', 'money'),
 C(18, 'III', 'scale', 'Quote &amp; Estimate Comparison',
   'Getting three quotes takes hours of phone tag. I call around, gather quotes from licensed AC, electrical and plumbing pros, contractors and shops, line them up side by side and tell you what a fair price looks like.',
   'Estimate comparison worksheet, quote question script, scope-of-work template and fair-rate benchmarks.', 'I make the calls, compare the quotes and help you schedule the one you choose.', 'estimate', 'estimates'),
 C(19, 'IV', 'paintbrush', 'Handyman Fixes, Painting &amp; AC Filter Basics',
   'Painting, drywall patches, caulking, assembly, TV and shelf mounting, door and cabinet hardware. I handle it or line up the handyman I work with and coordinate the job, plus AC filter changes and a troubleshooting checklist before you pay for a service call.',
   'Home maintenance calendar, AC filter &amp; troubleshooting checklist, paint &amp; patch how-to and a job-scope template.', 'Hands-on fixes and handyman coordination from start to finish.', '', 'homefix'),
 C(20, 'IV', 'car', 'Car Basics',
   'Battery, bulbs, wipers and check-engine code reads, explained in plain English before the shop visit.',
   'Code-read lookup guide, battery &amp; bulb part-finder steps, a road-trip checklist and shop-quote comparison.', 'Quick fixes and code reads, plus shop quotes compared.', '', 'auto'),
]
NC = len(CONCEPTS)

# ---------------- SERVICES (positive-only, Texas-safe wording)
SERVICES = [
  ('paintbrush', 'Handyman Fixes &amp; Painting', 'Hands-on help, or I line up the handyman I work with and coordinate the job.', [
     'Interior painting and touch-ups', 'Drywall patches and caulking', 'Furniture, grill and equipment assembly',
     'TV, shelf and curtain-rod mounting', 'Door and cabinet hardware', 'Minor repairs around the house']),
  ('scale', 'Quote &amp; Estimate Comparison', 'I make the calls, collect the quotes and line them up for you.', [
     'I call around and gather quotes on the same scope of work', 'Quotes from licensed AC, electrical and plumbing pros, compared side by side',
     'Price, scope, warranty and timeline lined up', 'Fair-rate check backed by years of hands-on pricing experience', 'You choose. I help schedule it and follow it through']),
  ('air-vent', 'AC Basics', 'Stay cool and skip the unnecessary service call.', [
     'Filter changes and seasonal checkups', 'Troubleshooting checklist before you call for service', 'Smart-thermostat app and schedule setup',
     'Quotes from licensed AC pros, gathered and compared']),
  ('car', 'Car Basics', 'Quick fixes and straight answers before the shop visit.', [
     'Battery testing and replacement', 'Headlight, taillight and bulb swaps', 'Wiper blades', 'Check-engine code reads, explained in plain English', 'Shop quotes compared']),
  ('cpu', 'Crypto Hardware Sourcing &amp; Setup', 'My lead specialty: the right machine at the right price, running.', [
     'Vetted ASIC and GPU/DePIN machine sourcing', 'Vendor quote audits vs. secondary-market value', 'Plug-in setup and pool configuration',
     '12-month ROI outlook modeling', 'Board cleaning and maintenance']),
  ('monitor', 'IT &amp; Tech Rescue', 'Computers, Wi-Fi and devices: fixed, set up and explained.', [
     'Wi-Fi, router and mesh network setup', 'Slow computer cleanup, backups and new-device setup', 'Printers, phones, tablets and smart TVs',
     'Smart-home apps: cameras, speakers and plugs', 'Password manager and 2-factor security', 'AI assistant and automation setup']),
  ('shield-check', 'Web3 Wallet &amp; Security', 'Self-custody done right: your keys stay in your hands.', [
     'Hardware wallet setup, with you creating and holding the keys', 'Cold storage and a backup plan', 'Scam and phishing defense', 'DePIN participation basics']),
  ('trending-up', 'Money &amp; Markets Education', 'What I do personally, laid out so you can learn it too.', [
     'Capital Flywheel and 401(k) literacy', 'Options, LEAPS and perps education with simulators', 'Rule-based trading process and the +20% profit gate', 'Budget and savings systems']),
  ('briefcase', 'Business Setup', 'From idea to open for business, with the paperwork done right.', [
     'Business plan outlines and pricing worksheets', 'DBA, LLC and EIN paperwork, walked through side by side', 'Websites, booking and invoicing tools',
     'Python/Go and AI/MCP automations for admin work']),
  ('file-text', 'Taxes, Insurance &amp; Paperwork', 'The shoebox, sorted. The confusing letter, explained.', [
     'Tax records organized for your preparer', 'Policies explained in plain English', 'Claim files and deadlines organized', 'Bills, letters and renewals on one calendar']),
  ('heart-handshake', 'Senior Care &amp; Family Logistics', 'Steady help for the people you care about.', [
     'Medical appointment logistics and ride coordination', 'Assisted-living research and paperwork', 'Errands, pickups, moves and hauling', 'Patient tech help for parents and grandparents']),
]
HOME_SERVICES = [0, 1, 2, 3, 4, 5, 7, 8, 10]
def svc_card(s, compact=False):
    icon, title, tag, items = s
    lst = items[:4] if compact else items
    lis = ''.join(f'<li><span>{i}</span></li>' for i in lst)
    return (f'<div class="card card-hover rounded-2xl p-6 flex flex-col gap-3"><div class="flex items-center gap-3"><span class="icon-tile">{ic(icon)}</span>'
            f'<h3 class="text-lg font-bold text-white leading-snug">{title}</h3></div><p class="text-sm text-gray-400">{tag}</p>'
            f'<ul class="chk space-y-1.5 text-sm text-gray-300">{lis}</ul></div>')
home_services = '\n'.join(svc_card(SERVICES[i], True) for i in HOME_SERVICES)
all_services = '\n'.join(svc_card(s) for s in SERVICES)

PROBLEMS = ['Handyman fix or painting', 'Get and compare quotes', 'AC filter or troubleshooting', 'Car trouble', 'Crypto hardware or mining setup',
            'Computer, Wi-Fi or tech', 'Crypto wallet or security', 'Money and markets education', 'Start or grow a business',
            'Taxes, insurance or paperwork', 'Senior care or family logistics', 'Something else (describe it below)']
def intake(p, title='What solvable problem can I help with?'):
    opts = ''.join(f'<option>{html.escape(x)}</option>' for x in PROBLEMS)
    radios = ''.join(f'<label class="flex items-center gap-2"><input type="radio" name="{p}-pref" value="{v}" {"checked" if v=="Call" else ""} onchange="updateIntake(\'{p}\')" />{v}</label>' for v in ['Call', 'Text', 'Email'])
    step = lambda n, t: f'<div class="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-gold-300"><span class="w-5 h-5 rounded-full bg-gold-400 text-navy-950 flex items-center justify-center font-bold">{n}</span>{t}</div>'
    return f'''<form class="card rounded-2xl p-5 sm:p-6 space-y-5 gold-glow" onsubmit="return false" aria-label="Intake form">
      <div><div class="eyebrow">What's the friction? • free first call</div><h2 class="serif text-2xl sm:text-3xl font-bold text-white mt-1">{title}</h2></div>
      <div class="space-y-3">{step(1, 'The friction')}
        <label class="block text-xs text-gray-400" for="{p}-type">What kind of problem is it?</label>
        <select id="{p}-type" class="field" onchange="updateIntake('{p}')">{opts}</select>
        <label class="block text-xs text-gray-400" for="{p}-desc">Describe it in a sentence or two</label>
        <textarea id="{p}-desc" rows="3" class="field" placeholder="e.g. Got two AC quotes and they are $3,000 apart." oninput="updateIntake('{p}')"></textarea></div>
      <div class="space-y-3 pt-4 border-t border-gold-400/15">{step(2, 'How should I reach you?')}
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div><label class="block text-xs text-gray-400 mb-1" for="{p}-name">First name</label><input id="{p}-name" class="field" oninput="updateIntake('{p}')" autocomplete="given-name" /></div>
          <div><label class="block text-xs text-gray-400 mb-1" for="{p}-reach">Phone or email</label><input id="{p}-reach" class="field" oninput="updateIntake('{p}')" /></div></div>
        <div class="flex flex-wrap gap-x-5 gap-y-2 text-sm text-gray-300" role="radiogroup" aria-label="Preferred contact">{radios}</div></div>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
        <a id="{p}-sms" href="sms:{PHONE_TEL}" class="btn-gold">{ic('message-square','w-4 h-4')}Send as a text</a>
        <a id="{p}-mail" href="mailto:{EMAIL}" class="btn-ghost">{ic('mail','w-4 h-4')}Send by email</a></div>
      <p class="text-[11px] text-gray-500">Opens your own text or email app with the message filled in. Please leave out account numbers and passwords. Need a detailed brief? Use the <a href="#/dispatch" class="text-gold-300 hover:underline">First-Call Dispatch</a>.</p>
    </form>'''
