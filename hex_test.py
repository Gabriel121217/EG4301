def hexa (hexa):
    ans = ''
    for i in hexa:
        digits = i[2:]
        print(i)
        print(len(i))
        if len(i)<4:
            digits+= "_"
        ans += digits
    print(ans)

cartridge = [
    ['0x60', '0xbb', '0xe9', '0x55'],
    ['0xfe', '0x43', '0x22', '0x1d'],
    ['0xa2', '0x4', '0xdc', '0x51'],
    ['0xee', '0xed', '0x65', '0x1d'],
    ['0xe8', '0x96', '0xff', '0xd'],
    ['0x53', '0x8f', '0x12', '0x34']]


hexa(['0xa2', '0x4', '0xdc', '0x51'])



ans = (37.345235235345346534//0.1 )/10

print(ans)