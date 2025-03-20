from sqlalchemy import create_engine, text

db_connection_string = 'mysql+pymysql://:2VYR4UeraYPWA8c.root:kI02KHeOZKmyNYrm@gateway01.ap-northeast-1.prod.aws.tidbcloud.com:4000/test?charset=utf8mb4'

engine = create_engine(db_connection_string)

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())
