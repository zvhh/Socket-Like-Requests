from setuptools import setup, find_packages


setup(
    name='Socket_Like_Requests',
    version='1.0.0',
    license='MIT',
    author="Sami",
    author_email='sami2700@outlook.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/zvhh/Socket-Like-Requests',
    keywords='simple socket',
)


from distutils.core import setup
setup(
  name = 'socket like requests',
  packages = ['socket like requests'],
  version = '0.1',
  license='MIT',
  description = 'Use Socket Like Requests Module',
  author = 'Sami',         
  author_email = 'sami2700@outlook.com', 
  url = 'https://github.com/zvhh/Socket-Like-Requests',
  download_url = 'https://github.com/zvhh/Socket-Like-Requests/archive/refs/tags/0.1.tar.gz',   
  keywords = ['Requests', 'TCP Request', 'Socket'],
  install_requires=[          
          'struct',
          'base64',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.11',
  ],
)