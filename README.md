공공자전거 파이프라인 구축
- 데이터를 추출한 후 csv로 변환해 Cloud Storage에 저장
- Cloud Storage의 csv 파일을 Bigquery의 테이블에 삽입
- 대여 이력과 대여소 정보 두 테이블을 join하여 새로운 테이블로 갱신
- 새로운 테이블을 Looker Studio로 연결해 시각화
- 위 일련의 과정을 1시간마다 주기적으로 이루어지도록 자동화