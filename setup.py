from setuptools import setup, find_packages

setup(
    name="CronGrpc",
    version="1.0.2",
    packages=find_packages(),
    install_requires=[
        # 'plan==0.5',
        'python-crontab==2.3.6',
        'django==2.2',
        'mysqlclient==1.4.2',
        'grpcio==1.17.0',
        'grpcio-tools==1.17.1',
        'grpc==0.3.post19',
        'mysql-connector-python==8.0.15',   #mysql连接驱动
        # 'Flask_Mail==0.9.1',
        # 'Flask==1.0.2',
        'setuptools==40.4.1',
        'futures==3.2.0',
        'protobuf==3.6.1',
        'grpc==0.3-19',
        'psycopg2==2.7.6.1',
        'configparser==3.5.0',
        'enum34==1.1.6 '
    ]
)
