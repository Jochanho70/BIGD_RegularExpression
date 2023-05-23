"""
정규식의 기본적인 사용법 
"""
# 모듈 임포트: 정규 표현식을 사용하기 위해 먼저 re 모듈을 임포트해야 합니다.

import re
# 패턴 컴파일: 검색하거나 추출하려는 패턴을 정규 표현식으로 작성하고, re.compile() 함수를 사용하여 패턴 객체를 생성합니다.
pattern = re.compile(r"패턴")

# 문자열 작업 수행: 패턴 객체를 사용하여 문자열 작업을 수행합니다. findall(), search(), match(), sub() 등 다양한 메서드를 사용할 수 있습니다. 

# findall(): 패턴과 일치하는 모든 부분을 찾아 리스트로 반환합니다.
matches = pattern.findall(text)

# search(): 패턴과 첫 번째로 일치하는 부분을 찾습니다.
match = pattern.search(text)

# match(): 문자열의 시작부터 패턴과 일치하는지 확인합니다.
match = pattern.match(text)

# sub(): 패턴과 일치하는 부분을 다른 문자열로 대체합니다.
new_text = pattern.sub(replacement, text)

# 매치 결과 사용: 찾은 매치 결과를 사용하거나 처리할 수 있습니다. group() 메서드를 사용하여 매치된 부분을 가져올 수 있습니다.
if match:
    matched_text = match.group()
    # 매치된 텍스트를 처리합니다.

# 아래는 정규식을 사용하는 예제이다.    

text = """
Contact us at email@example.com or support@example.com
Phone: 123-456-7890 or 9876543210
Visit our website at https://www.example.com or http://example.com
This is a sample sentence.
The price is $10.00.
"""

# 이메일 주소 추출하기
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
emails = re.findall(email_pattern, text)
print("Emails:", emails)    # Emails: ['email@example.com', 'support@example.com']

# 전화번호 추출하기
phone_pattern = r"\b\d{3}-\d{3}-\d{4}\b"
phone_numbers = re.findall(phone_pattern, text)
print("Phone numbers:", phone_numbers) # Phone numbers: ['123-456-7890']

# URL 추출하기
url_pattern = r"https?://(?:www\.)?\w+\.\w+"
urls = re.findall(url_pattern, text)
print("URLs:", urls) # URLs: ['https://www.example.com', 'http://example.com']

# 단어 개수 세기
word_pattern = r"\b\w+\b"
word_count = len(re.findall(word_pattern, text))
print("Word count:", word_count) # Word count: 38

# 이스케이프 문자 검색
escape_pattern = r"\$"
escape_count = len(re.findall(escape_pattern, text))
print("Escape count:", escape_count) # Escape count: 1
