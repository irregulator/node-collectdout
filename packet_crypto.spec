Signed CollectD Packet
POS        TYPE            SIZE  NOTES
----------------------------------------------
0-1        ptype              2  val: 0x0200
2-3        plen               2  header length: [0, N]
4-35       mac               32  calculated on uname and payload: [36, M]
36-N       uname    plen-2-2-32  length is header length minus rest header fields
(N+1)-M    payload    remaining  encapsulated plaintext packet

Overhead: 36 + len(username)


Encrypted CollectD Packet
=========================

POS   TYPE            SIZE  NOTES
----------------------------------------------
0-1   ptype              2  val: 0x0210
2-3   plen               2  encr payload length: [4, M]
4-5   plen               2  username length
6-N   uname
      IV                 16
      checksum           20
      payload               remaining  encapsulated encrypted packet

Overhead: 42 + len(username)
