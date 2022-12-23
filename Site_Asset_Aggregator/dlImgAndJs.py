import urllib.request as urllib2
import requests # request img from web
import shutil # save img locally
import os
import time
import stat
import matplotlib.image as mpimg
import json
og = os.getcwd()+'/new_dl/'

import os.path
def checkIfDud(x):
    if  x != None:
        if len(x)>0:
            if len(x) >1:
                  return x
    return False
def eatX(x):
    if checkIfDud(x) != False:
        while x[-1] == slash and len(x)>1:
            x = x[:-1]
    return x
def eatY(y):
    if checkIfDud(y) != False:
        while y[0] == slash and len(y) >1:
            y[1:]
    return y
def createPath(x,y):
    return eatX(x)+'/'+eatY(y)
def getTime():
    return time.time()
def eatInnerMod(x,ls):
    if strInList(x,ls) != False:
        x = strInList(x,ls)
    return x
def eatOuterMod(x,ls):
    if strInListRev(x,ls) != False:
        x = strInListRev(x,ls)
    return x
def isLs(x):
    if type(x) is list:
        return True
    return False
def strInList(x,ls):
    if ifOverZero(x) == True:
        if x[0] in ls:
            return x[1:]
    return False
def strInListRev(x,ls):
    if ifOverZero(x) == True:
        if x[-1] in ls:
            return x[:-1]
    return False
def ifOverZero(x):

    if len(x) >1:
        return True
    return False
def chmodIt(x):
    st = os.stat(x)
    os.chmod(x, st.st_mode | stat.S_IEXEC)
    os.chmod(x, 0o775)
    return 'sh '+str(x)
def pen(txt,x):
    f = open(x, "w")
    f.write(str(txt))
    f.close()
    return
def reader(x):
    f = open(x, "r")
    txt = f.read()
    return txt
def home_it():
    curr = os.getcwd()
    slash = '//'
    if '//' not in str(curr):
        slash = '/'
    changeGlob('slash',slash)
    changeGlob('home',curr)
    return curr,slash
def changeGlob(x,v):
    globals()[x] = v
def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)
def is_int(x):
    try:
        int(x)
        return True
    except:
        return False
def rid_check(x):
    if is_int(x) == True or x == ' ' or x == '-':
        return True
    else:
        return False
def strip_non_num(x):
    og = x
    done = 0
    while is_int(x[0]) == False and len(x) > 2 and done !=2:
        if len(x) < 2:
            done = 2
    while is_int(x[-1]) == False and len(x) > 2 and done !=2:
        if len(x) < 2:
            done = 2
        x = x[:-1]
    if done == 2:
        return 'other'
    else:
        new_ = os.listdir(str(fold))[-1]
        x = og.replace(str(new_),str(int(x) + int(1)))
        return x
    
def rid_it(x):
    name = fold
    done = 0
    while rid_check(x[0]) == True and len(x) > 2 and done !=2:
        if len(x) < 2:
            done = 2
        x = x[1:]
    while rid_check(x[-1]) == True and len(x) > 2 and done !=2:
        if len(x) < 2:
            done = 2
        x = x[:-1]
    if done == 2:
        new_ = strip_non_num(os.listdir(str(fold))[-1])
        name = os.getcwd()+'/new_dl/'+str(new_)
    if done != 2 and is_int(x) != True:
        name = os.getcwd()+'/new_dl/'+str(x)
    if os.path.isdir(name) == False:
        os.mkdir(name)
    return name
def findIt(x,ls):
    for i in range(0,len(ls)):
        if x == ls[i]:
            return i
def url(ur):
    page = urllib2.urlopen(ur)
    data = page.read()
    return data
def bash_it(x):
    sh_str = reader('sample_whole_sh.txt')
    pen(sh_str.replace('^^killme^^', x),'script.sh')
    os.popen("gnome-terminal -x  "+chmodIt('./script.sh')).read()
def req_it(ur):
    import ssl
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.poolmanager import PoolManager
    from urllib3.util import ssl_
    import json

    CIPHERS = "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"

    class TLSAdapter(HTTPAdapter):
        
        def __init__(self, ssl_options=0, *args, **kwargs):
            self.ssl_options = ssl_options
            super().__init__(*args, **kwargs)
        
        def init_poolmanager(self, *args, **kwargs):
            context = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
            self.poolmanager = PoolManager(*args, ssl_context=context, **kwargs)


    url = ur
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53",
    }
    adapter = TLSAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)

    with requests.session() as session:
        r = requests.get(url = url)
        DATA = r.text
        return DATA
def isWeb(x):
    for i in range(0,len(jsN['domains'])):
        
        if jsN['domains'][i] in x:
             return True
    return False
def countIt(x,y):
    return (len(x)-len(x.replace(y,'')))/len(y)
def stripWeb(x):
    
    #if countIt(x,'/') == 1 and x[0] == '/':
    #    return x[1:]
  # 
    #for i in range(0,len(jsN['domains'])):
    #    if jsN['domains'][i] in x:
    #        return x.split(jsN['domains'][i])[-1]
    exs = json.loads(reader('exts.json').replace("'",'"'))
    for i in range(0,len(exs)):
        if exs[i]+'/' in x and exs[i] not in exts:
            return x.split(exs[i]+'/')[-1]
    
    return x
def isWebFile(x):
    try:
        dat = req_it(x)
        return True
    except:
        return False
def isWeb(x):
    try:
        res = requests.get(x, stream = True)
        if res == 200:
            return True
    except:
        return False
def createWebAdd(li,x):
    return createPath(li,x)
def getImages(ls):
    
    for i in range(0,len(ls)):
      ur = ls[i]
 
      import matplotlib.image as mpimg
      k = 0
      while isWebFile(ur) != True and k <len(jsN['domains']):
          ur = createDomain(jsN['domains'][k],ls[i].replace(jsN['domains'][k-1],''),k)
          print(ur)
          k +=1
      res = requests.get(ur, stream = True)

      if res.status_code == 200:
          with open(cleanForSave('assets/img/',ur,k,ls[i]),'wb') as f:
              shutil.copyfileobj(res.raw, f)
      else:
            input(res)
            print('Image Couldn\'t be retrieved')
def returnAllWeb(ls):
        for i in range(0,len(ls)):
            if isWeb(ls[i]) != True:
                ls[i] = createPath(jsN['domains'][0],ls[i])
        return ls
def createDomain(li,x,k):
    x = x.replace(jsN['domains'][k-1],'').replace('https://','').replace('http://','')
    while x[0] == '/':
        x = x[1:]
    if 'http' not in x:
        x = x.replace('//','/')
    if li[-2:] != '//' and  li[-3:] != '://':
        while li[-1] == '/':
            li = li[:-1]
    if li not in ['https://','http://']:
        return li+'/'+x
    return  li+x
def cleanForSave(pa,ur,k,li):
    ne = pa+stripWeb(ur).replace(jsN['domains'][k],'').split('/')[-1]
    jsN['replace'][li] = './'+ne
    jsN['replace']['names'].append(li)
    return ne
def geCss(ls):
    for i in range(0,len(ls)):
       ur = ls[i]
       k = 0
   
       while isWebFile(ur) != True and k <len(jsN['domains']):
           ur = createDomain(jsN['domains'][k],ls[i].replace(jsN['domains'][k-1],''),k)
           k +=1
           print(ur)
       pen(req_it(ur),cleanForSave('assets/css/',ls[i],k,ls[i]))
def getJs(ls):
    for i in range(0,len(ls)):
       ur = ls[i]
       k = 0
  
       while isWebFile(ur) != True and k <len(jsN['domains']):
           ur = createDomain(jsN['domains'][k],ls[i].replace(jsN['domains'][k-1],''),k)
           k +=1
       
   
       pen(req_it(ur),cleanForSave('assets/js/',ur,k,ls[i]))
def checkjsAll(jsN):
    changeGlob('jsN',jsN)
    for i in range(0,len(exts)):
        if exts[i] in jsN:
            if len(jsN[exts[i]]) >0:
                if exts[i] in ['svg','png','jpeg']:
                    getImages(jsN[exts[i]])
                elif exts[i] == 'css':
                    geCss(jsN[exts[i]])
                elif exts[i] == 'js':
                    getJs(jsN[exts[i]])
    return jsN
global exts
home_it()
my_makedirs('assets')
my_makedirs('assets/js/')
my_makedirs('assets/img/')
my_makedirs('assets/css/')
exts = ['svg','png','jpeg','css','js']
#imgls = ['https://app.enhancv.com/96a69c0f7ca11e2f828ad13f3f3db3ea.png','https://app.enhancv.com/bcf178e66a652aa966585b48b18bad77.png','https://app.enhancv.com/711a3ebafca12ff3a7acdf2c53b318f1.png','https://app.enhancv.com/bcf178e66a652aa966585b48b18bad77.png','https://app.enhancv.com/2120b7c2be9b25a4bde1a74b7358eaef.svg','https://app.enhancv.com/b6da16d2ad9aa631b5601f406780624e.svg','https://app.enhancv.com/daf211eb9284595affceffc6094b9831.svg','https://app.enhancv.com/4c56f85eec682100e6a2b993a1aa2be4.svg','https://app.enhancv.com/2854b6cc6bda4b21dcbc901d5c9898e9.svg','https://app.enhancv.com/96f339787dadc3bfb416d51f8d5cd7c4.svg','https://app.enhancv.com/c7c215a23d5acf17a7b4072943324a38.svg','https://app.enhancv.com/e0ea4f4f6f8fd9cfdeba568f1c54e631.svg','https://app.enhancv.com/4c56f85eec682100e6a2b993a1aa2be4.svg','https://app.enhancv.com/96ff63dd778a6748085a49a2b9f7dcc6.svg','https://app.enhancv.com/b7eb8bb39677dbe34aec84a4b9cd8611.svg','https://app.enhancv.com/96a69c0f7ca11e2f828ad13f3f3db3ea.png','https://app.enhancv.com/7a15dc77acb3fb3f5f41388c4e05db6b.png','https://app.enhancv.com/bcf178e66a652aa966585b48b18bad77.png','https://app.enhancv.com/711a3ebafca12ff3a7acdf2c53b318f1.png','https://app.enhancv.com/7a15dc77acb3fb3f5f41388c4e05db6b.png','https://app.enhancv.com/bcf178e66a652aa966585b48b18bad77.png']
#jsLs = ['https://assets.customer.io/assets/track.js','https://dna8twue3dlxq.cloudfront.net/js/profitwell.js','https://cdn.amplitude.com/libs/amplitude-4.5.0-min.gz.js','https://www.google-analytics.com/analytics.js','https://enhancv.com/thirdPartys.js','https://app.enhancv.com/static.hotjar.com/c/hotjar-582574.js','https://script.hotjar.com/modules.bc1117deb4413903e9ac.js','https://dna8twue3dlxq.cloudfront.net/js/profitwell.js','https://app.enhancv.com/app.41f2876716ae72c3a0ff.js','https://cdn.paddle.com/paddle/paddle.js']
#cssLs = ['https://app.enhancv.com/app.bbea82837bb0268ef6ae.css','https://cdn.paddle.com/paddle/assets/css/animate.css','https://cdn.paddle.com/paddle/assets/css/paddle.css']


