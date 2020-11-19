import requests

def downloadVideo(url):
    fileName = url.split('/')[-1]   ### we will remove the '/' until the lssts leter to obtain name by using out of bound index
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
    with open(fileName, 'wb') as f:    ##### this will transfer the data
        for chunk in r.iter_content(chunk_size=8192):    ## this will  go through the chunk and allow a large size
            if chunk: ### write out to the local file
                f.write(chunk)
    return fileName




### call vide dowload method
downloadVideo("https://cdn.videvo.net/videvo_files/video/free/2013-08/small_watermarked/hd0998_preview.webm")