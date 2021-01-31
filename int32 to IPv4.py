
def int32_to_ip(int32: int) -> str:
    thirty_two = '{:032b}'.format(int32)
    egiht_bits = [thirty_two[i:i+8] for i in range(0, len(thirty_two), 8)]
    return ".".join([str(int(ele, 2)) for ele in egiht_bits])


print(int32_to_ip(2154959208))
