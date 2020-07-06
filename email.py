f = open('1.txt')
data = f.read()
f.close()

import re
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", data)
#if emails:
    #print (emails)
#else:
    #print ('not match')

results = []
count = 0
for address in emails:
    print (address)
    count += 1

    result = '%s \n' % (address[0:])
    results.append(result)

print ('Total=',count)

output = open('output.txt', 'w')
output.writelines(results)
output.close()
# 从文本文件提取email
# ver1.0