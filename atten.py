import pandas as pd
import requests

url = "https://niet.instituteoncloud.com/AttendanceReport/GetAcademicSemster?Type=GetStudentSemesterAttedance&Semester=10010000004"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
df = df.drop('SUbjectCode', axis=1)
df = df[['SCode', 'SName', 'NoofLecture', 'Present', 'Absent', 'Percentage']]
df.to_excel('attendance.xlsx', index=False)
