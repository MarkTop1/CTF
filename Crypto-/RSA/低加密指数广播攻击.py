import binascii
import gmpy2

n =  [
0x683fe30746a91545a45225e063e8dc64d26dbf98c75658a38a7c9dfd16dd38236c7aae7de5cbbf67056c9c57817fd3da79dc4955217f43caefde3b56a46acf5d,
0xa39292e6ad271bb6a2d1345940dfab8001a53d28bc7468f285d2873d784004c2653549c589dae91c6d8238977ff1c4bea4f17d424a0fc4d5587661cc7dde3a77,
0x52c32366d84d34564a5fdc1650fc401c41ad2a63a2d6ef57c32c7887bb25da9d42c0acfb887c6334c938839c9a43aca93b2c7468915d1846576f92c342046d1f
]
c =  [
0x673c72ace143441c07cba491074163c003f1a550eab56b1255e5ea9fa2bbd68fd6a9ccb48db9fd66d5dfc6a55c79cad3d9de53f700a1e3c2a29731dc56ba43cd,
0x6111357d180d966a495f38566ebe4ea51fa0d54159b22bbd443cde9387687d87c08638483b39221883453a5ad09f6a0e3726b214e8e333037d178a3d0f125343,
0x26cd2225c0229b6a3f1d1d685e53d114aa3d792737d040fbc14189336ac12fb780872792b0c0b259847badffd1427897ede0d60247aa5e79633f27ccb43e7cc2
]
def CRT(mi, ai):
    assert(reduce(gmpy2.gcd,mi)==1)
    assert (isinstance(mi, list) and isinstance(ai, list))
    M = reduce(lambda x, y: x * y, mi)
    ai_ti_Mi = [a * (M / m) * gmpy2.invert(M / m, m) for (m, a) in zip(mi, ai)]
    return reduce(lambda x, y: x + y, ai_ti_Mi) % M
e=0x7
m=gmpy2.iroot(CRT(n, c), e)[0]
print(binascii.unhexlify(hex(m)[2:].strip("L")))