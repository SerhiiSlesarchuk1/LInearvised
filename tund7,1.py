
+ACM- def Loe+AF8-failist(fail:str)-+AD4-list:
+ACM-     f+AD0-open(fail,'r',encording+AD0AIg-utf-8-sig+ACI-)
+ACM-     jarjend+AD0AWwBd-
+ACM-     for rida in f:
+ACM-         jarjend.append(rida.strip())
+ACM-     f.close()
+ACM-     return jarjend
+ACM- def Kirjuta+AF8-failisse(fail:str,jarjend:list):
+ACM-     f+AD0-open(fail,'w',encoding+AD0AIg-utf-8-sig+ACI-)
+ACM-     for line in jarjend:
+ACM-         f.write(line+-'+AFw-n')
+ACM-     f.close()

+ACM- loetelu+AD0-Loe+AF8-failist('')
