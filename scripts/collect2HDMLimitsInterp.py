import os
A=[300,400,500,600,700,800]
Z=[600,800,1000,1200,1400,1700,2000,2500]


dirs=['Zprime600A300','Zprime600A325','Zprime600A350','Zprime600A375','Zprime600A400','Zprime600A425','Zprime600A450','Zprime600A475','Zprime600A525','Zprime600A550','Zprime600A625','Zprime600A675','Zprime600A700','Zprime600A750','Zprime600A775','Zprime600A800','Zprime600A825','Zprime600A875','Zprime600A900','Zprime600A925','Zprime650A350','Zprime650A375','Zprime650A400','Zprime650A425','Zprime650A450','Zprime650A475','Zprime650A500','Zprime650A525','Zprime650A550','Zprime650A600','Zprime650A625','Zprime650A650','Zprime650A675','Zprime650A700','Zprime650A725','Zprime650A750','Zprime650A775','Zprime650A800','Zprime650A825','Zprime650A850','Zprime650A875','Zprime650A900','Zprime650A925','Zprime650A975','Zprime700A300','Zprime700A325','Zprime700A375','Zprime700A400','Zprime700A425','Zprime700A450','Zprime700A475','Zprime700A500','Zprime700A575','Zprime700A625','Zprime700A650','Zprime700A725','Zprime700A750','Zprime700A825','Zprime700A850','Zprime700A875','Zprime700A900','Zprime700A925','Zprime700A950','Zprime700A975','Zprime750A300','Zprime750A325','Zprime750A350','Zprime750A375','Zprime750A450','Zprime750A500','Zprime750A550','Zprime750A575','Zprime750A600','Zprime750A625','Zprime750A650','Zprime750A675','Zprime750A700','Zprime750A725','Zprime750A775','Zprime750A800','Zprime750A850','Zprime750A875','Zprime750A900','Zprime750A925','Zprime750A950','Zprime750A975','Zprime800A300','Zprime800A350','Zprime800A375','Zprime800A400','Zprime800A425','Zprime800A450','Zprime800A475','Zprime800A500','Zprime800A525','Zprime800A550','Zprime800A575','Zprime800A600','Zprime800A625','Zprime800A675','Zprime800A700','Zprime800A750','Zprime800A775','Zprime800A800','Zprime800A825','Zprime800A850','Zprime800A875','Zprime800A900','Zprime800A925','Zprime800A950','Zprime850A300','Zprime850A325','Zprime850A350','Zprime850A375','Zprime850A400','Zprime850A425','Zprime850A450','Zprime850A475','Zprime850A500','Zprime850A525','Zprime850A575','Zprime850A600','Zprime850A625','Zprime850A650','Zprime850A675','Zprime850A700','Zprime850A725','Zprime850A750','Zprime850A775','Zprime850A825','Zprime850A850','Zprime850A900','Zprime850A950','Zprime850A975','Zprime900A300','Zprime900A325','Zprime900A350','Zprime900A375','Zprime900A400','Zprime900A425','Zprime900A450','Zprime900A475','Zprime900A525','Zprime900A550','Zprime900A575','Zprime900A675','Zprime900A700','Zprime900A725','Zprime900A750','Zprime900A775','Zprime900A825','Zprime900A850','Zprime900A900','Zprime900A950','Zprime900A975','Zprime950A300','Zprime950A325','Zprime950A350','Zprime950A375','Zprime950A400','Zprime950A450','Zprime950A475','Zprime950A500','Zprime950A525','Zprime950A575','Zprime950A600','Zprime950A625','Zprime950A675','Zprime950A700','Zprime950A750','Zprime950A775','Zprime950A800','Zprime950A850','Zprime950A875','Zprime950A900','Zprime950A950','Zprime950A975','Zprime1000A300','Zprime1000A375','Zprime1000A400','Zprime1000A425','Zprime1000A450','Zprime1000A500','Zprime1000A550','Zprime1000A575','Zprime1000A600','Zprime1000A625','Zprime1000A650','Zprime1000A675','Zprime1000A700','Zprime1000A725','Zprime1000A800','Zprime1000A825','Zprime1000A875','Zprime1000A900','Zprime1000A950','Zprime1000A975','Zprime1050A300','Zprime1050A325','Zprime1050A350','Zprime1050A400','Zprime1050A425','Zprime1050A450','Zprime1050A475','Zprime1050A550','Zprime1050A600','Zprime1050A625','Zprime1050A675','Zprime1050A700','Zprime1050A725','Zprime1050A750','Zprime1050A775','Zprime1050A800','Zprime1050A850','Zprime1050A875','Zprime1050A900','Zprime1050A925','Zprime1050A950','Zprime1050A975','Zprime1100A300','Zprime1100A350','Zprime1100A375','Zprime1100A400','Zprime1100A450','Zprime1100A525','Zprime1100A550','Zprime1100A575','Zprime1100A600','Zprime1100A625','Zprime1100A650','Zprime1100A675','Zprime1100A725','Zprime1100A750','Zprime1100A775','Zprime1100A800','Zprime1100A825','Zprime1100A850','Zprime1100A875','Zprime1100A900','Zprime1100A925','Zprime1100A950','Zprime1150A300','Zprime1150A325','Zprime1150A350','Zprime1150A375','Zprime1150A400','Zprime1150A425','Zprime1150A450','Zprime1150A475','Zprime1150A500','Zprime1150A525','Zprime1150A550','Zprime1150A600','Zprime1150A625','Zprime1150A650','Zprime1150A675','Zprime1150A700','Zprime1150A725','Zprime1150A775','Zprime1150A800','Zprime1150A825','Zprime1150A850','Zprime1150A875','Zprime1150A900','Zprime1150A925','Zprime1150A950','Zprime1150A975','Zprime1200A300','Zprime1200A325','Zprime1200A400','Zprime1200A475','Zprime1200A500','Zprime1200A525','Zprime1200A550','Zprime1200A575','Zprime1200A600','Zprime1200A625','Zprime1200A650','Zprime1200A675','Zprime1200A700','Zprime1200A725','Zprime1200A750','Zprime1200A775','Zprime1200A800','Zprime1200A825','Zprime1200A925','Zprime1200A950','Zprime1250A325','Zprime1250A400','Zprime1250A425','Zprime1250A450','Zprime1250A475','Zprime1250A500','Zprime1250A525','Zprime1250A650','Zprime1250A750','Zprime1250A800','Zprime1250A850','Zprime1250A875','Zprime1250A925','Zprime1250A950','Zprime1300A325','Zprime1300A350','Zprime1300A400','Zprime1300A450','Zprime1300A500','Zprime1300A550','Zprime1300A575','Zprime1300A600','Zprime1300A650','Zprime1300A725','Zprime1300A750','Zprime1300A775','Zprime1300A800','Zprime1300A825','Zprime1300A850','Zprime1300A875','Zprime1300A900','Zprime1300A925','Zprime1300A975','Zprime1350A325','Zprime1350A350','Zprime1350A375','Zprime1350A400','Zprime1350A425','Zprime1350A450','Zprime1350A475','Zprime1350A500','Zprime1350A525','Zprime1350A550','Zprime1350A575','Zprime1350A600','Zprime1350A650','Zprime1350A675','Zprime1350A725','Zprime1350A750','Zprime1350A775','Zprime1350A800','Zprime1350A825','Zprime1350A850','Zprime1350A875','Zprime1350A900','Zprime1350A925','Zprime1350A950','Zprime1350A975','Zprime1400A300','Zprime1400A350','Zprime1400A400','Zprime1400A450','Zprime1400A475','Zprime1400A500','Zprime1400A525','Zprime1400A550','Zprime1400A650','Zprime1400A675','Zprime1400A700','Zprime1400A725','Zprime1400A750','Zprime1400A825','Zprime1400A875','Zprime1400A900','Zprime1400A925','Zprime1450A300','Zprime1450A350','Zprime1450A375','Zprime1450A400','Zprime1450A425','Zprime1450A450','Zprime1450A475','Zprime1450A500','Zprime1450A525','Zprime1450A550','Zprime1450A650','Zprime1450A700','Zprime1450A725','Zprime1450A750','Zprime1450A775','Zprime1450A875','Zprime1450A900','Zprime1450A925','Zprime1450A975','Zprime1500A300','Zprime1500A325','Zprime1500A350','Zprime1500A375','Zprime1500A425','Zprime1500A450','Zprime1500A475','Zprime1500A500','Zprime1500A525','Zprime1500A550','Zprime1500A575','Zprime1500A600','Zprime1500A675','Zprime1500A700','Zprime1500A725','Zprime1500A800','Zprime1500A850','Zprime1500A900','Zprime1500A950','Zprime1500A975','Zprime1550A325','Zprime1550A375','Zprime1550A400','Zprime1550A425','Zprime1550A450','Zprime1550A500','Zprime1550A550','Zprime1550A600','Zprime1550A625','Zprime1550A650','Zprime1550A675','Zprime1550A700','Zprime1550A750','Zprime1550A775','Zprime1550A800','Zprime1550A875','Zprime1550A900','Zprime1550A950','Zprime1600A425','Zprime1600A450','Zprime1600A675','Zprime1600A750','Zprime1600A775','Zprime1600A825','Zprime1650A325','Zprime1650A350','Zprime1650A425','Zprime1650A450','Zprime1650A725','Zprime1650A850','Zprime1700A300','Zprime1700A500','Zprime1700A750','Zprime1700A975','Zprime1750A400','Zprime1750A425','Zprime1750A475','Zprime1750A700','Zprime1750A800','Zprime1750A825','Zprime1750A900','Zprime1750A925','Zprime1750A975','Zprime1800A300','Zprime1800A350','Zprime1800A375','Zprime1800A400','Zprime1800A450','Zprime1800A475','Zprime1800A500','Zprime1800A525','Zprime1800A550','Zprime1800A575','Zprime1800A600','Zprime1800A650','Zprime1800A675','Zprime1800A700','Zprime1800A750','Zprime1800A775','Zprime1800A800','Zprime1800A850','Zprime1800A875','Zprime1800A925','Zprime1800A950','Zprime1800A975','Zprime1850A300','Zprime1850A325','Zprime1850A350','Zprime1850A375','Zprime1850A425','Zprime1850A450','Zprime1850A475','Zprime1850A500','Zprime1850A525','Zprime1850A550','Zprime1850A575','Zprime1850A600','Zprime1850A625','Zprime1850A700','Zprime1850A725','Zprime1850A750','Zprime1850A775','Zprime1850A850','Zprime1850A900','Zprime1850A925','Zprime1850A975','Zprime1900A300','Zprime1900A400','Zprime1900A425','Zprime1900A450','Zprime1900A475','Zprime1900A500','Zprime1900A525','Zprime1900A600','Zprime1900A625','Zprime1900A800','Zprime1900A825','Zprime1900A900','Zprime1900A925','Zprime1900A975','Zprime1950A300','Zprime1950A325','Zprime1950A350','Zprime1950A375','Zprime1950A400','Zprime1950A425','Zprime1950A450','Zprime1950A475','Zprime1950A550','Zprime1950A575','Zprime1950A600','Zprime1950A625','Zprime1950A650','Zprime1950A675','Zprime1950A700','Zprime1950A750','Zprime1950A800','Zprime1950A850','Zprime1950A875','Zprime1950A925','Zprime1950A975','Zprime2000A300','Zprime2000A325','Zprime2000A350','Zprime2000A400','Zprime2000A425','Zprime2000A450','Zprime2000A475','Zprime2000A550','Zprime2000A575','Zprime2000A600','Zprime2000A625','Zprime2000A650','Zprime2000A700','Zprime2000A725','Zprime2000A775','Zprime2000A800','Zprime2000A825','Zprime2000A850','Zprime2000A875','Zprime2000A900','Zprime2000A925','Zprime2000A950','Zprime2050A300','Zprime2050A325','Zprime2050A350','Zprime2050A375','Zprime2050A400','Zprime2050A425','Zprime2050A450','Zprime2050A475','Zprime2050A500','Zprime2050A525','Zprime2050A550','Zprime2050A575','Zprime2050A600','Zprime2050A625','Zprime2050A650','Zprime2050A675','Zprime2050A700','Zprime2050A725','Zprime2050A750','Zprime2050A775','Zprime2050A800','Zprime2050A825','Zprime2050A850','Zprime2050A875','Zprime2050A900','Zprime2050A925','Zprime2050A950','Zprime2050A975','Zprime2100A300','Zprime2100A325','Zprime2100A350','Zprime2100A375','Zprime2100A400','Zprime2100A425','Zprime2100A450','Zprime2100A475','Zprime2100A500','Zprime2100A525','Zprime2100A550','Zprime2100A575','Zprime2100A600','Zprime2100A625','Zprime2100A650','Zprime2100A675','Zprime2100A700','Zprime2100A725','Zprime2100A750','Zprime2100A775','Zprime2100A800','Zprime2100A825','Zprime2100A850','Zprime2100A875','Zprime2100A900','Zprime2100A925','Zprime2100A950','Zprime2100A975','Zprime2150A300','Zprime2150A325','Zprime2150A375','Zprime2150A400','Zprime2150A450','Zprime2150A475','Zprime2150A500','Zprime2150A525','Zprime2150A550','Zprime2150A575','Zprime2150A600','Zprime2150A625','Zprime2150A650','Zprime2150A675','Zprime2150A700','Zprime2150A750','Zprime2150A775','Zprime2150A800','Zprime2150A825','Zprime2150A850','Zprime2150A875','Zprime2150A900','Zprime2150A925','Zprime2150A950','Zprime2150A975','Zprime2200A300','Zprime2200A325','Zprime2200A350','Zprime2200A375','Zprime2200A400','Zprime2200A425','Zprime2200A450','Zprime2200A475','Zprime2200A500','Zprime2200A525','Zprime2200A550','Zprime2200A575','Zprime2200A600','Zprime2200A625','Zprime2200A650','Zprime2200A675','Zprime2200A700','Zprime2200A725','Zprime2200A750','Zprime2200A775','Zprime2200A825','Zprime2200A850','Zprime2200A875','Zprime2200A900','Zprime2200A925','Zprime2200A950','Zprime2250A300','Zprime2250A325','Zprime2250A350','Zprime2250A375','Zprime2250A400','Zprime2250A425','Zprime2250A450','Zprime2250A475','Zprime2250A500','Zprime2250A525','Zprime2250A550','Zprime2250A575','Zprime2250A600','Zprime2250A625','Zprime2250A650','Zprime2250A675','Zprime2250A700','Zprime2250A725','Zprime2250A750','Zprime2250A775','Zprime2250A800','Zprime2250A825','Zprime2250A850','Zprime2250A875','Zprime2250A900','Zprime2250A925','Zprime2250A975','Zprime2300A300','Zprime2300A325','Zprime2300A375','Zprime2300A400','Zprime2300A425','Zprime2300A450','Zprime2300A500','Zprime2300A525','Zprime2300A550','Zprime2300A575','Zprime2300A600','Zprime2300A625','Zprime2300A650','Zprime2300A675','Zprime2300A700','Zprime2300A725','Zprime2300A750','Zprime2300A800','Zprime2300A825','Zprime2300A850','Zprime2300A875','Zprime2300A900','Zprime2300A925','Zprime2300A950','Zprime2300A975','Zprime2350A300','Zprime2350A325','Zprime2350A350','Zprime2350A375','Zprime2350A400','Zprime2350A425','Zprime2350A450','Zprime2350A475','Zprime2350A500','Zprime2350A525','Zprime2350A550','Zprime2350A575','Zprime2350A600','Zprime2350A625','Zprime2350A650','Zprime2350A700','Zprime2350A725','Zprime2350A750','Zprime2350A800','Zprime2350A825','Zprime2350A850','Zprime2350A875','Zprime2350A900','Zprime2350A925','Zprime2350A950','Zprime2350A975','Zprime2400A300','Zprime2400A325','Zprime2400A350','Zprime2400A375','Zprime2400A400','Zprime2400A425','Zprime2400A450','Zprime2400A475','Zprime2400A525','Zprime2400A550','Zprime2400A575','Zprime2400A600','Zprime2400A625','Zprime2400A650','Zprime2400A675','Zprime2400A700','Zprime2400A725','Zprime2400A750','Zprime2400A775','Zprime2400A825','Zprime2400A850','Zprime2400A875','Zprime2400A900','Zprime2400A925','Zprime2400A975','Zprime2450A300','Zprime2450A325','Zprime2450A350','Zprime2450A375','Zprime2450A400','Zprime2450A425','Zprime2450A450','Zprime2450A475','Zprime2450A500','Zprime2450A525','Zprime2450A550','Zprime2450A600','Zprime2450A625','Zprime2450A650','Zprime2450A675','Zprime2450A700','Zprime2450A725','Zprime2450A750','Zprime2450A775','Zprime2450A800','Zprime2450A825','Zprime2450A850','Zprime2450A875','Zprime2450A900','Zprime2450A925','Zprime2450A950','Zprime2450A975','Zprime2500A300','Zprime2500A325','Zprime2500A350','Zprime2500A375','Zprime2500A400','Zprime2500A425','Zprime2500A450','Zprime2500A475','Zprime2500A500','Zprime2500A525','Zprime2500A575','Zprime2500A600','Zprime2500A625','Zprime2500A650','Zprime2500A675','Zprime2500A700','Zprime2500A750','Zprime2500A775','Zprime2500A800','Zprime2500A825','Zprime2500A850','Zprime2500A875','Zprime2500A900','Zprime2500A925','Zprime2500A975']

for d in dirs:
        cmd = "combineTool.py -M CollectLimits "+d+ "/cmb/*/*.limit.* -o "+d+".json"
        os.system(cmd)
