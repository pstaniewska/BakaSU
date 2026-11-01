p="manager/app/src/main/AndroidManifest.xml"
s=open(p).read()
line='android:zygotePreloadName="org.bakasu.bakasu.magica.AppZygotePreload">'
assert line in s, "anchor missing"
s=s.replace(' '+line+'\n','')
s=s.replace(' '+line,'>')
open(p,"w").write(s)
print("stripped")
