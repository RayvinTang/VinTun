'''
import hitungan.physic.fisika
print(hitungan.physic.fisika.gravitasi)

from hitungan.physic import fisika
print(fisika.gravitasi)
'''
from hitungan.physic.fisika import tekanan_tiang, tekanan_pipa

print(tekanan_tiang(100, 20, 10))
print(tekanan_pipa(100, 20))