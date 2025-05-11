from ipaddress import *
for A in range(256):
    net = ip_network(f'32.0.{A}.5/20',0)
    for ip in net:
        b_ip = bin(int(ip))[2:]
        while len(b_ip) < 32:
            b_ip = '0' + b_ip
        if b_ip[:16].count('1') > b_ip[16:].count('1'):
            break
    else:
        print(A)
        break




'''ДЗ 6'''
# net = ip_network('151.192.0.0/255.224.0.0')
# cnt = 0
# for ip in net:
#     b_ip = bin(int(ip))[2:]
#     if b_ip.count('1') == b_ip.count('0'):
#         cnt += 1
# print(cnt)

'''ДЗ 5'''
# net = ip_network('129.128.0.0/255.128.0.0')
# print(bin(int(net[-1]))[2:].count('0'))

'''ДЗ 4'''
# for byte in range(255,0,-1):
#     net = ip_network(f'248.112.{byte}.132/255.255.255.240',0)
#     for ip in net:
#         b_ip = bin(int(ip))[2:]
#         if b_ip[:16].count('0') > b_ip[16:].count('0'):
#             break
#     else:
#         print(byte)
#         break

'''ДЗ 3'''
# net = ip_network('171.128.0.0/255.128.0.0')
# cnt = 0
# for ip in net:
#     b_ip = bin(int(ip))[2:]
#     if b_ip[:16].count('1') < b_ip[16:].count('1'):
#         cnt += 1
# print(cnt)

'''ДЗ 2'''
# print(math.comb(10,0) + math.comb(10,1) + math.comb(10,2) + math.comb(10,3) + math.comb(10,4))
# net = ip_network('101.157.240.0/255.255.252.0')
# cnt = 0
# for ip in net:
#     b_ip = bin(int(ip))[2:]
#     while len(b_ip) < 32:
#         b_ip = '0' + b_ip
#     if b_ip[:16].count('1') > b_ip[16:].count('1'):
#         cnt += 1
# print(cnt)

'''ДЗ 1'''
# for mask in range(16,25):
#     net = ip_network(f'152.65.245.132/{mask}',0)
#     for ip in net:
#         b_ip = bin(int(ip))[2:]
#         if b_ip[:16].count('0') < b_ip[16:].count('0'):
#             break
#     else:
#         print(mask)
#         break


# for mask in range(33):
#     net = ip_network(f'116.109.66.45/{mask}', 0)
#     if str(net.network_address) == '116.109.64.0':
#         print(net)

# for a in range(256):
#     net=ip_network(f'32.0.{a}.5/255.255.240.0', 0)
#     for ip in net:
#         if f'{ip:b}'[0:16].count('1') > f'{ip:b}'[16:32].count('1'):
#             break
#     else:
#         print(a)
#         break

# for mask in range(33):
#     flag = True
#     net = ip_network(f'116.109.66.45/{mask}', 0)
#     if str(net.network_address) == '116.109.64.0':
#         print(mask)
# print(int('11111100',2))


'''demo'''
# from ipaddress import ip_network
# cnt = 0
# addresses = ip_network('172.16.168.0/255.255.248.0')
# for address in addresses:
#     if bin(int(address)).count('1') % 5 != 0:
#         cnt += 1
# print(cnt)

''' dosrok '''
# net = ip_network(f'143.168.72.213/255.255.255.240',0)
# for ip in net:
#     print(ip)

''' 15var '''
# for A in range(256):
#     flag = True
#     net = ip_network(f'32.0.{A}.5/20',0)
#     for ip in net:
#         b = bin(int(ip))[2:]
#         if b[:16].count('1') > b[16:].count('1'):
#             flag = False
#             break
#     if flag:
#         print(A)
#         break

''' 14var '''
# for mask in range(16, 24 + 1):
#     flag = True
#     net = ip_network(f'199.59.129.3/{mask}',0)
#     for ip in net:
#         b = bin(int(ip))[2:]
#         if b[:16].count('1') < b[16:].count('1'):
#             flag = False
#             break
#     if flag:
#         print(mask)
#         break

'''580BC7'''
# from ipaddress import ip_network
# cnt = 0
# addresses = ip_network('172.16.192.0/255.255.192.0')
# for x in addresses:
#     b = bin(int(x))
#     if b.count('1') % 5 != 0:
#         cnt += 1
# print(cnt)

'''6B2DF4'''
# from ipaddress import ip_network
#
# net = ip_network('122.159.136.144/255.255.255.248',0)
# cnt = 0
# for ip in net:
#     b_ip = bin(int(ip))[2:]
#     if b_ip.count('1') % 4 != 0:
#         cnt += 1
# print(cnt)


    # b_ip = bin(int(ip))[2:]
    # while len(b_ip) < 32:
    #     b_ip = '0' + b_ip
    # b_ip = b_ip[:8] + '.' + b_ip[8:16] + '.' + b_ip[16:24] + '.' + b_ip[24:]














