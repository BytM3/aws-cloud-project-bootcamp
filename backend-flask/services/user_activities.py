from lib.db import db

#from aws_xray_sdk.core import xray_recorder


class UserActivities:
  def run(user_handle):
      # xray ---
      #segment = xray_recorder.begin_segment('user_activities')
      #try:
      model = {
        'errors': None,
        'data': None
      }

      #now = datetime.now(timezone.utc).astimezone()
      #dict = {
      #  "now": now.isoformat()
      #}
      if user_handle == None or len(user_handle) < 1:
        model['errors'] = ['blank_user_handle']
      else:
        print("else:")
        sql = db.template('users','show')
        results = db.query_object_json(sql,{'handle': user_handle})
        model['data'] = results

      # xray ---
      #subsegment = xray_recorder.begin_subsegment('mock-data')

      #dict = {
      #  "now": now.isoformat(),
      #  "results-size": len(model['data'])
      #}
      #subsegment.put_metadata('key', dict, 'namespace')  

      ## SOLVING
      #xray_recorder.end_subsegment()
    #finally:
      #xray_recorder.end_subsegment()
      return model
