alphabet = []
for i in range(ord("a"), ord("z") + 1):
    alphabet.append(chr(i))


def caesar_decrypt(key: int, data: str):
    result = ""
    for element in data:
        if element == " ":
            result += " "
        elif element.isupper():
            result += alphabet[
                (ord(element.lower()) - key - ord("a")) % len(alphabet)
            ].upper()
        else:
            result += alphabet[(ord(element) - key - ord("a")) % len(alphabet)]
    return result


for i in range(26):
    decrypted = caesar_decrypt(i, "Dfdj ftu vo uftu")
    print(f"{i} --> {decrypted}")

# 0  --> Dfdj ftu vo uftu
# 1  --> Ceci est un test <-- la clé est donc 1 !
# 2  --> Bdbh drs tm sdrs
# 3  --> Acag cqr sl rcqr
# 4  --> Zbzf bpq rk qbpq
# 5  --> Yaye aop qj paop
# 6  --> Xzxd zno pi ozno
# 7  --> Wywc ymn oh nymn
# 8  --> Vxvb xlm ng mxlm
# 9  --> Uwua wkl mf lwkl
# 10 --> Tvtz vjk le kvjk
# 11 --> Susy uij kd juij
# 12 --> Rtrx thi jc ithi
# 13 --> Qsqw sgh ib hsgh
# 14 --> Prpv rfg ha grfg
# 15 --> Oqou qef gz fqef
# 16 --> Npnt pde fy epde
# 17 --> Moms ocd ex docd
# 18 --> Lnlr nbc dw cnbc
# 19 --> Kmkq mab cv bmab
# 20 --> Jljp lza bu alza
# 21 --> Ikio kyz at zkyz
# 22 --> Hjhn jxy zs yjxy
# 23 --> Gigm iwx yr xiwx
# 24 --> Fhfl hvw xq whvw
# 25 --> Egek guv wp vguv
