import re
regexp = r'(\d\d)(\w)'
target = '78y05m27d'
resultado = re.search(regexp,target)
resultado.group()
resultado.group(1)
resultado.group(2)
resultado.start()
resultado.end()

resultados = re.finditer(regexp, target)
for resultado in resultados:
    print "%s | %s | %s [%s,%s]" % (resultado.group(), resultado.group(1), resultado.group(2), resultado.start(), resultado.end())  

