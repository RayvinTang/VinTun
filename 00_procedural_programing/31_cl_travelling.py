'''
1. bayangkan kita akan pergi ke 5 tempat baru
2. buatkan lists dari 5 tempat tersebut dan tidak perlu terutut
3. cetak lists yang original
4. cetak lists terurut tanpa mengubah list yang asli
5. karena dana terbatas hapus 2 tujuan, yang pertama hapus
'''

negara = ['cina', 'rusia', 'jepang', 'kanada', 'usa']
print(negara)

negara.sort()
print(negara)

negara.sort(reverse=True)
print(negara)

negara.remove('cina')
print(negara)

negara.remove('rusia')
print(negara)

negara.insert(0, 'paris')
print(negara)