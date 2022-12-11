# cryptography

#MOTIVATION
Increasing the confidentiality and integrity of radio frequency identification
systems. RFID systems are inexpensive, capable of scanning outside of a line of sight, and
have unique identification. RF ID systems are utilized for IoT networks and supply chain
management, in contrast to bar codes and magnetic tapes. They developed a model to deal
with this issue since RF ID tags can be captured by enemies and can be sent across a greater
distance over a radio channel.
There have been several models presented before this one, but they have all
failed since they can be used as targets for numerous types of attacks. A less cost-effective
paradigm called UR MAP (ultra-lightweight resilient mutual authentication protocol) has been
put out by the author to ensure security across RF-ID systems. The operations in this are
carried out using n-bit bitwise operations. Per-XOR and Inverse Per-XOR algorithms are used in
this as the 2 implemented algorithms. With this concept, communication between two parties is
more secure or resistant to outside threats. The outcomes are contrasted with the GNY Logic
analysis as well.
As a result, the model is the safest and obtains Integrity and Confidentiality.
Tag (T), Reader (R), and the back-end database are the three components of RFID that we
should be aware of (D). Tag is a term used to describe a little electronic chip that is actually
used to conceal information about an object or hidden message. ”It contains all the information
about the linked tags,” the reader means. D stands for ”the database that is referred to as
containing the information of each tag.” Every time a tag reaches the area where this reader is2
located, it continuously emits or sends the beacon message and gets a ”Hello” message (pilot
signal). Upon receiving this information, the "T" then sends the "R" the most recent IDS.
If a match is discovered, the "R" generates some pseudorandom numbers, uses
previously revealed secrets to conceal them in messages, and sends them to the "T." The "R"
searches its "D" and discovers the matched entry (received IDS). The real "T" receives the
fictitious random numbers and confirms the sender.
Finally, the "T" encrypts its secret ID within the cypher message and sends it in order for
the "R" to authenticate the tag. The author grouped the security protocols into four major types
based on the computation of the tags, which are as follows:
● Full Fledged Protocols
● Simple protocols
● Lightweight Protocols
● Ultra lightweight Protocols
1. Full-fledged protocols signify conventional techniques such as AES, DES, and hash
functions, among others. In this, there are no power limitations necessary for computation.
2. Simple Protocols refer to an environment that mostly uses one-way hash functions and
pseudo-random number generators like LCG (Linear Congruential Generators), Kasami
sequences, etc.
3. It is CRC (Cyclic Redundancy Check) and lightweight random number generators like LFSR
(Linear Feedback Shift Register), LAMED, etc. that are meant by "lightweight protocols."
4. "Bitwise logical operators and some specific purpose ultralight weight primitives, such as
Rotation, Recursive Hash, Mix Bits, etc.," are examples of ultralight weight protocols.
We are trying to implement the per-XOR algorithm and also per-Inverse-XOR
algorithms to encrypt the bits we will be using one key or fixed number of bits to encrypt it and
also for the decryption in this process. In this, we are trying to get authentication

