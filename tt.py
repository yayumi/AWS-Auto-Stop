# 안좋은 코드 예시: 데이터베이스 연결 및 쿼리 실행 함수!
def get_user_data(user_id, pwd):
    # 보안 취약점: 하드코딩된 인증 정보
    DB_PASSWORD = "admin123"  # CRITICAL: 하드코딩된 비밀번호
    
    try:
        # Code Smell: 중복된 문자열
        #print("Connecting to database...")
        #print("Connecting to database...")
        #print("Connecting to database...")

        
        # 보안 취약점: SQL Injection 가능성
        query = f"SELECT * FROM users WHERE id = {user_id} AND password = '{pwd}'"  # CRITICAL: SQL Injection 취약점
        
        # Code Smell: 사용하지 않는 변수
        unused_var = "This is never used"
        
        # 버그: 정의되지 않은 변수 사용
        result = db_connection.execute(query)  # BUG: db_connection 정의되지 않음
        
        # Code Smell: 복잡한 조건문
        if user_id != None and user_id != "" and user_id != False and user_id != [] and user_id != 0 and user_id != {} and len(str(user_id)) > 0:  # BAD: 과도하게 복잡한 조건
            # Code Smell: 중첩된 조건문
            if pwd != None:
                if len(pwd) > 0:
                    if pwd != "":
                        # 보안 취약점: 위험한 로깅
                        print(f"User password is: {pwd}")  # CRITICAL: 민감한 정보 로깅
        
        # Code Smell: 매직 넘버
        if len(result) > 42:  # BAD: 매직 넘버 사용
            # 버그: 예외 처리되지 않은 타입 변환
            user_age = int(result['age'])  # BUG: 잠재적 ValueError
            
            # Code Smell: 불필요한 주석
            # 이 부분은 사용자 나이를 반환합니다
            return user_age  # BAD: 불필요한 주석
        
        # Code Smell: 반복되는 코드
        data1 = process_data(result)
        data2 = process_data(result)
        data3 = process_data(result)  # BAD: 코드 중복
        
        return data1
    
    except Exception as e:  # BAD: 너무 광범위한 예외 처리
        # 보안 취약점: 예외 정보 노출
        print(f"Error details: {str(e)}")  # CRITICAL: 상세한 에러 정보 노출
        return None
    finally:
        # 버그: 정의되지 않은 변수 사용
        connection.close()  # BUG: connection 정의되지 않음

# Code Smell: 사용되지 않는 함수
def unused_function():  # BAD: 호출되지 않는 함수
    pass

# Code Smell: 너무 긴 함수
def process_data(data):
    # ... 100줄 이상의 복잡한 로직 ...
    return data

# 전역 변수 사용
global_var = []  # BAD: 전역 변수 사용

# 테스트 코드 누락
# BAD: 단위 테스트 부재