import crawler

#config
#sites to obtain links
sitesfile = 'inputsites.txt' #input (websites where are links displayed)
outputFile = 'randomsites.txt' #output file with the displayed links 


sites = []
try:
    f = open(sitesfile,'r')
    lines = f.readlines()
    for line in lines:
        print("readed line: " + line)
        sites.append(line)
    f.close()
except:
    print(sitesfile + ' not found, please add it in this same folder. Remember to execute the script from here')


crawl = crawler.crawler()

generated = crawl.generate(sites)

print('=================================')
print('=================================')
print('generated:\n')

for x in generated:
    print(x)
    
f = open(outputFile,'w')
f.writelines(line + '\n' for line in generated)
f.close()