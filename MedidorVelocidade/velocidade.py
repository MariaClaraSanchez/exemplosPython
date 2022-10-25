# pip install speedtest-cli
import speedtest

speed = speedtest.Speedtest()

def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * 1024

    return int(bytes/MB)

download_seed = bytes_to_mb(speed.download())
# upload_seed = bytes_to_mb(speed.upload())

print(f"Velocidade Download é: {download_seed} MB")
# print(f"Velocidade Upload é: {upload_seed} MB")