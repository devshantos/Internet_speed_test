import speedtest
speed=speedtest.Speedtest()

Download_speed= speed.download()
Upload_test= speed.upload()
print("Your download speed: ", Download_speed)
print("Your upload speed: ", Upload_test)
