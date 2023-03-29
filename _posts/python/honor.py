# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import threading
import time


def _curl():
    # import pdb
    # pdb.set_trace()
    try:
        while True:
            url = "https://ord01.vmall.com/order/pwm86t/createOrder.do"
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = {'User-Agent': user_agent}
            values = {
                'sign': '0A44317EF76AB9769428B22DAB2050C228839397FABC989894D9EF4D6B0FE258',
                'data': 'HE4vx7dBFhYnVy5p7re%2BPhkYLQZr3P84HfkZrgEvVTbEJtx3DO%2F439nvLRIvEvXLbT978kBH7tnYKr9cq7ho5ujUW8qegWvCTuL0rrAXAIkR3mjIZbeexaaNjNjwpArT%2ByUIMyJvEdrLuDis9d9CIXFkkqvwMehpuKsb2619QZGy%2FSDyuWOzeTtYOsbV319YEZlYie0pyoHixwEQIXhucpQ9CjcRh5m%2BOrDAiCCO89YTnqk4R3UVhexweZ5UPtd5nFLYPspRc5x3BA%2Bgc6SYpZVq1MFiBqfan9OfNH4cqZKJ6lqPAtJrJjs7vGd7OJFtT3IOIxvwG%2Fl5ynjNtjW%2Bwa7PLEzGrrRbOmlHAuyeYvbrVE3VHOCY3cr2BRzM3JZtZvcbBGHA7KxWcZ9SjWZUfWIyfBtSGz1tSgT20aLZxLpKOnA5GWxXsDuLcyJ9rDLbjsncFz9va9v7%2FadNvTF5gNYR7MuxknAY9HESwA051OsxnwfxxIcp1HDrRsyRYz6WlAvl0WNvMCqVmv3%2FvEahunoFg%2BhBLTwPTedCg%2BnR7EFxg5UI8ZAof7dXETbNdvS7JujTPdufxNW0vLfv9pk0LOg1n2YCvPE0ZrzQjnCKQVLxlG0v32eIptTF4oYgIMGHL25iAzbErII%3D',
                'uid': 55511337,
                'skuId': 546837584,
                'skuIds': 546837584,
                'callback': 'callback' + str(int(time.time() * 1000)),
                't': int(time.time() * 1000),
            }
            print values
            data = urllib.urlencode(values)
            request = urllib2.Request(url, data, headers=headers)
            response = urllib2.urlopen(request)
            content = response.read()
            print content, time.time()
            time.sleep(2)
            if 'ture' in content:
                print content, "恭喜您已经预定成功"
                exit()
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason


# def timer():
#     while True:
#         t = threading.Timer(2, _curl)
#         t.start()
#         t.join()
if __name__ == '__main__':
    _curl()
