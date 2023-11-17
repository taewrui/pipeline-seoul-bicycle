from google.cloud import bigquery
import os

credentials_path = "/app/credentials.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
client = bigquery.Client.from_service_account_json(credentials_path)

sql_query = """
INSERT INTO `delta-discovery-405105.dataset_cycle.CycleRentStInfo`
SELECT RentData.*, 
RentStInfo.STA_LAT AS RENT_LAT, RentStInfo.STA_LONG AS RENT_LONG,
RentStInfo.STA_ADD1 AS RENT_ADD1, RentStInfo.STA_ADD2 AS RENT_ADD2,
ReturnStInfo.STA_LAT AS RETURN_LAT, ReturnStInfo.STA_LONG AS RETURN_LONG,
ReturnStInfo.STA_ADD1 AS RETURN_ADD1, ReturnStInfo.STA_ADD2 AS RETURN_ADD2

FROM `delta-discovery-405105.dataset_cycle.CycleRentData` AS RentData

LEFT JOIN `delta-discovery-405105.dataset_cycle.CycleStationInfo` AS RentStInfo
ON RentData.RENT_STATION_ID = RentStInfo.RENT_ID

LEFT JOIN `delta-discovery-405105.dataset_cycle.CycleStationInfo` AS ReturnStInfo
On RentData.RETURN_STATION_ID = ReturnStInfo.RENT_ID
LIMIT 200
"""

query_job = client.query(sql_query)


