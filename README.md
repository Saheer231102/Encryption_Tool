Top algorithms of each method

1. Ceaser cipher:
    The Caesar cipher is a basic substitution cipher that shifts letters in the alphabet. While historically significant, it's not very secure due to its simplicity and small key space.
    Encryption: 
        C = (P + k) mod 26
    Decryption: 
        P = (C - k) mod 26

2. DES:
    DES is a symmetric-key block cipher that encrypts data in 64-bit blocks. It's a historic algorithm that was widely used but is now considered insecure due to its relatively short key length (56 bits).
    Encryption:
        R<sub>i+1</sub> = L<sub>i</sub>
        L<sub>i+1</sub> = R<sub>i</sub> ⊕ F(R<sub>i</sub>, K<sub>i</sub>)
    Decryption:
        R<sub>i+1</sub> = L<sub>i</sub>
        L<sub>i+1</sub> = R<sub>i</sub> ⊕ F(R<sub>i</sub>, K<sub>16-i</sub>)

3. AES:
    AES is a symmetric-key block cipher that encrypts data in blocks of 128 bits. It's considered a very secure and widely used algorithm.   
    Encryption:
        State<sub>i+1</sub> = AddRoundKey(MixColumns(ShiftRows(SubBytes(State<sub>i</sub>))))
    Decryption:
        InvShiftRows(InvSubBytes(InvMixColumns(AddRoundKey(State<sub>i</sub>))))

4. RSA:
    RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem, one of the oldest widely used for secure data transmission.
    Encryption:
        C, C = M^e mod n
    Decryption:
        P, M = C^d mod n
5. SHA256:
    The Secure Hash Algorithm 256-bit (SHA-256) is a cryptographic hash function that produces a 256-bit (32-byte) hash value from any length of input data.
    Encryption:
        T1 = h + S1(e) + Ch(e, f, g) + K<sub>t</sub> + W<sub>t</sub>
        T2 = S0(a) + Maj(a, b, c)
        h = g
        g = f
        f = e
        e = d + T1
        d = c
        c = b
        b = a
        a = T1 + T2
        
        Where:
        S0(x) = ROTR<sup>2</sup>(x) ⊕ ROTR<sup>13</sup>(x) ⊕ ROTR<sup>22</sup>(x)
        S1(x) = ROTR<sup>6</sup>(x) ⊕ ROTR<sup>11</sup>(x) ⊕ ROTR<sup>25</sup>(x)
        Ch(x, y, z) = (x ∧ y) ⊕ ((¬x) ∧ z)
        Maj(x, y, z) = (x ∧ y) ⊕ (x ∧ z) ⊕ (y ∧ z)

6. Base64:
    