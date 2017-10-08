import tbapy
import json
import xlsxwriter

#events = list()
#events_json = str()
teams = list()

tba = tbapy.TBA('hjzCpHdD7EYfs0SBAdidF6yq0jpdJf3tqQplhQhgVPkSCMFQC2hDp57YVko9V8BG')
data = tba.event_teams("2018nyny")

"""for event in data:
    events.append(event.json)

events_json = ''.join(str(events))
events_json = events_json.replace("'","\"")"""

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

fh = open('data.json').read()
info = json.loads(fh)

count, row, col, award_count = 0,1,0,0

workbook = xlsxwriter.Workbook('2018nyny.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,col,"Team")
worksheet.write(0,col+1,"FRC")
worksheet.write(0,col+1,"Awards")
url_format = workbook.add_format({
    'font_color': 'blue',
    'underline':  1
})

for item in info:
    print("Team:",item['key'])
    try:
        worksheet.write_url(row, col, item['website'],url_format, item['nickname'])
    except:
        worksheet.write(row,col,item['nickname'])
    worksheet.write(row, col + 1, int(item['key'].replace("frc","")))
    team_awards = tba.team_awards(item['key'])
    for award in team_awards:
        if (award['award_type'] == 1 or award['award_type'] == 2):
            award_count += 1
    worksheet.write(row, col + 2, award_count)
    count += 1
    row += 1
    award_count = 0

print("Teams Registered:",count)

workbook.close()