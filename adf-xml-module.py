#parser 3
f1 = open('xml-template.txt','r')
f2 = open('xml-lead.xml', 'w')

def makexml(name):
    num = "12345"
    store="JSCWR"
    checkWords = ("Chevrolet","Blazer","1999", "John Doe", "393-999-3922", "Acura of Bellevue")
    repWords = ("MAKE","MODEL","YEAR",name,num,store)



    for line in f1:
        for check, rep in zip(checkWords, repWords):
            line = line.replace(check, rep)
            #print(line)
        f2.write(line)
    f1.close()
    f2.close()
    return line

if __name__=="__main__":
    makexml()
