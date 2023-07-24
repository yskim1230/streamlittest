import streamlit as st
import mysql.connector

# AWS RDS MySQL 인스턴스 정보
db_config = {
    'host': 'aibsection6pjt.cbodywvxd8v5.ap-northeast-2.rds.amazonaws.com',       # AWS RDS 엔드포인트
    'user': 'admin',            # MySQL 사용자 이름
    'password': 'aibsection6pjt',        # MySQL 비밀번호
    'database': 'aibsection6pjt'    # 사용할 데이터베이스 이름
}

# MySQL 연결 함수
def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            st.write('Connected to MySQL database')
            return connection
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Streamlit 앱 시작
def main():
    st.title('AWS MySQL 연동 예제')
    
    # MySQL 연결
    connection = connect_to_database()
    
    if connection:
        # 여기에서 데이터베이스 쿼리 및 조작을 수행합니다.
        # 이 예제에서는 단순히 연결 여부만 확인합니다.
        connection.close()
        st.write('Disconnected from MySQL database')

if __name__ == '__main__':
    main()