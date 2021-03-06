import requests
import sys
import argparse

parse = argparse.ArgumentParser(description='A')

parse.add_argument("--vid", default=None, type=str,help="Bypass 1 video has videoID=video_ID, this arg is obligatory",dest="video_ID")
parse.add_argument("--all",default=None, type=str, help="Bypass all video has ID <= n, suggest n = 10000, not obligatory",dest="n")
vidID = parse.parse_args().video_ID
all = parse.parse_args().n
url = "http://e-learning.hcmut.edu.vn/mod/hvp/ajax.php?contextId=1010672&token=5c0156c3b9be2&action=set_finished&contentId=437&data_type=state&sub_content_id=0&score=0&maxScore=0&opened=1585754436&finished=1585755546"

print("---------------Start bypass--------------")
headers={
    "Accept":"*/*",
    "Accept-Language":"en-US,en;q=0.5",
    "Accept-Encoding":"gzip, deflate",
    "X-Requested-With":"XMLHttpRequest",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Connection":"close",
    "Cookie":"_ga=GA1.3.868064709.1551606029; MoodleSession=vpgm0fvgmlrnp8pcc04opbvdg1; _gid=GA1.3.2084628101.1585907499"
}

i=0

# url = "http://e-learning.hcmut.edu.vn/mod/hvp/ajax.php?contextId={}&token={}&action=set_finished&contentId={}&data_type=state&sub_content_id=0&score=0&maxScore=0&opened=1585754436&finished=1585755546".format(contextId,token,i)
# res=requests.get(url, headers=headers)

if vidID != None and all == None:
    url = "http://e-learning.hcmut.edu.vn/mod/hvp/view.php?id={}".format(vidID)
    res = requests.get(url, headers=headers)
    try:
        contentId = res.text.split("content\/")[1]
        #print (res.text)
        contentId = contentId.split("\"")[0]
        token = res.text.split("token=")[1]
        token = token.split("&")[0]
        url = "http://e-learning.hcmut.edu.vn/mod/hvp/ajax.php?contextId=123&token={}&action=set_finished&contentId={}&data_type=state&sub_content_id=0&score=0&maxScore=0&opened=1585754436&finished=1585755546".format(token,contentId)
    except:
        print ("Video ID is not available, pls check it again!")
        sys.exit()
    res=requests.get(url, headers=headers)
    if res.text.find('true') != -1:
        print ("[*] Success, video bypass watching, ID=" + vidID)
    else:
        print ("[*] Fail, video is not avaiable, check pls!")
else:
    print ("Wait...")
    while i < int(all):
        #token = input("[*] Token: ")
        url = "http://e-learning.hcmut.edu.vn/mod/hvp/view.php?id={}".format(vidID)
        res = requests.get(url, headers=headers)
        try:
            contentId = res.text.split("content\/")[1]
            #print (res.text)
            contentId = contentId.split("\"")[0]
            token = res.text.split("token=")[1]
            token = token.split("&")[0]
            url = "http://e-learning.hcmut.edu.vn/mod/hvp/ajax.php?contextId=123&token={}&action=set_finished&contentId={}&data_type=state&sub_content_id=0&score=0&maxScore=0&opened=1585754436&finished=1585755546".format(token,contentId)
        except:
            print ("Video ID is not available, pls check it again!")
            sys.exit()
        url = "http://e-learning.hcmut.edu.vn/mod/hvp/ajax.php?contextId=123&token={}&action=set_finished&contentId={}&score=0&maxScore=0&opened=1585754436&finished=1585755546".format(token,i)
        res=requests.get(url, headers=headers)
        if res.text.find('true') != -1:
            print ("[*] Success, video bypass watching, ID=" + str(i))
        i+=1




