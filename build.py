import json,re
p=json.load(open('/tmp/pack.json'))
p['i18n']={'en':p['i18n']['en']}
p['languages']=[x for x in p['languages'] if x['code']=='en']
eng=open('/home/claude/src/ARAPAI-FARM-TWIN-main/ARAPAI-FARM-TWIN-main/frontend/engine.js').read()
eng=re.sub(r'^export ','',eng,flags=re.M)
app=open('app.js').read()
app=app.replace('/* ---------- glossary','renderCtrl();run();\n/* ---------- glossary',1)
js=eng+'\nconst PACK='+json.dumps(p,separators=(',',':'))+';\n'+app
html=open('index.template.html').read().replace('/*CSS*/',open('style.css').read()).replace('/*JS*/',js.replace('</script','<\\/script'))
open('index.html','w').write(html);print(len(html))
