# TI_Lab_2
<h1> Streaming cryptosystems <h1\>

Laboratory work **II** on the Theory of Information.
Teacher: Boltak S.V.
***
Find me: [Telegram](t.me/AlexeyShilo)
---


*The basic idea of `streaming cryptosystems` is to encrypt the source
text M using a cryptographic key K, whose length is equal to the length of the text.
Each ciphertext bit C i is a function of the corresponding bits of the source text.
and key stream.*

*The symbol ⊕ denotes the addition operation "EXCLUSIVE-OR".
Due to the linear properties of this operation when encrypting and decrypting
the same key stream K is used. Obviously, in this case
the length K must be equal to the length of the transmitted message. However, key exchange
large size is often impossible. Therefore, in practice, to form
keystream use pseudo-random sequence generators*


