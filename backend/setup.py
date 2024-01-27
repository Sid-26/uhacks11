from setuptools import setup 

  
setup( 
    name='services', 
    version='0.1', 
    description='Cohere API Services', 
    author='Siddhant Das', 
    author_email='jdoe@example.com', 
    packages=['services'], 
    install_requires=[ 
        'cohere'
    ],
    setup_requires=['wheel'], 
) 