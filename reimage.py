import json
from flask import jsonify
import tools
import logs
import copy
import db

def restartImage(request):
    ip = json.loads(request.get_data()).get('ip')
    id = json.loads(request.get_data()).get('id')
    path = json.loads(request.get_data()).get('image')
    insertData = copy.deepcopy(list(db.getDbData('web_system_db', 'board_list', {"id": id})))
    if ip and path:
        res = tools.reimage(path, ip)
        logs.insertLogList('flashImage', insertData)
    else:
        res = 'ip or path not found'
    return jsonify({"code": 200, "data": {"restartImage": res, 'user':tools.getUser() }})
    