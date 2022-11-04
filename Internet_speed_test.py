import speedtest
speed=speedtest.Speedtest()

Download_speed= speed.download()
Upload_test= speed.upload()
print("Your internet speed: ", Download_speed)
print("Your download speed: ", Upload_test)