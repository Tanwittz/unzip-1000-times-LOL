from zipfile import ZipFile

i = int(input("Enter : How times U want to unzip that file"))

while True:
	zright = ZipFile(f'{i}.zip','r')
	zright.extractall()
	print(f"The {i} File Has Unzipped...")
	i = i -1



