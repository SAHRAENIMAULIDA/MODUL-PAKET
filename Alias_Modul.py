import geometri2D as duaD

def main():
	p = 10
	l = 8

	luas = duaD.luasPersegiPanjang(p, l)

	print("PERSEGI PANJANG")
	print("panjang\t :", p)
	print("Lebar\t :", l)
	print("Luas\t = ",luas)

if __name__ == "__main__":
	main()
