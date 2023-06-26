import requests
import json

link = "https://us04web.zoom.us/j/71227612939?pwd=QtbYaF5oSy0RNZb7LK3Yvpxi7D8IEP.1"

def getPassword(link):
    first = link.split("?")

    if (first[0].split("j")[0] != "https://us04web.zoom.us/"):
        return ("link incorrect")
    else:
        meeting_id = first[0].split("/")[4]
        pwd = first[1].split("=")[1]

        req_link = f'https://pwa.zoom.us/wc/{meeting_id}/join?from=pwa&_x_zm_rtaid=BVH31TdOQbaYRwpoIuvWWQ.1687205112656.6115d5b1b424bd0f8492a9f959ceaf55&_x_zm_rhtaid=577'
        payload = {"meetingId": meeting_id, "name": "ff", "pwd": f'{pwd}', "email": ""}
        headers = {
            "Content-Type": "application/json;odata=verbose",
        }

        req = requests.post(req_link, json=payload, headers=headers)


        req_json = req.json()
        print(req_json)

        if (req_json['status'] == False):
            return req_json["errorMessage"]
        else:
            password = req_json["result"]["MeetingConfig"]["h323password"]
            return (f'meeting id: {meeting_id}\nmeeting password: {password}')


print(getPassword(link=link))