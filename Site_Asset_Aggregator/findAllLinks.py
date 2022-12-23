import json
def pen(txt,x):
    f = open(x, "w")
    f.write(str(txt))
    f.close()
    return
def reader(x):
    f = open(x, "r")
    txt = f.read()
    return txt
def goToStop(x,ls):
  for i in range(1,len(x)+1):
    z = x[-i:]
    for k in range(0,len(ls)):
      if len(z) >= len(ls[k]):
        if z[:len(ls[k])] == ls[k]:
          if ls[k] in ['https://','http://']:
            return z
          else:
            return z[len(ls[k]):]
  return False
def isHere(x,ls):
  for i in range(0,len(ls)):
    if x[-len(ls[i]):] == ls[i]:
      return goToStop(x,['(',"'",'"','https://','http://','./'])
  return False
def whatIsIt(x,ls):
  for i in range(0,len(ls)):
    if x[-len(ls[i]):] == ls[i]:
      return ls[i]
def makeAlljs(js,ls):
  for i in range(0,len(ls)):
    js[ls[i][1:]] = []
  return js
def isExtInIt(x):
    print(x)
    exs = json.loads(reader('exts.json').replace("'",'"'))
    for i in range(0,len(exs)):
        if exs[i]+'/' in x and exs[i] not in exts:
            dom = x.split(exs[i])[0]+exs[i]
            if dom not in jsN['domains']:
                jsN['domains'].append(dom)
                return 
global jsN
exts = ['.svg','.png','.css','.jpeg','.js']
sheet = reader('sourceCode.txt')
source = ['https://app.enhancv.com','https://enhancv.com','https://','http://',]
jsN = makeAlljs({'domains':source,'replace':{'names':[]}},exts)
z = ''
for i in range(0,len(sheet)):
  z = z+ sheet[i]
  potent = isHere(z,exts)
  if potent != False:
    isExtInIt(potent)
    jsN[whatIsIt(potent,exts)[1:]].append(potent)
    z = ''
import dlImgAndJs
dlImgAndJs.checkjsAll(jsN)
source =reader('sourceCode.txt')
for i in range(0,len(jsN['replace']['names'])):
    link = jsN['replace']['names'][i]
    source = source.replace(link,jsN['replace'][link])
pen(source,'newSource')
