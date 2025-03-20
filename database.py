from sqlalchemy import create_engine, text, URL

db_connection_string = 'mysql+pymysql://2VYR4UeraYPWA8c.root:kI02KHeOZKmyNYrm@gateway01.ap-northeast-1.prod.aws.tidbcloud.com:4000/test'

engine = create_engine(db_connection_string,
                       connect_args={'ssl': {
                           'ssl_ca': '/etc/ssl/cert.pem'
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())
  result_all = result.all()
  print(type(result_all))
  first_result = result_all[0]
  first_result_dict = first_result.__dict__
  print(type(first_result_dict))
