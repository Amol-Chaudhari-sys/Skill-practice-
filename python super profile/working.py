import webbrowser as wb 

urls = ["https://youtube.com/playlist?list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&si=sCjOeFFGEZh4jLlF", 
        "https://youtube.com/playlist?list=PLmXKhU9FNesTaKDC-MKWt-rFuB8OwqrCY&si=AIQDiALIJuoEF6Je", 
        "https://infyspringboard.onwingspan.com/web/en/app/goals/me",
        "https://superprofile.bio/view_course/696fc913041d980014983832?courseId=54be1068-b282-45bc-a6c5-4bc4adc95979&openSideSheet=true"]


for url in urls :
    wb.open_new_tab(url)