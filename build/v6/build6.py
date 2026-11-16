#!/usr/bin/env python3
"""FelRon IT-Legacy-Capital site build v6: v5 website structure + Gemini app tools (ROI, Codex & Vault, LEAPS & Perps Lab,
Capital Flywheel, First-Call Dispatch) + members preview.  Run: python3 build/v6/build6.py -> /workspace/felron-site/index.html
Content data lives in content6.py; page HTML in pages6.py; JS in app6.js."""
import json, sys
sys.path.insert(0, '/workspace/felron-site/build/v6')
from content6 import *
from pages6 import *
body = home + services + how + pricing + roi + codex + lab + flywheel + dispatch + members + about + contact + book + legal + waiver
js = R('app6.js').replace('/*CONCEPTS_JSON*/', json.dumps(CONCEPTS)).replace('/*CATS_JSON*/', json.dumps(CATS))
out = R('head.html').replace('</head>', extra_css, 1) + header + body + footer + '  <script>\n' + js + '\n  </script>\n</body>\n</html>\n'
banned = ['licensed partner', 'partner network', 'trade partner', 'HVAC partner', 'mechanic partner', 'electrical partner', 'capacitor', 'contactor', 'remodel']
low = out.lower()
for b in banned:
    assert b.lower() not in low, 'banned phrase present: ' + b
open('/workspace/felron-site/index.html', 'w').write(out)
print('wrote', len(out), 'chars;', NC, 'modules')
