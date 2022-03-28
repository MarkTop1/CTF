from Crypto.Util.number import *

p = 64464091191308356774703439660771627086045800299627641179047457478059588557461
a = 31926335967105564755113987930261069322507794703287741857397622356704769886356
b = 34835808070187351680507689900273321615070127680320357724483770400791707112940
Gx = 2053202552422630348010474635096983783565667661786369125783579647572276572403
Gy = 51320753844844801021362329076409450910659564359017581255542897537756778371539
Zp = Zmod(p)
EC = EllipticCurve(Zp, [a, b])
G = EC(Gx, Gy)
K = EC(31981799071949968743482831587417174146463993877255771340814476669214408840460,15144025062588325012239455117890516531350002058200271280110877844265896081387)

Da = [4,3,1246057,2357351,435374689]
Db = [1,1,1016839,813641,35993350]
kn = crt(Db,Da)
n = 4*3*1246057*2357351*435374689
set = {(n*i*1500+kn)*G:i for i in range(1500)}

for i in range(1500):
    C = n*i*G+K
    if(C in set):
        k = 1500*set[C]*n+kn-n*i
        print(long_to_bytes(k))
        break