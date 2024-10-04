import os

def ch_size(path):
	size = 0
	if os.path.getsize(path):
		size = os.path.getsize(path)
	else:
		for dirpath, dirnames, filenames in os.walk(path):
			for filename in filenames:
				fp = os.path.join(dirpath,filename)
				if os.path.isfile(fp):
					size += os.path.getsize(fp)
	return size

def hread_size(size):
	for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
		if size < 1024:
			break
		size /= 1024
	return "{:.1f} {}".format(size, unit)

def main():
	pwd = os.getcwd()
	items = os.listdir(pwd)
	file_list = []

	for item in items:
		full_path = os.path.join(pwd, item)
		size = ch_size(full_path)
		file_list.append((size, item))

	file_list.sort(key=lambda x: x[0], reverse=True)
	for size, item in file_list:
		print("{} {}".format(hread_size(size), item))

if __name__ == "__main__":
	main()