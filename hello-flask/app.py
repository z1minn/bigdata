from flask import Flask, request, render_template
app = Flask(__name__)

import nvapi



@app.route('/')
def hello():
    return 'Hello, World! skrrrrrrrr'

@app.route('/baseball')
def baseball():
    return 'Hello, baseball!'

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/youtube', methods=['GET', 'POST'])
def youtube():
    linklist = ['https://www.youtube.com/embed/S7UW5NfKLAQ?si=e5gq7tSrGipXKbV9', 'https://www.youtube.com/embed/Ve3_XoThvS4?si=3YonH3caT25z8swA']
    keyword = request.form["keyword"]
    print(keyword)
    linknum = 0 # 0은 토트넘, 1은 첼시
    if keyword == '토트넘':
        linknum = 0
    elif keyword == '첼시':
        linknum = 1
    else:
        print('잘못된 입력') 
    return render_template('youtube.html', name=keyword, link=linklist[linknum])

@app.route('/ytpage')
def ytpage():
    return render_template('ytpage.html')

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        keyword = request.form["keyword"]
        print(keyword)
        data = nvapi.blog(keyword)
        # return f"POST로 전달된 당신이 입력한 검색어: {keyword}"
        return render_template("result.html", keyword=keyword, blist=data)


if __name__ == '__main__':
    app.run(host="210.110.167.53")


