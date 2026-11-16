#!/usr/bin/env python3
"""FelRon IT-Legacy-Capital site build v5: professional multi-section site + members preview.
Run: python3 build/v5/build5.py  ->  writes /workspace/felron-site/index.html"""
import re, html
V = '/workspace/felron-site/build/v5/'
R = lambda f: open(V + f).read()
PHONE, PHONE_TEL, EMAIL = '(210) 535-4987', '+12105354987', 'MattDiazSA@gmail.com'
NAME = 'Matthew Alexander Diaz'

def ic(name, cls='w-5 h-5'):
    return f'<i data-lucide="{name}" class="{cls}"></i>'

# ---------------------------------------------------------------- SERVICES (positive-only)
SERVICES = [
  ('wrench', 'Home Fixes &amp; Everyday Repairs', 'The small jobs that pile up, handled in one visit.', [
     'Leaky faucets, running toilets, sticky doors and hinges',
     'Drywall patches, caulking and weatherstripping',
     'Furniture, grill and equipment assembly',
     'TV mounting, shelves, curtain rods and picture hanging',
     'Light fixture, ceiling fan and switch swaps',
     'Appliance troubleshooting before you pay for a service call']),
  ('air-vent', 'AC &amp; Heating Help', 'Hands-on AC know-how from Electrical &amp; HVAC coursework and real repairs.', [
     'Filter changes and seasonal checkups',
     'Thermostat and smart-thermostat installs',
     'Troubleshooting: no cooling, short cycling, frozen lines, clogged drains',
     'Capacitor, contactor and part swaps, plus full HVAC service with my licensed HVAC partner',
     'Quote comparison on new systems and major repairs']),
  ('car', 'Car Basics', 'Quick fixes and straight answers before the shop visit.', [
     'Battery testing and replacement',
     'Headlight, taillight and bulb swaps; wiper blades',
     'Check-engine code reads, explained in plain English',
     'Fluids, tire pressure and pre-road-trip checks',
     'Bigger repairs through my trusted mechanic partner']),
  ('scale', 'Estimates &amp; Price Comparison', 'I make the calls, collect the quotes and line them up for you.', [
     'I call around and gather quotes on the same scope of work',
     'Side-by-side comparison: price, scope, warranty and timeline',
     'Fair-rate check backed by years of hands-on pricing experience',
     'The right questions to ask, and padded line items spotted',
     'You choose. I help schedule it and follow it through to done']),
  ('hammer', 'Remodeling &amp; Trade Partner Network', 'One contact for the whole job: I coordinate my trusted partners.', [
     'Remodeling: kitchens, baths, flooring and paint',
     'Electrical work by my licensed electrical partner',
     'AC and HVAC work by my licensed HVAC partner',
     'Mechanic and auto repair',
     'I coordinate the job and keep you updated start to finish']),
  ('monitor', 'IT &amp; Tech Rescue', 'Computers, Wi-Fi and devices: fixed, set up and explained.', [
     'Wi-Fi, router and mesh network setup',
     'Slow computer cleanup, backups and new-device setup',
     'Printers, phones, tablets and smart TVs',
     'Smart-home setup: doorbells, cameras, locks and speakers',
     'Password manager and 2-factor security',
     'AI assistant and automation setup for home or business']),
  ('shield-check', 'Crypto Wallet &amp; Security', 'Self-custody done right: your keys stay in your hands.', [
     'Hardware wallet setup, with you creating and holding the keys',
     'Cold storage and a backup plan',
     'Scam and phishing defense',
     'DePIN and mining hardware setup and diagnostics']),
  ('trending-up', 'Money &amp; Markets Education', 'How I learned it, laid out so you can learn it too.', [
     'Budgeting, savings and emergency-fund systems',
     '401(k) literacy: reading your fund menu',
     'How the market works, plus options and LEAPS education',
     'Stocks, Treasuries and the macro picture',
     'My research process, including how I use AI tools']),
  ('briefcase', 'Business Setup', 'From idea to open for business, with the paperwork done right.', [
     'Business plan outlines and pricing worksheets',
     'DBA, LLC and EIN paperwork, walked through side by side',
     'Websites, booking and invoicing tools',
     'Business banking and record-keeping setup',
     'API and AI automations for repetitive admin work']),
  ('file-text', 'Taxes, Insurance &amp; Paperwork', 'The shoebox, sorted. The confusing letter, explained.', [
     'Tax records organized and ready for your preparer',
     'Health, life and auto policies explained in plain English',
     'Claim files and deadlines organized',
     'Bills, letters and renewals on one calendar']),
  ('heart-handshake', 'Senior Care &amp; Family Logistics', 'Steady help for the people you care about.', [
     'Medical appointment logistics and ride coordination',
     'Assisted-living research and paperwork',
     'Errands, pickups, moves and hauling',
     'Patient tech help for parents and grandparents']),
]
HOME_SERVICES = [0, 1, 2, 3, 4, 5, 6, 8, 10]

def svc_card(s, compact=False):
    icon, title, tag, items = s
    lst = items[:4] if compact else items
    return f'''<div class="card card-hover rounded-2xl p-6 flex flex-col gap-3">
          <div class="flex items-center gap-3"><span class="icon-tile">{ic(icon)}</span><h3 class="text-lg font-bold text-white leading-snug">{title}</h3></div>
          <p class="text-sm text-gray-400">{tag}</p>
          <ul class="chk space-y-1.5 text-sm text-gray-300">{''.join(f'<li><span>{i}</span></li>' for i in lst)}</ul>
        </div>'''

home_services = '\n        '.join(svc_card(SERVICES[i], True) for i in HOME_SERVICES)
all_services = '\n        '.join(svc_card(s) for s in SERVICES)

PROBLEMS = ['Home repair or fix', 'AC or heating', 'Car trouble', 'Get and compare quotes', 'Remodel or bigger project',
            'Computer, Wi-Fi or tech', 'Crypto wallet or security', 'Money and markets education', 'Start or grow a business',
            'Taxes, insurance or paperwork', 'Senior care or family logistics', 'Something else (describe it below)']

def intake(prefix, title='What solvable problem can I help with?'):
    opts = ''.join(f'<option>{html.escape(p)}</option>' for p in PROBLEMS)
    return f'''<form class="card rounded-2xl p-5 sm:p-6 space-y-5 gold-glow" onsubmit="return false" aria-label="Intake form">
          <div>
            <div class="eyebrow">Start here • free first call</div>
            <h2 class="serif text-2xl sm:text-3xl font-bold text-white mt-1">{title}</h2>
          </div>
          <div class="space-y-3">
            <div class="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-gold-300"><span class="w-5 h-5 rounded-full bg-gold-400 text-navy-950 flex items-center justify-center font-bold">1</span>The friction</div>
            <label class="block text-xs text-gray-400" for="{prefix}-type">What kind of problem is it?</label>
            <select id="{prefix}-type" class="field" onchange="updateIntake('{prefix}')">{opts}</select>
            <label class="block text-xs text-gray-400" for="{prefix}-desc">Describe it in a sentence or two</label>
            <textarea id="{prefix}-desc" rows="3" class="field" placeholder="e.g. AC is running but blowing warm air since Saturday." oninput="updateIntake('{prefix}')"></textarea>
          </div>
          <div class="space-y-3 pt-4 border-t border-gold-400/15">
            <div class="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-gold-300"><span class="w-5 h-5 rounded-full bg-gold-400 text-navy-950 flex items-center justify-center font-bold">2</span>How should I reach you?</div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div><label class="block text-xs text-gray-400 mb-1" for="{prefix}-name">First name</label><input id="{prefix}-name" class="field" oninput="updateIntake('{prefix}')" autocomplete="given-name" /></div>
              <div><label class="block text-xs text-gray-400 mb-1" for="{prefix}-reach">Phone or email</label><input id="{prefix}-reach" class="field" oninput="updateIntake('{prefix}')" /></div>
            </div>
            <div class="flex flex-wrap gap-x-5 gap-y-2 text-sm text-gray-300" role="radiogroup" aria-label="Preferred contact">
              <label class="flex items-center gap-2"><input type="radio" name="{prefix}-pref" value="Call" checked onchange="updateIntake('{prefix}')" />Call</label>
              <label class="flex items-center gap-2"><input type="radio" name="{prefix}-pref" value="Text" onchange="updateIntake('{prefix}')" />Text</label>
              <label class="flex items-center gap-2"><input type="radio" name="{prefix}-pref" value="Email" onchange="updateIntake('{prefix}')" />Email</label>
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
            <a id="{prefix}-sms" href="sms:{PHONE_TEL}" class="btn-gold">{ic('message-square','w-4 h-4')}Send as a text</a>
            <a id="{prefix}-mail" href="mailto:{EMAIL}" class="btn-ghost">{ic('mail','w-4 h-4')}Send by email</a>
          </div>
          <p class="text-[11px] text-gray-500">Opens your own text or email app with the message filled in. Please leave out account numbers and passwords.</p>
        </form>'''

# ---------------------------------------------------------------- PRICING
MODULES = [
  ('wrench', 'Home Fixes &amp; AC Basics'), ('scale', 'Getting &amp; Comparing Estimates'), ('car', 'Car Basics'),
  ('monitor', 'Home/Office IT Rescue'), ('shield-check', 'Crypto Self-Custody &amp; Security'), ('briefcase', 'Business Setup (DBA / LLC / EIN)'),
  ('file-text', 'Tax Records &amp; Paperwork'), ('heart-handshake', 'Insurance &amp; Claims Paperwork'), ('badge-dollar-sign', 'Money Basics &amp; Budgeting'),
  ('trending-up', 'How the Market Works'), ('graduation-cap', 'Stocks &amp; Treasuries'), ('bot', 'Ticker Evaluation with AI'), ('zap', 'Options &amp; LEAPS Education'),
]
module_rows = ''.join(f'<div class="flex items-center gap-3 p-3 rounded-xl bg-navy-950/60 border border-gray-800"><span class="text-gold-300">{ic(i,"w-4 h-4")}</span><span class="text-sm text-gray-200 flex-1">{t}</span><span class="font-mono text-gold-300 text-sm font-bold">$29</span></div>' for i, t in MODULES)

PACKAGES = [
  ('starter', 'Starter', '$75', 'Start with the basics', ['Any 3 learning modules', 'One 1-hour walkthrough session', '3 months of the FelRon App', 'Written recap after the session']),
  ('builder', 'Builder', '$175', 'Most popular', ['All learning modules', '3 walkthrough sessions', '6 months of the FelRon App with every quiz', 'Estimate worksheet and intake tracker', 'Written recaps after every session']),
  ('full', 'Full-Service', 'from $375', 'Done with you', ['Everything in Builder', 'I make the calls and compare your quotes', 'Hands-on help and partner coordination', 'Ongoing walkthrough sessions', 'Priority scheduling']),
]
def pkg_card(p, i):
    pid, name, price, tag, feats = p
    hot = i == 1
    return f'''<div class="card rounded-2xl p-6 sm:p-7 flex flex-col gap-4 relative {'border-2 border-gold-400 gold-glow' if hot else ''}">
          {'<span class="absolute -top-3 left-6 px-3 py-1 rounded-full bg-gold-400 text-navy-950 text-[11px] font-bold uppercase tracking-wider">Most popular</span>' if hot else ''}
          <div><div class="eyebrow">{tag if not hot else 'Learn it all'}</div><h3 class="serif text-3xl font-bold text-white mt-1">{name}</h3></div>
          <div><span class="text-4xl font-extrabold text-white">{price}</span>{'<div class="text-xs text-gray-400 mt-1">or $75/mo • done with you</div>' if pid=='full' else '<span class="text-sm text-gray-400"> one-time</span>'}</div>
          <ul class="chk space-y-2 text-sm text-gray-300 flex-1">{''.join(f'<li><span>{f}</span></li>' for f in feats)}</ul>
          <a href="#/book?item={pid}" class="{'btn-gold' if hot else 'btn-ghost'} w-full">Choose {name} {ic('arrow-right','w-4 h-4')}</a>
        </div>'''
packages = '\n        '.join(pkg_card(p, i) for i, p in enumerate(PACKAGES))
extras = f'''<div class="grid grid-cols-1 md:grid-cols-3 gap-5">
        <div class="card rounded-2xl p-6 space-y-2"><span class="icon-tile">{ic('layout-dashboard')}</span><h3 class="text-lg font-bold text-white pt-1">FelRon App only</h3><div class="text-2xl font-extrabold text-white">$9.50<span class="text-sm text-gray-400 font-normal">/mo</span> <span class="text-sm text-gray-400 font-normal">or $49/yr</span></div><p class="text-sm text-gray-400">Members area, guides, quizzes, worksheets and progress tracking. Included in every package.</p><a href="#/book?item=app" class="btn-ghost mt-2">Get the App</a></div>
        <div class="card rounded-2xl p-6 space-y-2"><span class="icon-tile">{ic('wrench')}</span><h3 class="text-lg font-bold text-white pt-1">Hands-on help &amp; sessions</h3><div class="text-2xl font-extrabold text-white">$30–50<span class="text-sm text-gray-400 font-normal">/hr</span></div><p class="text-sm text-gray-400">Everyday fixes, IT help, quote gathering and comparison, errands and walkthrough sessions. Bigger jobs quoted upfront.</p><a href="#/book?item=hourly" class="btn-gold mt-2">Book hands-on help</a></div>
        <div class="card rounded-2xl p-6 space-y-2"><span class="icon-tile">{ic('handshake')}</span><h3 class="text-lg font-bold text-white pt-1">Partner projects</h3><div class="text-2xl font-extrabold text-white">Quoted per job</div><p class="text-sm text-gray-400">Remodeling, mechanic, electrical and HVAC work through my trusted partners, with quotes compared side by side before you commit.</p><a href="#/contact" class="btn-ghost mt-2">Request a quote</a></div>
      </div>'''
price_note = '<p class="text-xs text-gray-500">Starting prices, subject to change. Final pricing is confirmed in writing before you pay. Flat fees only.</p>'

# ---------------------------------------------------------------- SHARED BLOCKS
three_step = f'''<div class="grid grid-cols-1 md:grid-cols-3 gap-5">
        <div class="card rounded-2xl p-6 relative overflow-hidden"><div class="serif text-6xl font-bold text-gold-400/20 absolute right-4 top-2">01</div><span class="icon-tile">{ic('route')}</span><h3 class="text-lg font-bold text-white mt-4">How I did it</h3><p class="text-sm text-gray-400 mt-1.5">I show you how I handled it myself, with real examples from real jobs, mistakes included.</p></div>
        <div class="card rounded-2xl p-6 relative overflow-hidden"><div class="serif text-6xl font-bold text-gold-400/20 absolute right-4 top-2">02</div><span class="icon-tile">{ic('book-open')}</span><h3 class="text-lg font-bold text-white mt-4">How you can do it</h3><p class="text-sm text-gray-400 mt-1.5">Step-by-step guides, checklists and quizzes in the members area, so you can do it yourself next time.</p></div>
        <div class="rounded-2xl p-6 relative overflow-hidden border-2 border-gold-400 bg-gold-400/10"><div class="serif text-6xl font-bold text-gold-400/25 absolute right-4 top-2">03</div><span class="icon-tile">{ic('hand')}</span><h3 class="text-lg font-bold text-white mt-4">Let's get it done together</h3><p class="text-sm text-gray-300 mt-1.5">I bring the hands-on work, the calls and the partner network. You approve every step.</p></div>
      </div>'''

def section_head(eyebrow, title, sub='', center=False):
    c = 'text-center mx-auto' if center else ''
    return f'''<div class="max-w-3xl {c} space-y-3"><div class="eyebrow">{eyebrow}</div><h2 class="serif h-section font-bold text-white">{title}</h2>{f'<p class="text-base text-gray-400 leading-relaxed">{sub}</p>' if sub else ''}</div>'''

def page_hero(eyebrow, title, sub):
    return f'''<section class="hero-bg border-b border-gold-400/15"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-14 sm:py-20 space-y-4"><div class="eyebrow">{eyebrow}</div><h1 class="serif h-display font-bold text-white max-w-4xl">{title}</h1><p class="text-lg text-gray-300 max-w-2xl leading-relaxed">{sub}</p></div></section>'''

cta_band = f'''<section class="max-w-7xl mx-auto px-5 sm:px-8 py-14"><div class="gold-band rounded-3xl p-7 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-6 items-center shadow-2xl">
      <div class="lg:col-span-7 space-y-2"><div class="font-mono text-xs uppercase tracking-[.2em] font-bold text-navy-800">Before the lawyer. Before the CPA. Before the contractor.</div><h2 class="serif text-3xl sm:text-4xl font-bold text-navy-950">Call FelRon first.</h2><p class="text-sm sm:text-base font-semibold text-navy-900">One contact for the knowledge, the quotes and the hands-on work.</p></div>
      <div class="lg:col-span-5 bg-navy-950 rounded-2xl p-5 space-y-3 text-sm">
        <a href="tel:{PHONE_TEL}" class="flex items-center gap-3 text-white font-semibold hover:text-gold-300">{ic('phone','w-4 h-4 text-gold-400')}{PHONE}</a>
        <a href="mailto:{EMAIL}" class="flex items-center gap-3 text-white font-semibold hover:text-gold-300 break-all">{ic('mail','w-4 h-4 text-gold-400')}{EMAIL}</a>
        <div class="flex items-center gap-3 text-gray-300">{ic('map-pin','w-4 h-4 text-gold-400')}San Antonio, TX</div>
        <div class="pt-2 border-t border-gray-800"><div class="text-[10px] font-mono uppercase tracking-widest text-gold-400">Founder</div><div class="serif text-xl font-bold text-white">{NAME}</div></div>
      </div></div></section>'''

story_band = f'''<section class="max-w-7xl mx-auto px-5 sm:px-8 py-14"><div class="rounded-3xl border border-dashed border-gold-400/40 p-8 sm:p-10 text-center space-y-3">
      <span class="icon-tile mx-auto">{ic('quote')}</span><div class="eyebrow">Client stories</div><h2 class="serif text-3xl font-bold text-white">Your story could be here.</h2>
      <p class="text-sm text-gray-400 max-w-xl mx-auto">FelRon is new, and client stories will appear here as they come in. Worked with me? I'd love to hear how it went.</p>
      <a href="#/contact" class="btn-ghost">Share your experience</a></div></section>'''

# ---------------------------------------------------------------- PAGES
home = f'''<div id="view-home" class="view">
  <section class="hero-bg grid-lines border-b border-gold-400/15">
    <div class="max-w-7xl mx-auto px-5 sm:px-8 py-12 sm:py-20 grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
      <div class="lg:col-span-7 space-y-6 pt-2">
        <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full border border-gold-400/40 bg-gold-400/10 text-xs font-semibold text-gold-300">{ic('sparkles','w-3.5 h-3.5')}The physical side of AI • San Antonio, TX</div>
        <h1 class="serif h-display font-bold text-white">What's the friction?<br /><span class="italic text-gold-300">Let's solve it.</span></h1>
        <p class="text-lg text-gray-300 leading-relaxed max-w-2xl">A broken AC, a car that won't start, a quote that feels too high, a business you want to launch, a pile of paperwork. Tell me what's stuck. <strong class="text-white">I bring the know-how and the hands-on work</strong>: I show you how I'd handle it, show you how you can, then we get it done together.</p>
        <div class="flex flex-wrap gap-3"><a href="#intake" onclick="document.getElementById('home-intake').scrollIntoView({{behavior:'smooth'}});return false" class="btn-gold">Tell me the problem {ic('arrow-right','w-4 h-4')}</a><a href="#/services" class="btn-ghost">See what I help with</a></div>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-2">
          <div class="flex items-center gap-2 text-sm text-gray-300">{ic('phone','w-4 h-4 text-gold-400 shrink-0')}Free 15-min call</div>
          <div class="flex items-center gap-2 text-sm text-gray-300">{ic('scale','w-4 h-4 text-gold-400 shrink-0')}Quotes compared</div>
          <div class="flex items-center gap-2 text-sm text-gray-300">{ic('handshake','w-4 h-4 text-gold-400 shrink-0')}Trusted partners</div>
          <div class="flex items-center gap-2 text-sm text-gray-300">{ic('badge-dollar-sign','w-4 h-4 text-gold-400 shrink-0')}Flat, upfront fees</div>
        </div>
        <div class="pt-5 border-t border-gold-400/20 max-w-md"><div class="text-[11px] font-mono uppercase tracking-widest text-gold-400">Founder</div><div class="serif text-2xl sm:text-3xl font-bold text-white">{NAME}</div><div class="text-sm text-gray-400">Son of a 29-year Army combat medic • San Antonio, TX</div></div>
      </div>
      <div id="home-intake" class="lg:col-span-5 scroll-mt-24">{intake('hi')}</div>
    </div>
  </section>

  <section class="border-b border-gold-400/15 bg-navy-900/60"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-14 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
    <div class="lg:col-span-5 space-y-3"><div class="eyebrow">Why FelRon</div><h2 class="serif h-section font-bold text-white">The physical side of <span class="italic text-gold-300">AI.</span></h2></div>
    <div class="lg:col-span-7 space-y-4 text-gray-300 leading-relaxed">
      <p class="text-lg">AI can tell you what's probably wrong. It can't swap the part, call three contractors, read the fine print on the quote, or sit with your mom at her appointment.</p>
      <p>That's where I come in. I'm the hands-on person for the friction points where online answers stop: <strong class="text-white">the knowledge and the physical work in one place</strong>, and one contact for the whole package, from the first question to the finished job.</p>
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2">
        <div class="card rounded-xl p-4"><div class="text-gold-300">{ic('bot')}</div><div class="font-bold text-white mt-2 text-sm">The knowledge</div><p class="text-xs text-gray-400 mt-1">Clear answers and a plan, explained plainly.</p></div>
        <div class="card rounded-xl p-4"><div class="text-gold-300">{ic('wrench')}</div><div class="font-bold text-white mt-2 text-sm">The hands</div><p class="text-xs text-gray-400 mt-1">Fixes, setups, calls, errands, done in person.</p></div>
        <div class="card rounded-xl p-4"><div class="text-gold-300">{ic('users')}</div><div class="font-bold text-white mt-2 text-sm">The network</div><p class="text-xs text-gray-400 mt-1">Trusted partners for the bigger jobs.</p></div>
      </div>
    </div></div></section>

  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-16 space-y-10">
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-4">{section_head('What I help with', 'Day-to-day fixes to <span class="italic text-gold-300">big-picture plans.</span>', 'If it is causing friction and it can be solved, bring it to me.')}<a href="#/services" class="btn-ghost shrink-0">All services {ic('arrow-right','w-4 h-4')}</a></div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        {home_services}
    </div>
  </section>

  <section class="bg-navy-900/60 border-y border-gold-400/15"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-16 space-y-10">
    {section_head('How it works', 'Show you. Teach you. <span class="italic text-gold-300">Get it done together.</span>', 'Every job follows the same three steps, so you walk away with the fix and the know-how.', True)}
    {three_step}
  </div></section>

  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-16 grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
    <div class="space-y-4">{section_head('Estimates &amp; price comparison', 'I make the calls. <span class="italic text-gold-300">You keep the savings.</span>', 'Getting three quotes takes hours of phone tag. I do the calling, line the estimates up side by side and tell you what a fair rate looks like, based on years of hands-on pricing and inventory experience.')}
      <ul class="chk space-y-2 text-sm text-gray-300"><li><span>Same scope, apples to apples</span></li><li><span>Price, warranty, timeline and license checked</span></li><li><span>Outliers and padded line items flagged</span></li><li><span>You pick the provider. I help it get done.</span></li></ul>
      <a href="#/contact" class="btn-gold">Get my quotes compared {ic('arrow-right','w-4 h-4')}</a></div>
    <div class="card rounded-2xl p-5 sm:p-6 space-y-3" aria-label="Sample comparison">
      <div class="flex items-center justify-between"><div class="text-sm font-bold text-white">Sample: AC repair quotes</div><span class="text-[10px] font-mono uppercase px-2 py-0.5 rounded bg-gold-400/15 text-gold-300 border border-gold-400/30">Example</span></div>
      <div class="overflow-x-auto"><table class="w-full text-sm"><thead><tr class="text-left text-[11px] font-mono uppercase tracking-wider text-gray-500"><th class="py-2">Provider</th><th>Price</th><th>Warranty</th><th>Licensed</th></tr></thead>
      <tbody class="text-gray-300"><tr class="border-t border-gray-800 bg-gold-400/10"><td class="py-2.5 font-semibold text-white">Provider A ★</td><td class="font-semibold text-white">$385</td><td>12 mo</td><td class="text-gold-300">Yes</td></tr><tr class="border-t border-gray-800"><td class="py-2.5">Provider B</td><td class="text-rose-300">$560 <span class="text-[10px]">+37%</span></td><td>6 mo</td><td class="text-gold-300">Yes</td></tr><tr class="border-t border-gray-800"><td class="py-2.5">Provider C</td><td>$410</td><td>12 mo</td><td class="text-gold-300">Yes</td></tr></tbody></table></div>
      <p class="text-xs text-gray-500">Illustration only. Members get the full Estimate Worksheet.</p></div>
  </section>

  <section class="bg-navy-900/60 border-y border-gold-400/15"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-16 space-y-10">
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-4">{section_head('Pricing', 'Simple, flat <span class="italic text-gold-300">pricing.</span>', 'Learning modules from $29. Packages include the FelRon App and members area.')}<a href="#/pricing" class="btn-ghost shrink-0">Full pricing {ic('arrow-right','w-4 h-4')}</a></div>
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 pt-3">
        {packages}
    </div>
    {price_note}
  </div></section>

  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-16 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
    <div class="lg:col-span-7 space-y-4">{section_head('About', 'Raised on <span class="italic text-gold-300">composure under pressure.</span>')}
      <p class="text-gray-300 leading-relaxed">I'm the son of a 29-year U.S. Army combat medic and Bronze Star recipient, and of a mother decorated for her Family Readiness Group service. In our house, when someone had a broken computer, a confusing bill or a schedule falling apart, we stepped up and fixed it. FelRon is named in my parents' honor and brings that same calm, hands-on help to every client.</p>
      <a href="#/about" class="btn-ghost">Read my story {ic('arrow-right','w-4 h-4')}</a></div>
    <div class="lg:col-span-5 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-1 gap-4">
      <div class="card rounded-2xl p-5 border-l-4 border-l-gold-400"><div class="serif text-2xl font-bold text-gold-300">29 Years • Bronze Star</div><p class="text-sm text-gray-400 mt-1">My father's career as a U.S. Army combat medic.</p></div>
      <div class="card rounded-2xl p-5 border-l-4 border-l-gold-400"><div class="serif text-2xl font-bold text-gold-300">FRG Honors</div><p class="text-sm text-gray-400 mt-1">My mother's medals for Family Readiness Group service.</p></div>
    </div>
  </section>
  {story_band}
  {cta_band}
</div>
'''

services = f'''<div id="view-services" class="view">
  {page_hero('Services', 'Everything I help <span class="italic text-gold-300">with.</span>', 'Hands-on fixes, calls and coordination, IT, paperwork and education, all from one contact. If it is causing friction and it can be solved, bring it to me.')}
  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-14 space-y-10">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        {all_services}
    </div>
    <div class="card rounded-2xl p-6 sm:p-8 grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
      <div class="lg:col-span-8 space-y-2"><div class="eyebrow">Don't see it listed?</div><h2 class="serif text-3xl font-bold text-white">Tell me the friction anyway.</h2><p class="text-gray-400">Most problems are solvable with the right knowledge, the right hands or the right partner. I'll tell you on the free first call how I'd approach it.</p></div>
      <div class="lg:col-span-4 flex flex-wrap gap-3 lg:justify-end"><a href="#/contact" class="btn-gold">Describe my problem</a><a href="#/pricing" class="btn-ghost">See pricing</a></div>
    </div>
  </section>
  {cta_band}
</div>
'''

how = f'''<div id="view-how" class="view">
  {page_hero('How it works', 'From friction to <span class="italic text-gold-300">finished.</span>', 'One simple process for every job, whether it is a thermostat install, a quote comparison or a new LLC.')}
  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-14 space-y-14">
    {three_step}
    <div class="space-y-6">{section_head('The process', 'What happens after you <span class="italic text-gold-300">reach out.</span>')}
      <ol class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
        {''.join(f'<li class="card rounded-2xl p-5"><div class="serif text-3xl font-bold text-gold-300">{n:02d}</div><div class="font-bold text-white mt-1">{t}</div><p class="text-sm text-gray-400 mt-1">{d}</p></li>' for n,(t,d) in enumerate([('Tell me the friction','Use the intake form, text or call. A sentence or two is plenty.'),('Free 15-min call','We talk it through and I lay out how I would approach it.'),('Plan &amp; quotes','A clear plan, a flat price, and quotes gathered and compared when needed.'),('Get it done','Hands-on work, partner coordination and walkthroughs, with you approving each step.'),('Written recap','What was done, what it cost and how to handle it next time.')],1))}
      </ol></div>
    <div class="space-y-6">{section_head('How I work', 'Private by design. <span class="italic text-gold-300">Clear by default.</span>')}
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div class="card rounded-2xl p-5"><span class="icon-tile">{ic('circle-check')}</span><div class="font-bold text-white mt-3">You approve every step</div><p class="text-sm text-gray-400 mt-1">Nothing happens without your OK. You stay the decision-maker.</p></div>
        <div class="card rounded-2xl p-5"><span class="icon-tile">{ic('badge-dollar-sign')}</span><div class="font-bold text-white mt-3">Flat, upfront pricing</div><p class="text-sm text-gray-400 mt-1">Confirmed in writing before any work or payment.</p></div>
        <div class="card rounded-2xl p-5"><span class="icon-tile">{ic('lock')}</span><div class="font-bold text-white mt-3">Your keys stay yours</div><p class="text-sm text-gray-400 mt-1">Passwords, seed phrases and logins stay in your hands. Need-to-know info only.</p></div>
        <div class="card rounded-2xl p-5"><span class="icon-tile">{ic('clipboard-list')}</span><div class="font-bold text-white mt-3">Written recap</div><p class="text-sm text-gray-400 mt-1">A record of every session and job for your files.</p></div>
      </div></div>
  </section>
  {cta_band}
</div>
'''

members_teaser = f'''<div class="card rounded-2xl p-6 sm:p-8 grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
      <div class="lg:col-span-7 space-y-3"><div class="eyebrow">Included with every package</div><h2 class="serif text-3xl font-bold text-white">The members area</h2><p class="text-gray-400">Where the answers live: step-by-step guides, the trusted resource directory, quizzes, the estimate comparison worksheet and your request tracker.</p>
        <div class="grid grid-cols-2 gap-2 text-sm text-gray-300">{''.join(f'<div class="flex items-center gap-2"><span class="text-gold-300">{ic(i,"w-4 h-4")}</span>{t}</div>' for i,t in [('list-checks','Step-by-step guides'),('library','Resource directory'),('graduation-cap','Quizzes &amp; testing'),('calculator','Estimate worksheet'),('clipboard-list','Request tracker'),('layout-dashboard','Progress dashboard')])}</div></div>
      <div class="lg:col-span-5 flex flex-wrap gap-3 lg:justify-end"><a href="#/members" class="btn-gold">{ic('lock-open','w-4 h-4')}Preview the members area</a></div>
    </div>'''

pricing = f'''<div id="view-pricing" class="view">
  {page_hero('Pricing', 'Flat fees. <span class="italic text-gold-300">No surprises.</span>', 'Pick a package, a single module or hands-on help by the hour. Every package includes the FelRon App and members area.')}
  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-14 space-y-14">
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 pt-3">
        {packages}
    </div>
    {extras}
    <div class="space-y-5">{section_head('Learning modules', 'Single modules, <span class="italic text-gold-300">$29 each.</span>', 'Each module: a lesson, a 1-on-1 walkthrough, and the guide, checklist and quiz in the members area.')}
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">{module_rows}</div></div>
    {members_teaser}
    {price_note}
  </section>
  {cta_band}
</div>
'''

about = f'''<div id="view-about" class="view">
  <section class="hero-bg border-b border-gold-400/15"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-14 sm:py-20 space-y-3">
    <div class="eyebrow">About • Founder, <span class="seg">FelRon IT-Legacy-Capital</span></div>
    <h1 class="serif h-display font-bold text-gold-300">{NAME}</h1>
    <p class="text-lg text-gray-300">San Antonio, Texas</p></div></section>
  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-14 grid grid-cols-1 lg:grid-cols-12 gap-10">
    <div class="lg:col-span-8 space-y-5 text-gray-300 leading-relaxed">
      <h2 class="serif h-section font-bold text-white">Raised by people who <span class="italic text-gold-300">show up for others.</span></h2>
      <p>I grew up in a family built on service. My father spent 29 years as a U.S. Army combat medic, serving with airborne, light infantry and Stryker units, and he earned the Bronze Star along the way. My mother held our family together through every move and deployment. She was decorated for her work with the Family Readiness Group (FRG), supporting other military families, and built her own career in fine retail and diamond jewelry.</p>
      <p>From them I learned to stay calm when things go wrong and to take care of the people around me. In our house, when a relative or friend had a computer that wouldn't work, an AC on the fritz, a confusing bill or a schedule falling apart, we helped. <strong class="text-white">FelRon IT-Legacy-Capital</strong> is named in my parents' honor and brings that same steady calm, patience and good faith to everyone I work with.</p>
      <p>Today I'm the hands-on person for the friction points where online answers stop. I fix what I can fix myself, I make the calls and compare the quotes, and I bring in trusted partners for remodeling, mechanic, electrical and AC work. You get the knowledge and the physical work in one place.</p>
    </div>
    <div class="lg:col-span-4 space-y-4">
      <div class="card rounded-2xl p-5 border-l-4 border-l-gold-400"><div class="serif text-2xl font-bold text-gold-300">29 Years • Bronze Star</div><p class="text-sm text-gray-400 mt-1">My father's career as a U.S. Army combat medic with airborne, light infantry and Stryker units.</p></div>
      <div class="card rounded-2xl p-5 border-l-4 border-l-gold-400"><div class="serif text-2xl font-bold text-gold-300">FRG Honors</div><p class="text-sm text-gray-400 mt-1">My mother, decorated for Family Readiness Group service.</p></div>
      <div class="card rounded-2xl p-5 space-y-2"><div class="eyebrow">Training &amp; experience</div><ul class="chk space-y-1.5 text-sm text-gray-300"><li><span>Electrical Concepts &amp; HVAC Systems coursework (Southern Careers Institute)</span></li><li><span>Logistics &amp; Supply Chain Management (Northeast Lakeview College)</span></li><li><span>Years of retail and assistant-GM management: pricing, inventory, vendors and teams</span></li><li><span>Data tools built in Python and Go</span></li><li><span>AP Macroeconomics</span></li></ul></div>
    </div>
  </section>
  {story_band}
  {cta_band}
</div>
'''

contact = f'''<div id="view-contact" class="view">
  {page_hero('Contact', 'Tell me the <span class="italic text-gold-300">friction.</span>', 'Describe the problem, then tell me how to reach you. The first 15-minute call is free.')}
  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-14 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
    <div class="lg:col-span-7">{intake('ci')}</div>
    <div class="lg:col-span-5 space-y-5">
      <div class="card rounded-2xl p-6 space-y-5">
        <div><div class="eyebrow">Phone</div><a href="tel:{PHONE_TEL}" class="serif text-3xl font-bold text-white hover:text-gold-300">{PHONE}</a></div>
        <div><div class="eyebrow">Email</div><a href="mailto:{EMAIL}" class="text-lg font-semibold text-white hover:text-gold-300 break-all">{EMAIL}</a></div>
        <div><div class="eyebrow">Service area</div><div class="text-white font-semibold">San Antonio, TX and surrounding area</div><div class="text-sm text-gray-400">On-site visits, plus remote sessions anywhere.</div></div>
        <div><div class="eyebrow">Founder</div><div class="serif text-2xl font-bold text-gold-300">{NAME}</div></div>
      </div>
      <div class="card rounded-2xl p-6 space-y-2"><div class="font-bold text-white">Ready to enroll?</div><p class="text-sm text-gray-400">Choose a module, package or hands-on help and book your free first call.</p><a href="#/book" class="btn-gold mt-1">Book &amp; enroll {ic('arrow-right','w-4 h-4')}</a></div>
    </div>
  </section>
</div>
'''

book = f'''<div id="view-book" class="view">
  {page_hero('Book &amp; enroll', 'Let\'s get <span class="italic text-gold-300">started.</span>', 'Pick what you want to start with, then follow four simple steps.')}
  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-14 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
    <div class="lg:col-span-5 card rounded-2xl p-6 space-y-4">
      <div class="eyebrow">Step 0 • Choose</div><h2 class="serif text-2xl font-bold text-white">What would you like to start with?</h2>
      <select id="enroll-item" onchange="updateEnroll()" class="field"></select>
      <div id="enroll-summary" class="p-4 rounded-xl bg-navy-950/70 border border-gray-800 text-sm text-gray-300 space-y-1"></div>
      <div class="p-4 rounded-xl border border-dashed border-gold-400/50 space-y-2">
        <div class="eyebrow">Online checkout • coming soon</div>
        <button disabled class="w-full btn-gold opacity-40 cursor-not-allowed" title="Payment link pending">Pay online</button>
        <p class="text-xs text-gray-400">Online payment is launching soon. Book your free first call and you'll get a payment link or invoice.</p>
        <!-- TODO: replace with real Stripe Payment Link or Square checkout URL per module/package -->
      </div>
    </div>
    <div class="lg:col-span-7 card rounded-2xl p-6 space-y-5">
      <div class="eyebrow">How enrollment works</div>
      <ol class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <li class="p-5 rounded-xl bg-navy-950/70 border border-gray-800"><div class="serif text-3xl font-bold text-gold-300">01</div><div class="font-bold text-white">Free 15-minute call</div><p class="text-sm text-gray-400 mt-1">We talk through the friction and the best way to solve it.</p></li>
        <li class="p-5 rounded-xl bg-navy-950/70 border border-gray-800"><div class="serif text-3xl font-bold text-gold-300">02</div><div class="font-bold text-white">Sign the acknowledgment</div><p class="text-sm text-gray-400 mt-1">A short, plain-language <a href="#/waiver" class="text-gold-300 hover:underline">client acknowledgment</a>.</p></li>
        <li class="p-5 rounded-xl bg-navy-950/70 border border-gray-800"><div class="serif text-3xl font-bold text-gold-300">03</div><div class="font-bold text-white">Pay</div><p class="text-sm text-gray-400 mt-1">Card, Cash App Business or invoice, with a receipt for every payment.</p></li>
        <li class="p-5 rounded-xl bg-navy-950/70 border border-gray-800"><div class="serif text-3xl font-bold text-gold-300">04</div><div class="font-bold text-white">Start</div><p class="text-sm text-gray-400 mt-1">Members area access, your first session and a written recap after each one.</p></li>
      </ol>
      <div class="flex flex-wrap gap-3"><a href="tel:{PHONE_TEL}" class="btn-gold">{ic('phone','w-4 h-4')}Call {PHONE}</a><a id="enroll-mail" href="mailto:{EMAIL}" class="btn-ghost">{ic('mail','w-4 h-4')}Email to book</a></div>
    </div>
  </section>
</div>
'''

# ---------------------------------------------------------------- MEMBERS PREVIEW (shell; content rendered by JS)
mtabs = [('dash','layout-dashboard','Dashboard'),('modules','book-open','My modules'),('lesson','graduation-cap','Open lesson'),('guides','list-checks','Step-by-step guides'),('resources','library','Resource directory'),('quiz','circle-check','Quizzes'),('estimate','calculator','Estimate worksheet'),('tracker','clipboard-list','Request tracker')]
members = f'''<div id="view-members" class="view">
  <section class="border-b border-gold-400/15 bg-navy-900/70"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-6 flex flex-wrap items-center justify-between gap-3">
    <div><div class="eyebrow">Members area</div><h1 class="serif text-3xl sm:text-4xl font-bold text-white">FelRon Members <span class="italic text-gold-300">Preview</span></h1></div>
    <div class="flex items-center gap-2 px-3 py-1.5 rounded-full bg-gold-400/15 border border-gold-400/40 text-xs font-bold text-gold-300 uppercase tracking-wider">{ic('sparkles','w-3.5 h-3.5')}Preview mode • demo data</div>
  </div></section>
  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-8 relative">
    <div id="m-gate" class="absolute inset-x-0 top-6 z-20 flex justify-center px-5">
      <div class="card rounded-3xl p-7 sm:p-9 max-w-lg w-full text-center space-y-4 gold-glow border-2 border-gold-400/60 bg-navy-900">
        <span class="icon-tile mx-auto">{ic('lock')}</span>
        <h2 class="serif text-3xl font-bold text-white">This is what members see.</h2>
        <p class="text-sm text-gray-300">Step-by-step guides, the trusted resource directory, quizzes, the estimate worksheet and your request tracker live here, behind the paywall. Accounts and online payment are launching soon.</p>
        <div class="flex flex-col sm:flex-row gap-3 justify-center"><button onclick="unlockDemo()" class="btn-gold">{ic('lock-open','w-4 h-4')}Unlock demo preview</button><a href="#/pricing" class="btn-ghost">See packages</a></div>
        <p class="text-[11px] text-gray-500">Demo only: no login, no payment and no real account data.</p>
      </div>
    </div>
    <div id="m-app" class="locked-blur grid grid-cols-1 lg:grid-cols-12 gap-6 min-h-[640px]">
      <aside class="lg:col-span-3 card rounded-2xl p-3 h-max lg:sticky lg:top-24">
        <div class="flex items-center gap-3 p-3 border-b border-gray-800 mb-2"><div class="w-10 h-10 rounded-full bg-gold-400 text-navy-950 font-bold flex items-center justify-center">DM</div><div class="min-w-0"><div class="text-sm font-bold text-white">Demo Member</div><div class="text-[11px] text-gold-300 font-mono uppercase">Starter plan • preview</div></div></div>
        <nav id="m-tabs" class="flex lg:flex-col gap-1 overflow-x-auto" aria-label="Members sections">{''.join(f'<button class="mtab" data-t="{t}" onclick="mShow(&#39;{t}&#39;)">{ic(i,"w-4 h-4 shrink-0")}{n}</button>' for t,i,n in mtabs)}</nav>
      </aside>
      <div id="m-body" class="lg:col-span-9 space-y-6 min-w-0"></div>
    </div>
  </section>
</div>
'''

# ---------------------------------------------------------------- LEGAL + WAIVER (kept intact, tightened)
legal_src = R('legal_src.html')
legal_src = legal_src.replace('Licensed Work I Refer Out', 'Licensed Work, Handled the Right Way')
legal_src = legal_src.replace('''<strong class="text-white">Electrical and HVAC work</strong> requires a <a class="text-lime-300 hover:underline" href="https://www.tdlr.texas.gov/LicenseSearch/" target="_blank" rel="noopener noreferrer">TDLR ↗</a> license. I handle plug-in setup and configuration only.''',
  '''<strong class="text-white">Electrical and HVAC work</strong> that requires a <a class="text-lime-300 hover:underline" href="https://www.tdlr.texas.gov/LicenseSearch/" target="_blank" rel="noopener noreferrer">TDLR ↗</a> license is performed by my appropriately licensed trade partners. Remodeling and mechanic work through partners is performed and warranted by that partner.''')
assert 'licensed trade partners' in legal_src
waiver_src = R('waiver_src.html')
waiver_src = waiver_src.replace('<li><strong>Written recaps.</strong>', '<li><strong>Partner work and estimates.</strong> FelRon may gather and compare estimates and coordinate trusted partners (such as remodeling, mechanic, electrical or HVAC providers). Partner work is performed and warranted by that partner under its own license and terms, and I choose whether to hire any provider.</li>\n          <li><strong>Written recaps.</strong>', 1)
waiver_src = waiver_src.replace('provides educational, organizational and logistical services, including learning modules, the FelRon App and done-with-you walkthrough help.', 'provides educational, organizational, logistical and hands-on help services, including learning modules, the FelRon App, quote comparison and done-with-you walkthrough help.')
waiver_src = waiver_src.replace('provides educational, organizational and logistical services only.', 'provides educational, organizational, logistical and hands-on help services, including learning modules, the FelRon App, quote comparison and done-with-you walkthrough help.')
assert 'Partner work and estimates' in waiver_src and 'quote comparison' in waiver_src
legal = f'''<div id="view-legal" class="view">{page_hero('Legal', 'The framework <span class="italic text-gold-300">I follow.</span>', 'The plain rules behind every session, module and job.')}<section class="max-w-7xl mx-auto px-5 sm:px-8 py-14 space-y-6">{legal_src}<div class="text-sm text-gray-400 leading-relaxed card rounded-2xl p-5"><strong class="text-gray-200">Full disclaimer:</strong> FelRon IT-Legacy-Capital provides educational, organizational, logistical and hands-on help services. Nothing on this site or in any session is legal, tax, insurance or investment advice, or a recommendation to buy, sell or hold any security or asset. {NAME} is not a licensed investment adviser, broker, CPA, attorney, insurance adjuster, electrician or HVAC contractor; work requiring a Texas license is performed by appropriately licensed partners. Clients make and are responsible for their own decisions. FelRon never takes custody of client funds, crypto keys or account logins and never places trades for clients. No results are guaranteed.</div></section></div>
'''
waiver = f'''<div id="view-waiver" class="view">{page_hero('Client acknowledgment', 'Acknowledgment <span class="italic text-gold-300">&amp; waiver.</span>', 'A short, plain-language agreement signed before personal sessions. Printable.')}<section class="max-w-5xl mx-auto px-5 sm:px-8 py-14 space-y-6">{waiver_src}</section></div>
'''

# ---------------------------------------------------------------- HEADER / FOOTER
NAV = [('home','Home'),('services','Services'),('how','How It Works'),('pricing','Pricing'),('members','Members'),('about','About'),('contact','Contact')]
crest = '''<svg viewBox="0 0 100 100" class="w-11 h-11 shrink-0" aria-hidden="true"><polygon points="50,4 93,27 93,73 50,96 7,73 7,27" fill="#0b1324" stroke="#d4af37" stroke-width="4"/><polygon points="50,11 86,31 86,69 50,89 14,69 14,31" fill="none" stroke="#d4af37" stroke-width="1.2" stroke-opacity=".5"/><text x="50" y="58" text-anchor="middle" fill="#f3d98b" font-family="Cormorant Garamond, Georgia, serif" font-weight="700" font-size="30" letter-spacing="2">FR</text></svg>'''
header = f'''<body class="min-h-screen flex flex-col">
  <header class="sticky top-0 z-50 bg-navy-950/95 backdrop-blur-md border-b border-gold-400/25 no-print">
    <div class="max-w-7xl mx-auto px-5 sm:px-8 h-[72px] flex items-center justify-between gap-4">
      <a href="#/" class="flex items-center gap-3 min-w-0" aria-label="FelRon home">{crest}
        <div class="min-w-0"><div class="brand-line serif font-bold text-gold-300 uppercase">FelRon IT-Legacy-Capital</div><div class="founder-line serif font-semibold text-white">{NAME} <span class="font-mono text-[10px] uppercase tracking-widest text-gold-400 align-middle">Founder</span></div></div></a>
      <nav class="hidden xl:flex items-center gap-1" aria-label="Main">{''.join(f'<a href="#/{"" if k=="home" else k}" data-nav="{k}" class="nav-link">{v}</a>' for k,v in NAV)}</nav>
      <div class="flex items-center gap-2">
        <a href="tel:{PHONE_TEL}" class="hidden md:inline-flex btn-ghost !py-2 !px-3">{ic('phone','w-4 h-4')}{PHONE}</a>
        <a href="#/book" class="hidden sm:inline-flex btn-gold !py-2 !px-3">Book a call</a>
        <button id="menu-btn" class="xl:hidden p-2 rounded-lg border border-gold-400/40 text-gold-300" aria-label="Open menu" onclick="toggleMenu()">{ic('menu','w-5 h-5')}</button>
      </div>
    </div>
    <div id="mobile-menu" class="hidden xl:hidden border-t border-gold-400/20 bg-navy-950">
      <nav class="max-w-7xl mx-auto px-5 py-3 grid grid-cols-2 sm:grid-cols-4 gap-1" aria-label="Mobile">{''.join(f'<a href="#/{"" if k=="home" else k}" data-nav="{k}" class="nav-link">{v}</a>' for k,v in NAV)}<a href="#/book" data-nav="book" class="nav-link">Book &amp; Enroll</a></nav>
      <div class="max-w-7xl mx-auto px-5 pb-4 flex flex-wrap gap-2"><a href="tel:{PHONE_TEL}" class="btn-gold !py-2">{ic('phone','w-4 h-4')}{PHONE}</a><a href="mailto:{EMAIL}" class="btn-ghost !py-2">{ic('mail','w-4 h-4')}Email</a></div>
    </div>
  </header>
  <main class="flex-1">
'''
fcol = lambda title, links: f'<div class="space-y-3"><div class="eyebrow">{title}</div><ul class="space-y-2 text-sm">{"".join(f"<li><a href=\"{h}\" class=\"text-gray-300 hover:text-gold-300\">{t}</a></li>" for h,t in links)}</ul></div>'
footer = f'''  </main>
  <div id="toast" class="fixed bottom-5 right-5 z-50 hidden px-4 py-3 rounded-xl bg-gold-400 text-navy-950 font-bold text-sm shadow-2xl">Copied to clipboard!</div>
  <footer class="border-t border-gold-400/20 bg-navy-900 no-print">
    <div class="max-w-7xl mx-auto px-5 sm:px-8 py-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-8">
      <div class="lg:col-span-2 space-y-3"><div class="flex items-center gap-3">{crest}<div><div class="serif text-lg font-bold text-gold-300 uppercase tracking-wide">FelRon IT-Legacy-Capital</div><div class="serif text-white font-semibold">{NAME}</div></div></div>
        <p class="text-sm text-gray-400 max-w-sm">The physical side of AI. Knowledge plus the hands-on work, all in one place. San Antonio, TX.</p>
        <div class="text-sm space-y-1"><a href="tel:{PHONE_TEL}" class="block text-white hover:text-gold-300">{PHONE}</a><a href="mailto:{EMAIL}" class="block text-white hover:text-gold-300 break-all">{EMAIL}</a></div></div>
      {fcol('Explore', [('#/services','Services'),('#/how','How It Works'),('#/pricing','Pricing'),('#/about','About')])}
      {fcol('Members', [('#/members','Members Preview'),('#/pricing','Packages'),('#/book','Book &amp; Enroll'),('#/contact','Contact')])}
      {fcol('Legal', [('#/legal','Legal Framework'),('#/waiver','Client Acknowledgment'),('#/how','Privacy &amp; How I Work')])}
    </div>
    <div class="border-t border-gray-800"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-5 text-xs text-gray-500 leading-relaxed space-y-1">
      <p>FelRon IT-Legacy-Capital provides education, guidance and hands-on help on flat fees, and clients make their own decisions. Not legal, tax, insurance or investment advice. FelRon never holds client funds, keys or logins. Work requiring a Texas license is performed by appropriately licensed partners. <a href="#/legal" class="text-gold-300 hover:underline">Legal framework</a> • <a href="#/waiver" class="text-gold-300 hover:underline">Acknowledgment</a></p>
      <p>© 2026 FelRon IT-Legacy-Capital • {NAME} • San Antonio, TX</p></div></div>
  </footer>
'''

body = home + services + how + pricing + members + about + contact + book + legal + waiver
out = R('head.html') + header + body + footer + '  <script>\n' + R('app.js') + '\n  </script>\n</body>\n</html>\n'
open('/workspace/felron-site/index.html', 'w').write(out)
print('wrote', len(out), 'bytes')
