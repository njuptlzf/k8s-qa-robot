import requests
import json
import sys

def ask_question(question):
    url = 'http://localhost:5000/ask'
    data = {'question': question}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return '请求失败'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('请传入问题, 例如 python3 test-flask-client.py 你好，你是谁')
    else:
        question = sys.argv[1]
        answer = ask_question(question)
        print(answer)