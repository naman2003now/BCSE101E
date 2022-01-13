def share_RegistrationNumber(total_p,p_share):
    r = int((total_p)*(p_share)/100)
    if r == total_p:
        print("No pens left to share")
    else:
        print(total_p - r)

total_p = int(input())
if total_p < 0:
    print("Pens should be >= 0")
else:
    p_share = int(input())
    if not 0 <= p_share <= 100:
        print("Percentage should be 0 to 100")
    else:
        share_RegistrationNumber(total_p, p_share)