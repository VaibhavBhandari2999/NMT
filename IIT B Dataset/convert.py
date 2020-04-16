import codecs
with codecs.open('pruned_train.hi',encoding='utf-8') as f,open('pruned_train.en','r') as f1,open('result.txt','w') as w:
    for i in range(788098):
        txt=f.readline()
        txt1=f1.readline()
        txt1=txt1[:-1]
        if(txt1[-1]==""):
            txt1=txt1[:-1]
        if(txt1[-1]!="."):
            txt1=txt1+" ."
        w.write(txt1+"\t")
        w.write(txt)