from onedrivedownloader import download
if __name__ == '__main__':
    str = input('输入URL\r\n')
    name = input('文件名\r\n')
    download(str, filename=name, unzip=False, clean=True)