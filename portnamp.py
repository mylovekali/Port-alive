def url_list():
	url_list = []
	url = "http://192.168.1.159"
	for i in range(8001,8051):
		shell_url = url + ":" + str(i)
		url_list.append(shell_url)
	for i in url_list:
		print(i)

if __name__ == '__main__':
	url_list()

//扫描端口存活