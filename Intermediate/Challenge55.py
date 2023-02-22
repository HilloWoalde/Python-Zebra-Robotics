final = ""
fOodd = open("55oddlines.txt")
fOeven = open("55evenlines.txt")
while True:
    chrodd = fOodd.readline()
    os = chrodd.strip()
    chreven = fOeven.readline()
    oe = chreven.strip()
    final+=oe+" "+os+" "
    if not chrodd and not chreven:
        break
fOodd.close
fOeven.close
print(final)
