import math

with open("key pairs.txt") as file:
    lines = [line.rstrip() for line in file]

key_pairs = []

for line in lines:
    if line.startswith("Key"):
        parts = line.split("=")

        e = int(parts[1].split(",")[0])
        n = int(parts[2])

        key_pairs.append((e, n))


with open("encrypted texts.txt") as file:
    lines = [line.rstrip() for line in file]

messages = []

for line in lines:
    if line.startswith("Message"):
        parts = line.split()

        numbers = parts[2:]
        messages.append([int(x) for x in numbers])


# Beräkna p och q för respektive n
def factorize(n):
 #Kolla om n är jämnt (kan vi utesluta jämna tal?)

    if n % 2 == 0:
        return 2, n // 2

    limit = int(math.sqrt(n)) + 1

    # Testa endast udda tal upp till roten ur n
    for i in range(3, limit, 2):        # Första udda talet är 3, stanna vid roten ur n, hoppa 2 steg (bara udda tal)

        if n % i == 0:                  # Kontrollera om d delar n jämnt
            p = i
            q = n // i
            return p, q

    return None, None

factors_list = []
for e, n in key_pairs:
    p, q = factorize(n)
    factors_list.append((e, n, p, q))

# Eukiledes algoritm
def eukiledes_algorithm(e, phi):
    t = 0
    new_t = 1
    r = phi
    new_r = e
    
    # Euklides utökade algoritm
   
    while new_r != 0:               # Loopar tills nuvarande resten är 0 (vi är klara då)
        kvot = r // new_r           # Vi får ett heltal ex. 23 / 5 = 4
        t, new_t = new_t, t - kvot * new_t      # Samma som modulo ex. 23 - (4*5) = 3 (vår rest)
        r, new_r = new_r, r - kvot * new_r      # Skiftar värderna ex. först var new_r = e men nu new_r = 3
        
    # Om resten är större än 1 finns ingen invers
    if r > 1:
        raise ValueError("ingen invers")
        
    # Om t är negativt gör vi det positivt med modulo
    if t < 0:
        t += phi
        
    return t

    
private_keys = []

for e, n, p, q in factors_list:
    phi = (p - 1) * (q - 1)
    d = eukiledes_algorithm(e, phi)
    private_keys.append((e, n, d))

print("(-- RESULTAT --)")

for message_number, message in enumerate(messages, start=1):
    found = False
    
    for key_number, (e, n, d) in enumerate(private_keys, start=1):
        full_text = ""
        try:
            # Dekryptera varje block och gör om till text
            for c in message:
                m = pow(c, d, n)
                
                # Omvandla till bytes
                byte_length = (m.bit_length() + 7) // 8
                if byte_length > 0:
                    byte_data = m.to_bytes(byte_length, byteorder='big')
                    full_text += byte_data.decode('latin-1', errors='ignore')
            
            # En enkel kontroll att texten mest innehåller vanliga tecken
            if len(full_text) > 0 and all(32 <= ord(c) <= 126 or c in '\n\r\t' for c in full_text):
                print()
                print("------------------------------------------")
                print(f"Meddelande {message_number}")
                print("------------------------------------------")
                print(f"Nyckel nr: {key_number}")
                print(f"e = {e}")
                print(f"n = {n}")
                print(f"d = {d}")
                print()
                print(f"Text:\n{full_text}")
                
                found = True
                break
        except Exception:
            # Om det blir fel vid byte-konvertering eller liknande hoppar vi till nästa nyckel
            continue