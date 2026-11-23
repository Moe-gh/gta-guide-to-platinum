import re
s=open('tools/master.html').read()
s=re.sub(r'<script type="application/json" id="state">.*?</script>','<script type="application/json" id="state">{"t":0,"s":{}}</script>',s,count=1,flags=re.S)
def rep(o,n):
    global s; assert s.count(o)>=1,o[:60]; s=s.replace(o,n)
rep('<title>GTA 6 — Platinum Workspace</title>','<title>GTA Guide to Platinum</title>')
rep('GTA 6 — Platinum Workspace 🌴','GTA Guide to Platinum 🌴')
rep('var SKEY="gta6plat_v1"','var SKEY="gta6guide_public_v1"')
rep('syncMsg="Saved on this device"','syncMsg="Your progress is saved in this browser on this device"')
rep('if(window.claude&&window.claude.use){window.claude.use("artifact")','if(false&&window.claude&&window.claude.use){window.claude.use("artifact")')
rep('var DEFCHAP="2";','var DEFCHAP="";')
rep('try{CHAP=localStorage.getItem("gta6chap")','try{CHAP=localStorage.getItem("gta6chap_pub")')
rep('try{localStorage.setItem("gta6chap",CHAP)','try{localStorage.setItem("gta6chap_pub",CHAP)')
rep("🗺️ opens the exact pin on GTABase.</footer>","🗺️ opens the exact pin on GTABase.<br>Map pins & the full checklist link to <a target=\"_blank\" rel=\"noopener\" href=\"https://www.gtabase.com/gta-6/map/\">GTABase.com</a> — go show them some love.</footer>")
d=open('tools/donate.html').read()
i=s.rindex('</body>')
s=s[:i]+d+s[i:]
open('index.html','w').write(s)
