from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'postgres://cssdkksrywlfnv:ba16723832aed2a2656d6da24d5bcb64e2ad9a45cb3610b44d21beaf8cc7b75f@ec2-54-217-213-79.eu-west-1.compute.amazonaws.com:5432/dn24ql2a7ul4r')
Session = sessionmaker(bind=engine)

Base = declarative_base()
