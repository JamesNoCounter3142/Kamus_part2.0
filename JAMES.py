meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "SIGMA" : "Pemimpin yang penyendiri, populer, dan keren",
            "ROFL" : "tanggapan terhadap lelucon",
            "SHEESH": "Sedikit ketidaksetujuan",
            "AGRO": "untuk menjadi agreesif/marah"
            }

word = input("Ketik kata yang tidak Kamu mengerti:").upper()

if word in meme_dict.keys():
    print("Makna kata",word,"adalah",meme_dict[word])
else:
    print('kata tidak ditemukan')
