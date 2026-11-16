"""FelRon v6 page HTML."""
from content6 import *

# ---------------- PRICING
module_rows = ''.join(f'<div class="flex items-center gap-3 p-3 rounded-xl bg-navy-950/60 border border-gray-800"><span class="font-mono text-[11px] text-gold-400 w-8 shrink-0">#{c["n"]:02d}</span><span class="text-sm text-gray-200 flex-1 min-w-0">{c["title"]}</span><span class="font-mono text-gold-300 text-sm font-bold">$29</span></div>' for c in CONCEPTS)
PACKAGES = [
  ('starter', 'Starter', '$75', 'Start with the basics', ['Any 3 learning modules', 'One 1-hour walkthrough session', '3 months of the FelRon App &amp; members area', 'Written recap after the session']),
  ('builder', 'Builder', '$175', 'Learn it all', [f'All {NC} learning modules + the full Concept Vault', '3 walkthrough sessions', '6 months of the FelRon App: every tool, quiz and worksheet', 'Full Machine ROI, LEAPS &amp; Perps and Flywheel tools', 'Written recaps after every session']),
  ('full', 'Full-Service', 'from $375', 'Done with you', ['Everything in Builder', 'I make the calls and compare your quotes', 'Hands-on help and handyman coordination', 'Machine sourcing and plug-in setup', 'Ongoing sessions and priority scheduling']),
]
def pkg_card(p, i):
    pid, name, price, tag, feats = p
    hot = i == 1
    badge = '<span class="absolute -top-3 left-6 px-3 py-1 rounded-full bg-gold-400 text-navy-950 text-[11px] font-bold uppercase tracking-wider">Most popular</span>' if hot else ''
    sub = '<div class="text-xs text-gray-400 mt-1">or $75/mo</div>' if pid == 'full' else '<span class="text-sm text-gray-400"> one-time</span>'
    lis = ''.join(f'<li><span>{f}</span></li>' for f in feats)
    return (f'<div class="card rounded-2xl p-6 sm:p-7 flex flex-col gap-4 relative {"border-2 border-gold-400 gold-glow" if hot else ""}">{badge}'
            f'<div><div class="eyebrow">{tag}</div><h3 class="serif text-3xl font-bold text-white mt-1">{name}</h3></div>'
            f'<div><span class="text-4xl font-extrabold text-white">{price}</span>{sub}</div>'
            f'<ul class="chk space-y-2 text-sm text-gray-300 flex-1">{lis}</ul>'
            f'<a href="#/book?item={pid}" class="{"btn-gold" if hot else "btn-ghost"} w-full">Choose {name} {ic("arrow-right","w-4 h-4")}</a></div>')
packages = '\n'.join(pkg_card(p, i) for i, p in enumerate(PACKAGES))
def xcard(icon, title, price, desc, href, label, gold=False):
    return (f'<div class="card rounded-2xl p-6 space-y-2"><span class="icon-tile">{ic(icon)}</span><h3 class="text-lg font-bold text-white pt-1">{title}</h3>'
            f'<div class="text-2xl font-extrabold text-white">{price}</div><p class="text-sm text-gray-400">{desc}</p><a href="{href}" class="{"btn-gold" if gold else "btn-ghost"} mt-2">{label}</a></div>')
extras = '<div class="grid grid-cols-1 md:grid-cols-3 gap-5">' + ''.join([
  xcard('layout-dashboard', 'FelRon App only', '$9.50<span class="text-sm text-gray-400 font-normal">/mo</span> <span class="text-sm text-gray-400 font-normal">or $49/yr</span>', 'Members area: Concept Vault, full tools, guides, quizzes, worksheets and progress tracking. Included in every package.', '#/book?item=app', 'Get the App'),
  xcard('wrench', 'Hands-on help &amp; sessions', '$30–50<span class="text-sm text-gray-400 font-normal">/hr</span>', 'Handyman fixes, IT help, quote gathering and comparison, machine setup, errands and walkthrough sessions. Bigger jobs quoted upfront.', '#/book?item=hourly', 'Book hands-on help', True),
  xcard('paintbrush', 'Painting &amp; handyman jobs', 'Quoted per job', 'I line up the handyman I work with for painting and easy fixes, coordinate the job and keep you updated.', '#/contact', 'Request a quote')]) + '</div>'
price_note = '<p class="text-xs text-gray-500">Starting prices, subject to change. Final pricing is confirmed in writing before you pay. Flat fees only.</p>'

# ---------------- SHARED BLOCKS
def step_card(num, icon, title, text, hot=False):
    box = 'rounded-2xl p-6 relative overflow-hidden border-2 border-gold-400 bg-gold-400/10' if hot else 'card rounded-2xl p-6 relative overflow-hidden'
    return (f'<div class="{box}"><div class="serif text-6xl font-bold text-gold-400/20 absolute right-4 top-2">{num}</div><span class="icon-tile">{ic(icon)}</span>'
            f'<h3 class="text-lg font-bold text-white mt-4">{title}</h3><p class="text-sm {"text-gray-300" if hot else "text-gray-400"} mt-1.5">{text}</p></div>')
three_step = '<div class="grid grid-cols-1 md:grid-cols-3 gap-5">' + step_card('01', 'route', 'How I did it', 'I show you how I handled it myself, with real examples from real jobs, mistakes included.') + \
  step_card('02', 'book-open', 'How you can do it', 'Step-by-step guides, the Concept Vault, simulators and quizzes in the members area, so you can do it yourself next time.') + \
  step_card('03', 'hand', "Let's get it done together", 'I bring the hands-on work, the calls and the coordination. You approve every step.', True) + '</div>'
def section_head(eyebrow, title, sub='', center=False):
    c = 'text-center mx-auto' if center else ''
    s = f'<p class="text-base text-gray-400 leading-relaxed">{sub}</p>' if sub else ''
    return f'<div class="max-w-3xl {c} space-y-3"><div class="eyebrow">{eyebrow}</div><h2 class="serif h-section font-bold text-white">{title}</h2>{s}</div>'
def page_hero(eyebrow, title, sub):
    return f'<section class="hero-bg border-b border-gold-400/15"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-12 sm:py-16 space-y-4"><div class="eyebrow">{eyebrow}</div><h1 class="serif h-display font-bold text-white max-w-4xl">{title}</h1><p class="text-lg text-gray-300 max-w-2xl leading-relaxed">{sub}</p></div></section>'
def tool_hero(num, eyebrow, title, sub):
    return f'<section class="hero-bg border-b border-gold-400/15"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-10 sm:py-14 space-y-3"><div class="eyebrow">Tool {num} • {eyebrow}</div><h1 class="serif h-tool font-bold text-white max-w-4xl">{title}</h1><p class="text-base sm:text-lg text-gray-300 max-w-3xl leading-relaxed">{sub}</p></div></section>'
cta_band = f'''<section class="max-w-7xl mx-auto px-5 sm:px-8 py-14"><div class="gold-band rounded-3xl p-7 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-6 items-center shadow-2xl">
  <div class="lg:col-span-7 space-y-2"><div class="font-mono text-xs uppercase tracking-[.2em] font-bold text-navy-800">Before a problem becomes an invoice</div><h2 class="serif text-3xl sm:text-4xl font-bold text-navy-950">Make FelRon your <span class="italic">first call.</span></h2><p class="text-sm sm:text-base font-semibold text-navy-900">Bring it to someone raised to resolve it calmly, privately and in good faith: the knowledge, the quotes and the hands-on work from one contact.</p>
    <div class="flex flex-wrap gap-2 pt-2"><a href="#/dispatch" class="px-4 py-2.5 rounded-lg bg-navy-950 text-gold-300 font-bold text-xs uppercase tracking-wider hover:bg-navy-800">Open First-Call Dispatch →</a><a href="#/pricing" class="px-4 py-2.5 rounded-lg border border-navy-950/60 text-navy-950 font-bold text-xs uppercase tracking-wider hover:bg-navy-950/10">See pricing</a></div></div>
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
PRIV = [('Need-to-Know Handling', 'I only ask for what the task requires.'), ('Minimal Retention', 'Your data is kept no longer than the work needs.'),
        ('Client-Held Keys', 'You stay at the keyboard for passwords, seed phrases and keys.'), ('Encrypted Channels', 'Sensitive conversations move over encrypted communications.'),
        ('Zero-Knowledge Infrastructure', 'Privacy-preserving tools, so I never need to see more than necessary.')]
priv_items = ''.join(f'<div class="p-4 rounded-xl {"bg-gold-400/10 border border-gold-400/40" if i == 4 else "bg-navy-950/60 border border-gray-800"}"><div class="text-sm font-bold text-white">{t}</div><p class="text-xs text-gray-400 mt-1 leading-relaxed">{d}</p></div>' for i, (t, d) in enumerate(PRIV))
privacy = f'''<div class="card rounded-2xl p-6 sm:p-7 space-y-5"><div class="flex flex-wrap items-center justify-between gap-3 border-b border-gold-400/20 pb-4"><div class="flex items-center gap-3"><span class="icon-tile">{ic('lock')}</span><h2 class="serif text-2xl sm:text-3xl font-bold text-white">Private by Design. <span class="italic text-gold-300">Zero-Knowledge by Default.</span></h2></div><span class="eyebrow">Core differentiator</span></div>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">{priv_items}</div></div>'''
TOOLS = [('1', '', 'Executive Dossier', 'layout-dashboard', ''),
         ('2', 'roi', 'Machine ROI &amp; Sourcing', 'cpu', 'Compare vendor quotes vs. sourced price, power cost and break-even for ASIC and DePIN machines.'),
         ('3', 'codex', f'Concept Codex &amp; Vault ({NC})', 'library', 'Every module: the free public view vs. what members unlock, side by side.'),
         ('4', 'lab', 'LEAPS &amp; Perps Lab', 'zap', 'Options payoff curves, breakeven and theta zones, plus a perps margin calculator.'),
         ('5', 'flywheel', 'Capital Flywheel', 'refresh-cw', 'The 4-stage loop I run personally, shared as an educational example.'),
         ('6', 'dispatch', 'First-Call Dispatch', 'send', 'Build a confidential first-call brief and send it straight to me.')]
tools_grid = ''.join(f'<a href="#/{r}" class="card card-hover rounded-2xl p-5 flex gap-4 items-start"><span class="icon-tile">{ic(i)}</span><div class="min-w-0"><div class="font-mono text-[11px] text-gold-400 font-bold">TOOL {n}</div><div class="font-bold text-white">{t}</div><p class="text-sm text-gray-400 mt-1">{d}</p></div></a>' for n, r, t, i, d in TOOLS[1:])
SPECIALTIES = [('01 • Machine sourcing', 'Crypto Hardware &amp; ASIC Procurement', 'Vetting secondary-market and distributor ASICs (Z9, Z9 Mini, Z11, Z15, S-Series), PSUs, PDUs and GPU/DePIN nodes, filtering out dead hashboards and overpriced listings.', 'roi'),
               ('02 • Estimation evaluation', 'Quote, Bid &amp; Cost Comparison', 'Line-by-line evaluation of hardware quotes, repair estimates and contractor bids. I call around and check what fair pricing looks like before you sign.', 'contact'),
               ('03 • Setup &amp; ROI outlook', 'Plug-In Deployment &amp; Payback Math', 'Plug-in ASIC/DePIN configuration, pool routing, airflow, board maintenance and realistic kWh-vs-yield projections across bull, base and bear cases.', 'roi'),
               ('04 • Capital flywheel', 'Self-Reinforcing Wealth Architecture', 'The 4-stage loop I run personally: cashflow &amp; quote savings → 401(k) anchor → bi-weekly LEAPS → compute &amp; bullion. Shared as education.', 'flywheel')]
specialties = ''.join(f'<a href="#/{r}" class="card card-hover rounded-2xl p-5 block"><div class="eyebrow !text-[10px]">{e}</div><div class="font-bold text-white mt-2">{t}</div><p class="text-sm text-gray-400 mt-1.5 leading-relaxed">{d}</p></a>' for e, t, d, r in SPECIALTIES)
STORY_P = [
  'FelRon is named for my parents, <strong class="text-white">Felicia and Ronald</strong>, and founded in their honor.',
  'My father, Ronald, served 29 years as a U.S. Army combat medic and paratrooper. He fought in the Gulf War with the 2nd Armored Cavalry Regiment at the Battle of 73 Easting, served separately with the 82nd Airborne Division at Fort Bragg, and was stationed in Italy and Germany. He deployed to Iraq in 2004–05 and again for the 2007–08 surge, made more than 80 jumps, earned the Bronze Star, and retired as a Sergeant First Class from the Warrior Transition Unit at Fort Sam Houston. My mother, Felicia, earned numerous medals for her Family Readiness Group service, supporting military families through every move and deployment, while building a career in fine retail and diamond jewelry.',
  'From them I learned composure under pressure and genuine caretaking. In our house, when family or friends hit a technical failure, a financial tangle or a logistical bottleneck, you stepped up and solved it. FelRon brings that same calm, precision and good faith to every client.']
legacy_cards = f'''<div class="card rounded-2xl p-5 border-l-4 border-l-gold-400"><div class="text-[10px] font-mono uppercase tracking-widest text-gold-400">Ron • Ronald</div><div class="serif text-2xl font-bold text-gold-300 mt-0.5">29 Years • Bronze Star</div><p class="text-sm text-gray-400 mt-1">U.S. Army combat medic &amp; paratrooper • Gulf War, 2nd Armored Cavalry (73 Easting) • 82nd Airborne • Iraq 2004–05 &amp; 2007–08 • 80+ jumps • Retired SFC</p></div>
  <div class="card rounded-2xl p-5 border-l-4 border-l-gold-400"><div class="text-[10px] font-mono uppercase tracking-widest text-gold-400">Fel • Felicia</div><div class="serif text-2xl font-bold text-gold-300 mt-0.5">FRG Honors</div><p class="text-sm text-gray-400 mt-1">Numerous Family Readiness Group medals • Career in fine retail &amp; diamond jewelry</p></div>'''

# ---------------- HOME
story_ps = ''.join(f'<p class="text-gray-300 leading-relaxed">{p}</p>' for p in STORY_P)
sample_rows = ('<tr class="border-t border-gray-800 bg-gold-400/10"><td class="py-2.5 font-semibold text-white">Provider A ★</td><td class="font-semibold text-white">$385</td><td>12 mo</td><td class="text-gold-300">Yes</td></tr>'
               '<tr class="border-t border-gray-800"><td class="py-2.5">Provider B</td><td class="text-rose-300">$560 <span class="text-[10px]">+37%</span></td><td>6 mo</td><td class="text-gold-300">Yes</td></tr>'
               '<tr class="border-t border-gray-800"><td class="py-2.5">Provider C</td><td>$410</td><td>12 mo</td><td class="text-gold-300">Yes</td></tr>')
def mini(icon, t, d):
    return f'<div class="card rounded-xl p-4"><div class="text-gold-300">{ic(icon)}</div><div class="font-bold text-white mt-2 text-sm">{t}</div><p class="text-xs text-gray-400 mt-1">{d}</p></div>'
home = f'''<div id="view-home" class="view">
  <section class="hero-bg grid-lines border-b border-gold-400/15">
    <div class="max-w-7xl mx-auto px-5 sm:px-8 py-12 sm:py-16 grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
      <div class="lg:col-span-7 space-y-6 pt-2">
        <div class="eyebrow">The trusted first call • What's the friction?</div>
        <h1 class="serif h-display font-bold text-white">Before the Lawyer.<br />Before the CPA.<br /><span class="italic text-gold-300">Call FelRon First.</span></h1>
        <p class="text-lg text-gray-300 leading-relaxed max-w-2xl">When hardware needs sourcing, a quote looks inflated, finances tangle or daily logistics stall, <strong class="text-white">FelRon is the single, discreet first call</strong>. I bring the know-how, the hands-on work and the coordination, so you only pay a CPA, attorney or licensed contractor for the final step that truly needs them.</p>
        <p class="text-sm text-gray-400">Specializing in <strong class="text-gold-300">Crypto Hardware &amp; Machine Sourcing</strong>, <strong class="text-gold-300">Quote &amp; Estimate Comparison</strong>, <strong class="text-gold-300">Plug-In Machine Setup &amp; ROI Outlook Modeling</strong> and the <strong class="text-gold-300">Capital Flywheel</strong>.</p>
        <div class="flex flex-wrap gap-3"><a href="#intake" onclick="document.getElementById('home-intake').scrollIntoView({{behavior:'smooth'}});return false" class="btn-gold">Tell me the friction {ic('arrow-right','w-4 h-4')}</a><a href="#/roi" class="btn-ghost">{ic('cpu','w-4 h-4')}Machine ROI Lab</a><a href="#/codex" class="btn-ghost">{ic('library','w-4 h-4')}Inspect all {NC} modules</a></div>
        <div class="pt-5 border-t border-gold-400/20 max-w-lg"><div class="text-[11px] font-mono uppercase tracking-widest text-gold-400">Founder</div><div class="serif text-2xl sm:text-3xl font-bold text-white">{NAME}</div><div class="serif italic text-lg text-gold-300">Private by design. Discreet by upbringing.</div></div>
      </div>
      <div id="home-intake" class="lg:col-span-5 scroll-mt-32">{intake('hi')}</div>
    </div>
  </section>
  <section class="border-b border-gold-400/15 bg-navy-900/60"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-14 sm:py-16 grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
    <div class="lg:col-span-7 space-y-4"><div class="eyebrow">The FelRon story</div>
      <h2 class="serif h-section font-bold text-white">Fel + Ron. <span class="italic text-gold-300">Felicia and Ronald.</span></h2>
      {story_ps}<div class="serif italic text-lg text-gold-300">— {NAME}, Founder</div></div>
    <div class="lg:col-span-5 space-y-4">{legacy_cards}<a href="#/about" class="btn-ghost">Read the full story {ic('arrow-right','w-4 h-4')}</a></div>
  </div></section>
  <section class="border-b border-gold-400/15"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-14 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
    <div class="lg:col-span-5 space-y-3"><div class="eyebrow">Why FelRon</div><h2 class="serif h-section font-bold text-white">The physical side of <span class="italic text-gold-300">AI.</span></h2></div>
    <div class="lg:col-span-7 space-y-4 text-gray-300 leading-relaxed">
      <p class="text-lg">AI can tell you what's probably wrong. It can't paint the wall, call three contractors, read the fine print on the quote, plug in the miner, or sit with your mom at her appointment.</p>
      <p>That's where I come in. I'm the hands-on person for the friction points where online answers stop: <strong class="text-white">the knowledge, the physical work and the coordination in one place</strong>, with one contact for the whole package.</p>
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2">{mini('bot', 'The knowledge', 'Clear answers and a plan, explained plainly.')}{mini('wrench', 'The hands', 'Fixes, setups, errands and machine installs, in person.')}{mini('phone-call', 'The coordination', 'Quotes compared, the handyman lined up, the job followed through.')}</div>
    </div></div></section>
  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-16 space-y-8">
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-4">{section_head('Signature specialties', 'Hardware sourcing, estimate audits &amp; <span class="italic text-gold-300">the FelRon Capital Flywheel.</span>')}<a href="#/roi" class="btn-ghost shrink-0">Test the ROI calculator {ic('arrow-right','w-4 h-4')}</a></div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">{specialties}</div>
  </section>
  <section class="bg-navy-900/60 border-y border-gold-400/15"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-16 space-y-10">
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-4">{section_head('What I help with', 'Day-to-day fixes to <span class="italic text-gold-300">big-picture plans.</span>', 'If it is causing friction and it can be solved, bring it to me.')}<a href="#/services" class="btn-ghost shrink-0">All services {ic('arrow-right','w-4 h-4')}</a></div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">{home_services}</div>
  </div></section>
  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-16 space-y-10">
    {section_head('How it works', 'Show you. Teach you. <span class="italic text-gold-300">Get it done together.</span>', 'Every job follows the same three steps, so you walk away with the fix and the know-how.', True)}
    {three_step}
  </section>
  <section class="bg-navy-900/60 border-y border-gold-400/15"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-16 space-y-8">
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-4">{section_head('The FelRon toolkit', 'Six tools. <span class="italic text-gold-300">Try them free.</span>', 'Public previews here. Members get the full versions, the Concept Vault and saved progress.')}<a href="#/members" class="btn-ghost shrink-0">{ic('lock-open','w-4 h-4')}Members preview</a></div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">{tools_grid}<a href="#/members" class="rounded-2xl p-5 flex gap-4 items-start border-2 border-dashed border-gold-400/40 hover:border-gold-400"><span class="icon-tile">{ic('lock')}</span><div><div class="font-mono text-[11px] text-gold-400 font-bold">MEMBERS</div><div class="font-bold text-white">The full vault</div><p class="text-sm text-gray-400 mt-1">Guides, checklists, templates and every tool unlocked.</p></div></a></div>
  </div></section>
  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-16 grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
    <div class="space-y-4">{section_head('Quote &amp; estimate comparison', 'I make the calls. <span class="italic text-gold-300">You keep the savings.</span>', 'Getting three quotes takes hours of phone tag. I do the calling, line the estimates up side by side and tell you what a fair price looks like, based on years of hands-on pricing and inventory experience.')}
      <ul class="chk space-y-2 text-sm text-gray-300"><li><span>Same scope, apples to apples</span></li><li><span>Price, warranty, timeline and license checked</span></li><li><span>Outliers and padded line items flagged</span></li><li><span>You pick the provider. I help it get done.</span></li></ul>
      <a href="#/contact" class="btn-gold">Get my quotes compared {ic('arrow-right','w-4 h-4')}</a></div>
    <div class="card rounded-2xl p-5 sm:p-6 space-y-3"><div class="flex items-center justify-between"><div class="text-sm font-bold text-white">Sample: AC repair quotes</div><span class="text-[10px] font-mono uppercase px-2 py-0.5 rounded bg-gold-400/15 text-gold-300 border border-gold-400/30">Example</span></div>
      <div class="overflow-x-auto"><table class="w-full text-sm"><thead><tr class="text-left text-[11px] font-mono uppercase tracking-wider text-gray-500"><th class="py-2">Provider</th><th>Price</th><th>Warranty</th><th>Licensed</th></tr></thead><tbody class="text-gray-300">{sample_rows}</tbody></table></div>
      <p class="text-xs text-gray-500">Illustration only. Members get the full Estimate Worksheet.</p></div>
  </section>
  <section class="max-w-7xl mx-auto px-5 sm:px-8 pb-16">{privacy}</section>
  <section class="bg-navy-900/60 border-y border-gold-400/15"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-16 space-y-10">
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-4">{section_head('Pricing', 'Simple, flat <span class="italic text-gold-300">pricing.</span>', 'Learning modules from $29. Packages include the FelRon App and members area.')}<a href="#/pricing" class="btn-ghost shrink-0">Full pricing {ic('arrow-right','w-4 h-4')}</a></div>
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 pt-3">{packages}</div>{price_note}
  </div></section>
  {story_band}
  {cta_band}
</div>
'''

# ---------------- OTHER PAGES
services = f'''<div id="view-services" class="view">
  {page_hero('Services', 'Everything I help <span class="italic text-gold-300">with.</span>', 'Hands-on fixes, calls and coordination, machine sourcing, IT, paperwork and education, all from one contact.')}
  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-14 space-y-10">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">{all_services}</div>
    <div class="card rounded-2xl p-6 sm:p-8 grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
      <div class="lg:col-span-8 space-y-2"><div class="eyebrow">Don't see it listed?</div><h2 class="serif text-3xl font-bold text-white">Tell me the friction anyway.</h2><p class="text-gray-400">Most problems are solvable with the right knowledge, the right hands or the right call. I'll tell you on the free first call how I'd approach it.</p></div>
      <div class="lg:col-span-4 flex flex-wrap gap-3 lg:justify-end"><a href="#/contact" class="btn-gold">Describe my problem</a><a href="#/pricing" class="btn-ghost">See pricing</a></div>
    </div>
  </section>
  {cta_band}
</div>
'''
PROCESS = [('Tell me the friction', 'Use the intake form, the First-Call Dispatch, text or call.'), ('Free 15-min call', 'We talk it through and I lay out how I would approach it.'),
           ('Plan &amp; quotes', 'A clear plan, a flat price, and quotes gathered and compared when needed.'), ('Get it done', 'Hands-on work, handyman coordination and walkthroughs, with you approving each step.'),
           ('Written recap', 'What was done, what it cost and how to handle it next time.')]
proc = ''.join(f'<li class="card rounded-2xl p-5"><div class="serif text-3xl font-bold text-gold-300">{n:02d}</div><div class="font-bold text-white mt-1">{t}</div><p class="text-sm text-gray-400 mt-1">{d}</p></li>' for n, (t, d) in enumerate(PROCESS, 1))
how = f'''<div id="view-how" class="view">
  {page_hero('How it works', 'From friction to <span class="italic text-gold-300">finished.</span>', 'One simple process for every job, whether it is a paint touch-up, a quote comparison, a miner install or a new LLC.')}
  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-14 space-y-14">{three_step}
    <div class="space-y-6">{section_head('The process', 'What happens after you <span class="italic text-gold-300">reach out.</span>')}<ol class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">{proc}</ol></div>
    {privacy}</section>
  {cta_band}
</div>
'''
pricing = f'''<div id="view-pricing" class="view">
  {page_hero('Pricing', 'Flat fees. <span class="italic text-gold-300">No surprises.</span>', 'Pick a package, a single module or hands-on help by the hour. Every package includes the FelRon App and members area.')}
  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-14 space-y-14">
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 pt-3">{packages}</div>
    {extras}
    <div class="space-y-5"><div class="flex flex-col md:flex-row md:items-end justify-between gap-4">{section_head('Module catalog', f'{NC} modules, <span class="italic text-gold-300">$29 each.</span>', 'Each module: a lesson, a 1-on-1 walkthrough, and its vault deliverables (checklists, calculators, templates) in the members area.')}<a href="#/codex" class="btn-ghost shrink-0">Compare free vs. vault {ic('arrow-right','w-4 h-4')}</a></div>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">{module_rows}</div></div>
    {price_note}
  </section>
  {cta_band}
</div>
'''
TRAINING = ['Logistics &amp; Supply Chain Management (Northeast Lakeview College)', 'Electrical Concepts &amp; HVAC Systems coursework (Southern Careers Institute)',
            'Years of retail and assistant-GM management: pricing, inventory, vendors and teams', 'Data tools built in Python and Go', 'AP Macroeconomics &amp; AP European History']
about = f'''<div id="view-about" class="view">
  <section class="hero-bg border-b border-gold-400/15"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-14 sm:py-20 space-y-3">
    <div class="eyebrow">About • Founder, <span class="seg">FelRon IT-Legacy-Capital</span></div>
    <h1 class="serif h-display font-bold text-gold-300">{NAME}</h1><p class="text-lg text-gray-300">San Antonio, Texas</p></div></section>
  <section class="max-w-7xl mx-auto px-5 sm:px-8 py-14 grid grid-cols-1 lg:grid-cols-12 gap-10">
    <div class="lg:col-span-8 space-y-5 text-gray-300 leading-relaxed">
      <h2 class="serif h-section font-bold text-white">Fel + Ron. <span class="italic text-gold-300">Felicia and Ronald.</span></h2>
      {''.join(f'<p>{p}</p>' for p in STORY_P)}
      <p>Today I'm the hands-on person for the friction points where online answers stop. I source and set up crypto hardware, fix what I can fix myself, line up the handyman I work with for painting and easy fixes, make the calls and compare the quotes, and teach the money and market concepts I use personally. You get the knowledge, the physical work and the coordination in one place.</p>
    </div>
    <div class="lg:col-span-4 space-y-4">{legacy_cards}
      <div class="card rounded-2xl p-5 space-y-2"><div class="eyebrow">Training &amp; experience</div><ul class="chk space-y-1.5 text-sm text-gray-300">{''.join(f'<li><span>{t}</span></li>' for t in TRAINING)}</ul></div></div>
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
        <div><div class="eyebrow">Direct line</div><a href="tel:{PHONE_TEL}" class="serif text-3xl font-bold text-white hover:text-gold-300">{PHONE}</a></div>
        <div><div class="eyebrow">Secure email</div><a href="mailto:{EMAIL}" class="text-lg font-semibold text-white hover:text-gold-300 break-all">{EMAIL}</a></div>
        <div><div class="eyebrow">Service area</div><div class="text-white font-semibold">San Antonio, TX and surrounding area</div><div class="text-sm text-gray-400">On-site visits, plus remote sessions anywhere.</div></div>
        <div><div class="eyebrow">Founder</div><div class="serif text-2xl font-bold text-gold-300">{NAME}</div></div>
      </div>
      <div class="card rounded-2xl p-6 space-y-2"><div class="font-bold text-white">Need a detailed brief?</div><p class="text-sm text-gray-400">Pick exact modules and generate a confidential scope sheet.</p><a href="#/dispatch" class="btn-gold mt-1">First-Call Dispatch {ic('arrow-right','w-4 h-4')}</a></div>
    </div>
  </section>
</div>
'''
ENR = [('01', 'Free 15-minute call', 'We talk through the friction and the best way to solve it.'), ('02', 'Sign the acknowledgment', 'A short, plain-language <a href="#/waiver" class="text-gold-300 hover:underline">client acknowledgment</a>.'),
       ('03', 'Pay', 'Card, Cash App Business or invoice, with a receipt for every payment.'), ('04', 'Start', 'Members area access, your first session and a written recap after each one.')]
enr = ''.join(f'<li class="p-5 rounded-xl bg-navy-950/70 border border-gray-800"><div class="serif text-3xl font-bold text-gold-300">{n}</div><div class="font-bold text-white">{t}</div><p class="text-sm text-gray-400 mt-1">{d}</p></li>' for n, t, d in ENR)
book = f'''<div id="view-book" class="view">
  {page_hero('Book &amp; enroll', "Let's get <span class=\"italic text-gold-300\">started.</span>", 'Pick what you want to start with, then follow four simple steps.')}
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
    <div class="lg:col-span-7 card rounded-2xl p-6 space-y-5"><div class="eyebrow">How enrollment works</div><ol class="grid grid-cols-1 sm:grid-cols-2 gap-4">{enr}</ol>
      <div class="flex flex-wrap gap-3"><a href="tel:{PHONE_TEL}" class="btn-gold">{ic('phone','w-4 h-4')}Call {PHONE}</a><a id="enroll-mail" href="mailto:{EMAIL}" class="btn-ghost">{ic('mail','w-4 h-4')}Email to book</a></div></div>
  </section>
</div>
'''
# ---------------- TOOL PAGES (content rendered by JS into hosts)
def tool_page(vid, hero, cta=True):
    return f'<div id="view-{vid}" class="view">{hero}<section class="max-w-7xl mx-auto px-5 sm:px-8 py-10"><div id="host-{vid}"></div></section>{cta_band if cta else ""}</div>\n'
roi = tool_page('roi', tool_hero(2, 'Lead specialty • hardware sourcing, quote evaluation &amp; ROI outlook', 'Machine Sourcing, Estimation Audit &amp; <span class="italic text-gold-300">ROI Simulator</span>', 'Evaluate ASIC and DePIN machine quotes, compare vendor markup against a sourced price, check circuit load, and project 12-month net ROI. Estimates only: prices, difficulty and yields change daily.'))
codex = tool_page('codex', tool_hero(3, 'Public overview + behind-the-paywall member preview', f'Interactive {NC}-Concept Codex &amp; <span class="italic text-gold-300">Client Vault</span>', 'See what visitors read for free versus the step-by-step checklists, calculators and templates unlocked in your paid modules. Flip the view to compare.'))
lab = tool_page('lab', tool_hero(4, 'Options, equities &amp; macro simulator', 'Options/LEAPS Payoff &amp; <span class="italic text-gold-300">Perpetuals Margin Lab</span>', 'Clarity before capital moves: stress-test LEAPS convexity, theta cliffs, isolated margin, mark price and funding rates. Hypothetical, education-only illustrations.'))
flywheel = tool_page('flywheel', tool_hero(5, 'Capital flywheel architecture • barbell + compute loop', 'The FelRon Capital Flywheel &amp; <span class="italic text-gold-300">401(k) Barbell</span>', 'What I do personally, shared as an educational example: Stage 1 (cashflow &amp; quote savings) feeds Stage 2 (a 401(k) defensive anchor) and Stage 3 (bi-weekly LEAPS), with gains above a +20% gate recycled into Stage 4 (compute hardware &amp; physical bullion). Not a recommendation.'))
dispatch = tool_page('dispatch', tool_hero(6, 'Zero-knowledge first-call dispatch • triage configurator', 'Build a Confidential <span class="italic text-gold-300">Client Triage Brief</span>', 'Select the exact modules you need, from crypto hardware sourcing to quote comparison and pre-CPA organization, then copy the scope sheet or send it straight to me.'), False)

# ---------------- MEMBERS PREVIEW
MTABS = [('dash','layout-dashboard','Dashboard'),('modules','book-open','My modules'),('lesson','graduation-cap','Open lesson'),('vault','library','Concept Vault'),('roi','cpu','Machine ROI'),('lab','zap','LEAPS &amp; Perps Lab'),('flywheel','refresh-cw','Capital Flywheel'),('guides','list-checks','Step-by-step guides'),('resources','book-marked','Resource directory'),('quiz','circle-check','Quizzes'),('estimate','calculator','Estimate worksheet'),('tracker','clipboard-list','Request tracker')]
mtab_html = ''.join(f'<button class="mtab" data-t="{t}" onclick="mShow(&#39;{t}&#39;)">{ic(i, "w-4 h-4 shrink-0")}{n}</button>' for t, i, n in MTABS)
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
        <p class="text-sm text-gray-300">The Concept Vault, step-by-step guides, the full Machine ROI, LEAPS &amp; Perps and Flywheel tools, quizzes, the estimate worksheet and your request tracker live here, behind the paywall. Accounts and online payment are launching soon.</p>
        <div class="flex flex-col sm:flex-row gap-3 justify-center"><button onclick="unlockDemo()" class="btn-gold">{ic('lock-open','w-4 h-4')}Unlock demo preview</button><a href="#/pricing" class="btn-ghost">See packages</a></div>
        <p class="text-[11px] text-gray-500">Demo only: no login, no payment and no real account data.</p>
      </div>
    </div>
    <div id="m-app" class="locked-blur grid grid-cols-1 lg:grid-cols-12 gap-6 min-h-[640px]">
      <aside class="lg:col-span-3 card rounded-2xl p-3 h-max lg:sticky lg:top-36 min-w-0">
        <div class="flex items-center gap-3 p-3 border-b border-gray-800 mb-2"><div class="w-10 h-10 rounded-full bg-gold-400 text-navy-950 font-bold flex items-center justify-center shrink-0">DM</div><div class="min-w-0"><div class="text-sm font-bold text-white">Demo Member</div><div class="text-[11px] text-gold-300 font-mono uppercase">Starter plan • preview</div></div></div>
        <nav id="m-tabs" class="flex lg:flex-col gap-1 overflow-x-auto" aria-label="Members sections">{mtab_html}</nav>
      </aside>
      <div id="m-body" class="lg:col-span-9 space-y-6 min-w-0"></div>
    </div>
  </section>
</div>
'''
# ---------------- LEGAL + WAIVER
legal_src = R('legal_src.html').replace('Licensed Work I Refer Out', 'Licensed Work, Handled the Right Way')
old_el = '<strong class="text-white">Electrical and HVAC work</strong> requires a <a class="text-lime-300 hover:underline" href="https://www.tdlr.texas.gov/LicenseSearch/" target="_blank" rel="noopener noreferrer">TDLR ↗</a> license. I handle plug-in setup and configuration only.'
assert old_el in legal_src
legal_src = legal_src.replace(old_el, '<strong class="text-white">Electrical, AC and plumbing repairs</strong> are performed by licensed professionals you can verify on <a class="text-lime-300 hover:underline" href="https://www.tdlr.texas.gov/LicenseSearch/" target="_blank" rel="noopener noreferrer">TDLR ↗</a>. I gather and compare their quotes so you can choose, and I handle plug-in machine setup and configuration.')
priv_li = '<li class="flex gap-3"><span class="text-lime-400 font-bold">☑</span><span><strong class="text-white">Privacy and no custody.</strong>'
assert priv_li in legal_src
legal_src = legal_src.replace(priv_li, '<li class="flex gap-3"><span class="text-lime-400 font-bold">☑</span><span><strong class="text-white">Independent handyman &amp; quotes.</strong> I line up and coordinate the independent handyman I work with for painting and easy fixes, and I gather and compare quotes from independent providers. You choose whether to hire anyone.</span></li>\n            ' + priv_li)
waiver_src = R('waiver_src.html')
for a, b in [
  ('provides educational, organizational and logistical services only.', 'provides educational, organizational, logistical and hands-on help services, including learning modules, the FelRon App and tools, crypto hardware sourcing and plug-in setup, quote comparison, handyman coordination and done-with-you walkthrough help.'),
  ('attorney, insurance adjuster or electrician, and', 'attorney, insurance adjuster, electrician, plumber or air-conditioning contractor, and'),
  ('<li><strong>Modules, packages and the App.</strong> Paid modules, walkthrough sessions, packages and FelRon App access are educational services.', '<li><strong>Modules, packages, tools and the App.</strong> Paid modules, walkthrough sessions, packages, tools and FelRon App access are educational services.'),
  ('<li><strong>Written recaps.</strong>', '<li><strong>Handyman coordination and estimates.</strong> FelRon may gather and compare estimates and quotes from independent providers, and may line up and coordinate the independent handyman FelRon works with for painting and minor fixes. Independent providers perform and stand behind their own work under their own terms, and I choose whether to hire any provider.</li>\n          <li><strong>Hardware sourcing.</strong> Machine prices, electricity costs and yields change constantly. ROI outlooks are estimates, not guarantees, and I decide whether to buy any equipment.</li>\n          <li><strong>Written recaps.</strong>'),
  ('Quizzes and simulators are practice tools, not predictions or recommendations.', 'Quizzes, simulators and calculators are hypothetical practice tools, not predictions or recommendations.')]:
    assert a in waiver_src, a
    waiver_src = waiver_src.replace(a, b, 1)
legal = f'''<div id="view-legal" class="view">{page_hero('Legal', 'The framework <span class="italic text-gold-300">I follow.</span>', 'The plain rules behind every session, module, tool and job.')}<section class="max-w-7xl mx-auto px-5 sm:px-8 py-14 space-y-6">{legal_src}<div class="text-sm text-gray-400 leading-relaxed card rounded-2xl p-5"><strong class="text-gray-200">Full disclaimer:</strong> FelRon IT-Legacy-Capital provides educational, organizational, logistical and hands-on help services. Nothing on this site, in any tool or in any session is legal, tax, insurance or investment advice, or a recommendation to buy, sell or hold any security, asset or equipment. Simulators and calculators are hypothetical illustrations. The Capital Flywheel describes what the founder does personally and is not a recommendation. {NAME} is not a licensed investment adviser, broker, CPA, attorney, insurance adjuster, electrician, plumber or air-conditioning contractor. Clients make and are responsible for their own decisions. FelRon never takes custody of client funds, crypto keys or account logins and never places trades for clients. No results are guaranteed.</div></section></div>
'''
waiver = f'''<div id="view-waiver" class="view">{page_hero('Client acknowledgment', 'Acknowledgment <span class="italic text-gold-300">&amp; waiver.</span>', 'A short, plain-language agreement signed before personal sessions. Printable.')}<section class="max-w-5xl mx-auto px-5 sm:px-8 py-14 space-y-6">{waiver_src}</section></div>
'''

# ---------------- HEADER / FOOTER
NAV = [('home','Home'),('services','Services'),('how','How It Works'),('pricing','Pricing'),('members','Members'),('about','About'),('contact','Contact')]
navlinks = ''.join(f'<a href="#/{"" if k == "home" else k}" data-nav="{k}" class="nav-link">{v}</a>' for k, v in NAV)
crest = '<svg viewBox="0 0 100 100" class="w-11 h-11 shrink-0" aria-hidden="true"><polygon points="50,4 93,27 93,73 50,96 7,73 7,27" fill="#0b1324" stroke="#d4af37" stroke-width="4"/><polygon points="50,11 86,31 86,69 50,89 14,69 14,31" fill="none" stroke="#d4af37" stroke-width="1.2" stroke-opacity=".5"/><text x="50" y="58" text-anchor="middle" fill="#f3d98b" font-family="Cormorant Garamond, Georgia, serif" font-weight="700" font-size="30" letter-spacing="2">FR</text></svg>'
toolstrip = ''.join(f'<a href="#/{r}" data-nav="{r or "home"}" class="tool-tab">{n}. {t}</a>' for n, r, t, _, _ in TOOLS)
header = f'''<body class="min-h-screen flex flex-col">
  <header class="sticky top-0 z-50 bg-navy-950/95 backdrop-blur-md border-b border-gold-400/25 no-print">
    <div class="max-w-7xl mx-auto px-5 sm:px-8 py-2.5 flex items-center justify-between gap-4">
      <a href="#/" class="flex items-center gap-3 min-w-0" aria-label="FelRon home">{crest}
        <div class="min-w-0"><div class="brand-line serif font-bold text-gold-300 uppercase">FelRon IT-Legacy-Capital</div>
          <div class="founder-line serif font-semibold text-white">{NAME} <span class="font-mono text-[10px] uppercase tracking-widest text-gold-400 align-middle">Founder</span></div>
          <div class="hidden md:block font-mono text-[10px] uppercase tracking-wider text-gray-400">San Antonio, TX • {PHONE}</div></div></a>
      <nav class="hidden xl:flex items-center gap-0.5" aria-label="Main">{navlinks}</nav>
      <div class="flex items-center gap-2">
        <a href="#/book" class="hidden sm:inline-flex btn-gold !py-2 !px-3">Book a call</a>
        <button id="menu-btn" class="xl:hidden p-2 rounded-lg border border-gold-400/40 text-gold-300" aria-label="Open menu" onclick="toggleMenu()">{ic('menu','w-5 h-5')}</button>
      </div>
    </div>
    <div class="border-t border-gold-400/15 bg-navy-900/80"><nav class="max-w-7xl mx-auto px-5 sm:px-8 py-1.5 flex gap-1.5 overflow-x-auto" aria-label="Tools">{toolstrip}</nav></div>
    <div id="mobile-menu" class="hidden xl:hidden border-t border-gold-400/20 bg-navy-950">
      <nav class="max-w-7xl mx-auto px-5 py-3 grid grid-cols-2 sm:grid-cols-4 gap-1" aria-label="Mobile">{navlinks}<a href="#/book" data-nav="book" class="nav-link">Book &amp; Enroll</a></nav>
      <div class="max-w-7xl mx-auto px-5 pb-4 flex flex-wrap gap-2"><a href="tel:{PHONE_TEL}" class="btn-gold !py-2">{ic('phone','w-4 h-4')}{PHONE}</a><a href="mailto:{EMAIL}" class="btn-ghost !py-2">{ic('mail','w-4 h-4')}Email</a></div>
    </div>
  </header>
  <main class="flex-1">
'''
def fcol(title, links):
    items = ''.join(f'<li><a href="{h}" class="text-gray-300 hover:text-gold-300">{t}</a></li>' for h, t in links)
    return f'<div class="space-y-3"><div class="eyebrow">{title}</div><ul class="space-y-2 text-sm">{items}</ul></div>'
footer = f'''  </main>
  <div id="toast" class="fixed bottom-5 right-5 z-50 hidden px-4 py-3 rounded-xl bg-gold-400 text-navy-950 font-bold text-sm shadow-2xl">Copied to clipboard!</div>
  <footer class="border-t border-gold-400/20 bg-navy-900 no-print">
    <div class="max-w-7xl mx-auto px-5 sm:px-8 py-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-8">
      <div class="lg:col-span-2 space-y-3"><div class="flex items-center gap-3">{crest}<div><div class="serif text-lg font-bold text-gold-300 uppercase tracking-wide">FelRon IT-Legacy-Capital</div><div class="serif text-white font-semibold">{NAME}</div></div></div>
        <p class="text-sm text-gray-400 max-w-sm">Fel + Ron: named for Felicia and Ronald. The physical side of AI: knowledge, hands-on work and coordination in one place. San Antonio, TX.</p>
        <div class="text-sm space-y-1"><a href="tel:{PHONE_TEL}" class="block text-white hover:text-gold-300">{PHONE}</a><a href="mailto:{EMAIL}" class="block text-white hover:text-gold-300 break-all">{EMAIL}</a></div></div>
      {fcol('Explore', [('#/services','Services'),('#/how','How It Works'),('#/pricing','Pricing'),('#/about','About')])}
      {fcol('Tools', [('#/roi','Machine ROI &amp; Sourcing'),('#/codex','Concept Codex &amp; Vault'),('#/lab','LEAPS &amp; Perps Lab'),('#/flywheel','Capital Flywheel'),('#/dispatch','First-Call Dispatch')])}
      {fcol('Members', [('#/members','Members Preview'),('#/pricing','Packages'),('#/book','Book &amp; Enroll'),('#/contact','Contact')])}
      {fcol('Legal', [('#/legal','Legal Framework'),('#/waiver','Client Acknowledgment'),('#/how','Privacy &amp; How I Work')])}
    </div>
    <div class="border-t border-gray-800"><div class="max-w-7xl mx-auto px-5 sm:px-8 py-5 text-xs text-gray-500 leading-relaxed space-y-1">
      <p>FelRon IT-Legacy-Capital provides education, guidance and hands-on help on flat fees, and clients make their own decisions. Not legal, tax, insurance or investment advice. Tools are hypothetical illustrations. FelRon never holds client funds, keys or logins. <a href="#/legal" class="text-gold-300 hover:underline">Legal framework</a> • <a href="#/waiver" class="text-gold-300 hover:underline">Acknowledgment</a></p>
      <p>© 2026 FelRon IT-Legacy-Capital • {NAME} • San Antonio, TX</p></div></div>
  </footer>
'''
extra_css = '''  <style>
    .tool-tab { padding: .38rem .7rem; border-radius: .45rem; font-size: .78rem; font-weight: 600; color: #cbd5e1; white-space: nowrap; }
    .tool-tab:hover { color: #f3d98b; } .tool-tab.active { background: #d4af37; color: #060c18; }
    .h-tool { font-size: clamp(1.9rem, 5.5vw, 3.2rem); line-height: 1.06; }
    .seg-btn { padding: .5rem .8rem; border-radius: .5rem; font-size: .8rem; font-weight: 700; color: #cbd5e1; white-space: nowrap; }
    .seg-btn.on { background: #d4af37; color: #060c18; }
    .chip { padding: .4rem .75rem; border-radius: .5rem; font-size: .75rem; font-family: 'JetBrains Mono', monospace; border: 1px solid #334155; color: #cbd5e1; white-space: nowrap; }
    .chip.on { background: #d4af37; color: #060c18; border-color: #d4af37; font-weight: 700; }
    .kpi { background: rgba(6,12,24,.7); border: 1px solid #1f2a44; border-radius: .9rem; padding: .9rem; min-width: 0; }
    .kpi .v { font-family: 'JetBrains Mono', monospace; font-size: 1.2rem; font-weight: 700; color: #fff; overflow-wrap: anywhere; }
    .kpi .l { font-size: .7rem; color: #94a3b8; }
    input[type="range"] { accent-color: #d4af37; width: 100%; }
    .rowlbl { display: flex; justify-content: space-between; gap: .5rem; font-size: .78rem; color: #cbd5e1; }
    .rowlbl b { font-family: 'JetBrains Mono', monospace; color: #f3d98b; white-space: nowrap; }
    .chart-box { position: relative; height: 280px; }
  </style>
</head>'''
