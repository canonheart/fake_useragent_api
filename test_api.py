import requests

# API 기본 URL
BASE_URL = "http://127.0.0.1:5000"

def test_user_agent_api():
    """User-Agent API 테스트"""
    
    print("=== User-Agent API 테스트 ===\n")
    
    # 1. 랜덤 user-agent 테스트
    print("1. 랜덤 User-Agent:")
    response = requests.get(f"{BASE_URL}/user-agent")
    print(f"Status: {response.status_code}")
    print(f"User-Agent: {response.text}\n")
    
    # 2. 특정 브라우저 user-agent 테스트
    browsers = ['chrome', 'firefox', 'safari', 'opera', 'edge', 'google', 'ff']
    
    for browser in browsers:
        print(f"2. {browser.upper()} 브라우저 User-Agent:")
        response = requests.get(f"{BASE_URL}/user-agent?browser={browser}")
        print(f"Status: {response.status_code}")
        print(f"User-Agent: {response.text}\n")
    
    # 3. 존재하지 않는 브라우저 테스트
    print("3. 존재하지 않는 브라우저 테스트:")
    response = requests.get(f"{BASE_URL}/user-agent?browser=invalid")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}\n")
    
    # 4. 홈페이지 테스트
    print("4. 홈페이지 테스트:")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}\n")

if __name__ == "__main__":
    test_user_agent_api() 